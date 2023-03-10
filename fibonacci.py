# SEARCHING FIBBONACI

def fib(n):
    if n < 1 :
        return 0
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

def Fibonaccisearch(arr,x):
    for c in range(len(arr)):
            if type(arr[c])==list:
                a = Fibonaccisearch(arr[c],x)
                if a == -1:
                    print('Menemukan data')
                else:
                    print(f'{x} ada pada indeks {c} kolom {a}')
                    exit()
    n = 0
    while fib(n) < len(arr):
        n = n + 1
    offset = -1
    while (fib(n) > 1):
        i = min(offset + fib(n-2), len(arr) - 1)
        # print("Current Element : ",arr[i])
        if (x > arr[i]):
            n = n -1
            offset = i
        elif (x < arr[i]):
            n = n - 2
        else :
            return i
    if(fib(n-1) and arr[offset + 1] == x):
        return offset + 1
    return -1
arr = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]
print(arr)
x = input('Masukan nama yang ingin dicari: ')
b = Fibonaccisearch(arr,x)
if b == -1:
    print('tidak ditemukan')
else:
    print(f'{x} ada pada indeks {b}') 
