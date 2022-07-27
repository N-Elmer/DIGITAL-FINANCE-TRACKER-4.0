import sys
import random
import sqlite3
from tkinter import *
from tkinter import messagebox
from matplotlib import style
style.use ('fivethirtyeight')
from prettytable import ALL
from prettytable import NONE
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from prettytable import from_db_cursor

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import os.path
import ewallet_support

conn = sqlite3.connect("ManageTransaction.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS TransactionTable (Id INTEGER PRIMARY KEY, Date TEXT, Income INTEGER, IncomeRemarks TEXT, Expenditure INTEGER, ExpenditureRemarks TEXT)")


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    ewallet_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    root = rt
    w = tk.Toplevel (root)
    ewallet_support.set_Tk_var()
    top = Toplevel1 (w)
    ewallet_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def SubmitButtonCommand(self):
        conn = sqlite3.connect("ManageTransaction.db")
        c = conn.cursor()
        
        self.MinId = 1000
        # MinId means Minimum Transaction Id Value
        self.MaxID = 2000
        # MaxId means Maximum Transaction Id Value
        self.IdRange = [i for i in range(self.MinId, self.MaxID+1)]
        # IdRange is the range formed by the MaxId and MinId Values
        random.shuffle(self.IdRange)
        self.id = self.IdRange[0]
        
        self.Database.insert(parent="", index="end", values=(self.id, self.DateEntryVar.get(), self.IncomeEntryVar.get(), self.IncomeRemarksEntryVar.get(), self.ExpenditureEntryVar.get(), self.ExpenditureRemarksEntryVar.get()))
        
        self.c.execute("INSERT INTO TransactionTable VALUES (:Id, :Date, :Income, :IncomeRemarks, :Expenditure, :ExpenditureRemarks)",
            {
                "Id": self.id,
                "Date": self.DateEntryVar.get(),
                "Income": self.IncomeEntryVar.get(),
                "IncomeRemarks": self.IncomeRemarksEntryVar.get(),
                "Expenditure": self.ExpenditureEntryVar.get(),
                "ExpenditureRemarks": self.ExpenditureRemarksEntryVar.get()
            }
        )
        
        if conn:
            conn.commit()
            c.close()
            conn.close()
        
        self.DateEntryVar.set("")
        self.IncomeEntryVar.set("")
        self.IncomeRemarksEntryVar.set("")
        self.ExpenditureEntryVar.set("")
        self.ExpenditureRemarksEntryVar.set("")
        
    def ClearButtonCommand(self):
        self.DateEntryVar.set("")
        self.IncomeEntryVar.set("")
        self.IncomeRemarksEntryVar.set("")
        self.ExpenditureEntryVar.set("")
        self.ExpenditureRemarksEntryVar.set("")
    
    def DeleteButtonCommand(self):
        while True:
             try:
                    conn = sqlite3.connect("ManageTransaction.db")
                    c = conn.cursor()
                    self.x = self.Database.selection()
                    self.DeleteMessage = messagebox.askyesno("CONFIRM", "DO YOU WANT TO DELETE?")
                    self.Database.delete(self.x)
                    break
             except ValueError:
                    self.ErrorMessage = messagebox.showwarning("ERROR", "ERROR: COULD NOT CONNECT TO DATABASE")
                    continue
        
        for record in self.x:
            self.Database.delete(record)
            self.c.execute("DELETE FROM TransactionTable WHERE Id = ?", self.Database.set(self.id, (self.x)))
        
        if conn:
            conn.commit()
            c.close()
            conn.close()   

    def IncomeSumButtonCommand(self):
        conn = sqlite3.connect("ManageTransaction.db")
        c = conn.cursor()
        
        self.c.execute("SELECT SUM(Income) as INCOME FROM TransactionTable")
        self.a = from_db_cursor(self.c, hrules = NONE, border = False, header = False)
        self.IncomeDisplayEntryVar.set(self.a)
        
        if conn:
            conn.commit()
            c.close()
            conn.close() 
    
    def ExpenditureSumButtonCommand(self):
        conn = sqlite3.connect("ManageTransaction.db")
        c = conn.cursor()
        
        self.c.execute("SELECT SUM(Expenditure) as EXPENDITURE FROM TransactionTable")
        self.b = from_db_cursor(self.c, hrules = NONE, border = False, header = False)
        self.ExpenditureDisplayEntryVar.set(self.b)
        
        if conn:
            conn.commit()
            c.close()
            conn.close()
    
    def BalanceButtonCommand(self):
        conn = sqlite3.connect("ManageTransaction.db")
        c = conn.cursor()
        
        self.c.execute("SELECT (SUM(Income) - SUM(Expenditure)) as BALANCE FROM TransactionTable")
        self.d = from_db_cursor(self.c, hrules = NONE, border = False, header = False)
        self.BalanceDisplayEntryVar.set(self.d)
        
        if conn:
            conn.commit()
            c.close()
            conn.close()
    
    def __init__(self, top=None):
        global DateEntryVar
        self.DateEntryVar = tk.StringVar()
        self.DateEntryVar.set("01/12/2021")
        global IncomeEntryVar
        self.IncomeEntryVar = tk.IntVar()
        self.IncomeEntryVar.set(250000)
        global IncomeRemarksEntryVar
        self.IncomeRemarksEntryVar = tk.StringVar()
        self.IncomeRemarksEntryVar.set("Salary")
        global ExpenditureEntryVar
        self.ExpenditureEntryVar = tk.IntVar()
        self.ExpenditureEntryVar.set(50000)
        global ExpenditureRemarksEntryVar
        self.ExpenditureRemarksEntryVar = tk.StringVar()
        self.ExpenditureRemarksEntryVar.set("Bills")
        global IncomeDisplayEntryVar
        self.IncomeDisplayEntryVar = tk.StringVar()
        self.IncomeDisplayEntryVar.set("")
        global ExpenditureDisplayEntryVar
        self.ExpenditureDisplayEntryVar = tk.IntVar()
        self.ExpenditureDisplayEntryVar.set("")
        global BalanceDisplayEntryVar
        self.BalanceDisplayEntryVar = tk.IntVar()
        self.BalanceDisplayEntryVar.set("")
    
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1195x604+163+4")
        top.minsize(1000, 500)
        top.maxsize(1366, 764)
        top.resizable(0,  0)
        top.title("ELECTRONIC WALLET")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.0, rely=0.0, relheight=1.023
                , relwidth=1.004)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1_1_1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1_1_1, padding=3)
        self.TNotebook1.tab(0, text="HOME",compound="left",underline="-1",)
        self.TNotebook1_t1_1_1.configure(background="#ffffff")
        self.TNotebook1_t1_1_1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1_1_1.configure(highlightcolor="black")
        self.TNotebook1_t2_1_1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2_1_1, padding=3)
        self.TNotebook1.tab(1, text="MANAGE",compound="left",underline="-1",)
        self.TNotebook1_t2_1_1.configure(background="#ffffff")
        self.TNotebook1_t2_1_1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2_1_1.configure(highlightcolor="black")

        self.TPanedwindow1 = ttk.Panedwindow(self.TNotebook1_t2_1_1
                , orient="horizontal")
        self.TPanedwindow1.place(relx=0.0, rely=0.0, relheight=0.998
                , relwidth=0.798)
        self.TPanedwindow1_p1 = ttk.Labelframe(width=75, text='DATA')
        self.TPanedwindow1.add(self.TPanedwindow1_p1, weight=0)
        self.TPanedwindow1_p2 = ttk.Labelframe(text='TRANSACTION')
        self.TPanedwindow1.add(self.TPanedwindow1_p2, weight=0)
        self.__funcid0 = self.TPanedwindow1.bind('<Map>', self.__adjust_sash0)

        self.Label1 = tk.Label(self.TPanedwindow1_p1)
        self.Label1.place(relx=0.041, rely=0.051, height=31, width=54
                , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#607D8B")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(relief="groove")
        self.Label1.configure(text='''DATE''')

        self.DateEntry = tk.Entry(self.TPanedwindow1_p1)
        self.DateEntry.place(relx=0.041, rely=0.102, height=30, relwidth=0.914
                , bordermode='ignore')
        self.DateEntry.configure(background="white")
        self.DateEntry.configure(disabledforeground="#a3a3a3")
        self.DateEntry.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.DateEntry.configure(foreground="#000000")
        self.DateEntry.configure(highlightbackground="#d9d9d9")
        self.DateEntry.configure(highlightcolor="black")
        self.DateEntry.configure(insertbackground="black")
        self.DateEntry.configure(selectbackground="blue")
        self.DateEntry.configure(selectforeground="white")
        self.DateEntry.configure(textvariable=self.DateEntryVar)

        self.Label1_1 = tk.Label(self.TPanedwindow1_p1)
        self.Label1_1.place(relx=0.041, rely=0.186, height=30, width=74
                , bordermode='ignore')
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#607D8B")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(relief="groove")
        self.Label1_1.configure(text='''INCOME''')

        self.IncomeEntry = tk.Entry(self.TPanedwindow1_p1)
        self.IncomeEntry.place(relx=0.041, rely=0.237, height=30, relwidth=0.914
                , bordermode='ignore')
        self.IncomeEntry.configure(background="white")
        self.IncomeEntry.configure(disabledforeground="#a3a3a3")
        self.IncomeEntry.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.IncomeEntry.configure(foreground="#000000")
        self.IncomeEntry.configure(highlightbackground="#d9d9d9")
        self.IncomeEntry.configure(highlightcolor="black")
        self.IncomeEntry.configure(insertbackground="black")
        self.IncomeEntry.configure(selectbackground="blue")
        self.IncomeEntry.configure(selectforeground="#ffffff")
        self.IncomeEntry.configure(textvariable=self.IncomeEntryVar)

        self.Label1_1_1 = tk.Label(self.TPanedwindow1_p1)
        self.Label1_1_1.place(relx=0.041, rely=0.321, height=30, width=154
                , bordermode='ignore')
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(activeforeground="black")
        self.Label1_1_1.configure(anchor='w')
        self.Label1_1_1.configure(background="#607D8B")
        self.Label1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label1_1_1.configure(foreground="#000000")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="black")
        self.Label1_1_1.configure(relief="groove")
        self.Label1_1_1.configure(text='''INCOME REMARKS''')

        self.IncomeRemarksEntry = tk.Entry(self.TPanedwindow1_p1)
        self.IncomeRemarksEntry.place(relx=0.041, rely=0.372, height=30
                , relwidth=0.914, bordermode='ignore')
        self.IncomeRemarksEntry.configure(background="white")
        self.IncomeRemarksEntry.configure(disabledforeground="#a3a3a3")
        self.IncomeRemarksEntry.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.IncomeRemarksEntry.configure(foreground="#000000")
        self.IncomeRemarksEntry.configure(highlightbackground="#d9d9d9")
        self.IncomeRemarksEntry.configure(highlightcolor="black")
        self.IncomeRemarksEntry.configure(insertbackground="black")
        self.IncomeRemarksEntry.configure(selectbackground="blue")
        self.IncomeRemarksEntry.configure(selectforeground="white")
        self.IncomeRemarksEntry.configure(textvariable=self.IncomeRemarksEntryVar)

        self.Label1_1_1_1 = tk.Label(self.TPanedwindow1_p1)
        self.Label1_1_1_1.place(relx=0.041, rely=0.459, height=30, width=124
                , bordermode='ignore')
        self.Label1_1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1_1.configure(activeforeground="black")
        self.Label1_1_1_1.configure(anchor='w')
        self.Label1_1_1_1.configure(background="#607D8B")
        self.Label1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label1_1_1_1.configure(foreground="#000000")
        self.Label1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_1.configure(highlightcolor="black")
        self.Label1_1_1_1.configure(relief="groove")
        self.Label1_1_1_1.configure(text='''EXPENDITURE''')

        self.ExpenditureEntry = tk.Entry(self.TPanedwindow1_p1)
        self.ExpenditureEntry.place(relx=0.041, rely=0.508, height=30
                , relwidth=0.914, bordermode='ignore')
        self.ExpenditureEntry.configure(background="white")
        self.ExpenditureEntry.configure(disabledforeground="#a3a3a3")
        self.ExpenditureEntry.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.ExpenditureEntry.configure(foreground="#000000")
        self.ExpenditureEntry.configure(highlightbackground="#d9d9d9")
        self.ExpenditureEntry.configure(highlightcolor="black")
        self.ExpenditureEntry.configure(insertbackground="black")
        self.ExpenditureEntry.configure(selectbackground="blue")
        self.ExpenditureEntry.configure(selectforeground="white")
        self.ExpenditureEntry.configure(textvariable=self.ExpenditureEntryVar)

        self.Label1_1_1_1_1 = tk.Label(self.TPanedwindow1_p1)
        self.Label1_1_1_1_1.place(relx=0.041, rely=0.592, height=31, width=194
                , bordermode='ignore')
        self.Label1_1_1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1_1_1.configure(activeforeground="black")
        self.Label1_1_1_1_1.configure(anchor='w')
        self.Label1_1_1_1_1.configure(background="#607D8B")
        self.Label1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_1_1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label1_1_1_1_1.configure(foreground="#000000")
        self.Label1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_1_1.configure(highlightcolor="black")
        self.Label1_1_1_1_1.configure(relief="groove")
        self.Label1_1_1_1_1.configure(text='''EXPENDITURE REMARKS''')

        self.ExpenditureRemarksEntry = tk.Entry(self.TPanedwindow1_p1)
        self.ExpenditureRemarksEntry.place(relx=0.041, rely=0.645, height=30
                , relwidth=0.914, bordermode='ignore')
        self.ExpenditureRemarksEntry.configure(background="white")
        self.ExpenditureRemarksEntry.configure(disabledforeground="#a3a3a3")
        self.ExpenditureRemarksEntry.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.ExpenditureRemarksEntry.configure(foreground="#000000")
        self.ExpenditureRemarksEntry.configure(highlightbackground="#d9d9d9")
        self.ExpenditureRemarksEntry.configure(highlightcolor="black")
        self.ExpenditureRemarksEntry.configure(insertbackground="black")
        self.ExpenditureRemarksEntry.configure(selectbackground="blue")
        self.ExpenditureRemarksEntry.configure(selectforeground="white")
        self.ExpenditureRemarksEntry.configure(textvariable=self.ExpenditureRemarksEntryVar)

        self.SubmitButton = tk.Button(self.TPanedwindow1_p1)
        self.SubmitButton.place(relx=0.041, rely=0.711, height=44, width=97
                , bordermode='ignore')
        self.SubmitButton.configure(activebackground="#ececec")
        self.SubmitButton.configure(activeforeground="#000000")
        self.SubmitButton.configure(background="#00ff40")
        self.SubmitButton.configure(command=self.SubmitButtonCommand)
        self.SubmitButton.configure(disabledforeground="#a3a3a3")
        self.SubmitButton.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.SubmitButton.configure(foreground="#000000")
        self.SubmitButton.configure(highlightbackground="#ffffff")
        self.SubmitButton.configure(highlightcolor="#ffffff")
        self.SubmitButton.configure(pady="0")
        self.SubmitButton.configure(text='''SUBMIT''')

        self.DeleteButton = tk.Button(self.TPanedwindow1_p1)
        self.DeleteButton.place(relx=0.571, rely=0.711, height=44, width=94
                , bordermode='ignore')
        self.DeleteButton.configure(activebackground="#ececec")
        self.DeleteButton.configure(activeforeground="#000000")
        self.DeleteButton.configure(background="#ff0000")
        self.DeleteButton.configure(command=self.DeleteButtonCommand)
        self.DeleteButton.configure(disabledforeground="#a3a3a3")
        self.DeleteButton.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.DeleteButton.configure(foreground="#ffffff")
        self.DeleteButton.configure(highlightbackground="#ffffff")
        self.DeleteButton.configure(highlightcolor="#ffffff")
        self.DeleteButton.configure(pady="0")
        self.DeleteButton.configure(text='''DELETE''')

        self.ClearButton = tk.Button(self.TPanedwindow1_p1)
        self.ClearButton.place(relx=0.041, rely=0.812, height=44, width=224
                , bordermode='ignore')
        self.ClearButton.configure(activebackground="#ececec")
        self.ClearButton.configure(activeforeground="#000000")
        self.ClearButton.configure(background="#808080")
        self.ClearButton.configure(command=self.ClearButtonCommand)
        self.ClearButton.configure(disabledforeground="#a3a3a3")
        self.ClearButton.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.ClearButton.configure(foreground="#000000")
        self.ClearButton.configure(highlightbackground="#ffffff")
        self.ClearButton.configure(highlightcolor="#ffffff")
        self.ClearButton.configure(pady="0")
        self.ClearButton.configure(text='''CLEAR''')

        self.AnalyticsButton = tk.Button(self.TPanedwindow1_p1)
        self.AnalyticsButton.place(relx=0.041, rely=0.897, height=44, width=224
                , bordermode='ignore')
        self.AnalyticsButton.configure(activebackground="#ececec")
        self.AnalyticsButton.configure(activeforeground="#000000")
        self.AnalyticsButton.configure(background="#0080c0")
        self.AnalyticsButton.configure(command=ewallet_support.AnalyticsButtonCommand)
        self.AnalyticsButton.configure(disabledforeground="#a3a3a3")
        self.AnalyticsButton.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.AnalyticsButton.configure(foreground="#ffffff")
        self.AnalyticsButton.configure(highlightbackground="#ffffff")
        self.AnalyticsButton.configure(highlightcolor="#ffffff")
        self.AnalyticsButton.configure(pady="0")
        self.AnalyticsButton.configure(text='''ANALYTICS''')

        self.style.configure('Treeview',  font="TkDefaultFont")
        self.Database = ScrolledTreeView(self.TPanedwindow1_p2)
        self.Database.place(relx=0.014, rely=0.237, relheight=0.739
                , relwidth=0.967, bordermode='ignore')
        self.Database.configure(columns="Col1 Col2 Col3 Col4 Col5 Col6")
        self.Database.heading("#0",text="Tree")
        self.Database.heading("#0",anchor="center")
        self.Database.column("#0",width="0")
        self.Database.column("#0",minwidth="0")
        self.Database.column("#0",stretch="0")
        self.Database.column("#0",anchor="center")
        self.Database.heading("Col1",text="ID")
        self.Database.heading("Col1",anchor="center")
        self.Database.column("Col1",width="76")
        self.Database.column("Col1",minwidth="76")
        self.Database.column("Col1",stretch="0")
        self.Database.column("Col1",anchor="center")
        self.Database.heading("Col2",text="DATE")
        self.Database.heading("Col2",anchor="center")
        self.Database.column("Col2",width="93")
        self.Database.column("Col2",minwidth="93")
        self.Database.column("Col2",stretch="0")
        self.Database.column("Col2",anchor="center")
        self.Database.heading("Col3",text="INCOME")
        self.Database.heading("Col3",anchor="center")
        self.Database.column("Col3",width="95")
        self.Database.column("Col3",minwidth="95")
        self.Database.column("Col3",stretch="0")
        self.Database.column("Col3",anchor="center")
        self.Database.heading("Col4",text="INCOME REMARKS")
        self.Database.heading("Col4",anchor="center")
        self.Database.column("Col4",width="156")
        self.Database.column("Col4",minwidth="156")
        self.Database.column("Col4",stretch="0")
        self.Database.column("Col4",anchor="center")
        self.Database.heading("Col5",text="EXPENDITURE")
        self.Database.heading("Col5",anchor="center")
        self.Database.column("Col5",width="95")
        self.Database.column("Col5",minwidth="95")
        self.Database.column("Col5",stretch="0")
        self.Database.column("Col5",anchor="center")
        self.Database.heading("Col6",text="EXPENDITURE REMARKS")
        self.Database.heading("Col6",anchor="center")
        self.Database.column("Col6",width="158")
        self.Database.column("Col6",minwidth="158")
        self.Database.column("Col6",stretch="0")
        self.Database.column("Col6",anchor="center")
        
        self.Label3_1 = tk.Label(self.TPanedwindow1_p2)
        self.Label3_1.place(relx=0.014, rely=0.068, height=81, width=673
                , bordermode='ignore')
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#0080ff")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''ELECTRONIC WALLET''')
        
        self.conn = sqlite3.connect("ManageTransaction.db")
        self.c = conn.cursor()
        
        self.c.execute("SELECT * FROM TransactionTable")
        self.rows = self.c.fetchall()
        for self.row in self.rows:
            self.Database.insert("", tk.END, values=self.row)

        self.TPanedwindow2 = ttk.Panedwindow(self.TNotebook1_t2_1_1
                , orient="vertical")
        self.TPanedwindow2.place(relx=0.803, rely=0.0, relheight=1.007
                , relwidth=0.203)
        self.TPanedwindow2_p1 = ttk.Labelframe(height=380, text='COMPARE')
        self.TPanedwindow2.add(self.TPanedwindow2_p1, weight=0)
        self.TPanedwindow2_p2 = ttk.Labelframe(height=192, text='BALANCE')
        self.TPanedwindow2.add(self.TPanedwindow2_p2, weight=0)
        
        self.IncomeSumButton = tk.Button(self.TPanedwindow2_p1)
        self.IncomeSumButton.place(relx=0.082, rely=0.087, height=34, width=197
                , bordermode='ignore')
        self.IncomeSumButton.configure(activebackground="#ececec")
        self.IncomeSumButton.configure(activeforeground="#000000")
        self.IncomeSumButton.configure(background="#607D8B")
        self.IncomeSumButton.configure(command=self.IncomeSumButtonCommand)
        self.IncomeSumButton.configure(disabledforeground="#a3a3a3")
        self.IncomeSumButton.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.IncomeSumButton.configure(foreground="#000000")
        self.IncomeSumButton.configure(highlightbackground="#ffffff")
        self.IncomeSumButton.configure(highlightcolor="#ffffff")
        self.IncomeSumButton.configure(pady="0")
        self.IncomeSumButton.configure(text='''GET TOTAL INCOME''')
   
        self.IncomeDisplayEntry = tk.Entry(self.TPanedwindow2_p1)
        self.IncomeDisplayEntry.place(relx=0.082, rely=0.232, height=100
                , relwidth=0.798, bordermode='ignore')
        self.IncomeDisplayEntry.configure(background="white")
        self.IncomeDisplayEntry.configure(disabledforeground="#a3a3a3")
        self.IncomeDisplayEntry.configure(font="-family {Segoe UI} -size 35 -weight bold")
        self.IncomeDisplayEntry.configure(foreground="#000000")
        self.IncomeDisplayEntry.configure(highlightbackground="#d9d9d9")
        self.IncomeDisplayEntry.configure(highlightcolor="black")
        self.IncomeDisplayEntry.configure(insertbackground="black")
        self.IncomeDisplayEntry.configure(selectbackground="blue")
        self.IncomeDisplayEntry.configure(selectforeground="white")
        self.IncomeDisplayEntry.configure(state='readonly')
        self.IncomeDisplayEntry.configure(textvariable=self.IncomeDisplayEntryVar)

        self.ExpenditureSumButton = tk.Button(self.TPanedwindow2_p1)
        self.ExpenditureSumButton.place(relx=0.082, rely=0.551, height=34
                , width=197, bordermode='ignore')
        self.ExpenditureSumButton.configure(activebackground="#ececec")
        self.ExpenditureSumButton.configure(activeforeground="#000000")
        self.ExpenditureSumButton.configure(background="#607D8B")
        self.ExpenditureSumButton.configure(command=self.ExpenditureSumButtonCommand)
        self.ExpenditureSumButton.configure(disabledforeground="#a3a3a3")
        self.ExpenditureSumButton.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.ExpenditureSumButton.configure(foreground="#000000")
        self.ExpenditureSumButton.configure(highlightbackground="#ffffff")
        self.ExpenditureSumButton.configure(highlightcolor="#ffffff")
        self.ExpenditureSumButton.configure(pady="0")
        self.ExpenditureSumButton.configure(text='''GET TOTAL EXPENDITURE''')
  
        self.ExpenditureDisplayEntry = tk.Entry(self.TPanedwindow2_p1)
        self.ExpenditureDisplayEntry.place(relx=0.082, rely=0.696, height=100
                , relwidth=0.798, bordermode='ignore')
        self.ExpenditureDisplayEntry.configure(background="white")
        self.ExpenditureDisplayEntry.configure(disabledforeground="#a3a3a3")
        self.ExpenditureDisplayEntry.configure(font="-family {Segoe UI} -size 35 -weight bold")
        self.ExpenditureDisplayEntry.configure(foreground="#000000")
        self.ExpenditureDisplayEntry.configure(highlightbackground="#d9d9d9")
        self.ExpenditureDisplayEntry.configure(highlightcolor="black")
        self.ExpenditureDisplayEntry.configure(insertbackground="black")
        self.ExpenditureDisplayEntry.configure(selectbackground="blue")
        self.ExpenditureDisplayEntry.configure(selectforeground="white")
        self.ExpenditureDisplayEntry.configure(state='readonly')
        self.ExpenditureDisplayEntry.configure(textvariable=self.ExpenditureDisplayEntryVar)
   
        self.BalanceButton = tk.Button(self.TPanedwindow2_p2)
        self.BalanceButton.place(relx=0.082, rely=0.163, height=34, width=197
                , bordermode='ignore')
        self.BalanceButton.configure(activebackground="#ececec")
        self.BalanceButton.configure(activeforeground="#000000")
        self.BalanceButton.configure(background="#607D8B")
        self.BalanceButton.configure(command=self.BalanceButtonCommand)
        self.BalanceButton.configure(disabledforeground="#a3a3a3")
        self.BalanceButton.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.BalanceButton.configure(foreground="#000000")
        self.BalanceButton.configure(highlightbackground="#ffffff")
        self.BalanceButton.configure(highlightcolor="#ffffff")
        self.BalanceButton.configure(pady="0")
        self.BalanceButton.configure(text='''GET FINAL BALANCE''')
   
        self.BalanceDisplayEntry = tk.Entry(self.TPanedwindow2_p2)
        self.BalanceDisplayEntry.place(relx=0.082, rely=0.366, height=100
                , relwidth=0.798, bordermode='ignore')
        self.BalanceDisplayEntry.configure(background="white")
        self.BalanceDisplayEntry.configure(disabledforeground="#a3a3a3")
        self.BalanceDisplayEntry.configure(font="-family {Segoe UI} -size 35 -weight bold")
        self.BalanceDisplayEntry.configure(foreground="#000000")
        self.BalanceDisplayEntry.configure(highlightbackground="#d9d9d9")
        self.BalanceDisplayEntry.configure(highlightcolor="black")
        self.BalanceDisplayEntry.configure(insertbackground="black")
        self.BalanceDisplayEntry.configure(selectbackground="blue")
        self.BalanceDisplayEntry.configure(selectforeground="white")
        self.BalanceDisplayEntry.configure(state='readonly')
        self.BalanceDisplayEntry.configure(textvariable=self.BalanceDisplayEntryVar)
        
    def __adjust_sash0(self, event):
        paned = event.widget
        pos = [245, ]
        i = 0
        for sash in pos:
            paned.sashpos(i, sash)
            i += 1
        paned.unbind('<map>', self.__funcid0)
        del self.__funcid0

    def __adjust_sash1(self, event):
        paned = event.widget
        pos = [295, ]
        i = 0
        for sash in pos:
            paned.sashpos(i, sash)
            i += 1
        paned.unbind('<map>', self.__funcid1)
        del self.__funcid1

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()

    if conn:
        conn.commit()
        c.close()
        conn.close()



