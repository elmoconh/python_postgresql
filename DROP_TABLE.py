from config import init_db
import sys

args = sys.argv
set_names = set(args[1:])


def drop_table(name):
    conn = init_db.connect()
    cur = conn.cursor()

    query = "DROP TABLE "+ name +";"
    
    try:
        cur.execute(query)
        conn.commit()
        cur.close()
        print("Table deleted successfully")
    except Exception as e:
        print(e)
        conn.rollback()
        cur.close()
        print("Table delete failed")


if __name__ == '__main__':
    for set_name in set_names:
        print(set_name)
        drop_table(set_name)