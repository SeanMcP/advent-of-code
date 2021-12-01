def get_lines(file):
    return list(map(lambda ln: int(ln.replace("\n", "")), file.readlines()))


def read_file(path):
    with open(path) as file:
        return get_lines(file)
