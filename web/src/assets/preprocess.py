'''
ぐるなびapiからとってきたjson fileを整形するコード
'''
import argparse
import json
import re
import copy


def refine_price(text):
    text = re.search(r'(?P<price>[0-9]*)円', text)
    if text is not None:
        return int(text.group("price"))
    return None


def valid_key(text):
    return re.search(r'税込[0-9]*円', text) is None


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input', type=str, help='input file path')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    json_data = json.load(open(args.input))
    output = []
    for data in json_data:
        output_dict = dict()
        output_dict["name"] = data["name"]
        output_dict["category"] = data["category"]
        output_dict["icon_url"] = data["img"]
        output_dict["lattitude"] = data["lat"]
        output_dict["longitude"] = data["lng"]
        output_dict["menu"] = dict()
        for k, v in data["menu"].items():
            if not valid_key(k):
                continue
            price = refine_price(v)
            if price is None:
                continue
            output_dict["menu"][k] = price

        output_dict["address"] = data["address"]
        output_dict["description"] = data["opentime"]
        output.append(copy.deepcopy(output_dict))

    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
