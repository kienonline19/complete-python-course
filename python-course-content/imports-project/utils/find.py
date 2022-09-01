# from .common.file_operations import save_to_file
# from utils.common.file_operations import save_to_file


class NotFoundError(Exception):
    pass


def find_in(iterable, finder, expected):
    for x in iterable:
        if finder(x) == expected:
            return x

    raise NotFoundError(f'{expected} not found in provided iterable.')


if __name__ == '__main__':
    print(find_in(['Rolf', 'Jose', 'Jen'], lambda x: x, 'Rolf'))
