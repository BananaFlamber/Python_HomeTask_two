print("\033c")

numb = input("Введите вещественное или целое число: ")

def sum(numb):
    if float(numb) < 0:
        numb = float(numb) * -1
        
    numbers = 0
    
    for i in str(numb):
        if i != ".":
            numbers += int(i)
    return numbers

print(f"Сумма цифр в указаном числе составляет:{sum(numb)}") 