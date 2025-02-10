from sympy import symbols, Eq, solve

# Объявляем переменные
D, A = symbols('D A')

# Уравнения
eq1 = Eq(D + A, 42)  # Данияр и Әлібек вместе 42 года
eq2 = Eq(D + 3, 1.5 * (A + 3))  # Через 3 года Данияр будет в 1.5 раза старше Әлібека

# Решаем систему уравнений
solution = solve((eq1, eq2), (D, A))

# Получаем целочисленные значения
Daniyar_age = int(solution[D])
Alibek_age = int(solution[A])

# Вывод результата
print(f"Даниярдың жасы: {Daniyar_age}")
print(f"Әлібектің жасы: {Alibek_age}")
