from pydantic import BaseModel, Extra, validator
from config.environment import FORMATS


class FileValidator(BaseModel, extra=Extra.forbid):
    format: str
    encoding: str
    separator: str

    @validator('format')
    def format_in_supported_format(cls, v):
        if v not in FORMATS:
            raise ValueError('Format not supported')
        return v
