# Timetable of classes
## Description
This is a parser of JSON files to Excel table.

##### Positional arguments:  

```input``` - input JSON file

##### Optional arguments:

```-o, --output``` - output .xlsx file

## Usage
- ```git clone https://github.com/Nikshepel/timetable-classes.git```
- ```cd timetable-classes```
- ```sudo python3 setup.py install```

- ```timetable-classes [-o, --output <output_xlsx>] json_file```



## Example:

This command converts my_json_file.json (JSON file) to file.xlsx (Excel file)  

```timetable-classes -o file.xlsx my_json_file.json```
