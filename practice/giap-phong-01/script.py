from utils import reading_data_file as rf
from configparser import ConfigParser

parser = ConfigParser()
parser.read("data/param.config")
FILE_PATTERN = parser.get("file_pattern", "pattern")
inps = rf.get_input_data()
keyword = parser.get("file_pattern", "keyword")

result = {}

for inp in inps:
    file_name = FILE_PATTERN.replace(keyword, inp)
    content = rf.read_common_pattern().replace(keyword, inp)
    result[file_name] = content

for file_name, content in result.items():
    with open(f'output/{file_name}', 'w', encoding='utf-8') as fw:
        fw.write(content)
