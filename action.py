import file as fi
from datetime import datetime as dtime
import log as lg

file = fi.file[0]


def input_data(mode=0):
    data_rec = []
    title = input('Enter title: ')
    data_rec.append(title)
    content = input('Enter note: ')
    data_rec.append(content)
    tm = dtime.now().strftime('%d.%m.%y %H:%M')
    data_rec.append(tm)
    data_rec.append(tm)

    return data_rec


def add_note():
    rec = input_data()
    print(rec)
    fi.writing_scv(rec, file)
    return 1


def edit_note():
    ide = input('Enter ID note for EDIT: ')
    reco = fi.read_rec_csv(file, ide)
    print(reco)
    fi.delete_rec_in_file(ide)
    rec = input_data()
    recn = [rec[0], rec[1], reco[3], rec[3]]

    fi.writing_scv(recn, file, ide)
    print("Note saved")
    return 1


def delete_note():
    idd = input('Enter ID note for DELETE: ')
    iddok = fi.delete_rec_in_file(idd)
    print(f"Note {iddok} deleted!")
    return 1


def view_note():
    idr = input('Enter ID to VIEW note: ')
    rec = fi.read_rec_csv(file, idr)
    print(rec)
    return 1


def view_search_title():
    work = fi.read_scv(file)
    title = input('Enter title: ')
    for line in work:
        st = line.strip('\n').split(";")
        if title in st[1]:
            print(st)
    return 1


def view_all_notes():
    print("All notes\n"
          f"{'=' * 30}")
    wk = []
    work = fi.read_scv(file)
    for w in work:
        wk = w.replace("\n", "").split(";")
        print(wk)
    print(f"{'-' * 30}")
    lg.logger_history("Output all notes", "", "")
    return 1