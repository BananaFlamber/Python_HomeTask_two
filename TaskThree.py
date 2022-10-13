print("\033c")

str = input("Задайте первую строку: ")
str2 = input("Задайте вторую строку: ")

n = 0

for i in range(len(str) - len(str2) + 1):
    if str[i:i+len(str2)] == str2:
        n += 1
print(f"Вторая строка встречается в первой {n} раз")