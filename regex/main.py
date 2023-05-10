import re
import csv

employ_list = []

organization_list = []

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

    # Соединияем ФИО:

    def name_list():
        for item in contacts_list:
            full_name=' '.join(item[:3]).split(' ')
            del full_name[3:]
            employ_list.append(full_name)

    # Форматируем номера и должности:

    def phone_formating():
        pattern=re.compile(r'(\+7|8)?\s*\(*(\d{3})\)*-?\s*(\d{3})-?(\d{2})-?(\d{2})\s*([(]?(\w{3}.\s\d{4}[)]?))*')
        substitution = r'+7(\2)\3-\4-\5 \6'
        org_pattern = re.compile(
            r'(ФНС|Минфин).((\w+\s\w+\s.?\s?\w+\s\w+\s\w+\s\w+\s\w+)(\s\w+\s\w+\s\w+\s\w+\s+\w+\s\w\s\w+\s\w+\s\w+)*)*')
        substitution1 = r'\1 \2 \3 \4'
        for item in contacts_list:
            item[5]=pattern.sub(substitution,item[5])
            item[3]=org_pattern.sub(substitution1,item[3])
    # Удаляем лишние значения:

    def del_cav():
        for sign in contacts_list:
            while '' in con:
                sign.remove('')
    # Применяем изменения:

    name_list()
    phone_formating()
    del_cav()

    # Финальное редактирование с использованием нового списка ФИО:
    contacts_list[2].insert(2,contacts_list[4][4])
    contacts_list[7].append(contacts_list[8][1])
    contacts_list.remove(contacts_list[8])
    contacts_list.remove(contacts_list[4])
    contacts_list[1].remove(contacts_list[1][0])
    employ_list.remove(employ_list[-1])

    string=[a for a in employ_list[1:]]

    contacts_list[1].extend(string[0])
    dir = contacts_list[1][-3:]
    contacts_list[1][-3:] = []
    contacts_list[1][:0] = dir
    contacts_list[2].remove(contacts_list[2][0])
    contacts_list[2].extend((string[1]))
    dir1 = contacts_list[2][-3:]
    contacts_list[2][-3:] = []
    contacts_list[2][:0] = dir1
    contacts_list[3].remove(contacts_list[3][1])
    contacts_list[3].remove(contacts_list[3][0])
    contacts_list[3].extend(string[2])
    dir2 = contacts_list[3][-3:]
    contacts_list[3][-3:] = []
    contacts_list[3][:0] = dir2
    contacts_list[4].remove(contacts_list[4][0])
    contacts_list[4].extend(string[4])
    dir3 = contacts_list[4][-3:]
    contacts_list[4][-3:] = []
    contacts_list[4][:0] = dir3
    contacts_list[5].remove(contacts_list[5][0])
    contacts_list[5].extend(string[5])
    dir4 = contacts_list[5][-3:]
    contacts_list[5][-3:] = []
    contacts_list[5][:0] = dir4
    contacts_list[6].remove(contacts_list[6][0])
    contacts_list[6].extend(string[6])
    dir5 = contacts_list[6][-3:]
    contacts_list[6][-3:] = []
    contacts_list[6][:0] = dir5
    contacts_list[3].insert(4,'')
    contacts_list[4].insert(4,'')
    contacts_list[5].insert(4,'')
    contacts_list[6].insert(4,'')

    # Записываем в конечный файл:

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)
