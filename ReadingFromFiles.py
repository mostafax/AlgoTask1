def HatMenFileSmall():
 x = open("Small_Numbers.txt", 'r')
 Hamada = ""

 for Numer in x:
    Hamada+=Numer
 #print(Hamada)
 Sub = Hamada.split("\n")
 #print(Sub)

 for x in range(1,12,2):
    print(Sub[x-1])
    Main = Sub[x].split(" ")

 return Main




#print(QuickSort(Sub))

def HatMenFileBig():
    x = open("LargeNumbers.txt", 'r')
    Hamada = ""

    for Numer in x:
        Hamada += Numer
    # print(Hamada)
    Sub = Hamada.split("\n")
    # print(Sub)

    for x in range(1, 3, 2):
        print(str(Sub[x - 1]+"\n"))
        Main = Sub[x].split(" ")
        #print(Main)
    return Main


def HatMenFileVBig():
    x = open("VLargeNumbers.txt", 'r')
    Hamada = ""

    for Numer in x:
        Hamada += Numer
    # print(Hamada)
    Sub = Hamada.split("\n")
    # print(Sub)

    for x in range(1, 3, 2):
        print(str(Sub[x - 1]+"\n"))
        Main = Sub[x].split(" ")
        #print(Main)
    return Main

