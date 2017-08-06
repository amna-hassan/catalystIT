import MySQLdb
import logging
import csv
import sys
def connect_db():
    db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                        name char(50),
                        surname char(50),
                        email char(200),
                        );""")
    logging.info('Database Connection Succesful')
    return [cursor,db]
    
def insert_csv_to_db(input_csv_file):
    cursor,db = connect_db()
    with open(input_csv_file) as c:
        rea=csv.reader(c,delimiter=',')
        for name,surname,email in rea:
            try:
                if name.isalpha():name=name.capitalize().strip()
                if surname.isalpha:surname=surname.capitalize().strip()
                if email:valid=re.match(r"""(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.
                               [a-zA-Z0-9-.]+$)""",email.strip())
            except Exception as e:
                print('Incomplete Input',e)
                logging.warning('Incomplete Input')
                continue
            if valid:
                cursor.execute("""INSERT INTO users SET (name,surname,email) VALUE
                            ('"""+name+"""','"""+surname+"""','"""+email+"""';""")
                cursor.commit()
            else:
                print(name,surname,email,'Invalid Email Address')
                logging.warning('Invalid Email Address')
                continue
        db.close()
if __name__ == '__main__':
    insert_csv_to_db(sys.argv[1])
