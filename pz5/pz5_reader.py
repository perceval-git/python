"""Read files"""
import json
import xml
import xml.etree.ElementTree as etree
from abc import ABC, abstractmethod


class Reader(ABC):
    """Abstract class"""
    @abstractmethod
    def read(self, filename):
        """Read"""


class ReaderJson(Reader):
    """Read JSON files"""
    def read(self, filename):
        """Read method"""
        try:
            with open(filename, "r") as read_file:
                data = json.load(read_file)
        except FileNotFoundError:
            print("File was not found!")
            exit(1)
        except json.decoder.JSONDecodeError:
            print("Invalid syntax in file!")
            exit(1)
        return data


class ReaderXml(Reader):
    """Read XML files"""
    def read(self, filename):
        """Read method"""
        try:
            tree = etree.parse(filename)
        except FileNotFoundError:
            print("File was not found!")
            exit(1)
        except xml.etree.ElementTree.ParseError:
            print("Invalid syntax in file!")
            exit(1)

        root = tree.getroot()
        return root


class ReaderIhl():
    """Iterator"""
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current
        self.current += 1
        return result


if __name__ == "__main__":
    READ_J = ReaderJson()
    BUF = READ_J.read("file.json")
    print(BUF)

    READ_X = ReaderXml()
    BUF = READ_X.read("file.xml")

    print(BUF.tag)

    LENGTH = len(BUF)
    for i in range(LENGTH):
        print(BUF[i].tag + ': ' + BUF[i].text)
