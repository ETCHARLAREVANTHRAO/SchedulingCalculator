from tkinter import *
class Sjf:
    def __init__(self, n, burst_name, arrival_time):
        self.n = n
        self.arrival_time = arrival_time
        self.burst_time = burst_name

    def arrangeArrival(self, n, array):
        for i in range(0, n):
            for j in range(i, n - i - 1):
                if array[1][j] > array[1][j + 1]:
                    for k in range(0, n):
                        array[k][j], array[k][j + 1] = array[k][j + 1], array[k][j]

    def CompletionTime(self,n, array):
        value = 0
        array[3][0] = array[1][0] + array[2][0]
        array[5][0] = array[3][0] - array[1][0]
        array[4][0] = array[5][0] - array[2][0]
        for i in range(1, n):
            temp = array[3][i - 1]
            mini = array[2][i]
            for j in range(i, n):
                if temp >= array[1][j] and mini >= array[2][j]:
                    mini = array[2][j]
                    value = j
            array[3][value] = temp + array[2][value]
            array[5][value] = array[3][value] - array[1][value]
            array[4][value] = array[5][value] - array[2][value]
            for k in range(0, 6):
                array[k][value], array[k][i] = array[k][i], array[k][value]

    def ans(self, n, arri, burst):
        arr = [[int(i) for i in range(1, n + 1)], burst ,arri, [0] * n, [0] * n, [0] * n]
        self.arrangeArrival(n, arr)
        self.CompletionTime(n, arr)
        print("Process  Arrival  Burst  Completion  \tWaiting  \tTurnaround ")
        waitingtime = 0
        turaroundtime = 0
        for i in range(0, n):
            print(arr[0][i], "\t\t\t", arr[1][i], "\t\t", arr[2][i], "\t\t", arr[3][i], "\t\t", arr[4][i], "\t\t",
                  arr[5][i])
            waitingtime += arr[4][i]
            turaroundtime += arr[5][i]
        print("Average waiting time is ", (waitingtime / n))
        print("Average Turnaround Time is  ", (turaroundtime / n))

def ans():
    n = d.get()
    num1 = b.get()
    num2 = c.get()
    n = int(n)
    ans1 = [int(i) for i in num1.split()]
    ans2 = [int(j) for j in num2.split()]
    a = Sjf(n,ans1, ans2)
    a.ans(n, ans1, ans2)


if __name__ == '__main__':
    root = Tk()
    d = StringVar()
    b = StringVar()
    c = StringVar()
    Label(root, text="n (no of processess)").grid(row=0, column=0)
    text = Entry(root, textvariable=d, bd=5).grid(row=0, column=1)
    Label(root, text="Burst Time").grid(row=1, column=0)
    text1 = Entry(root, textvariable=b, bd=5).grid(row=1, column=1)
    Label(root, text="Arrival Time").grid(row=2, column=0)
    text2 = Entry(root, textvariable=c, bd=5).grid(row=2, column=1)
    Button(root, text="submit", bd=4, fg="Orange", command=ans).grid(row=3, column=0)
    Button(root, text="Show Answer", bd=4, fg="Green", command=root.quit).grid(row=3, column=1)
    root.mainloop()

