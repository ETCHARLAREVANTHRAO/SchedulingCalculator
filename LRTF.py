from tkinter import *

class Lrtf:
    def __init__(self, p, n):
        self.p = p
        self.n = n

    def findlargest(self,p, n, at):
        max = 0
        for i in range(n):
            if (p[i][1] <= at):
                if (p[i][2] > p[max][2]):
                    max = i
        return max

    def findCT(self,n,p, totaltime, prefinaltotal):
        i = p[0][1]
        while (1):
            if (i <= 4):
                index = self.findlargest(p, n, i)
            else:
                index = self.findlargest(p, n, 4)
            p[index][2] -= 1
            totaltime += 1
            i += 1
            if (p[index][2] == 0):
                p[index][6] = totaltime
            if (totaltime == prefinaltotal):
                break

    def answer(self,p, n, at, bt, prefinaltotal, totaltime):
        for i in range(n):
            p[i][0] = i + 1

        for i in range(n):  # taking AT
            p[i][1] = at[i]

        for i in range(n):
            p[i][2] = bt[i]
            p[i][3] = p[i][2]
            prefinaltotal += p[i][2]

        p = sorted(p, key=lambda p: p[1])
        totaltime += p[0][1]
        prefinaltotal += p[0][1]
        self.findCT(n,p, totaltime, prefinaltotal)
        totalWT = 0
        totalTAT = 0
        for i in range(n):
            # since, TAT = CT - AT
            p[i][5] = p[i][6] - p[i][1]
            p[i][4] = p[i][5] - p[i][3]
            totalWT += p[i][4]
            totalTAT += p[i][5]

        # after all process executes
        print("PNo\tAT\tBT\tCT\t\tTAT\t\tWT")

        for i in range(n):
            print(p[i][0], "\t", p[i][1], "\t",
                  p[i][3], "\t", end=" ")
            print(p[i][6], "\t",
                  p[i][5], "\t", p[i][4])
        print()
        print("Average TAT = ", totalTAT / n)
        print("Average WT = ", totalWT / n)


def fun():
    t = d.get()
    num1 = b.get()
    num2 = c.get()
    p = []
    n = int(t)
    totaltime = 0
    prefinaltotal = 0
    for i in range(n):
        p.append([0, 0, 0, 0, 0, 0, 0])
    ans1 = [int(i) for i in num1.split()]
    ans2 = [int(j) for j in num2.split()]
    a = Lrtf(p, n)
    a.answer(p, n, ans2, ans1, totaltime, prefinaltotal)

    # initializing the process number
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