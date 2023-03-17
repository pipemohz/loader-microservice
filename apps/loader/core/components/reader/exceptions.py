class InvalidFileError(Exception):
    def __init__(self) -> None:
        super().__init__('File content is invalid.')


class InvalidJsonlFileError(Exception):
    def __init__(self) -> None:
        super().__init__('Jsonl file content is invalid or encoding format is invalid.')


class InvalidEncodingFormatError(Exception):
    def __init__(self) -> None:
        super().__init__('Encoding format is invalid.')


class InvalidColumnName(Exception):
    def __init__(self, column) -> None:
        super().__init__(f'File does not contain column: {column}')
