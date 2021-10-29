from tkinter import *
from tkinter import messagebox
s=[]
def newTask():
    task = my_entry.get()
    if task != "":
        task=" "+task+" "
        s.append(task)
        y=','.join(s)
        fi=open('file1.txt','w')
        fi.write(y)
        fi.close()
        lb.insert(END, task)
        si=lb.size()
        m=' '+'['+str(si)+'] '
        lb1.insert(END,m)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    a=lb.index(ANCHOR)
    j=lb.size()
    d=1
    while(lb1.size()>0):
        lb1.delete(0)
    while(d<=j):
        lb1.insert(END, '['+str(d)+']')
        d+=1
    fi=open('file1.txt','w')
    try:
        s.remove(s[a])
        y=','.join(s)
        fi.write(y)
    except:
        messagebox.showwarning("warning", "Please select some task.")
    fi.close()

def deleteAllTask():
    z=lb.size()
    while(lb1.size()>0):
        lb1.delete(0)
    if(z>0):
        while(z>0):
            lb.delete(0)
            z=z-1
        s.clear()
        fi=open('file1.txt','w')
        y=','.join(s)
        fi.write(y)
    else:
        messagebox.showwarning("warning", "There are no tasks")

    
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('TO DO LIST')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=5)

lb1 = Listbox(
    frame,
    width=3,
    height=8,
    font=('Times', 18),
    bd=0,
    bg='#FFE4E1',
    fg='#000000',
    highlightthickness=0,
    selectbackground='#000000',
    activestyle="underline",
    
)
lb1.pack(side=LEFT, fill=BOTH)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#000000',
    highlightthickness=1,
    selectbackground='#008B8B',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

fi = open('file1.txt','r')
lines = []
try:
    with fi as f:
        lines = f.readlines()
        s=lines[0].split(',')
        fi.close()
except:
    pass

if(s):
    for item in s:
        lb.insert(END, item)
        si=lb.size()
        m=' '+'['+str(si)+'] '
        lb1.insert(END,m)

sb = Scrollbar(frame)
sb.pack(side=LEFT, fill=BOTH)


lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delAllTask_btn = Button(
    button_frame,
    text='Delete-All Tasks',
    font=('times 14'),
    bg='#FFB6C1',
    padx=10,
    pady=5,
    command=deleteAllTask
)
delAllTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()


