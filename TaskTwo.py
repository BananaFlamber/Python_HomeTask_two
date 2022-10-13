print("\033c")

try:
    num = int(input("Введите целое число: "))
    fucktorial = 1
    list = []
    for i in range(num):
        i = i + 1
        fucktorial = i * fucktorial
        list.append(fucktorial)
    print(list)
except:
    print("Неверные данные!")