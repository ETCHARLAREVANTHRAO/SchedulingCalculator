from tkinter import *

class RoundRobin:
    def __init__(self, n,tq, arrival_time, burst_time):
        self.n = n
        self.tq = tq
        self.arrival_time = arrival_time
        self.burst_time = burst_time

    def queueUpdation(self,queue, timer, arrival, n, maxProcessIndex):
        zeroIndex = 0
        for i in range(0, n):
            if queue[i] == 0:
                zeroIndex = i
                break
        queue[zeroIndex] = maxProcessIndex + 1

    def queueMaintainence(self,queue, n):
        for i in range(0, n):
            if i < n - 1 and queue[i + 1] != 0:
                queue[i], queue[i + 1] = queue[i + 1], queue[i]

    def checkNewArrival(self,timer, arrival, n, maxProcessIndex, queue):
        if timer <= arrival[n - 1]:
            newArrival = False
            for j in range((maxProcessIndex + 1), n):
                if arrival[j] <= timer:
                    if maxProcessIndex < j:
                        maxProcessIndex = j
                        newArrival = True

            if (newArrival):
                self.queueUpdation(queue, timer, arrival, n, maxProcessIndex)

    def answer(self,n, tq, arrival, burst):
        timer = 0
        avgWait = 0
        avgTT = 0
        maxProcessIndex = 0
        turn = [0] * n
        wait = [0] * n
        temp_burst = [int(i) for i in burst]
        complete = [False] * n
        queue = [0] * n
        while (timer < arrival[0]):
            timer += 1
        queue[0] = 1

        while (True):
            flag = True
            for i in range(0, n):
                if temp_burst[i] != 0:
                    flag = False
                    break
            if flag:
                break
            for i in range(0, n):
                if i < n and queue[i] != 0:
                    ctr = 0
                    while ((ctr < tq) and (temp_burst[queue[0] - 1] > 0)):
                        temp_burst[queue[0] - 1] -= 1
                        timer += 1
                        ctr += 1
                        self.checkNewArrival(timer, arrival, n, maxProcessIndex, queue)
                    if temp_burst[queue[0] - 1] == 0 and complete[queue[0] - 1] == False:
                        turn[queue[0] - 1] = timer
                        complete[queue[0] - 1] = True

                idle = True
                if queue[n - 1] == 0:
                    for i in range(0, n):
                        if i < n and queue[i] != 0:
                            if complete[queue[i] - 1] == False:
                                idle = False
                else:
                    idle = False
                if idle:
                    timer += 1
                    self.checkNewArrival(timer, arrival, n, maxProcessIndex, queue)

                self.queueMaintainence(queue, n)
        for i in range(0, n):
            turn[i] = turn[i] - arrival[i]
            wait[i] = turn[i] - burst[i]
        print("\nProgram No.\tArrival Time\tBurst Time\tWait Time\tTurnAround Time")
        for i in range(0, n):
            print(i + 1, "\t\t", arrival[i], "\t\t", burst[i], "\t\t", wait[i], "\t\t", turn[i])
        for i in range(0, n):
            avgWait += wait[i]
            avgTT += turn[i]
        print("Average wai time: ", avgWait / n)
        print("Average Turn Around Time", avgTT / n)


def fun():
    n = d.get()
    tq = e.get()
    num1 = b.get()
    num2 = c.get()
    n = int(n)
    tq = int(tq)
    ans1 = [int(i) for i in num1.split()]
    ans2 = [int(j) for j in num2.split()]
    a = RoundRobin(n,tq,ans2,ans1)
    a.answer(n,tq,ans2,ans1)
if __name__ == '__main__':
    root = Tk()
    e = StringVar()
    d = StringVar()
    b = StringVar()
    c = StringVar()
    Label(root, text="n (no of processess)").grid(row = 0, column= 0)
    text = Entry(root, textvariable=d, bd= 5).grid(row = 0, column= 1)
    Label(root, text="tq (time quanta)").grid(row=1, column=0)
    text3 = Entry(root, textvariable=e, bd=5).grid(row=1, column=1)
    Label(root, text="Burst Time").grid(row= 2, column= 0)
    text1 = Entry(root, textvariable=b, bd= 5).grid(row= 2, column= 1)
    Label(root, text="Arrival Time").grid(row= 3, column= 0)
    text2 = Entry(root, textvariable=c, bd = 5).grid(row= 3, column= 1)
    Button(root, text= "submit",bd=4,fg="Orange", command= fun).grid(row= 4, column= 0)
    Button(root, text="Show Answer",bd= 4,fg="Green", command=root.quit).grid(row=4, column=1)
    root.mainloop()
