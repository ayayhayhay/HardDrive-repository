# Random Password Generator
import random

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
    'R', 'S' 'T', 'V', 'U', 'W', 'X', 'Y', 'Z', '!', '£', '$', '%', '&', '*']

#randMultiplyer = random.randint(1, len(list1))

list2 = []
list3 = []
list4 = []
list5 = []
list6 = []

random.shuffle(list1)
#x = randMultiplyer

for x in list1:
#while x < len(list1):
    list2.append(x)
    if len(list2) >= 15:
        break


list3 = str(list2)
list4 = list3.replace(",", "")
list5 = list4.replace("'", "")
list6 = list5.replace(" ", "")
print(list6)