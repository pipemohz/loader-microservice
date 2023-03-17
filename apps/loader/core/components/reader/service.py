from apps.common.service import BaseService
from apps.loader.core.components.reader.exceptions import InvalidFileError, InvalidJsonlFileError, InvalidEncodingFormatError, InvalidColumnName
import json
from json.decoder import JSONDecodeError
from pandas import read_csv, DataFrame
import numpy as np


class Service(BaseService):
    def run(self):
        config = self.orchestrator.payload['service.formatter']
        file = self.orchestrator.base_data['file']

        try:
            if config['format'] == 'jsonl':
                lines = [
                    json.loads(line.decode(config['encoding']))
                    for line in file.stream.readlines()
                ]
                df = DataFrame.from_records(lines)
            else:
                df = read_csv(
                    file, sep=config['separator'], encoding=config['encoding'], dtype=np.str_)

            # Replace all blank values for NaN
            df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
            # Remove all rows with NaN values
            df.dropna(inplace=True)
            # Add a new column with concatenation of site and id
            df['ids'] = df['site'] + df['id']

        except KeyError as e:
            raise InvalidColumnName(str(e))
        except UnicodeDecodeError:
            raise InvalidFileError()
        except JSONDecodeError:
            raise InvalidJsonlFileError()
        except LookupError:
            raise InvalidEncodingFormatError()
        except Exception as e:
            raise Exception(
                f'An error has ocurred in reader module: {type(e)}: {e}]')

        self.temp_data = {'data': df}
        self.store_temporal_data()
