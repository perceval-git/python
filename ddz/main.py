# -*- coding: utf-8 -*-
"""Выполнение программы для преобразования данных из input_file.json в out.xlsx"""
import json2xlsx


def main():
    """Последовательность вызова методов"""
    json_object = json2xlsx.load_data(input("Введите название json-файла: "))
    json_object = json2xlsx.sort_data(json_object)
    days = json2xlsx.parse_json(json_object)
    json2xlsx.write(days)
    print("Готово!")


if __name__ == '__main__':
    main()
