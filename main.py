#importing required modules/libraries etc
import tkinter as tk
from tkinter import ttk
from tkinter import *
#import Image
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox
import datetime
from fpdf import FPDF

from PIL import Image, ImageTk



pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
pdf.add_font('Arial', '', 'K:\Laboratory\Font\\arial.ttf', uni=True)

#FUNCTIONS SECTION
def call_mainroot():
   sroot.destroy()
   mainroot()


'''SQL Connection Section
BackEnd : SQLite3/DB Browser for SQLite
Database Name: Laboratory
'''

conn = sqlite3.connect('Laboratory.db')  

cursor = conn.cursor()

#--------MAIN--------
#Window design
sroot = tk.Tk()
sroot.title("Dr. DB's Laboratory")
sroot.minsize(height=516,width=1150)
sroot.geometry("1080x500")
sroot.configure(bg='plum')

#Splash Screen
Label(sroot,text="        Welcome to ",font=("Helvetica", 40, 'bold'),bg = 'plum',fg='black').place(x=300,y=140)
Label(sroot,text=" Dr. DB's Laboratory ",font=("Helvetica", 40, 'bold'),bg = 'plum',fg='black').place(x=300,y=210)

#MAIN Screen
now = datetime.datetime.now()
def mainroot():
   root = Tk()
   root.geometry('1080x500')
   root.minsize(width=1080,height=550)
   root.maxsize(width=1080,height=550)
   root.configure(bg='white')
   root.title("Dr. DB's Laboratory")

   sep = Frame(height=500,bd=1,relief='sunken',bg='white')

   #----------top frame--------------
   top_frame = Frame(root,height=70,width=1080,bg='plum1')

   top_frame.place(x=0,y=0)
   tf_label = Label(top_frame,text="Dr. DB's Laboratory",font='msserif 33',fg='black',bg='plum1',height=70)
   tf_label.pack(anchor='center')
   top_frame.pack_propagate(False)

   b_frame = Frame(root,height=400,width=1080,bg='gray91')
   b_frame.place(x=0,y=120+6+20+60+11)
   b_frame.pack_propagate(False)

#--------------------------------------------------------------------------------------------
##########################################
#######  LABORATORIANS  ##################
   def disp_all_labo():
      view = tk.Tk()
      tree = ttk.Treeview(view, columns=("c1", "c2", "c3","c4","c5"), show='headings')
      tree.column("#1", anchor=tk.CENTER)
      tree.heading("#1", text="ID")
      tree.column("#2", anchor=tk.CENTER)
      tree.heading("#2", text="NAME")
      tree.column("#3", anchor=tk.CENTER)
      tree.heading("#3", text="AGE")
      tree.column("#4", anchor=tk.CENTER)
      tree.heading("#4", text="DEPARTMENT")
      tree.column("#5", anchor=tk.CENTER)
      tree.heading("#5", text="LAB ID")
      tree.pack()
      cursor.execute("select * from laboratorian")
      rows = cursor.fetchall()
      for row in rows:
         print(row)
         tree.insert("", tk.END, values=row)

   def disp_labo_by_id(labo_id_val):

      comm = "select Laboratorian.*, Image.img_data from Laboratorian, Image where Laboratorian.labo_id="+str(labo_id_val)+";" #comm = "select * from Laboratorian where labo_id="+str(labo_id_val)+";"
      
      cursor.execute(comm)
      
      rows = cursor.fetchall()
      
      if len(rows)==0:
         messagebox.showinfo('Invalid', "Please enter a valid Laboratorian ID")
      else:
         view = tk.Tk()
         style=ttk.Style(view)
         style.configure("Treeview",rowheight=50)
         tree = ttk.Treeview(view, columns=("c1", "c2", "c3","c4","c5"), show='headings')

         tree.column("#1", anchor=tk.CENTER)
         tree.heading("#1", text="ID")
         tree.column("#2", anchor=tk.CENTER)
         tree.heading("#2", text="NAME")
         tree.column("#3", anchor=tk.CENTER)
         tree.heading("#3", text="AGE")
         tree.column("#4", anchor=tk.CENTER)
         tree.heading("#4", text="DEPARTMENT")
         tree.column("#5", anchor=tk.CENTER)
         tree.heading("#5", text="LAB ID")
         tree.pack()

         for row in rows:
            tree.insert('', tk.END, values=row)
         
         
            
         
      
      
   def labo_by_id():
      global labo_id

      def search_labo_():
         labo_id_val = labo_id.get()
         if labo_id.get() == '' or labo_id.get() == 'Laboratorian ID..':
            messagebox.showinfo("Error","Please fill Laboratorian ID")
         else:
            print(labo_id_val)
            disp_labo_by_id(labo_id_val)

      b_frame = Frame(root,height=400,width=1080,bg='white')
      Label(b_frame, text='View Laboratorian By ID', font='msserif 30',bg='white').place(x=350,y=10)

      Label(b_frame, text="Enter Laboratorian ID:", font='msserif 12',bg='white').place(x=400,y=65)

      labo_id = Entry(b_frame, width=20, font=('Arial 20'))
      labo_id.place(x=400, y=110)

      search_labo = Button(b_frame, font='mssherif 20', text= " View", bg='plum1',fg='orchid4',width=20, command=search_labo_).place(x=400,y=170)

      b_frame.place(x=0,y=120+6+20+60+11)
      b_frame.pack_propagate(False)
      b_frame.tkraise()

   def disp_labo_by_lab(lab_id_val):

      comm = "select * from Laboratorian where lab_id="+str(lab_id_val)+";"
      cursor.execute(comm)
      rows = cursor.fetchall()

      if len(rows)==0:
         messagebox.showinfo('Invalid', "Please enter a valid Lab ID")
      else:
         view = tk.Tk()
         tree = ttk.Treeview(view, columns=("c1", "c2", "c3","c4","c5"), show='headings')
         tree.column("#1", anchor=tk.CENTER)
         tree.heading("#1", text="ID")
         tree.column("#2", anchor=tk.CENTER)
         tree.heading("#2", text="NAME")
         tree.column("#3", anchor=tk.CENTER)
         tree.heading("#3", text="AGE")
         tree.column("#4", anchor=tk.CENTER)
         tree.heading("#4", text="DEPARTMENT")
         tree.column("#5", anchor=tk.CENTER)
         tree.heading("#5", text="LAB ID")
         tree.pack()

         for row in rows:
            print(row)
            tree.insert("", tk.END, values=row)

   def labo_by_lab():
      global lab_id

      def search_labo_2():
         lab_id_val = lab_id.get()
         if lab_id.get() == '' or lab_id.get() == 'Lab ID..':
            messagebox.showinfo("Error","Please fill Lab ID")
         else:
            print(lab_id_val)
            disp_labo_by_lab(lab_id_val)

      b_frame = Frame(root,height=400,width=1080,bg='white')
      Label(b_frame, text='View Laboratorians By Lab', font='msserif 30',bg='white').place(x=380,y=10)
      Label(b_frame, text="Enter Lab ID:", font='msserif 12',bg='white').place(x=400,y=65)


      lab_id = Entry(b_frame, width=20, font=('Arial 20'))
      lab_id.place(x=400, y=110)

      search_labo_2 = Button(b_frame, font='mssherif 20', text= " View", bg='plum1',fg='orchid4',width=20, command=search_labo_2).place(x=400,y=170)

      b_frame.place(x=0,y=120+6+20+60+11)
      b_frame.pack_propagate(False)
      b_frame.tkraise()

   def laboratorians():
      b_frame = Frame(root,height=400,width=1080,bg='white')
      view_all = Button(b_frame,font='mssherif 20', text= " View All", bg='plum1',fg='orchid4',width=20, command=disp_all_labo).place(x=90,y=70)
      view_by_id = Button(b_frame,font='mssherif 20', text= " View by ID", bg='plum1',fg='orchid4',width=20, command=labo_by_id).place(x=640,y=70)
      view_by_lab = Button(b_frame,font='mssherif 20', text= " View by Lab", bg='plum1',fg='orchid4',width=20, command=labo_by_lab).place(x=360,y=190)


      b_frame.place(x=0,y=120+6+20+60+11)
      b_frame.pack_propagate(False)
      b_frame.tkraise()

########################################
########################################

#--------------------------------------------------------------------------------------------

##########################################
#######  PATIENTS  ##################

   def disp_pat_by_id(pat_id_val):

      comm = "select * from Patient where pat_id="+str(pat_id_val)+";"
      cursor.execute(comm)
      rows = cursor.fetchall()

      if len(rows)==0:
         messagebox.showinfo('Invalid', "Please enter a valid Patient ID")
      else:
         view = tk.Tk()
         tree = ttk.Treeview(view, columns=("c1", "c2", "c3","c4"), show='headings')
         tree.column("#1", anchor=tk.CENTER)
         tree.heading("#1", text="Patient ID")
         tree.column("#2", anchor=tk.CENTER)
         tree.heading("#2", text="NAME")
         tree.column("#3", anchor=tk.CENTER)
         tree.heading("#3", text="AGE")
         tree.column("#4", anchor=tk.CENTER)
         tree.heading("#4", text="GENDER")
         tree.pack()

         for row in rows:
            print(row)
            tree.insert("", tk.END, values=row)

   def view_patient():
      global pat_id

      def search_pat_():
         pat_id_val = pat_id.get()
         if pat_id.get() == '' or pat_id.get() == 'Patient ID..':
            messagebox.showinfo("Error","Please fill Patient ID")
         else:
            print(pat_id_val)
            disp_pat_by_id(pat_id_val)

      b_frame = Frame(root,height=400,width=1080,bg='white')
      Label(b_frame, text='Search Patient', font='msserif 30',bg='white').place(x=420,y=10)
      Label(b_frame, text="Enter Patient ID:", font='msserif 12',bg='white').place(x=400,y=65)


      pat_id = Entry(b_frame, width=20, font=('Arial 20'))
      pat_id.place(x=400, y=110)

      search_pat = Button(b_frame, font='mssherif 20', text= " Search", bg='plum1',fg='orchid4',width=20, command=search_pat_).place(x=390,y=170)

      b_frame.place(x=0,y=120+6+20+60+11)
      b_frame.pack_propagate(False)
      b_frame.tkraise()

   def view_all_patients():
      comm = "select * from Patient;"
      cursor.execute(comm)
      rows = cursor.fetchall()

      view = tk.Tk()
      tree = ttk.Treeview(view, columns=("c1", "c2", "c3","c4"), show='headings')
      tree.column("#1", anchor=tk.CENTER)
      tree.heading("#1", text="Patient ID")
      tree.column("#2", anchor=tk.CENTER)
      tree.heading("#2", text="NAME")
      tree.column("#3", anchor=tk.CENTER)
      tree.heading("#3", text="AGE")
      tree.column("#4", anchor=tk.CENTER)
      tree.heading("#4", text="GENDER")
      tree.pack()

      for row in rows:
         print(row)
         tree.insert("", tk.END, values=row)

   def add_new_patient():
      global pat_id_, name_, age_, gender_

      def check_val_pat():

         pat_id_ = pat_id.get()
         name_ = Name.get()
         age_ = Age.get()
         gender_ = Gender.get()
         gender_set = ['M', 'F']

         print(pat_id_, name_, age_, gender_)
         if  pat_id_ == '' or name_ == '' or age_== '' or gender_ == '':
            messagebox.showinfo('Invalid', 'Please enter all values')
         elif gender_ not in gender_set:
            messagebox.showinfo('Invalid', 'Please enter gender as M or F')
         elif name_.isalpha == False:
            messagebox.showinfo('Invalid', 'Please enter proper name')
         elif age_.isnumeric == False:
            messagebox.showinfo('Invalid', 'Please enter correct age')
         else:
            cursor.execute("insert into Patient values(?,?,?,?)", (pat_id_, name_, age_, gender_))
            messagebox.showinfo("Successful","Patient added successfully")
            conn.commit()

      b_frame = Frame(root, height=400,width=1080,bg='white')
      Label(b_frame, text='New Patient Registration', font='msserif 30',bg='white').place(x=350,y=10)
      
      Label(b_frame, text='Patient ID : ', font=('Arial 15'), bg='plum1',).place(x=100, y=110)
      pat_id = Entry(b_frame, width=20, font=('Arial 15'))
      pat_id.place(x=250, y=110)

      Label(b_frame, text='Name : ', font=('Arial 15'), bg='plum1',).place(x=650, y=110)
      Name = Entry(b_frame, width=20, font=('Arial 15'))
      Name.place(x=800, y=110)

      Label(b_frame, text='Age : ', font=('Arial 15'), bg='plum1',).place(x=100, y=180)
      Age = Entry(b_frame, width=20, font=('Arial 15'))
      Age.place(x=250, y=180)

      Label(b_frame, text='Gender : ', font=('Arial 15'), bg='plum1',).place(x=650, y=180)
      Gender = Entry(b_frame, width=20, font=('Arial 15'))
      Gender.place(x=800, y=180)

      submit = Button(b_frame, font='mssherif 20', text= " Submit", bg='plum1',fg='orchid4',width=20, command=check_val_pat).place(x=390,y=210)
      

      b_frame.place(x=0,y=120+6+20+60+11)
      b_frame.pack_propagate(False)
      b_frame.tkraise()

   def patients():
      b_frame = Frame(root,height=400,width=1080,bg='white')
      view_pat = Button(b_frame,font='mssherif 20', text= " Search Patient", bg='plum1',fg='orchid4',width=20, command=view_patient).place(x=90,y=70)
      add_new_pat = Button(b_frame,font='mssherif 20', text= " Add New Patient", bg='plum1',fg='orchid4',width=20, command=add_new_patient).place(x=640,y=70)
      view_all_pat = Button(b_frame,font='mssherif 20', text= " View All Patients", bg='plum1',fg='orchid4',width=20, command=view_all_patients).place(x=360,y=190)
      
      b_frame.place(x=0,y=120+6+20+60+11)
      b_frame.pack_propagate(False)
      b_frame.tkraise()
   
########################################
########################################

#--------------------------------------------------------------------------------------------

##########################################
#######  TESTS  ##################

   def disp_rec_by_id(rec_id_val):
      comm = "select rc.record_num, rc.date, rc.pat_id, p.name, rc.sample_id,rc.test_id,rc.labo_id,rc.status,rc.result from Records rc, Patient p where record_num="+str(rec_id_val)+" and rc.pat_id = p.pat_id;"
      cursor.execute(comm)
      rows = cursor.fetchall()
      
      pdf.set_font("Arial", size = 30)
      pdf.add_page()
      pdf.cell(200, 10, txt = "Dr.DB Laboratory",ln = 1, align = 'C')
      pdf.set_font("Arial", size = 20)
      # add another cell
      pdf.cell(200, 10, txt = "Laboratory Test Record",ln = 2, align = 'C')
      
      ln=3
      pdf.set_font("Arial", size = 10)
      if len(rows)==0:
         messagebox.showinfo('Invalid', "Please enter a valid Record ID")
      else:
         view = tk.Tk()
         tree = ttk.Treeview(view, columns=("c1", "c2", "c3","c4", "c5", "c6", "c7","c8","c9"), show='headings')
         tree.column("#1", anchor=tk.CENTER)
         tree.heading("#1", text="RECORD NO.")
         tree.column("#2", anchor=tk.CENTER)
         tree.heading("#2", text="DATE")
         tree.column("#3", anchor=tk.CENTER)
         tree.heading("#3", text="PATIENT ID")
         tree.column("#4", anchor=tk.CENTER)
         tree.heading("#4", text="PATIENT NAME")
         tree.column("#5", anchor=tk.CENTER)
         tree.heading("#5", text="SAMPLE ID")
         tree.column("#6", anchor=tk.CENTER)
         tree.heading("#6", text="TEST ID")
         tree.column("#7", anchor=tk.CENTER)
         tree.heading("#7", text="LABORATORIAN")
         tree.column("#8", anchor=tk.CENTER)
         tree.heading("#8", text="STATUS")
         tree.column("#9", anchor=tk.CENTER)
         tree.heading("#9", text="RESULT")
         tree.pack()
         
         ct=0
         ln=3 
         
         headings = ['RECORD NO.', 'DATE', 'PATIENT ID','PATIENT NAME', 'SAMPLE ID', 'TEST ID', 'LABORATORIAN', 'STATUS', 'RESULT']
        
         for row in rows:
            for i in row: 
               lst=list(row)
               head=headings[ct].ljust(50)
               cellname=head+': '+str(lst[ct])
               print(cellname)
               pdf.cell(200, 10, cellname,ln=ln+1, align = 'L')
               ct=ct+1 
            print(row)
            tree.insert("", tk.END, values=row)
               
      recname='Rec'+str(rec_id_val)+'.pdf'
      pdf.output(name = recname)  
      #pdf.output("K:\Laboratory\Rec"+str(rec_id_val)".pdf")  

   def retrieve_record():
      global rec_id

      def search_rec_():
         rec_id_val = rec_id.get()
         if rec_id.get() == '' or rec_id.get() == 'Record ID..':
            messagebox.showinfo("Error","Please fill Record ID")
         else:
            print(rec_id_val)
            disp_rec_by_id(rec_id_val)

      b_frame = Frame(root,height=400,width=1080,bg='white')
      Label(b_frame, text='Retrieve Test Record', font='msserif 30',bg='white', fg='plum').place(x=380,y=10)
      Label(b_frame, text="Enter Record Number:", font='msserif 12',bg='white').place(x=400,y=65)


      rec_id = Entry(b_frame, width=20, font=('Arial 20'))
      rec_id.place(x=400, y=110)

      search_rec_ = Button(b_frame, font='mssherif 20', text= " Retrieve", bg='plum1',fg='orchid4',width=20, command=search_rec_).place(x=390,y=170)

      b_frame.place(x=0,y=120+6+20+60+11)
      b_frame.pack_propagate(False)
      b_frame.tkraise()
   
   def update_status():
      def set_status_button():
         rec_id_val = rec_id.get()
         com = "select * from Records where record_num="+str(rec_id_val)+";"
         cursor.execute(com)
         row = cursor.fetchall()

         if rec_id.get() == '' or rec_id.get() == 'Record ID..':
            messagebox.showinfo("Error","Please fill Record ID")
         elif len(row) == 0:
            messagebox.showinfo("Error","Please fill a valid Record ID")
         else:
            print(rec_id_val)
            set_status(rec_id_val)

      b_frame = Frame(root,height=400,width=1080,bg='white')
      Label(b_frame, text='Update Test Status', font='msserif 30',bg='white', fg='plum').place(x=420,y=10)
      Label(b_frame, text="Enter Record Number:", font='msserif 12',bg='white').place(x=400,y=65)

      rec_id = Entry(b_frame, width=20, font=('Arial 20'))
      rec_id.place(x=400, y=110)

      update = Button(b_frame, font='mssherif 20', text= " Retrieve", bg='plum1',fg='orchid4',width=20, command=set_status_button).place(x=390,y=170)

      b_frame.place(x=0,y=120+6+20+60+11)
      b_frame.pack_propagate(False)
      b_frame.tkraise()

   def set_status(rec_id_val):

      b_frame = Frame(root,height=400,width=1080,bg='white')
      Label(b_frame, text='Update Test Status', font='msserif 30',bg='white', fg='plum').place(x=420,y=20)
      txt = "Updating status for record number "+str(rec_id_val)+"...."
      Label(b_frame, text= txt, font='msserif 12',bg='white').place(x=350,y=70)

      com1 = "select result from Records where record_num="+str(rec_id_val)+";"
      cursor.execute(com1)
      result = cursor.fetchall()
      print(result[0][0])
      if result[0][0]=='Ready':
         b_frame = Frame(root,height=400,width=1080,bg='white')
         Label(b_frame, text='Test Result is Ready.', font='msserif 20',bg='white').place(x=420,y=100)
         b_frame.place(x=0,y=120+6+20+60+11)
         b_frame.pack_propagate(False)
         b_frame.tkraise()

      elif result[0][0]=='Not Ready':
         b_frame = Frame(root,height=400,width=1080,bg='white')
         txt = 'Update result for ID '+str(rec_id_val)
         Label(b_frame, text=txt, font='msserif 20',bg='white').place(x=420,y=20)
         com2 = "select status from Records where record_num="+str(rec_id_val)+";"
         cursor.execute(com2)
         status = cursor.fetchall()

         if status[0][0]=='Waiting':

            def update_final():
               sel = clicked.get()
               if sel == 'Completed':
                  comm_fin = "update Records set status='Completed',  result = 'Ready' where record_num="+str(rec_id_val)+";"
                  print(comm_fin)
                  cursor.execute(comm_fin)
                  conn.commit()
               messagebox.showinfo("Successful","Status updated successfully")

            options = ['Waiting','Completed']
            clicked = StringVar()
            clicked.set( "Waiting")
            drop = OptionMenu( b_frame , clicked , *options ).place(x=500, y=80)
            #drop.pack()
            ubutton = Button( b_frame , text = "Update" , command = update_final).place(x=510, y= 150)
            
            label = Label( b_frame , text = " " )
            label.pack()

            b_frame.place(x=0,y=120+6+20+60+11)
            b_frame.pack_propagate(False)
            b_frame.tkraise()

         if status[0][0]=='In Progress':

            def update_final():
               sel = clicked.get()
               if sel == 'Waiting':
                  comm_fin = "update Records set status='Waiting', result = 'Not Ready' where record_num="+str(rec_id_val)+";"
               elif sel == 'In Progress':
                  comm_fin = "update Records set status='In Progress', result = 'Not Ready' where record_num="+str(rec_id_val)+";"
               elif sel == 'Completed':
                  comm_fin = "update Records set status='Completed', result = 'Ready' where record_num="+str(rec_id_val)+";"

               print(comm_fin)
               cursor.execute(comm_fin)
               conn.commit()
               messagebox.showinfo("Successful","Status updated successfully")

            options = ['In Progress','Waiting','Completed']
            clicked = StringVar()
            clicked.set( "In Progress")
            drop = OptionMenu( b_frame , clicked , *options ).place(x=500, y=80)
            #drop.pack()
            ubutton = Button( b_frame , text = "Update" , command = update_final).place(x=510, y= 150)
            label = Label( b_frame , text = " " )
            label.pack()

            b_frame.place(x=0,y=120+6+20+60+11)
            b_frame.pack_propagate(False)
            b_frame.tkraise()

      b_frame.place(x=0,y=120+6+20+60+11)
      b_frame.pack_propagate(False)
      b_frame.tkraise()

   def tests():
      b_frame = Frame(root,height=400,width=1080,bg='white')
      view_pat = Button(b_frame,font='mssherif 20', text= " Retrieve Record", bg='plum1',fg='orchid4',width=20, command=retrieve_record).place(x=90,y=100)
      add_new_pat = Button(b_frame,font='mssherif 20', text= " Update Status", bg='plum1',fg='orchid4',width=20, command=update_status).place(x=640,y=100)
      
      b_frame.place(x=0,y=120+6+20+60+11)
      b_frame.pack_propagate(False)
      b_frame.tkraise()

########################################
########################################

#--------------------------------------------------------------------------------------------

##########################################
#######  HISTORY  ##################

   def fetch(pat_id_val):
      comm = "select * from Records where pat_id="+str(pat_id_val)+";"
      cursor.execute(comm)
      rows = cursor.fetchall()

      if len(rows)==0:
         messagebox.showinfo('Invalid', "Please enter a valid Patient ID")
      else:
         view = tk.Tk()
         tree = ttk.Treeview(view, columns=("c1", "c2", "c3","c4", "c5", "c6", "c7","c8"), show='headings')
         tree.column("#1", anchor=tk.CENTER)
         tree.heading("#1", text="RECORD NO.")
         tree.column("#2", anchor=tk.CENTER)
         tree.heading("#2", text="DATE")
         tree.column("#3", anchor=tk.CENTER)
         tree.heading("#3", text="PATIENT ID")
         tree.column("#4", anchor=tk.CENTER)
         tree.heading("#4", text="SAMPLE ID")
         tree.column("#5", anchor=tk.CENTER)
         tree.heading("#5", text="TEST ID")
         tree.column("#6", anchor=tk.CENTER)
         tree.heading("#6", text="LABORATORIAN")
         tree.column("#7", anchor=tk.CENTER)
         tree.heading("#7", text="STATUS")
         tree.column("#8", anchor=tk.CENTER)
         tree.heading("#8", text="RESULT")
         tree.pack()

         for row in rows:
            print(row)
            tree.insert("", tk.END, values=row)
   
   def history():
      global pat_id

      def history_():
         pat_id_val = pat_id.get()
         if pat_id.get() == '' or pat_id.get() == 'Record ID..':
            messagebox.showinfo("Error","Please fill Patient ID")
         else:
            print(pat_id_val)
            fetch(pat_id_val)

      b_frame = Frame(root,height=400,width=1080,bg='white')
      Label(b_frame, text='History', font='msserif 30',bg='white', fg='plum').place(x=500,y=10)
      Label(b_frame, text="Enter Patient ID:", font='msserif 12',bg='white').place(x=400,y=65)


      pat_id = Entry(b_frame, width=20, font=('Arial 20'))
      pat_id.place(x=400, y=110)

      htry_btn = Button(b_frame, font='mssherif 20', text= " Retrieve", bg='plum1',fg='orchid4',width=20, command=history_).place(x=390,y=170)

      b_frame.place(x=0,y=120+6+20+60+11)
      b_frame.pack_propagate(False)
      b_frame.tkraise()

########################################
########################################

#--------------------------------------------------------------------------------------------

##########################################
#######  NEW TEST  ##################

   def new_test():

      global clicked1, b_frame_t, pat_id, dt, pat_id__, date, sample_id, status, result, rec_num

      b_frame_t = Frame(root, height=400,width=1080,bg='white')
      Label(b_frame_t, text='New Test', font='msserif 30',bg='white').place(x=450,y=10)
      
      ext_val = "select count(record_num) from records;"
      cursor.execute(ext_val)
      rec_num = cursor.fetchone()
      rec_num = int(rec_num[0])
      rec_num += 1
      sample_id = rec_num
      status = 'In Progress'
      result = 'Not Ready'

      Label(b_frame_t, text='Patient ID : ', font=('Arial 12'), bg='plum1',).place(x=100, y=110)
      pat_id = Entry(b_frame_t, width=20, font=('Arial 12'))
      pat_id.place(x=250, y=110)

      Label(b_frame_t, text='Date : (YYYY-MM-DD)', font=('Arial 12'), bg='plum1',).place(x=100, y=180)
      dt = Entry(b_frame_t, width=20, font=('Arial 12'))
      dt.place(x=250, y=180)

      pat_id__ = pat_id.get()
      date = dt.get()

#test_id from test type, find available labo id from test from department, extract sample type from test
      Label(b_frame_t, text='Test Name :', font=('Arial 12'), bg='plum1',).place(x=600, y=110)
      test_options = ["Complete Blood Count Test","BMP clinical Test","CMP clinical test","Lipid Panel","Liver Panel","Thyroid Function","Urinalysis","Blood Sugar","Acute Leukemia panel","Adrenal antibody","ANCA","B2 Microglobulin","CD34","CD4 Count","Covid19 Antibodies","Ganglioslide Abs GQ1b","Ovary Antibodies","Rheumatoid factor","Serum Protein","Bacterial culture and sensitivity testing (Aerobic)","Blood culture and sensitivity","Hepatitis A","Hepatitis B","Hepatitis C","Hepatits E","Herpes Simplex virus","HIV","Dengue IgM ELISA","Malaria Antigen","Fungal Blood Culture","Anal pap","Body cavity fluids","Bronchoalveolar lavage","Brush biopsy specimen","Cerebrospinal fluid","Cyst fluid","Pap test","Skin scrape","Sputum","Urine","Wash/washing","Full Blood Picture (FBP)","PT / APTT","ESR","G6PD Screening","G6PD Assay","Osmotic Fragility Test (OFT)","Haemoglobinopathy Analysis","Haemoglobin Electrophoresis","NAP Score","Carbohydrates","Lipids","Enzymes","Protein","Metabolites"]
      clicked1 = StringVar()
      clicked1.set("Select")
      drop1 = OptionMenu( b_frame_t , clicked1 , *test_options ).place(x=750, y=110)
      #drop.pack()
      
      ubutton1 = Button( b_frame_t , text = "Next" , command = next).place(x=950, y= 110)
      

      b_frame_t.place(x=0,y=120+6+20+60+11)
      b_frame_t.pack_propagate(False)
      b_frame_t.tkraise()

   def next():
      global clicked2, test_id, sample_type
      sel1 = clicked1.get()
      tst_comm = "select test_id from Test where test_name='"+str(sel1)+"';"
      print(tst_comm)
      cursor.execute(tst_comm)
      test_id = cursor.fetchone()
      test_id = int(test_id[0])

      samp_comm = "select specimen_type from Test where test_id="+str(test_id)+";"
      print(samp_comm)
      cursor.execute(samp_comm)
      sample_type = cursor.fetchone()
      sample_type = str(sample_type[0])

      dep_comm = "select department from Test where test_id="+str(test_id)+";"
      print(dep_comm)
      cursor.execute(dep_comm)
      dept = cursor.fetchone()
      dept = str(dept[0])

      labo_comm = "select labo_id from Laboratorian where department='"+str(dept)+"';"
      print(labo_comm)
      cursor.execute(labo_comm)
      
      labo_list = [item[0] for item in cursor.fetchall()]
      print(labo_list)

      clicked2 = StringVar()
      clicked2.set('Select')
      Label(b_frame_t, text='Assign Laboratorian :', font=('Arial 12'), bg='plum1',).place(x=600, y=180)
      drop2 = OptionMenu( b_frame_t , clicked2 , *labo_list ).place(x=750, y=180)
      ubutton2 = Button( b_frame_t , text = "Next" , command = next2).place(x=950, y= 180)

   def next2():
      global labo_id_,pat_id__, date
      sel2 = clicked2.get()
      labo_id_ = int(sel2)

      pat_id__ = str(pat_id.get())
      date = str(dt.get())
      print(pat_id__)
      print(date)


      if pat_id__=="" or date=="":
         messagebox.showinfo("Error","Please fill all values")
      else:
         submit_button = Button( b_frame_t , text = "SUBMIT" , command = submit).place(x=500, y= 250)
   def submit():
      st_pid = str(pat_id__)
      print(st_pid)

      labo_comm = "select pat_id from Patient where pat_id="+pat_id__+";"
      cursor.execute(labo_comm)
      chkp = cursor.fetchall()
      if len(chkp) == 0:
         messagebox.showinfo('Error', 'Patient ID not found! Please register new patient first')
      else:
         s_conn = "insert into sample values ("+str(sample_id)+",'"+sample_type+"',"+str(labo_id_)+","+pat_id__+",'"+date+"');"
         print(s_conn)

         cursor.execute(s_conn)
         conn.commit()

         r_conn = "insert into records values ("+str(rec_num)+",'"+date+"',"+pat_id__+","+str(sample_id)+","+str(test_id)+","+str(labo_id_)+",'"+status+"','"+result+"');"
         print(r_conn)
         cursor.execute(r_conn)
         conn.commit()

         messagebox.showinfo('Success', 'Successfully added new test!')

      b_frame.place(x=0,y=120+6+20+60+11)
      b_frame.pack_propagate(False)
      b_frame.tkraise()





#--------------------------------------------------------------------------------------------

##########################################

   def logout():
      q = messagebox.askyesno("Exit","Do you really want to exit ?")
      if(q):
         conn.close()
         root.destroy()


   sl_frame = Frame(root,height=130,width=1080,bg='white')
   sl_frame.place(x=0,y=70+6)

   path = "icons/new_test_logo.png"
   img = ImageTk.PhotoImage(Image.open(path))
   b1 = Button(sl_frame,image=img,text='b1',bg='white',width=180, command=new_test)
   b1.image = img
   b1.place(x=0,y=0)

   path = "icons/patient_icon.png"
   img = ImageTk.PhotoImage(Image.open(path))
   b1 = Button(sl_frame,image=img,text='b1',bg='white',width=180, command=patients)
   b1.image = img
   b1.place(x=180,y=0)

   path2 = "icons/test_icon.png"
   img2 = ImageTk.PhotoImage(Image.open(path2))
   b2 = Button(sl_frame,image=img2,text='b2',bg='white',width=180, command=tests)
   b2.image = img2
   b2.place(x=180*2,y=0)

   path3='icons/history_icon.png'
   img3 = ImageTk.PhotoImage(Image.open(path3))
   b3 = Button(sl_frame,image=img3,text='b2',bg='white',width=180, command=history)
   b3.image = img3
   b3.place(x=180*3,y=0)

   path4='icons/laboratorian_icon.png'
   img4 = ImageTk.PhotoImage(Image.open(path4))
   b4 = Button(sl_frame,image=img4,text='b2',bg='white',width=180, command=laboratorians)
   b4.image = img4
   b4.place(x=180*4,y=0)

   path5='icons/exit_icon.png'
   img5 = ImageTk.PhotoImage(Image.open(path5))
   b5 = Button(sl_frame,image=img5,text='b2',bg='white',width=180,height=100, command=logout)
   b5.image = img5
   b5.place(x=180*5,y=0)
   
   Label(sl_frame,text='New Test',font='msserif 13',bg='white').place(x=45,y=106)
   Label(sl_frame,text='Patients',font='msserif 13',bg='white').place(x=248,y=106)
   Label(sl_frame,text='Tests',font='msserif 13',bg='white').place(x=417,y=106)
   Label(sl_frame,text='History',font='msserif 13',bg='white').place(x=600,y=106)
   Label(sl_frame,text='Laboratorians',font='msserif 13',bg='white').place(x=760,y=106)
   Label(sl_frame,text='Exit',font='msserif 13',bg='white').place(x=968,y=106)
   sl_frame.pack_propagate(False)
   #-------------------extra frame------------------------------------------------------------------------------------------------------------------
   redf = Frame(root,height=6,width=1080,bg='lightsteelblue3')
   redf.place(x=0,y=70)
   redf1 = Frame(root,height=40,width=1080,bg='lightsteelblue3')
   redf1.place(x=0,y=210)
   mainloop()
  
sroot.after(2000,call_mainroot)
mainloop()