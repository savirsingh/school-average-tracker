# code by savir singh
# interface.py - School Average Tracker

def add_Grade():
    def push_Grade():
        newline=True
        temp = int(en.get())
        a = open("data.singh", "r")
        if a.read()=="NULL":
            f = open("data.singh", "w")
            newline=False
            f.write("")
        w = open("data.singh", "a")
        if newline:
            w.write("\n")
        w.write(str(temp))
        w.write("%")
    root.update()
    grade = Tk()
    grade.title("Savir's School Average Tracker - New Grade")
    grade.config(bg="white")
    grade.minsize(500, 500)
    lbl1 = Label(grade, text="Percentage (don't add %):", bg="white", font="Sans 20")
    lbl1.pack()
    en = Entry(grade, bg="white", font="Sans 20 underline")
    en.pack()
    btn2 = Button(grade, text="Submit", border=0, bg="white", font="Sans 20 underline", command=push_Grade)
    btn2.pack()

from tkinter import *

average=0

root = Tk()
root.title("Savir's School Average Tracker")
root.config(bg="white")
root.minsize(500, 500)

lbl=Label(root, text="School Average Tracker", bg="white", font="Sans 50 bold underline")
lbl.pack()

lbl2=Label(root, text="Current Grades:", bg="white", font="Sans 20")
lbl2.pack()

w = open("data.singh", "r")
lbl3=Label(root, text=w.read(), bg="white", font="Sans 16")
lbl3.pack()

lbl2=Label(root, text="Current Average:", bg="white", font="Sans 20")
lbl2.pack()

r = open("data.singh", "r")
if r.readlines()==["NULL"]:
    avg=Label(root, text="NULL", bg="white", font="Sans 16")
    avg.pack()
else:
    r = list(open("data.singh", "r"))
    total = 0
    for i in range(len(r)):
        r[i] = r[i].replace("\n", "").replace("%", "")
        total+=int(r[i])
    string = str(total/len(r))+'%'
    avg=Label(root, text=string, bg="white", font="Sans 16")
    avg.pack()
    average=total/len(r)

btn=Button(root, text="Add New Grade", bg="white", font="Sans 20 underline", command=add_Grade, border=0)
btn.pack()

if average<50:
    info=Label(root, text="You'll likely fail this year. Sorry.", bg="white", fg="red", font="Sans 20")
    info.pack()    
elif average<60:
    info=Label(root, text="Step up your game or you'll end up with a 50%.", bg="white", fg="orange", font="Sans 20")
    info.pack()
elif average<75:
    info=Label(root, text="Try a little harder to be in the green zone.", bg="white", fg="sandy brown", font="Sans 20")
    info.pack()
elif average<95:
    info=Label(root, text="Keep it up!!", bg="white", fg="light green", font="Sans 20")
    info.pack()
else:
    info=Label(root, text="This is ingenious!", bg="white", fg="green", font="Sans 20")
    info.pack()

root.mainloop()
