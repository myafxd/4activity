import random
numbers = [5, 10, 22, -27, 12]
minn = min(numbers)
maxn = max(numbers)
print("самое большое число: ", maxn,"\n","самое маленькое число: ", minn, end="\n")
n = 6         # int     интегрежер - целое число
b = 4.35      # float   дробное число
stroka = "wtf"# string  строка
boolean = True# bool    сохраняет тру или фалс
random_number = random.choice(numbers)
mf = input("введите техт: ")
if mf == "пашол нахуй" and maxn == 22:
    print("сам иди", maxn)
elif mf == "я добр":
    print("ок я тож")
else: 
    print(random_number)           