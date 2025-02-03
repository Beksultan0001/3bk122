# Пайдаланушыдан температураны енгізуді сұраймыз
celsius = float(input("Температураны Цельсий бойынша енгізіңіз: "))

# Цельсийді Фаренгейтке түрлендіру формуласы
fahrenheit = (celsius * 9/5) + 32

# Нәтижені шығару
print(f"{celsius}°C = {fahrenheit:.2f}°F")

# Су күйін анықтау
if celsius < 0:
    print("Су мұз күйінде.")
elif celsius > 100:
    print("Су қайнап жатыр.")
