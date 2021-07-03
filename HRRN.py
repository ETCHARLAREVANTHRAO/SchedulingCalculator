from tkinter import *
class HRRN:
    def __init__(self, n, arrival_time , burst_time):
        self.n = n
        self.arrival_time = arrival_time
        self.burst_time = burst_time

    def sortByArrival(self,at, n):
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if at[i] > at[j]:
                    at[i], at[j] = at[j], at[i]

    def answer(self,n,arrival_time, burst_time):
        sum_bt = 0
        avgwt = 0
        avgTT = 0
        completed = [0] * n
        waiting_time = [0] * n
        turnaround_time = [0] * n
        for i in range(0, n):
            sum_bt += burst_time[i]
        self.sortByArrival(arrival_time, n)
        print("Name", "Arrival time", "Burst time", "Waiting Time", "Turnaround ", "Normalized TT")
        t = arrival_time[0]
        while (t < sum_bt):
            hrr = -9999
            temp, loc = 0, 0
            for i in range(0, n):
                if arrival_time[i] <= t and completed[i] != 1:
                    temp = (burst_time[i] + (t - arrival_time[i])) / burst_time[i]
                    if hrr < temp:
                        hrr = temp
                        loc = i

            t += burst_time[loc]
            waiting_time[loc] = t - arrival_time[loc] - burst_time[loc]
            turnaround_time[loc] = t - arrival_time[loc]
            avgTT += turnaround_time[loc]

            normalised_TT = float(turnaround_time[loc] / burst_time[loc])
            completed[loc] = 1
            avgwt += waiting_time[loc]
            print(loc, "\t\t", arrival_time[loc], "\t\t", burst_time[loc], "\t\t", waiting_time[loc], "\t\t",
                  turnaround_time[loc], "\t\t", normalised_TT)

        print("Average waiting Time: ", avgwt / n)
        print("Average Turn Around Time:  ", avgTT / n)

def fun():
    n = d.get()
    num1 = b.get()
    num2 = c.get()
    n = int(n)
    ans1 = [int(i) for i in num1.split()]
    ans2 = [int(j) for j in num2.split()]
    a = HRRN(n, ans2, ans1)
    a.answer(n, ans2, ans1)
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
