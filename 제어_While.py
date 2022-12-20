# 제어 While문

treeHit = 0

while treeHit < 10:

    treeHit += 1
    print("i have cut the tree %d times". %treeHit)
    if treeHit == 10:
        print("Tree is falling down.")


prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 1

while number != 4:
    print(prompt)
    number = int(input())

coffee = 10
money = 300

while money:

    print("i get the money so give you coffee")
    coffee = coffee -1
    print("The nuber of coffee left is %d." %coffee)
    if coffee == 0:
        print("Coffee is soldout so we are stop selling coffee")
        break

coffee = 10

while True:
    money = int(input("Plz insert coin"))
    if money == 300:
        print("Give your coffee.")
        coffee -=1
    elif money > 300:
        print("Here your %d Charge and your coffee." %(money-300))
        coffee -=1
    else:
        print("Here your money and Not give your coffee.")
        print("The nuber of coffee left is %d." % coffee)
    if coffee == 0:
        print("Coffee is soldout so we are stop selling coffee")
        break

a = 0 

while a < 10:

    a +=1 
    if a % 2 == 0:continue
    print(a)

# 무한루프시 컨트롤 씨를 활용해 exit
