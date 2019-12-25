# -*- coding: utf-8 -*-
"""Выполнение программы для преобразования данных из input_file.json в out.xlsx"""
import main_prog.json2xlsx

# КАК УСТАНОВИТЬ: sudo python3 to_setup.py install
# КАК ЗАПУСТИТЬ: tableK732 test_readable.json -o out_file.xlsx
# (можно и без -o out_file.xlsx, есть default_file "timetableK732.xlsx")


def main():
    """Последовательность вызова методов"""
    arg = main_prog.json2xlsx.arguments_parser().parse_args(main_prog.json2xlsx.sys.argv[1:])
    json_object = main_prog.json2xlsx.load_data(arg.input.name)
    json_object = main_prog.json2xlsx.sort_data(json_object)
    days = main_prog.json2xlsx.parse_json(json_object)
    main_prog.json2xlsx.write(days, arg.out)
    print("Готово!")


if __name__ == '__main__':
    main()
