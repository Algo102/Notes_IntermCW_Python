import os
import random
import log as lg

file = ['notes.csv', 'history.log']

file_head = [
    'id_note;title;content;date_create;date_edit\n',
    ''
]


def search_max_id():
    if check_file(file[0]):
        with open(file[0], 'r', encoding='utf-8') as f1:
            line = f1.readline()
            lines = f1.readlines()
            idmax = 0
            index = 0
            for line in lines:
                index += 1
                idi = int(line.strip('\n').split(";")[0])
                if idi > idmax: idmax = idi
            return idmax, index


def search_index_rec(ids):
    try:
        with open(file[0], 'r', encoding='utf-8') as f1:
            line = f1.readline()
            lines = f1.readlines()
            index = 1
            for line in lines:
                index += 1
                st = line.strip('\n').split(";")[0]
                if st == ids:
                    return index
    except:
        print("File error")


def check_file(f1: str):
    if os.access(f1, os.F_OK):
        return True
    else:
        return False


def writing_scv(rec: list, fl: str, idr=0):
    if check_file(fl):
        with open(fl, 'a', encoding='utf-8') as f1:
            if idr == 0:
                idr = search_max_id()[0] + 1
            rec.insert(0, idr)
            f1.write(f'{rec[0]};{rec[1]};{rec[2]};{rec[3]};{rec[4]}\n')
            lg.logger_history("New note", f"{rec[0]} {rec[1]} {rec[3]}", "Successfully")
    else:
        print(f"File {fl} not found!")
        lg.logger_history("New note not saved", f"{rec[0]} {rec[1]} {rec[3]}", "File not found")


def creat_file():
    for i, f in enumerate(file):
        if not check_file(f):
            with open(f, 'w', encoding='utf-8') as f1:
                f1.write(file_head[i])
                lg.logger_history("File created ", f"{f}", "")


def read_scv(fl: str):
    if check_file(fl):
        with open(fl, 'r', encoding='utf-8') as f1:
            return f1.readlines()
    else:
        print(f"File {fl} not found!")
        lg.logger_history("File read error", f"{fl}", "not found")
        return []


def read_rec_csv(fl: str, ids):
    if check_file(fl):
        with open(fl, 'r', encoding='utf-8') as f1:
            lines = f1.readlines()
            for line in lines:
                st = line.strip('\n').split(";")
                if st[0] == ids:
                    return st
    else:
        print(f"File {fl} not found!")
        lg.logger_history("File read error", f"{fl}", "not found")
        return []


def delete_rec_in_file(ids):
    try:
        with open('notes.csv', 'r', encoding='utf-8') as fr:
            lines = fr.readlines()

            with open('notes.csv', 'w', encoding='utf-8') as fw:
                for line in lines:
                    st = line.strip('\n').split(";")[0]
                    if st != ids:
                        fw.write(line)
                    else:
                        lg.logger_history("Note deleted", f"id={st}", "Successfully!")
                        delrec = st
                return delrec
    except:
        print("Error")