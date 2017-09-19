import os


def find_filepath(filename=None):
    # TODO expand functionality to return all related files
    """Returns path like string for a single specified file or directory

    Parameters
    ----------
    filename
        string which  is the name of the file to be found

    Returns
    -------
        Path like string for specified file"""

    for root, dirs, files in os.walk(os.getcwd(), False):
        for name in files:
            if filename in name :
                return os.path.join(root, name)
        for dir in dirs:
            if filename in dir:
                return os.path.join(root, dir)

    return FileNotFoundError

if __name__ == '__main__':
    print(find_filepath('networks'))
    print(find_filepath('basic_template'))

