from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        #variables
        self.varcaseid=StringVar()
        self.varcriminalno=StringVar()
        self.varcrimename=StringVar()
        self.varnickname=StringVar()
        self.vararrestdate=StringVar()
        self.vardateofcrime=StringVar()
        self.varaddress=StringVar()
        self.varage=StringVar()
        self.varoccupation=StringVar()
        self.varbirthmark=StringVar()
        self.varcrimetype=StringVar()
        self.varfathername=StringVar()
        self.vargender=StringVar()
        self.varwanted=StringVar()

        lbl_title = Label(self.root, text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE', font=('times new roman', 40, 'bold'),bg='black', fg='gold')
        lbl_title.place(x=0, y=0, width=1530, height=70)

        # nlogo
        img_logo = Image.open('images/nr.png')
        img_logo = img_logo.resize((60,60))
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=80, y=5, width=60, height=60)

        # Img_frame
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=70, width=1530, height=130)

        img1=Image.open('images/p1.jpeg')
        img1=img1.resize((540,160))
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        img1 = Image.open('images/p1.jpeg')
        img1 = img1.resize((540, 160))
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img1 = Label(img_frame, image=self.photo1)
        self.img1.place(x=0, y=0, width=540, height=160)

        img2 = Image.open('images/p2.jpeg')
        img2 = img2.resize((540, 160))
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img2 = Label(img_frame, image=self.photo2)
        self.img2.place(x=540, y=0, width=540, height=160)

        img3 = Image.open('images/p3.jpeg')
        img3 = img3.resize((540, 160))
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=1080, y=0, width=540, height=160)

        #Main Frame
        Main_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_Frame.place(x=10,y=200,width=1500,height=560)

        #upperImage
        upper_frame=LabelFrame(Main_Frame,bd=2,relief=RIDGE,text='Criminal Information', font=('times new roman', 11, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1480, height=270)
        #case id
        caseid=Label(upper_frame,text='CASE ID:',font=('arial',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,width=22,textvariable=self.varcaseid,font=("arial",11,"bold"))
        caseentry.grid(row=0, column=1, padx=2, sticky=W)
        #criminal No
        lbl_crimina_no = Label(upper_frame, text='CRIMINAL NO:', font=('arial', 11, 'bold'), bg='white')
        lbl_crimina_no.grid(row=0, column=2, padx=2, sticky=W,pady=7)

        tcriminalno= ttk.Entry(upper_frame, width=22,textvariable=self.varcriminalno, font=("arial", 11, "bold"))
        tcriminalno.grid(row=0, column=3, padx=2,pady=7)
        #Criminal name
        lcriminal_name = Label(upper_frame, text='CRIMINAL NAME:', font=('arial', 11, 'bold'), bg='white')
        lcriminal_name.grid(row=1, column=0, padx=2, sticky=W,pady=7)

        tcriminalno= ttk.Entry(upper_frame, width=22, textvariable=self.varcrimename,font=("arial", 11, "bold"))
        tcriminalno.grid(row=1, column=1, padx=2,pady=7)
        #nick name
        lnickname = Label(upper_frame, text='NICK NAME:', font=('arial', 11, 'bold'), bg='white')
        lnickname.grid(row=1, column=2, padx=2, sticky=W, pady=7)

        tnickname = ttk.Entry(upper_frame, width=22,textvariable=self.varnickname, font=("arial", 11, "bold"))
        tnickname.grid(row=1, column=3, padx=2, pady=7)
        #Arrest Date
        larrestdate = Label(upper_frame, text='ARREST DATE:', font=('arial', 11, 'bold'), bg='white')
        larrestdate.grid(row=2, column=0, padx=2, sticky=W, pady=7)

        tarrestdate = ttk.Entry(upper_frame, width=22, textvariable=self.vararrestdate,font=("arial", 11, "bold"))
        tarrestdate.grid(row=2, column=1, padx=2, pady=7)
        #dATE OF CRIME
        ldate = Label(upper_frame, text='DATE OF CRIME:', font=('arial', 11, 'bold'), bg='white')
        ldate.grid(row=2, column=2, padx=2, sticky=W, pady=7)

        tdate = ttk.Entry(upper_frame, width=22, textvariable=self.vardateofcrime,font=("arial", 11, "bold"))
        tdate.grid(row=2, column=3, padx=2, pady=7)

        #address
        laddress = Label(upper_frame, text='ADDRESS:', font=('arial', 11, 'bold'), bg='white')
        laddress.grid(row=3, column=0, padx=2, sticky=W, pady=7)

        taddress= ttk.Entry(upper_frame, width=22, textvariable=self.varaddress,font=("arial", 11, "bold"))
        taddress.grid(row=3, column=1, padx=2, pady=7)
        #occupation
        loccupation=Label(upper_frame, text='OCCUPATION:', font=('arial', 11, 'bold'), bg='white')
        loccupation.grid(row=4, column=0, padx=2, sticky=W,pady=7)

        toccupation= ttk.Entry(upper_frame, width=22, textvariable=self.varoccupation,font=("arial", 11, "bold"))
        toccupation.grid(row=4, column=1, padx=2,pady=7)

        #age
        lage= Label(upper_frame, text='AGE:', font=('arial', 11, 'bold'), bg='white')
        lage.grid(row=3, column=2, padx=2, sticky=W, pady=7)

        tage = ttk.Entry(upper_frame, width=22,textvariable=self.varage, font=("arial", 11, "bold"))
        tage.grid(row=3, column=3, padx=2, pady=7)
        # Birth Mark
        lbm = Label(upper_frame, text='BIRTH MARK:', font=('arial', 11, 'bold'), bg='white')
        lbm.grid(row=4, column=2, padx=2, sticky=W, pady=7)

        tbm = ttk.Entry(upper_frame, width=22, textvariable=self.varbirthmark,font=("arial", 11, "bold"))
        tbm.grid(row=4, column=3, padx=2, pady=7)
        # CRIME TYPE
        lCT = Label(upper_frame, text='CRIME TYPE:', font=('arial', 11, 'bold'), bg='white')
        lCT.grid(row=0, column=4, padx=2, sticky=W, pady=7)

        tCT = ttk.Entry(upper_frame, width=22, textvariable=self.varcrimetype,font=("arial", 11, "bold"))
        tCT.grid(row=0, column=5, padx=2, pady=7)
        #Father name
        lfn = Label(upper_frame, text='FATHER NAME:', font=('arial', 11, 'bold'), bg='white')
        lfn.grid(row=1, column=4, padx=2, sticky=W, pady=7)

        tfn = ttk.Entry(upper_frame, width=22,textvariable=self.varfathername, font=("arial", 11, "bold"))
        tfn.grid(row=1, column=5, padx=2, pady=7)
        #gender
        lgender = Label(upper_frame, text='GENDER:', font=('arial', 11, 'bold'), bg='white')
        lgender.grid(row=2, column=4, padx=2, sticky=W, pady=7)

        tGN = ttk.Entry(upper_frame, width=22,font=("arial", 11, "bold"))
        tGN.grid(row=2, column=5, padx=2, pady=7)

        radio_buttongn= ttk.Radiobutton(tGN, width=10, variable=self.vargender,text="MALE",value="MALE")
        radio_buttongn.grid(row=0, column=0, padx=5, pady=2,sticky=W)
        #self.vargender.set('MALE')

        radio_buttonf= ttk.Radiobutton(tGN, width=10, variable=self.vargender,text="FEMALE",value="FEMALE")
        radio_buttonf.grid(row=0, column=1, padx=5, pady=2,sticky=W)
        #most wanted
        lmw = Label(upper_frame, text='MOST WANTED:', font=('arial', 11, 'bold'), bg='white')
        lmw.grid(row=3, column=4, padx=2, sticky=W, pady=7)
        tmw = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"))
        tmw.grid(row=3, column=5, padx=2, pady=7)

        radio_buttonmw = ttk.Radiobutton(tmw, width=10,variable=self.varwanted,text="YES",value="YES")
        radio_buttonmw.grid(row=0, column=0, padx=5, pady=2,sticky=W)

        radio_buttonmno = ttk.Radiobutton(tmw, width=10, variable=self.varwanted,text="NO",value="NO")
        radio_buttonmno.grid(row=0, column=1, padx=5, pady=2,sticky=W)

        #buttons frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE, bg='white')
        button_frame.place(x=5,y=200,width=620,height=45)

        #add button
        add = Button(button_frame, width=14, command=self.add_data,text="RECORD SAVE",font=("arial", 13, "bold"),fg="white",bg='blue')
        add.grid(row=0, column=0, padx=3, pady=5, sticky=W)
        #update

        update= Button(button_frame, width=14,command=self.update_data, text="UPDATE", font=("arial", 13, "bold"),fg="white", bg='blue')
        update.grid(row=0, column=1, padx=3, pady=5, sticky=W)

        delete = Button(button_frame, width=14,command=self.delete_data, text="DELETE", font=("arial", 13, "bold"),fg="white", bg='blue')
        delete.grid(row=0, column=2, padx=3, pady=5, sticky=W)

        clear = Button(button_frame, width=14, command=self.clear_data,text="CLEAR",font=("arial", 13, "bold"), fg="white", bg='blue')
        clear.grid(row=0, column=3, padx=3, pady=5, sticky=W)

        img4 = Image.open('images/img4.jpg')
        img4 = img4.resize((470,245))
        self.photo4 = ImageTk.PhotoImage(img4)

        self.img_4 = Label(upper_frame, image=self.photo4)
        self.img_4.place(x=1000, y=0, width=470, height=245)

        #down Frame
        down_frame = LabelFrame(Main_Frame, bd=2, relief=RIDGE, text='Criminal Information Table' ,font=('times new roman', 11, 'bold'), fg='red')
        down_frame.place(x=10, y=280, width=1480, height=270)

        #search frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, text='Search Criminal Record',font=('times new roman', 11, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1470, height=60)

        searchlabel= Label(search_frame, text='SEARCH BY:', font=('arial', 11, 'bold'), bg='red',fg='white')
        searchlabel.grid(row=0, column=0, padx=5, sticky=W)

        self.var_com_search=StringVar()
        comboxsearch=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial', 11, 'bold'),width=18)
        comboxsearch['value']=('Select option','Case_id','criminal_no')
        comboxsearch.current(0)
        comboxsearch.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        tsearch = ttk.Entry(search_frame, width=18,textvariable=self.var_search, font=("arial", 11, "bold"))
        tsearch.grid(row=0, column=2, padx=5)

        #search button
        btnsearch = Button(search_frame, width=14,command=self.search_data, text="SEARCH", font=("arial", 13, "bold"), fg="white", bg='blue')
        btnsearch.grid(row=0, column=3, padx=3, pady=5, sticky=W)

        btnall= Button(search_frame, command=self.fetch_data,width=14, text='SHOW ALL', font=("arial", 13, "bold"), fg="white", bg='blue')
        btnall.grid(row=0, column=4, padx=3, pady=5, sticky=W)

        crimeagency=Label(search_frame,text='NATIONAL CRIME AGENCY',font=("arial", 30, "bold"),fg='crimson',bg='white')
        crimeagency.grid(row=0,column=5,padx=60)

        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminaltable=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminaltable.xview)
        scroll_y.config(command=self.criminaltable.yview)

        self.criminaltable.heading('1',text='CASE ID')
        self.criminaltable.heading('2', text='CRIME NO')
        self.criminaltable.heading('3',text='CRIMINAL NAME')
        self.criminaltable.heading('4', text='NICK NAME')
        self.criminaltable.heading('5', text='ARREST DATE')
        self.criminaltable.heading('6', text='CRIME OF DATE')
        self.criminaltable.heading('7', text='ADDRESS')
        self.criminaltable.heading('8', text='AGE')
        self.criminaltable.heading('9', text='OCCUPATION')
        self.criminaltable.heading('10', text='BIRTH MARK')
        self.criminaltable.heading('11', text='CRIME TYPE')
        self.criminaltable.heading('12', text='FATHER NAME')
        self.criminaltable.heading('13', text='GENDER')
        self.criminaltable.heading('14', text='WANTED')

        self.criminaltable['show']='headings'
        self.criminaltable.column('1',width=100)
        self.criminaltable.column('2', width=100)
        self.criminaltable.column('3', width=100)
        self.criminaltable.column('4', width=100)
        self.criminaltable.column('5',width=100)
        self.criminaltable.column('6', width=100)
        self.criminaltable.column('7', width=100)
        self.criminaltable.column('8', width=100)
        self.criminaltable.column('9', width=100)
        self.criminaltable.column('10', width=100)
        self.criminaltable.column('11', width=100)
        self.criminaltable.column('12', width=100)
        self.criminaltable.column('13', width=100)
        self.criminaltable.column('14', width=100)

        self.criminaltable.pack(fill=BOTH,expand=1)
        self.criminaltable.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #add Function

    def add_data(self):
        if self.varcaseid.get()=="":
            messagebox.showerror('Error','All fields Are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Mdubey@2001',database='managment')
                my_cursor=conn.cursor()
                my_cursor.execute(
                    'INSERT INTO criminal1 (case_id, criminal_no, criminal_name, nickname, arrest_date, dateofcrime, address, age, occupation, birth_mark, crime_type, father_name, gender, wanted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (
                        self.varcaseid.get(),
                        self.varcriminalno.get(),
                        self.varcrimename.get(),
                        self.varnickname.get(),
                        self.vararrestdate.get(),
                        self.vardateofcrime.get(),
                        self.varaddress.get(),
                        self.varage.get(),
                        self.varoccupation.get(),
                        self.varbirthmark.get(),
                        self.varcrimetype.get(),
                        self.varfathername.get(),
                        self.vargender.get(),
                        self.varwanted.get()
                    ))

                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal Record has been added')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')
    #fetchdata
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Mdubey@2001', database='managment')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from criminal1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminaltable.delete(*self.criminaltable.get_children())
            for i in data:
                self.criminaltable.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.criminaltable.focus()
        content=self.criminaltable.item(cursor_row)
        data=content['values']

        self.varcaseid.set(data[0])
        self.varcriminalno.set(data[1])
        self.varcrimename.set(data[2])
        self.varnickname.set(data[3])
        self.vararrestdate.set(data[4])
        self.vardateofcrime.set(data[5])
        self.varaddress.set(data[6])
        self.varage.set(data[7])
        self.varoccupation.set(data[8])
        self.varbirthmark.set(data[9])
        self.varcrimetype.set(data[10])
        self.varfathername.set(data[11])
        self.vargender.set(data[12])
        self.varwanted.set(data[13])

    def update_data(self):
        if self.varcaseid.get()=="":
            messagebox.showerror('Error', 'All fields Are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure to update this criminal record')
                if update > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Mdubey@2001',
                                               database='managment')
                    my_cursor = conn.cursor()

                    my_cursor.execute(
                    'update criminal1 set criminal_no=%s, criminal_name=%s, nickname=%s, arrest_date=%s, dateofcrime=%s, address=%s, age=%s, occupation=%s, birth_mark=%s, crime_type=%s, father_name=%s, gender=%s, wanted=%s where Case_id=%s',
                       (
                        self.varcriminalno.get(),
                        self.varcrimename.get(),
                        self.varnickname.get(),
                        self.vararrestdate.get(),
                        self.vardateofcrime.get(),
                        self.varaddress.get(),
                        self.varage.get(),
                        self.varoccupation.get(),
                        self.varbirthmark.get(),
                        self.varcrimetype.get(),
                        self.varfathername.get(),
                        self.vargender.get(),
                        self.varwanted.get(),
                        self.varcaseid.get()

                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record Succesfully update')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    #delete
    def delete_data(self):
        if self.varcaseid.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                delete= messagebox.askyesno('Delete', 'Are you sure to delete this criminal record')
                if delete > 0:
                    conn=conn=mysql.connector.connect(host='localhost',username='root',password='Mdubey@2001',database='managment')
                    my_cursor=conn.cursor()
                    sql='delete from criminal1 where case_id=%s'
                    value=(self.varcaseid.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success', 'Criminal record Successfully deleted')
            except Exception as es:
                messagebox.showerror('Error', f'Due To{str(es)}')
    #clear
    def clear_data(self):

        self.varcaseid.set("")
        self.varcriminalno.set("")
        self.varcrimename.set("")
        self.varnickname.set("")
        self.vararrestdate.set("")
        self.vardateofcrime.set("")
        self.varaddress.set("")
        self.varage.set("")
        self.varoccupation.set("")
        self.varbirthmark.set("")
        self.varcrimetype.set("")
        self.varfathername.set("")
        self.vargender.set("")
        self.varwanted.set("")
    #search
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Mdubey@2001',
                                               database='managment')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from criminal1 where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminaltable.delete(*self.criminaltable.get_children())
                    for i in rows:
                        self.criminaltable.insert("", END, values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due To{str(es)}')

























if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()