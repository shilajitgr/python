# Problem statement in one note (HackerRank)
from multiprocessing import Process
from multiprocessing import Manager


def happinessCount(a, arr, val):
    happiness = 0
    for i in arr:
        if i in a:
            happiness += 1
    val["0"] = happiness


def UnhappinessCount(b, arr, val):
    happiness = 0
    for i in arr:
        if i in b:
            happiness -= 1
    val["1"] = happiness


lengths = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
a = set(map(int, input().split(" ")))
b = set(map(int, input().split(" ")))
manager = Manager()
return_val = manager.dict()
# For each  integer i in the array, if i belongs to A , you add 1 to your happiness. If i belongs to B, you subtract 1 from your happiness

p1 = Process(target=happinessCount, args=(a, arr, return_val))
p1.start()
p2 = Process(target=UnhappinessCount, args=(b, arr, return_val))
p2.start()
p1.join()
p2.join()
print(return_val["0"] + return_val["1"])
