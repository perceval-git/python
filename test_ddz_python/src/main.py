import sys
import argparse as ap
from src.parser import parse_json
from src.excel_write import write
from src.data_json import load_data
from src.date import sort_data


def arguments_parser():
    parser = ap.ArgumentParser(description="""It parses a JSON-file to .xlsx file""",
                               prog='timetable-classes')

    parser.add_argument('input',
                        help='input JSON file',
                        type=ap.FileType())

    parser.add_argument('-o', '--output',
                        help='output .xlsx file (default="output.xlsx")',
                        default='output.xlsx',
                        type=str)

    parser.add_argument('-k', '--kvant',
                        help='move information about lessons in KVANT to the first line under date',
                        action='store_true')

    parser.add_argument('-d', '--date',
                        help='write information about days between these dates',
                        type=str)

    return parser


def main():
    args = arguments_parser().parse_args(sys.argv[1:])

    json_object = load_data(args.input.name)
    json_object = sort_data(json_object)
    days = parse_json(json_object, args.kvant, args.date)
    write(days, args.output)


if __name__ == '__main__':
    main()
