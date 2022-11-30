import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file, delimeter=',', new_line='\n') -> list[dict]:
    with open(file) as f:
        list_csv = [line.replace(new_line, '').split(delimeter) for line in f]
        headers = list_csv[0]
        values = list_csv[1:]
        list_answer = []
        for line in values:
            dict_ = {headers[i]: line[i] for i in range(len(line))}
            list_answer.append(dict_)
    return list_answer


# TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
