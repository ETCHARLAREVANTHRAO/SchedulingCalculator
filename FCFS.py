from tkinter import *

class Fcfs:
    def __init__(self, n, burst_time, arrival_time):
        self.n = n
        self.arrival_time = arrival_time
        self.burst_time = burst_time
    def waiting_time(self,n,  bt, wt, at):
        service_time = [0] *n
        service_time[0] = 0
        wt[0] = 0
        for i in range(1, n):
            service_time[i] = service_time[i-1] + bt[i-1]
            wt[i] = service_time[i] - at[i]

            if wt[i] < 0:
                wt[i] = 0

    def turnaround_time(self, n, bt, wt, tat):
        for i in range(n):
            tat[i] = bt[i] + wt[i]

    def average_time(self, n, bt, at):
        wt = [0] * n
        tat = [0] * n
        self.waiting_time(n,bt,wt, at)
        self.turnaround_time(n, bt, wt, tat)
        print("Process Burst time Arrival time Watiting time"
              "turn-Arond time completion time")
        total_wt = 0
        total_tat = 0
        for i in range(n):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]
            compl_time = tat[i] + at[i]
            print(" ", i+1, "\t\t", bt[i],"\t\t",at[i],"\t\t", wt[i], "\t\t", tat[i], "\t\t", compl_time)
        print("Average watiting time =  ",round(total_wt/n, 5))
        print("Average Turnaround Time = ", total_tat/n)


def fun():
    n = d.get()
    num1 = b.get()
    num2 = c.get()
    n = int(n)
    ans1 = [int(i) for i in num1.split()]
    ans2 = [int(j) for j in num2.split()]
    a = Fcfs(n,ans1,ans2)
    a.average_time(n,ans1,ans2)
if __name__ == '__main__':
    root = Tk()
    d = StringVar()
    b = StringVar()
    c = StringVar()
    Label(root, text="n (no of processess)").grid(row = 0, column= 0)
    text = Entry(root, textvariable=d, bd= 5).grid(row = 0, column= 1)
    Label(root, text="Burst Time").grid(row= 1, column= 0)
    text1 = Entry(root, textvariable=b, bd= 5).grid(row= 1, column= 1)
    Label(root, text="Arrival Time").grid(row= 2, column= 0)
    text2 = Entry(root, textvariable=c, bd = 5).grid(row= 2, column= 1)
    Button(root, text= "submit",bd=4,fg="Orange", command= fun).grid(row= 3, column= 0)
    Button(root, text="Show Answer",bd= 4,fg="Green", command=root.quit).grid(row=3, column=1)
    root.mainloop()
