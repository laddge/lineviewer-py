import sys
import shutil
import datetime
import sqlite3
import argparse


def list():
    conn = sqlite3.connect("/data/data/jp.naver.line.android/databases/naver_line")
    cur = conn.cursor()
    cur.execute("SELECT chat_id FROM chat ORDER BY last_created_time desc;")
    chats = cur.fetchall()
    res = []
    for chat in chats:
        cur.execute("SELECT name FROM contacts WHERE m_id = '{}';".format(chat[0]))
        contact = cur.fetchall()
        if contact:
            res.append(contact[0][0])
        else:
            cur.execute("SELECT name FROM groups WHERE id = '{}';".format(chat[0]))
            group = cur.fetchall()
            if group:
                res.append(group[0][0])
    for i in range(len(res)):
        print(f"{i}. {res[i]}")


def view(i, c=0):
    conn = sqlite3.connect("/data/data/jp.naver.line.android/databases/naver_line")
    cur = conn.cursor()
    cur.execute("SELECT m_id, name FROM contacts")
    names = cur.fetchall()
    cur.execute("SELECT id, name FROM groups")
    names.append(cur.fetchall())
    ntable = {}
    for n in names:
        ntable.update({n[0]: n[1]})
    cur.execute("SELECT chat_id FROM chat ORDER BY last_created_time desc;")
    chat_id = cur.fetchall()[i][0]
    cur.execute(
        "SELECT from_mid, created_time, content FROM chat_history WHERE chat_id = '"
        + chat_id
        + "' ORDER BY created_time;"
    )
    chats = cur.fetchall()
    ts = shutil.get_terminal_size()
    print('─' * ts[0])
    c = 0 if c < 0 else c
    for chat in chats[-c:]:
        if chat[0]:
            print("\033[007;1m " + ntable[chat[0]] + " \033[m")
        else:
            print("\033[042;1m self \033[m")
        print(
            "["
            + datetime.datetime.fromtimestamp(int(chat[1]) / 1000).strftime(
                "%y-%m-%d %H:%M"
            )
            + "]"
        )
        print()
        print(chat[2])
        print()
        ts = shutil.get_terminal_size()
        print('─' * ts[0])


parser = argparse.ArgumentParser()
parser.add_argument('-l', '--list', action='store_true')
parser.add_argument('-i', '--index', type=int)
parser.add_argument('-c', '--count', type=int, default=0)
args = parser.parse_args()
if args.list:
    list()
else:
    if args.index is None:
        parser.print_help()
        sys.exit(1)
    view(args.index, args.count)
