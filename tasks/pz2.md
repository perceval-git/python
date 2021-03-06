## Практическое занятие №2. Основные типы данных в Python

### Рассматриваемые вопросы
1. int
2. bool
3. str
4. None
5. if, for, while, def

### Домашнее задание
К следующему занятию прочитать главы Getting Started и Git Basics из книги Pro Git. Книгу можно найти по адресу https://git-scm.com/book/ru/v2. Есть русское и английское издания.

### Числовой тип данных - int
Из первого занятия вы знакомы со справкой help() или pydoc, с помощью dir() вы можете изучать любой объект. Примеры численных типов данных

```python
a = 100
b = 36.6
c = 15 + 2j
```
С помощью type() определите, какими типами данных являются переменные a, b и c. Основные операции:

```python
a + b
a * b
a ** b  # возведение в степень
102 / 10
102 // 10  # целочисленное деление
c.real
c.imag
```
Имеются и битовые операции |, \^, &, <<, >>, ~.

Используем знакомую нам функцию dir для числа

```python
num = 7
dir(a)
```
Для переменной num определено множество методов. Напрашивается вопрос, как вообще переменные могут обладать методами. Ответ - в особенности устройства языка Python. Переменные является объектами. На C-уровне определена структура PyObject:

```C
typedef struct _object {
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt; // Счетчик ссылок
    struct _typeobject *ob_type; // Указатель на тип объекта
} PyObject;
```
Эта структура содержит два важных поля. Поле ob_refcnt - счётчик ссылок, и когда мы создаём новую связь переменной с объектом, он увеличивается на единицу. Если какая-то связь становится не нужна, соответствующий счётчик ссылок на единицу уменьшается. Когда он достигает нуля, объект удаляется из памяти. Так в Python организована автоматическая сборка мусора. Второе важное поле - указатель на тип объекта. Этот указатель может менять своё значение в процессе работы программы, и именно таким образом в Python реализована динамическая типизация.

Также реализованы не только простые типы данных, но модули, функции и классы. Все они являются объектами со своими методами и атрибутами. Из этого следует, то что в Python любой объект можно присвоить переменной или передать как аргумент в функцию.

### Логический тип данных - bool
Логический тип данных представлен значениями True и False. Обратите внимание на заглавную первую букву.

```python
3 > 4
3 >= 6
3 >= 3
x = 5
# поддерживаются даже такие конструкции
3 < x < 10
8 < x < 10
```
Логические операции представлены словами and, or, not. То есть не x будет написано как not x, что существенно повышает читаемость кода. Важный нюанс - результат работы логических операций and и or не является bool. Python сохраняет численное значение определяющего аргумента, например,

```python
5 and 2 == 2
5 or 2 == 5

```


Сформулируем выражение для определения високосного года. Год високосный, если он кратен 4, но при этом не кратен 100, либо кратен 400.

```python
year = 2019
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap)
```
Но это не Python-style, как говорят. В модуле calender есть функция islear для определения високосного года.

```python
import calendar

print(calendar.isleap(2019))
print(calendar.isleap(1980))
```
### Строки - str

```python
a = 'это строка'
b = "и это строка"  # просто внутри можно использовать одинарную кавычку без экранирования
c = """и это строка
но во много строк
"""

# строки можно просто складывать
d = a + b

# можно получать подстроки разного вида
e = a[0:3]
```
Последняя операция - так называемые срезы (slices). Общий вид у неё такой str[start:stop:step]. При этом по умолчанию start=0, stop=длине строки, step=1, и эти значения можно не указывать. Попробуйте примеры ниже:

```python
a = '1234567890'
a[5:7]
a[:5]
a[5:]
a[::2]
```
Операция срезов настолько удобная, что используется повсеместно. При этом в скобках допускаются отрицательные символы, что значит "с конца". Например:

```python
a[-3:]  # только 3 последних символа
a[:-3]  # всё, кроме трёх последних
a[::-1]  # строка в обратном порядке
```
Ещё ряд полезных методов для строк

```python
len(b)
b.upper()

# проверка наличия подстроки в строке
if 'строка' in b:
    print('нашёл')
    
# итерация по буквам
for letter in c:
    print('Нашёл букву ', letter)
```
Метод str() позволяет получить строку из любого объекта, а метод int() позволяет получить целое число из строки. Есть возможность разбить строку на части, разделённые любым символом (или группой символов). Результатом является список, этот тип данных мы расмотрим на следующим занятии. Но Питон поддерживает множественное присваивание, воспользуемся им. После каждой строки проверяйте содержимое a и b.

```python
# множественное присваивание
a, b = 7, 17
# кстати, так можно менять переменные местами
a, b = b, a

a, b = 'моя строка'.split(' ')
a, b = '1234'.split('23')
```

Существуют несколько способов форматирования строк

```python
answer = input('Введите число: ')
print('Вы ввели %s' % answer)
# если нужно подставить 2 строки, то синтаксис чуть сложнее
print('Вы ввели %s. Точно %s?' % (answer, answer))

print ('Форматировать ваш ответ {0} можно и так'.format(answer))

print ('Если много подстановок, то в порядке аргументов можно запутаться. Их можно именовать. А вы ввели {number}. Но вариантов больше, чем {count}'.format(number=answer, count=5))

# доступно с Python3.6 - так называемые f-строки
subject = 'оптимизация'
author = 'Дональд Кнут'
print(f'Преждевременная {subject} - корень всех зол. {author})
```


### Объект None
Аналог нулевого указателя в C. Например, если данных ещё нет, можно использовать None. Важным нюансом является проверка на None, которая выглядит так

```python
if answer is None:
    print('Ответа ещё нет')
```
Оператор is проверяет, является ли объект тем же самым (то есть одинаков ли у них id). Очевидно, что Питон не создаёт множество различных None-объектов, а всегда пользуется одним и тем же.

### Операторы условных переходов if, for, while. Создание функций
Перед вами пример небольшой программы Определятор. Определена функция, которая умеет распознавать 3, 4 и 5 группы третьего курса. В main циклом for просматриваются ряд групп. После чего запрашивается пользовательский ввод до тех пор, пока не будет введено exit или q. Этот код демонстрирует простые моменты использования if, for, while и def.

```python
def group_parser(group):
    if not group.startswith('733'):
        print('Это не группа 3 курса')
        return
        
    if group.endswith('3'):
        print('%s - Третья группа' % group)
    elif group.endswith('4'):
        print('%s - Четверная группа' % group)
    elif group.endswith('5'):
        print('%s - Пятая группа' % group)
    else:
        print('%s - Непонятная группа' % group)

def main():
    """Определятор"""
    group_parser('abc')
    for group_num in range(7331, 7336):
        group = str(group_num)
        group_parser(group)
        
    answer = input('Попробуйте выйти: ')
    while answer != 'exit' and answer != 'q':
        answer = input('Неправильно! Попробуйте ещё раз: ')
    print('Успех!')
    
if __name__ == '__main__':
    main()
```

### Самостоятельная работа
1. Написать функцию shout\_on\_me, которая просит пользователя ввести строку, а результат отправляет ему в верхнем регистре. Выход по вводу exit. Пример вывода такой:

    ```
    Что ты сказал? отойди
    Сам ты ОТОЙДИ. И не кричи на меня
    
    Что ты сказал?
    ```

1. Написать калькулятор, реализующий +. Пользователь вводит 1+4, ему возвращается 5. Выход по вводу exit. Пример вывода

    ```
    Введите выражение: 5+2
    7
    
    Введите выражение: 10+11
    21
    ```
    Подсказка: воспользуйтесь split и множественным присваиванием. В этом задании считайте, что обязательно два числа, между ними плюс, другие символы (в том числе пробел) не допускаются.

1. Доработайте Определятор так, чтобы при вводе слова "угадайка" вместо номера группы запускалась Угадайка по выбору числа из ПЗ1, при вводи "покричи" запускась функция shout\_on\_me из первого задания, при вводе "калькулятор" запускался калькулятор из второго задания. **Замечание**. Слова "угадайка", "калькулятор" и "покричи" принимать в любом регистре, то есть "Угадайка", "уГаДаЙкА" или иные варианты.

1. Весь наработанный код загрузить в свой личный проект python на gitlabnto. Воспользуйтесь [инструкцией на вики](http://gitlabnto/anetto/wiki/wikis/gitlab-ssh) (вам нужен вариант 1). Нужно создать новый проект с названием python, приватный, и добавить anetto в members проекта с ролью developer. Не забудьте сохранить ssh-ключи для работы из другого класса.