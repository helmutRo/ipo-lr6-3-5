import random
pol = 0 #счетчик положительных
otr = 0 #счетчик отрицательных
zero = 0 #счетчик нулевых
number = [random.randint(-50, 50) for i in range(25)] #создает список
print("список: ", number) #выводится список
for i in number: #счет пол отр и нул элементов
    if i > 0: #если больше нуля то к счетчику +1
        pol += 1
    elif i < 0:
        otr += 1
    else:
        zero += 1
print(f"положительные элементы:  {pol}, {float(pol)/25*100:.0f}%") #вывод колва пол знач
print(f"отрицательные элементы:  {otr}, {float(otr)/25*100:.0f}%") #вывод колва отр знач
print(f"нулевые  элементы:  {zero}, {float(zero)/25*100:.0f}%") #вывод колва 0 знач
print(f"мин значение:  {min(number)}", sep="\n") #вывод мин
print(f"макс значение:  {max(number)}", sep="\n") #вывод макс
