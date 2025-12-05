import random

def son_topish():
    print("1 dan 100 gacha son o‘yladim. Topa olasizmi?")

    tasodifiy_son = random.randint(1, 100)
    
    while True:
        taxmin = int(input("Son kiriting: "))

        if taxmin < tasodifiy_son:
            print("Kichik! Yana urinib ko‘ring.")
        elif taxmin > tasodifiy_son:
            print("Katta! Yana urinib ko‘ring.")
        else:
            print("Tabriklayman! To‘g‘ri topdingiz! 🎉")
            break

son_topish()
