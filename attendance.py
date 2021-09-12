from os import read
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 


class Attendance:
    def __init__(self,root,):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Student")


    #       first image
        img=Image.open(r"img\smart-attendance.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)


#second image

        img1=Image.open(r"img\clg.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=130)

##################bg image 
        img3=Image.open(r"img\bgimg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white" )
        main_frame.place(x=20,y=55,width=1480,height=600)


###################  left label frame  ###################3

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)


        img_left=Image.open(r"img\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white" )
        left_inside_frame.place(x=0,y=135,width=720,height=370)


        ##################3 Label entry ##############################
    #attendance id

        attendanceID_label=Label(left_inside_frame,text="Attendance ID: ",font=("times new roman",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

#################### RollNO ########################################


        rollno_label=Label(left_inside_frame,text="Roll No: ",font=("times new roman",12,"bold"),bg="white")
        rollno_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        rollno_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=0,column=3,pady=8,sticky=W)

################################ Name############################################



        name_label=Label(left_inside_frame,text="Name ",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

################  Department ####################33

        department_label=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        department_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
    
#########################3 time $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        time_label=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)



############################### Date ##################################################################

        date_label=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)






################################## Attendance #######################################################



        attendanceLabel=Label(left_inside_frame,text="Attendance Status",bg="white",font="comicsansna 11 bold")
        attendanceLabel.grid(row=3,column=0)



        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="comicsansns 11 bold ",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)



        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

######################  IMPORT BUTTON save#########################3
        save_btn=Button(btn_frame,text="Import Csv",font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        save_btn.grid(row=0,column=0)


################### EXPORT Button ###################
        update_btn=Button(btn_frame,text="Export Csv",font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        update_btn.grid(row=0,column=1)

###################################  UPDATE Button #################################################33

        delete_btn=Button(btn_frame,text="Update",font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        delete_btn.grid(row=0,column=2)


####################################Reset data ##########################################################

        reset_btn=Button(btn_frame,text="Reset",font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        reset_btn.grid(row=0,column=3)












###################  Right label frame  ###################3

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=710,height=580)



        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        ############################# Scroll Bar Table ###################################33


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","data","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll ")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)





        self.AttendanceReportTable.pack(fill=BOTH,expand=1)



















if __name__ == "__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop()