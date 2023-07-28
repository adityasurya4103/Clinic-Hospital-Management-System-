#pip install PyMySQL
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import page_after_login

def add_patient():
    #connection for phpmyadmin
    def connection():
        conn = pymysql.connect(
            host='localhost',
            user='root', 
            password='your_password',
            db='PATIENTS_DB',
        )
        return conn

    def refreshTable():
        for data in my_tree.get_children():
            my_tree.delete(data)

        for array in read():
            my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

        my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
        my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

    root = Tk()
    root.title("SIDDHESHWAR CLINIC MANAGEMENT SYSTEM")
    root.geometry("1166x718")

    root.resizable(0, 0)
    root.state('zoomed')
    my_tree = ttk.Treeview(root)


    #placeholders for entry
    ph1 = tk.StringVar()
    ph2 = tk.StringVar()
    ph3 = tk.StringVar()
    ph4 = tk.StringVar()
    ph5 = tk.StringVar()

    #placeholder set value function
    def setph(word,num):
        if num ==1:
            ph1.set(word)
        if num ==2:
            ph2.set(word)
        if num ==3:
            ph3.set(word)
        if num ==4:
            ph4.set(word)
        if num ==5:
            ph5.set(word)

    def read():
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patients")
        results = cursor.fetchall()
        conn.commit()
        conn.close()
        return results

    def add():
        MOBILE = str(MOBILEEntry.get())
        NAME = str(NAMEEntry.get())
        DOB = str(DOBEntry.get())
        HISTORY = str(HISTORYEntry.get())
        MEDICINES = str(MEDICINESEntry.get())

        if (MOBILE == "" or MOBILE == " ") or (NAME == "" or NAME == " ") or (DOB == "" or DOB == " ") or (HISTORY == "" or HISTORY == " ") or (MEDICINES == "" or MEDICINES == " "):
            messagebox.showinfo("Error", "Please fill up the blank entry")
            return
        else:
            try:
                conn = connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO patients VALUES ('"+MOBILE+"','"+NAME+"','"+DOB+"','"+HISTORY+"','"+MEDICINES+"') ")
                conn.commit()
                conn.close()
            except:
                messagebox.showinfo("Error", "Patient already exist")
                return

        refreshTable()
        

    def reset():
        decision = messagebox.askquestion("Warning!!", "Delete all data?")
        if decision != "yes":
            return 
        else:
            try:
                conn = connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM patients")
                conn.commit()
                conn.close()
            except:
                messagebox.showinfo("Error", "Sorry an error occured")
                return

            refreshTable()

    def delete():
        decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
        if decision != "yes":
            return 
        else:
            selected_item = my_tree.selection()[0]
            deleteData = str(my_tree.item(selected_item)['values'][0])
            try:
                conn = connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM patients WHERE MOBILE='"+str(deleteData)+"'")
                conn.commit()
                conn.close()
            except:
                messagebox.showinfo("Error", "Sorry an error occured")
                return

            refreshTable()

    def select():
        try:
            selected_item = my_tree.selection()[0]
            MOBILE = str(my_tree.item(selected_item)['values'][0])
            NAME = str(my_tree.item(selected_item)['values'][1])
            DOB = str(my_tree.item(selected_item)['values'][2])
            HISTORY = str(my_tree.item(selected_item)['values'][3])
            MEDICINES = str(my_tree.item(selected_item)['values'][4])

            setph(MOBILE,1)
            setph(NAME,2)
            setph(DOB,3)
            setph(HISTORY,4)
            setph(MEDICINES,5)
        except:
            messagebox.showinfo("Error", "Please select a data row")

    def search():
        MOBILE = str(MOBILEEntry.get())
        NAME = str(NAMEEntry.get())
        DOB = str(DOBEntry.get())
        HISTORY = str(HISTORYEntry.get())
        MEDICINES = str(MEDICINESEntry.get())

        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patients WHERE MOBILE='"+
        MOBILE+"' or NAME='"+
        NAME+"' or DOB='"+
        DOB+"' or HISTORY='"+
        HISTORY+"' or MEDICINES='"+
        MEDICINES+"' ")
        
        try:
            result = cursor.fetchall()

            for num in range(0,5):
                setph(result[0][num],(num+1))

            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "No data found")
    def back():
        root.destroy()
        page_after_login.page_after_login()
        
    def update():
        selectedMOBILE = ""

        try:
            selected_item = my_tree.selection()[0]
            selectedMOBILE = str(my_tree.item(selected_item)['values'][0])
        except:
            messagebox.showinfo("Error", "Please select a data row")

        MOBILE = str(MOBILEEntry.get())
        NAME = str(NAMEEntry.get())
        DOB = str(DOBEntry.get())
        HISTORY = str(HISTORYEntry.get())
        MEDICINES = str(MEDICINESEntry.get())

        if (MOBILE == "" or MOBILE == " ") or (NAME == "" or NAME == " ") or (DOB == "" or DOB == " ") or (HISTORY == "" or HISTORY == " ") or (MEDICINES == "" or MEDICINES == " "):
            messagebox.showinfo("Error", "Please fill up the blank entry")
            return
        else:
            try:
                conn = connection()
                cursor = conn.cursor()
                cursor.execute("UPDATE patients SET MOBILE='"+
                MOBILE+"', NAME='"+
                NAME+"', DOB='"+
                DOB+"', HISTORY='"+
                HISTORY+"', MEDICINES='"+
                MEDICINES+"' WHERE MOBILE='"+
                selectedMOBILE+"' ")
                conn.commit()
                conn.close()
            except:
                messagebox.showinfo("Error", "Patient already exist")
                return

        refreshTable()

    label = Label(root, text="PATIENT DATA MANAGEMENT", font=('Arial Bold', 30))
    label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

    MOBILELabel = Label(root, text="MOBILE No", font=('Arial', 15))
    NAMELabel = Label(root, text="Firstame", font=('Arial', 15))
    DOBLabel = Label(root, text="DOB", font=('Arial', 15))
    HISTORYLabel = Label(root, text="Med History", font=('Arial', 15))
    MEDICINESLabel = Label(root, text="Medicines", font=('Arial', 15))

    MOBILELabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
    NAMELabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
    DOBLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
    HISTORYLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=15)
    MEDICINESLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

    MOBILEEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph1)
    NAMEEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
    DOBEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
    HISTORYEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph4)
    MEDICINESEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph5)

    MOBILEEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
    NAMEEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
    DOBEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
    HISTORYEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
    MEDICINESEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

    addBtn = Button(
        root, text="Add", padx=65, pady=25, width=10,
        bd=5, font=('Arial', 15), bg="#84F894", command=add)
    updateBtn = Button(
        root, text="Update", padx=65, pady=25, width=10,
        bd=5, font=('Arial', 15), bg="#84E8F8", command=update)
    deleteBtn = Button(
        root, text="Delete", padx=65, pady=25, width=10,
        bd=5, font=('Arial', 15), bg="#FF9999", command=delete)
    searchBtn = Button(
        root, text="Search", padx=65, pady=25, width=10,
        bd=5, font=('Arial', 15), bg="#F4FE82", command=search)
    resetBtn = Button(
        root, text="Reset", padx=65, pady=25, width=10,
        bd=5, font=('Arial', 15), bg="#F398FF", command=reset)
    selectBtn = Button(
        root, text="Select", padx=65, pady=25, width=10,
        bd=5, font=('Arial', 15), bg="#EEEEEE", command=select)

    backBtn = Button(
        root, text="Back", padx=65, pady=25, width=10,
        bd=5, font=('Arial', 15), bg="#94A1FF", command=back)



    addBtn.grid(row=3, column=10, columnspan=1, rowspan=2)
    updateBtn.grid(row=5, column=10, columnspan=1, rowspan=2)
    deleteBtn.grid(row=7, column=10, columnspan=1, rowspan=2)
    searchBtn.grid(row=9, column=10, columnspan=1, rowspan=2)
    resetBtn.grid(row=11, column=10, columnspan=1, rowspan=2)
    selectBtn.grid(row=13, column=10, columnspan=1, rowspan=2)
    backBtn.grid(row=15, column=10, columnspan=1, rowspan=2)


    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Arial Bold', 15))

    my_tree['columns'] = ("Mobile","Firstname","Date_of_Birth","HISTORY","MEDICINES")

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Mobile", anchor=W, width=170)
    my_tree.column("Firstname", anchor=W, width=150)
    my_tree.column("Date_of_Birth", anchor=W, width=150)
    my_tree.column("HISTORY", anchor=W, width=165)
    my_tree.column("MEDICINES", anchor=W, width=150)

    my_tree.heading("Mobile", text="MOBILE", anchor=W)
    my_tree.heading("Firstname", text="Name", anchor=W)
    my_tree.heading("Date_of_Birth", text="DOB", anchor=W)
    my_tree.heading("HISTORY", text="History", anchor=W)
    my_tree.heading("MEDICINES", text="Medicines", anchor=W)

    refreshTable()

    root.mainloop()

