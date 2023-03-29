import re
import csv

employ_list = []

organization_list = []

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

    ##TODO 1: выполните пункты 1-3 ДЗ
    def name_list():
        for item in contacts_list:
            full_name = ' '.join(item[:3]).split(' ')
            del full_name[3:]
            employ_list.append(full_name)

    def phone_formating():
        pattern=re.compile(r'(\+7|8)?\s*\(*(\d{3})\)*-?\s*(\d{3})-?(\d{2})-?(\d{2})\s*[(]?(\w{3}.\s\d{4}[)]?)*')
        substitution = r'+7(\2)\3-\4-\5\6'
        org_pattern = re.compile(
            r'(ФНС|Минфин).((\w+\s\w+\s.?\s?\w+\s\w+\s\w+\s\w+\s\w+)(\s\w+\s\w+\s\w+\s\w+\s+\w+\s\w\s\w+\s\w+\s\w+)*)*')
        substitution1 = r'\1 \2 \3 \4'
        for item in contacts_list:
            item[5]=pattern.sub(substitution,item[5])
            item[3]=org_pattern.sub(substitution1,item[3])
            return

    employ_dict = {}
    for item in employ_list:
        lastname=item[0]
        if lastname not in employ_list:
            employ_dict[lastname]=item[0:]
        else:
            item[0]=item[0:]


    print(employ_dict)
    name_list()
    phone_formating()