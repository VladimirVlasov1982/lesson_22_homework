csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = _read(csv)
    data = _sorted_data(data)
    return _filtered_data(data)


def _read(csv):
    return [x.split(";") for x in csv.split('\n')]


def _sorted_data(data):
    return sorted(data, key=lambda x: int(x[1]))


def _filtered_data(data):
    return [item for item in data if int(item[1]) > 10]


if __name__ == '__main__':
    print(get_users_list())
