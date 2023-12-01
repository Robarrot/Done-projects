import tkinter as tk
import dframe as df
import Admin as adm
from tkinter import*
from Admin import *
import sqlite3
from tkinter import *
from dframe import *
from sqlite3 import *
from tkinter import ttk

def reg_server(root, frame1, name, sex, RegNo, Faculty, passw):
            if(passw=='' or passw==' '):
                msg = Message(frame1, text="Error: Missing Fileds", width=500)
                msg.grid(row = 10, column = 0, columnspan = 5)
                return -1
            try:
                   conn = sqlite3.connect("/home/roba/Desktop/Voting_System-main/voter.db")
                   c = conn.cursor()
                   c.execute(f"INSERT INTO voters (name, sex, RegNo, Faculty , passwd) VALUES ({str(name)},{str(sex)},{str(RegNo)},{str(Faculty)},{str(passw)})")
                   conn.commit()
                   print('Registered successfully')
            except sqlite3.Error as e:
                   print(e)
            vid = df.taking_data_voter(name, sex, RegNo, Faculty, passw)
            for widget in frame1.winfo_children():
                widget.destroy()
            txt = "Registered Voter with\n\n VOTER I.D. = " #+ str(vid)
            Label(frame1, text=txt,bg="steel purple" , font=('Helvetica', 18, 'bold')).grid(row = 2, column = 1, columnspan=2)
def Register(root,frame1):

            root.title("Register Voter")
            for widget in frame1.winfo_children():
                widget.destroy()

            Label(frame1, text="Register Voter", bg="steel blue" ,font=('Helvetica', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
            Label(frame1, text="Register voter", bg="steel blue" ,).grid(row = 1,column = 0)
            Label(frame1, text="Voter ID:      ", anchor="e", justify=LEFT).grid(row = 2,column = 0)
            Label(frame1, text="Name:         ",bg="steel blue" , anchor="e", justify=LEFT).grid(row = 3,column = 0)
            Label(frame1, text="Sex:              ",bg="steel blue" , anchor="e", justify=LEFT).grid(row = 4,column = 0)
            Label(frame1, text="RegNo:           ", bg="steel blue" ,anchor="e", justify=LEFT).grid(row = 5,column = 0)
            Label(frame1, text="Faculty:             ",bg="steel blue" , anchor="e", justify=LEFT).grid(row = 6,column = 0)
            Label(frame1, text="Password:   ", bg="steel blue" ,anchor="e", justify=LEFT).grid(row = 7,column = 0)

            voter_ID = tk.StringVar()
            name = tk.StringVar()
            sex = tk.StringVar()
            RegNo=tk.StringVar()
            Faculty= tk.StringVar()
            password = tk.StringVar()

            e1 = Entry(frame1, textvariable = voter_ID).grid(row = 2, column = 2)
            e2 = Entry(frame1, textvariable = name).grid(row = 3, column = 2)
            e5 = Entry(frame1, textvariable = RegNo).grid(row = 5, column = 2)
            e6 = Entry(frame1, textvariable = Faculty).grid(row=6, column=2)
            e6 = ttk.Combobox(frame1, textvariable = Faculty, width=17)
            e6['values']=("SOT", "SOB", "SOE", "SPP")
            e6.grid(row = 6, column = 2)
            
            e6.current()
            e7 = Entry(frame1, textvariable = password).grid(row = 7, column = 2)
            e4 = Entry(frame1, textvariable = sex).grid(row=4, column=2)
            
            e4 = ttk.Combobox(frame1, textvariable = sex, width=17)
            e4['values'] = ("Male","Female")
            e4.grid(row = 4, column = 2)
            e4.current()
            reg = Button(frame1, text="Register",bg="light steel blue" ,command = lambda: 
            reg_server(root, frame1, name.get(),   sex.get(),                    
            RegNo.get(), Faculty.get(), password.get()), width=10)
            Label(frame1, text="",bg="steel blue" ,).grid(row = 8,column = 0)
            reg.grid(row = 9, column = 1, columnspan = 2)
 
               
            frame1.pack()
            root.mainloop()

        # if __name__ == "__main__":
        #         root = Tk()
        #         root.geometry('500x500')
        #         frame1 = Frame(root)
        #         Register(root,frame1)
