"""Each value in the Json-object represents as
{
    'Date':
            {
                'Note_1' : list_info_about_teachers,
                ...
                'Note_4' : list_info_about_teachers
            }
}
Therefore, there is defines a parser of json-object,
then defines a parser of Notes and list of teachers
with theirs attributes(name, groups, classroom, is computer)"""

# pylint: disable=too-few-public-methods

from src.data_json import load_data
from src.date import to_date, WEEKDAY

NAME_INDEX = 0
GROUPS_INDEX = 1
CLASSROOM_INDEX = 2
IS_COMPUTER_INDEX = 3


def parse_teachers(list_info):
    """Gets a list of teachers with attributes"""
    teachers = []
    if list_info:
        for info in list_info:
            if info:
                name = info[NAME_INDEX]
                attributes = [info[GROUPS_INDEX], info[CLASSROOM_INDEX], info[IS_COMPUTER_INDEX]]
                teachers.append(Teacher(name, attributes))
    return teachers or None


def parse_notes(list_notes: dict, kvant=False) -> tuple:
    """Gets a list of notes classes like 'title' : list_of_teachers_with_attributes """
    kvants = set()
    notes = [[], []]

    for title, value in list_notes.items():
        teachers = parse_teachers(value)
        if teachers:
            if kvant:
                for teacher in teachers:
                    if teacher.is_kvant:
                        kvants.add(teacher)
                        teachers.remove(teacher)

            if teachers:
                notes[0].append(Note(title, teachers))

    if kvants:
        notes[1].append(Note("K", kvants))

    return tuple(notes) if notes[0] or notes[1] else None


def parse_json(json_object: dict, kvant=False, date_filter=None) -> tuple:
    """Function parses json object to a list of days"""
    days = []

    if date_filter:
        date_start, date_end = date_filter.split(':')
        date_start = to_date(date_start)
        date_end = to_date(date_end)

    for date, value in json_object.items():
        date_object = to_date(date)

        if date_filter:
            if date_object < date_start:
                continue
            if date_object > date_end:
                break

        notes = parse_notes(value, kvant)
        if notes:
            weekday = WEEKDAY[date_object.weekday()]
            day = Day(date + ' (' + weekday + ')', notes)
            days.append(day)
    return tuple(days) or None


class Day:
    """Class contains info about educational day like: date - notes"""

    def __init__(self, date, notes):
        self.date = date
        self.notes = notes[0]
        self.kvants = notes[1]


class Note:
    """Class represents info about note of lesson like: title - list of teachers"""

    def __init__(self, title, teachers):
        self.title = title
        self.teachers = teachers

    def __eq__(self, other):
        return self.title == other.title and self.teachers == other.teachers \
            if isinstance(other, Note) else False


class Teacher:
    """Contains information about the teacher"""

    def __init__(self, name, attributes):
        self.name = name
        self.groups = attributes[0]
        self.classroom = attributes[1]
        self.is_computer = attributes[2]
        self.is_kvant = True if 'КВАНТ' in self.classroom else False

    def __eq__(self, other):
        return self.name == other.name and self.groups == other.groups \
               and self.classroom == other.classroom \
               and self.is_computer == other.is_computer \
            if isinstance(other, Teacher) else False

    def __hash__(self):
        hash_sum = hash(self.name) + hash(self.is_kvant) + \
                   hash(self.classroom) + hash(self.is_computer)

        for group in self.groups:
            hash_sum += hash(group)

        return hash(hash_sum)
