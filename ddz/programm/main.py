# -*- coding: utf-8 -*-
"""Выполнение программы для преобразования данных из input_file.json в out.xlsx"""
import programm.json2xlsx


def main():
    """Последовательность вызова методов"""
    arg = programm.json2xlsx.arguments_pars().parse_args(programm.json2xlsx.sys.argv[1:])
    json_object = programm.json2xlsx.load_data(arg.input.name)
    json_object = programm.json2xlsx.sort_data(json_object)
    days = programm.json2xlsx.parse_json(json_object)
    programm.json2xlsx.write(days, arg.out)
    print("Готово! Создан файл ", arg.out)


if __name__ == '__main__':
    main()
