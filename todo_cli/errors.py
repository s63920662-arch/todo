class TodoError(Exception):

    pass

class StorageError(TodoError):

    pass

class ValidationError(TodoError):

    pass
