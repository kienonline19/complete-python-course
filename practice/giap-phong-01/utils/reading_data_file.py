def get_input_data():
    with open('data/inp.txt', 'r', encoding='utf-8') as fr:
        return [line.strip() for line in fr]


def read_common_pattern():
    with open('data/COMMON_PATTERN.DAT', 'r', encoding='utf-8') as fcp:
        return fcp.read()
