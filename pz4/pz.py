# -*- coding: utf-8 -*-
"""
pz4
"""

import os


def first_task():
    """
    Аналог 'ls'
    """
    parent_path = "/home/user/"
    folder_path = input("Введите название папки: ")
    if ".." in folder_path:
        print("Нет доступа")
        return
    folder_path.replace(" ", r"\ ")
    path = os.path.join(parent_path, folder_path)
    if parent_path not in path:
        print("Нет доступа")
        return
    try:
        files = os.listdir(path)
        print(files)
    except FileNotFoundError as error:
        print("Каталога не существует", error)
        return


if __name__ == '__main__':
    first_task()
