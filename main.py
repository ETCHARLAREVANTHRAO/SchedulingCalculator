from tkinter import *
from subprocess import *

def func():
    proc = Popen("FCFS.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)
def func1():
    proc = Popen("SJF.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)
def func2():
    proc = Popen("Priority_Scheduling.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)
def func3():
    proc = Popen("SRTF.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)
def func4():
    proc = Popen("LRTF.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)
def func5():
    proc = Popen("Round_Robin.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)

def func6():
    proc = Popen("HRRN.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)
def func7():
    proc = Popen("Premtive_priority.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)

if __name__ == '__main__':
    Master = Tk()
    frame = Frame(Master)
    frame.pack()
    Button(frame, text="FCFS",bd= 4,padx=20,activeforeground="blue", command=func).grid(row=0, column=0, padx= 20, pady=8)
    Button(frame, text="SJF",bd= 4,padx=20,activeforeground="blue",command= func1).grid(row=0, column= 1, padx = 20, pady=8)
    Button(frame, text="SRTF",bd= 4,padx=20,activeforeground="blue", command=func3).grid(row=0, column=2, padx=20, pady=8)
    Button(frame, text="LRTF",bd= 4,padx=20,activeforeground="blue", command=func4).grid(row=0, column=3, padx=20, pady=8)
    Button(frame, text="RR",bd= 4,padx=20,activeforeground="blue", command=func5).grid(row=1, column=0, padx=20, pady=8)
    Button(frame, text="Priority",bd= 4,padx=20,activeforeground="blue", command=func2).grid(row=1, column=1, padx=20, pady=8)
    Button(frame, text="Premtive Priority",bd= 4,padx=20,activeforeground="blue", command=func7).grid(row=1, column=2, padx=20, pady=8)
    Button(frame, text="HRRN",bd= 4,padx=20,activeforeground="blue", command=func6).grid(row=1, column=3, padx=20, pady=8)

    output = Text(Master, width=100, height=20)

    output.pack()
    Master.mainloop()