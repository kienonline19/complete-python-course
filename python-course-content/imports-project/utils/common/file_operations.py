from utils.find import NotFoundError


def save_to_file(content, filename):
    with open(filename, 'w') as fw:
        fw.write(content)


def read_file(filename):
    with open(filename, 'r') as fr:
        return fr.read()


# print('hello')
print(__name__)
