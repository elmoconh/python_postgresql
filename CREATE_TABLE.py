from config import init_db
import sys


args = sys.argv
set_names = set(args[1:])

def create_table(name):
    conn = init_db.connect()
    cur = conn.cursor()

    query = "CREATE TABLE "+ name +"(id_"+name+" SERIAL PRIMARY KEY);"
    
    try:
        cur.execute(query)
        conn.commit()
        cur.close()
        print("Table created successfully")
    except Exception as e:
        print(e)
        conn.rollback()
        cur.close()
        print("Table creation failed")


if __name__ == '__main__':
    for set_name in set_names:
        print('Create Table: ' +set_name+'...')
        create_table(set_name)