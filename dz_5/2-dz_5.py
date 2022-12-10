def Arhiv() :
    with open("text.txt","r") as file:
        st = file.readline()
    count = 1
    rez=''
    for i in range(len(st)-1):
        if st[i]==st[i+1]:
            count+=1
            #print(count, end=", ")
        else: 
            rez=rez+str(count)+st[i]
            #print (rez)
            count=1
    rez=rez+str(count)+st[-1] 
    with open("rez_arhiv.txt","w") as file1:
        file1.write(rez)
    

def Razarhiv ():
    with open("rez_arhiv.txt","r") as file:
        st = file.readline()
    rez=''
    count = '' 
    for i in st:
        if i.isdigit():
            #print("i= ",i)
            count +=i            
        else:
            #print(count)
            rez = rez + i*int(count)
            count=''
    with open("rez_razarhiv.txt","w") as file1:
        file1.write(rez)



with open("text.txt","r") as file:
    st1 = file.readline()

n = int(input('Что будем делать. \n 1 - Архивировать: \n 2 - Разархивировать:\n -> '))
if n == 1:
    Arhiv()
elif n==2: 
    Razarhiv()
else:
    print('Эта функция не реализована')