import string
import random

p1 = list(string.ascii_lowercase)
p2 = list(string.ascii_uppercase)
p3 = list(string.digits)

U_input = input("How many characters do you want in your password? Min. 8 ")

while True:
        try:
                C_number = int(U_input)

                if C_number < 8:
                        print("Your password should at least be 8 characters ")
                        U_input = input("Please, enter new number")
                        
                else:
                    break
                
        except:
            print("Please, enter numbers only ")
            U_input = input(" How many characters do you want in your password? Min. 8 ")
                                    
random.shuffle(p1)
random.shuffle(p2)
random.shuffle(p3)

Part1 = round(C_number * (40/100))
Part2 = round(C_number * (10/100))

result = []

for x in range(Part1):

    result.append(p1[x])
    result.append(p2[x])

for x in range(Part2):
    result.append(p3[x])
    result.append(p3[x])

random.shuffle(result)

password = "".join(result)
print("Password: ", password)