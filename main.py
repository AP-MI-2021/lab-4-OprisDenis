def acelasi_numar(list1,list2):
    k = 0
    z = 0
    for i in range(len(list1)):
        if int(list1[i]) % 2 == 0:
            k = k + 1
    for j in range(len(list2)):
        if int(list2[j]) % 2 == 0:
            z = z + 1
    if z == k :
        return True
    else:
        return False


def intersectie(list1,list2):
    list3=[]
    for i in range(len(list1)):
        j = 1
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                list3.append(list2[j])
    print(list3)


def palindrom(num):
    conv_num = str(num)
    return conv_num == conv_num[::-1]


def concatenare(list1,list2):
    if len(list1) > len(list2):
        maxi = len(list1)
    else:
        maxi = len(list2)

    for i in range(maxi):
        if palindrom(str(list1[i])+str(list2[i])):
            print(list1[i]+list2[i])

def oglindit(num):
    while num:
        d = d*10 + num%10
    return d

def oglindire(list1,list2):
    l3 = []
    for i in range(len(list1)):
        k = 0
        for j in range(len(list2)):
            if int(list1[i]) % int(list2[j]) != 0:
                k = k +1
                if k == 0:
                    l3.append[oglindit(int(list1[i]))]

    print(l3)

def main():
    print("Selectati un numar :")
    print("1. Pentru a citi doua liste de numere intregi")
    print("2. Pentru a verifica daca cele doua liste au acelasi numar de elemente pare")
    print("3. Pentru a vedea intersectia celor 2 liste")
    print("4. Pentru a vedea daca prin concatenarea a doua elemente de pe aceeasi pozitie din cele doua liste este un palindrom")
    print("5. Pentru a introduce o noua lista care va oglindi numerele din listele initiale daca acestea sunt divizibile cu toate numerele din lista noua")
    print("0. Pentru a iesi din aplicatie")
    choice = 1
    while choice:
        choice = int(input())
        if choice ==  1:
           list1 = input("Introduceti numerele in prima lista separate printr-o virgula ")
           l1 = list1.split(',')
           list2 = input("Introduceti numerele in a doua lista separate printr-o virgula")
           l2 = list2.split(',')
        elif choice == 2:
            print(acelasi_numar(l1,l2))
        elif choice == 3:
            intersectie(l1,l2)
        elif choice == 4:
            print(concatenare(l1,l2))
        elif choice == 5:
            list3= input("introduceti al treilea sir")
            l3=list3.split(',')
            oglindire(l1,l3)
            oglindire(l2,l3)

if __name__ == '__main__':
    main()
