from tkinter import *

class Priority:
    def __init__(self, proc, n):
        self.proc = proc
        self.n = n

    def findWaitingTime(self,processes, n, wt):
        wt[0] = 0

        # calculating waiting time
        for i in range(1, n):
            wt[i] = processes[i - 1][1] + wt[i - 1]

    # Function to calculate turn around time
    def findTurnAroundTime(self,processes, n, wt, tat):
        # Calculating turnaround time by
        # adding bt[i] + wt[i]
        for i in range(n):
            tat[i] = processes[i][1] + wt[i]

    # Function to calculate average waiting
    # and turn-around times.
    def findavgTime(self, processes, n):
        wt = [0] * n
        tat = [0] * n

        # Function to find waiting time
        # of all processes
        self.findWaitingTime(processes, n, wt)

        # Function to find turn around time
        # for all processes
        self.findTurnAroundTime(processes, n, wt, tat)

        # Display processes along with all details
        print("\nProcesses Burst Time Waiting",
              "Time Turn-Around Time")
        total_wt = 0
        total_tat = 0
        for i in range(n):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]
            print(" ", processes[i][0], "\t\t",
                  processes[i][1], "\t\t",
                  wt[i], "\t\t", tat[i])

        print("\nAverage waiting time = %.5f " % (total_wt / n))
        print("Average turn around time = ", total_tat / n)

    def priorityScheduling(self,proc, n):
        # Sort processes by priority
        proc = sorted(proc, key=lambda proc: proc[2],
                      reverse=True)

        print("Order in which processes gets executed")
        for i in proc:
            print(i[0], end=" ")
        self.findavgTime(proc, n)

def fun():
    n = d.get()
    num1 = b.get()
    num2 = c.get()
    n = int(n)
    processes = [int(i) for i in range(1, n+1)]
    ans1 = [int(i) for i in num1.split()]
    ans2 = [int(j) for j in num2.split()]
    proc = []
    for i in range(0, n):
        proc.append([processes[i], ans1[i], ans2[i]])
    a = Priority(proc,n)
    a.priorityScheduling(proc, n)


# Driver code
if __name__ == "__main__":
    root = Tk()
    d = StringVar()
    b = StringVar()
    c = StringVar()
    Label(root, text="n (no of processess)").grid(row=0, column=0)
    text = Entry(root, textvariable=d, bd=5).grid(row=0, column=1)
    Label(root, text="Burst Time").grid(row=1, column=0)
    text1 = Entry(root, textvariable=b, bd=5).grid(row=1, column=1)
    Label(root, text="Priority").grid(row=2, column=0)
    text2 = Entry(root, textvariable=c, bd=5).grid(row=2, column=1)
    Button(root, text="submit", bd=4, fg="Orange", command=fun).grid(row=3, column=0)
    Button(root, text="Show Answer", bd=4, fg="Green", command=root.quit).grid(row=3, column=1)
    root.mainloop()

