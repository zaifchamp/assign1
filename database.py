
import MySQLdb #connecting with database
from Tkinter import * #import GUI libraray
import tkFont
import getpass
import tkMessageBox

db = MySQLdb.connect("localhost", "root", "", "quiz_system") #database name and table name
cursor = db.cursor() #opening database
count=0
def star(): #function for for student

        count=0
        sql5 = "SELECT id,questions,answers,quiz_id FROM question " # query to question , quiz id and ID
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(sql5)

        result_set = cursor.fetchall()
        for row in result_set:
            print "%s, %s" % (row["id"], row["questions"])
            sql4="SELECT optionchoice, optionchoice2, optionchoice3, optionchoice4 FROM mcqsoptions WHERE question_id=%s"
            cursor.execute(sql4,str(row["id"])) # loop for collecting MCQs option
            user1 = cursor.fetchone()
            print user1
            student_answer=raw_input("Enter the answer") #taking user answer
            if (student_answer==row["answers"]): # checking user answer
                count=count+1


            print "Your score is "

        print count
def answer(event, arg, arg1):

        student_answer=arg.get()

        if (student_answer==arg1):
            star().count=count+1


def _teacher(): # function for the user
    root = Tk()
    T = Text(root, height=2, width=30)
    T.pack()
    T.insert(END, "Enter the title of the quiz\n") # title and description
    title=raw_input("Now Enter the title of quiz\n")
    description=raw_input("Enter the description of quiz\n")
    sql1 = "INSERT INTO quizzes(title, \
       description) \
       VALUES ('%s', '%s')" % \
       (title, description) #query for inserting title and description

    # Execute the SQL command
    cursor.execute(sql1)
    # Commit your changes in the database

    sql71 = cursor.lastrowid
    for x in range(0, 10):
        keypress=raw_input("What type of quiz you wnat to take?\n1.MCQs\n2.TrueFalse\n3.Numeric\n")
        if(keypress=='MCQs') : # asking what type of question
            question=raw_input("Enter the questions of quiz\n")
            answer=raw_input("Enter the answer\n")


        elif(keypress=='TrueFalse'):
            ans=raw_input()
        elif(keypress=='Numeric'):
            ans1=raw_input()


        sql2 = "INSERT INTO question (questions, \
           answers,quiz_id) \
           VALUES ('%s','%s','%s')" % \
           (question, answer,sql71)

            # Execute the SQL command
        cursor.execute(sql2)
            # Commit your changes in the database

        print"Enter the Multiple choice of question"
        # sql7="SELECT id from question ORDER BY id DESC"
        # cursor.execute(sql7)
        #sql7 = cursor.fetchone()
        #sql71=str(sql7)
        sql7 = cursor.lastrowid

        choice1=raw_input("Enter the 1st choice")#taking choice from teacher
        choice2=raw_input("Enter the 2nd choice")
        choice3=raw_input("Enter the 3rd choice")
        choice4=raw_input("Enter the 4th choice")

        sql3 = "INSERT INTO mcqsoptions(optionchoice, \
           optionchoice2,optionchoice3,optionchoice4,question_id) \
           VALUES ('%s','%s','%s','%s','%s')" % \
           (choice1, choice2,choice3,choice4,sql7)
        cursor.execute(sql3)
        db.commit() #inserting mcqs option from teacher


        db.close()
        response=raw_input("Do you want to add another question \nPress y/n ")
        if(response=='y'):
            continue

        else:
            break

    db.close()

def _login(): #login function
    usr=e1.get()
    pas=e2.get()
    sql=("SELECT * from login WHERE username=%s AND password=%s")
    cursor.execute(sql,(usr,pas))
    user, passw, role = cursor.fetchone()
    if (role=="teacher"):
        _teacher()
    if (role=="student"):
    #       master1 = Tk()
    #       Label(master1, text="thisis").grid(row=0)
    #        Label(master1, text="Pass").grid(row=1)
    #        e3 = Entry(master1)
    #        e4 = Entry(master1)
    #        e3.grid(row=0, column=1)
    #        e4.grid(row=1, column=1)
    #       Button(master1,text="Login",command=star).grid(row=2)
    #        mainloop( )
        star()
        print user,passw,role
class FullScreenApp(object):#full screen function
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


master = Tk()
app=FullScreenApp(master)
Label(master, text="Username").grid(row=0)
Label(master, text="Password").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(master,text="Login",command=_login).grid(row=2)
mainloop( )

#username = raw_input("USERNAME: ")
#password = raw_input("PASSWORD: ")

#sql = "SELECT * from login WHERE username=%s AND password=%s"
#entry = (username,password)
#cursor.execute(sql, entry)
#user, passw, role = cursor.fetchone()
#print user,passw, role





