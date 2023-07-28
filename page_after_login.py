from tkinter import *
from PIL import ImageTk, Image
import Login_PAGE
import AddPatients
import Appoinment_FILE

import tkinter as tk
import tkinter as TK
def page_after_login():
    def addpatients():
        window.destroy()
        AddPatients.add_patient()

    
    def addappointment():
        window.destroy()
        Appoinment_FILE.book_appointment()
        
    def sign_out():     
        window.destroy()
        Login_PAGE.page()


    window = Tk()
    window.geometry('1166x718')
    window.resizable(0, 0)
    window.state('zoomed')
    window.title('Login Page')

     # ========================================================================
     # ============================background image============================
     # ========================================================================
    bg_frame = Image.open('images\\hospital1.jpeg')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(window, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')

            # ====== Login Frame =========================


    lgn_frame = Frame(window, bg='#150220', width=950, height=600)
    lgn_frame.place(x=200, y=70)


            # ========================================================================
            # ========================================================
            # ========================================================================

    txt = "SIDDHESHWAR CLINIC"
    heading = Label(lgn_frame, text=txt, font=('yu gothic ui', 25, "bold"), bg="#9AECF5",
                                 fg='black',
                                 bd=5,
                                 relief=FLAT)
    heading.place(x=80, y=30, width=500, height=45)

            # ========================================================================
            # ============ Left Side Image ================================================
            # ========================================================================
    side_image = Image.open('images\\hospt.png')
    photo = ImageTk.PhotoImage(side_image)


    side_image = side_image.resize((400, 400))

    side_image_label = Label(lgn_frame, image=photo, bg='#150220')
    side_image_label.image = photo
    side_image_label.place(x=130, y=150)

 


            # ========================================================================
            # ============================DATA ENTRY ================================
            # ========================================================================
    lgn_button = Image.open('images\\btn1.png')
    photo = ImageTk.PhotoImage(lgn_button)
    lgn_button_label = Label(lgn_frame, image=photo, bg='#150220')
    lgn_button_label.image = photo
    lgn_button_label.place(x=550, y=200)
    login = Button(lgn_button_label, text='DATA ENTRY', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=addpatients)
    login.place(x=20, y=10)

            # ========================================================================
            # ============================APPOINTMENT ENTRY ================================
            # ========================================================================
    lgn_button = Image.open('images\\btn1.png')
    photo = ImageTk.PhotoImage(lgn_button)
    lgn_button_label = Label(lgn_frame, image=photo, bg='#150220')
    lgn_button_label.image = photo
    lgn_button_label.place(x=550, y=300)
    login = Button(lgn_button_label, text='APPOINTMENT', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=addappointment)
    login.place(x=20, y=10)

            
   
            # ========================================================================
            # ============================SIGN OUT BUTTON ================================
            # ========================================================================
    lgn_button = Image.open('images\\btn1.png')
    photo = ImageTk.PhotoImage(lgn_button)
    lgn_button_label = Label(lgn_frame, image=photo, bg='#150220')
    lgn_button_label.image = photo
    lgn_button_label.place(x=550, y=400)
    login = Button(lgn_button_label, text='SIGN OUT ', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command = sign_out)
    login.place(x=20, y=10)
         


    window.mainloop()

