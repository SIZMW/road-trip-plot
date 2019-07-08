import os

def file(path):
    """
    Return absolute path for a file.

    Arguments:
        path: The path to get the OS path for.
    Returns:
        A file path.
    """
    return os.path.abspath(path)
