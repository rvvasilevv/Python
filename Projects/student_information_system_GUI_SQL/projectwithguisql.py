from tkinter import *
import tkinter #module for gui
import pymysql

prozorec = tkinter.Tk()
prozorec.configure(bg="blue")#Color
prozorec.geometry("800x450") #SIZE
L = Label(prozorec, text='Enter Student Id: ', font=("arial", 30), fg='red',bg='blue')#Body/fg=color,font=font and size/bg=background
L.grid(row=0, column=0)
E= Entry(prozorec, bd=5,width=50,bg='blue')
E.grid(row=0, column=1)

L1 = Label(prozorec, text='Enter Student Name: ', font=("arial", 30), fg='red',bg='blue')
L1.grid(row=1, column=0)
E1= Entry(prozorec, bd=5,width=50,bg='blue')
E1.grid(row=1, column=1)

L2 = Label(prozorec, text='Enter Student Address: ', font=("arial", 30), fg='red',bg='blue')
L2.grid(row=2, column=0)
E2= Entry(prozorec, bd=5,width=50,bg='blue')
E2.grid(row=2, column=1)


def ButtonFunciton(selection):
    print("Student id is : ", E.get())
    print("Student Name is : ", E1.get())
    print("Student Address is : ", E2.get())
    id = E.get()
    name = E1.get()
    address = E2.get()
    if selection in ('Insert'):
        con = pymysql.connect(host='localhost',user='root',password='123brawo123',database='studentproject')
        cursr = con.cursor()
        query = "CREATE TABLE IF NOT EXISTS student (id CHAR (20) PRIMARY KEY,name CHAR(20),address CHAR(20))"
        cursr.execute(query)
        con.commit()
        print("Table student created successfully")
        insert_command='INSERT INTO student (id,name,address) VALUES ("%s","%s","%s")'%(id,name,address)
        try:
            cursr.execute(insert_command)
            con.commit()
            print('Student saved successfully',id,name,address)
            con.close()
        except :
            print("Error occurred at database data insertion")
            con.rollback()# reverses all changes if there is a Error with the rollback function
            con.close()
    elif selection in ('Update'):
        try:
            updatequery="UPDATE STUDENT SET name='%s'"%(name)+",address = '%s'"%(address)+" WHERE id = '%s'"%(id)
            con = pymysql.connect(host='localhost', user='root', password='123brawo123', database='studentproject')
            cursr = con.cursor()
            cursr.execute(updatequery)
            con.commit()
            con.close()
            print("Student updated successfully..",id)
        except:
            print('Error occured at database Updation')
            con.rollback()
            con.close()
    elif selection in ('Delete'):
        try:
            deletequery=f'DELETE FROM student WHERE id={id}'
            con = pymysql.connect(host='localhost', user='root', password='123brawo123', database='studentproject')
            cursr = con.cursor()
            cursr.execute(deletequery)
            con.commit()
            con.close()
            print("Student deleted successfully..", id)
        except:
            print('Error occured at database Deletion')
            con.rollback()
            con.close()
    elif selection in ('Select'):
        try:
            selectquery=f'SELECT * FROM student WHERE id={id}'
            con = pymysql.connect(host='localhost', user='root', password='123brawo123', database='studentproject')
            cursr = con.cursor()
            cursr.execute(selectquery)
            rows=cursr.fetchall()
            addres1 = ''
            name1 = ''
            id1 =''
            for row in rows:
                id1=row[0]
                addres1=row[2]
                name1=row[1]
            E.delete(0,END)
            E1.delete(0,END)
            E2.delete(0,END)
            E.insert(0,id1)
            E1.insert(0, name1)
            E2.insert(0, addres1)
            con.close()
            print("Student Fetch successfully :", id)
        except:
            print('Error occured at database Deletion')
            con.close()



Button1=tkinter.Button(text='Insert',fg='black',bg='orange',font=('arial',20,'bold'),command=lambda:ButtonFunciton('Insert')) #fg-font color,bg-background color INSERT BUTTON
Button1.grid(row=5, column=0)

Button2=tkinter.Button(text='Update',fg='black',bg='orange',font=('arial',20,'bold'),command=lambda:ButtonFunciton('Update')) #UPDATE BUTTON
Button2.grid(row=5, column=1)

Button3=tkinter.Button(text='Delete',fg='black',bg='orange',font=('arial',20,'bold'),command=lambda:ButtonFunciton('Delete')) #DELETE BUTTON
Button3.grid(row=7, column=0)

Button4=tkinter.Button(text='Select',fg='black',bg='orange',font=('arial',20,'bold'),command=lambda:ButtonFunciton('Select')) #SELECT BUTTON
Button4.grid(row=7, column=1)


prozorec.mainloop()
