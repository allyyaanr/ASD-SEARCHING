# SEARCHING JUMPSEARCH

def jumpSearch( list_data , x , n ):
    langkah = n**0.5
    prev = 0
    for b in range(len(list_data)):
        if type(list_data[b]) == list:  
            output1 = jumpSearch(list_data[int(b)],x,len(list_data[int(b)]))
            if output1 == -1:
                list_data[int(b)] = 'Menemukan Data'
            else:
                print(x,"ada di indeks",int(b),"kolom ",output1)
                exit()
    while list_data[int(min(langkah, n)-1)] < x:
                prev = langkah
                langkah += n**0.5
                if prev >= n:
                    return -1
    while list_data[int(prev)] < x:        
                prev += 1
                if prev == min(langkah, n):
                    return -1
    if list_data[int(prev)] == x:
            return int(prev)
    return -1

list_data = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]
n = len(list_data)
print(list_data)
x = input('Masukan nama yang dicari: : ')
output = jumpSearch(list_data,x,n)
if output == -1:
    print(x,'Nama tidak ditemukan')
else:
    print(f'{x} Nama ada pada indeks {output}')
