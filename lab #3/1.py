def approve_loan():
    age = int(input("Жасыңызды енгізіңіз: "))
    if age < 21:
        return "Несие мақұлданбады: Жасыңыз 21-ден жоғары болуы керек."

    annual_income = int(input("Жылдық табысыңызды енгізіңіз: "))
    credit_history = input("Несие тарихыңыз (таза/нашар): ").strip().lower()

    if annual_income < 2000000:
        return "Несие мақұлданбады: Жылдық табыс 2 000 000 теңгеден жоғары болуы керек."

    if credit_history != "таза":
        return "Несие мақұлданбады: Несие тарихыңыз таза болуы керек."

    return "Несие мақұлданды!"

# Тестирование
print(approve_loan())