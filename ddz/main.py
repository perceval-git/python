import json
from time import gmtime, strftime

from openpyxl import Workbook
obj = json.load(open("./test_readable.json"))
wb = Workbook()
ws = wb.active
f = open("text_test.txt", "w+")
for date, data in obj.items():
    if sum([len(pars) for pars in data.values()]) == 0:
        continue
    f.write("{}:\n".format(date))
    print("{}:".format(date))
    for time, pars in data.items():
        for para in pars:
            f.write("{} | {}-{} | {}\n".format(para[0], para[2], para[3], ', '.join(para[1])))
            print("{} | {}-{} | {}".format(para[0], para[2], para[3], ', '.join(para[1])))

f.write(strftime("\n%Y-%m-%d %H:%M:%S", gmtime()))
print(strftime("\n%Y-%m-%d %H:%M:%S", gmtime()))
