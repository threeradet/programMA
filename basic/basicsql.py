
import sqlite3

'''
name = v_name.get()
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_number.get()
    tel = v_tel.get()
'''

#สร้าง connecttion เพื่อเชื่อมต่อ database
conn = sqlite3.connect('maintenance.sqlite3')

# สร้าง cursor # ตัวที่เอาไว้สั่ง sql
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS mt_workorder (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    tsid TEXT,
                    name TEXT,
                    department TEXT,
                    machine  TEXT,
                    problem  TEXT,
                    number  TEXT,
                    tel  TEXT) """) 

def insert_mtworkorder(tsid,name,department,machine,problem,number,tel):
    #create
    with conn:
        command = 'INSERT INTO mt_workorder VALUES (?,?,?,?,?,?,?,?)'
        c.execute(command,(None,tsid,name,department,machine,problem,number,tel))
    conn.commit() #save database
    print('saved')

#insert_mtworkorder('TS1002','ลุง','it','monitor','พัง','PT1992','452')

def view_mtworkorder():
    command = 'SELECT *FROM mt_workorder'
    c.execute(command)
    result = c.fetchall()
    print(result)
    return result


def update_mtworkorder(tsid,field,newvalue):
    with conn:
        command = 'UPDATE mt_workorder SET {} = (?) WHERE tsid=(?)'.format(field)
        c.execute(command,(newvalue,tsid))
    conn.commit()
    print('updated')

#update_mtworkorder('TS1002','problem','ไม่ติด')


def delete_mtworkorder(tsid):
    with conn:
        command = 'DELETE FROM mt_workorder WHERE tsid=(?)'
        c.execute(command,([tsid]))
    conn.commit()
    print('deleted')

delete_mtworkorder('TS1001')




result = view_mtworkorder()
#print(result[1][1])




