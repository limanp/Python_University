
# Task_03 -----------------------------------------

print("Введіть вартість покупки: ")
price = float(input())

# Перевіряємо яку потрібно знижку згідно вартості
if price >= 1000:
    discount = 5
elif price >= 500:
    discount = 3
else:
    discount = 0

# Обчислюємо якщо є знижка та виводимо дані
if discount == 0:
    print("Вартість покупки:")
else:
    print("Вартість покупки з урахуванням знижки", str(discount) + "%:")
print(price - (price / 100 * discount))