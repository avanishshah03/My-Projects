import mysql.connector as driver
import sys
def menu():
    loop='y'
    while(loop=='y' or loop=='Y'):
        print("........MENU.......")
        print("1. CREATE DATABASE")
        print("2. SHOW DATABASES")
        print("3. CREATE TABLE")
        print("4. SHOW TABLES")
        print("5. INSERT RECORD")
        print("6. UPDATE RECORD")
        print("7. DELETE RECORD")
        print("8. SEARCH RECORD")
        print("9. DISPLAY RECORD")
        print()
        print()
        choice=int(input("Enter the choice (1-9) : "))
        if(choice==1):
            create_database()
        elif(choice==2):
            show_databases()
        elif(choice==3):
            create_table()
        elif(choice==4):
            show_tables()
        elif(choice==5):
            insert_record()
        elif(choice==6):
            update_record()
        elif(choice==7):
            delete_record()
        elif(choice==8):
            search_record()
        elif(choice==9):
            display_record()
        else:
            print("Wrong Choice.")
        loop=input("Press 'y' to continue...")
    else:
        sys.exit()
        
def create_database():
    con=driver.connect(host='localhost',user='root', passwd='')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('create database if not exists employee')
    print()
    print("Database Created")
    con.close()
    
def show_databases():
    con=driver.connect(host='localhost',user='root',passwd='')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('show databases')
    for i in cur:
        print(i)
    con.close()
    
def create_table():
    con=driver.connect(host='localhost',user='root',passwd='',database='employee')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('create table if not exists emp(id integer primary key, ename varchar(15), salary float)')
    print()
    print("Table Created -> EMP")
    cur.execute('DESC emp')
    print("+-------------|--------------|-----------+")
    print("+Column Name  |DataType(Size)|NULL       |")
    print("+-------------|--------------|-----------+")
    for i in cur:
        print('|{0:12} | {1:12} | {2:10}|'.format(i[0],i[1],i[2])) 
    print("+-------------|--------------|-----------+")
    con.close()
    
def show_tables():
    con=driver.connect(host='localhost',user='root',passwd='',database='employee')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('show tables')
    for i in cur:
        print(i)
    con.close()

def insert_record():
    con=driver.connect(host='localhost',user='root',passwd='',database='employee')
    if con.is_connected():
        #print("Successfully Connected")
        cur=con.cursor()
        ID=int(input("ENTER EMPLOYEE ID : "))
        NAME=input("ENTER NAME OF EMPLOYEE : ")
        SALARY=float(input("ENTER EMPLOYEE SALARY : "))
        query1="INSERT INTO emp(id,ename,salary) VALUES({},'{}',{})".format(ID,NAME,SALARY)
        cur.execute(query1)
        con.commit()
        print('Record Inserted')
        con.close()
    else:
        print("Error : Not Connected")

def update_record():
    con=driver.connect(host='localhost',user='root',passwd='',database='employee')
    cur=con.cursor()
    d=int(input("Enter Employee ID for update record : "))
    ID=int(input("ENTER NEW EMPLOYEE ID : "))
    name=input("ENTER NEW NAME OF EMPLOYEE : ")
    salary=float(input("ENTER NEW SALARY FOR EMPLOYEE : "))
    query1="update emp set id=%s, ename='%s', salary=%s where id=%s" %(ID,name,salary,d)
    cur.execute(query1)
    con.commit()
    print("Record Updated")
    con.close()

def delete_record():
    con=driver.connect(host='localhost',user='root',passwd='',database='employee')
    cur=con.cursor()
    d=int(input("Enter Employee ID for deleting record : "))
    query1="delete from emp where id={0}".format(d)
    cur.execute(query1)
    con.commit()
    print("Record Deleted")
    con.close()

def search_record():
    con=driver.connect(host='localhost',user='root',passwd='',database='employee')
    cur=con.cursor()
    print("ENTER THE CHOICE ACCORDING TO YOU WANT TO SEARCH RECORD: ")
    print("1. ACCORDING TO ID")
    print("2. ACCORDING TO NAME")
    print("3. ACCORDING TO SALARY")
    print()
    choice=int(input("ENTER THE CHOICE (1-3) : "))
    if choice==1:
          d=int(input("Enter Employee ID which you want to search : "))
          query1="select * from emp where id=%s" %(d)
    elif choice==2:
          name=input("Enter Employee Name which you want to search : ")
          query1="select * from emp where ename='%s'" %(name)
    elif choice==3:
          sal=float(input("Enter Employee Salary which you want to search : "))
          query1="select * from emp where salary=%s" %(sal)
    else:
          print("Wrong Choice")
    cur.execute(query1)
    rec=cur.fetchall()
    count=cur.rowcount
    print("Total no. of records found : ",count)
    for i in rec:
        print(i)
    print("Record Searched")
    con.close()

def display_record():
    con=driver.connect(host='localhost',user='root',passwd='',database='employee')
    if con.is_connected():
        #print("Successfully Connected")
        cur=con.cursor()
        cur.execute('select * from emp')
        rec=cur.fetchall()
        count=cur.rowcount
        print("+----------|--------------|-----------+")
        print("+  Emp ID  |   Emp Name   |   Salary  |")
        print("+----------|--------------|-----------+")
        for i in rec:
            print('|{0:^9} | {1:12} | {2:10}|'.format(i[0],i[1],i[2])) 
        print("+----------|--------------|-----------+")
        print("+   Total no. of records are : ",count,"    |")
        print("+-------------------------------------+")
        #for i in rec:
        #    print(i)
        con.close()
    else:
        print("Error : Database Connection is not success" )

menu()


