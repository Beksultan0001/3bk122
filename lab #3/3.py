def calculate_ticket_price(age, is_vip=False, is_student=False):
    full_price = 1000  # Билеттің толық бағасы
    discount = 0

    # VIP-клиенттерге тегін билет
    if is_vip:
        return 0

    # Балалар мен зейнеткерлер үшін 50% жеңілдік
    if age < 18 or age >= 65:
        discount = 0.5
    # Студенттер үшін 30% жеңілдік
    elif is_student:
        discount = 0.3
    # Қалғандар толық бағаны төлейді
    else:
        discount = 0

    # Жеңілдікпен баға есептеу
    final_price = full_price * (1 - discount)
    return final_price

# Клиенттің мәліметтерін енгізу
role = input("Сіз кімсіз? (балалар/зейнеткер/студент/қалған): ").lower()

age = int(input("Сіздің жасыңыз қанша? "))
is_vip = False
is_student = False

if role == "балалар" or role == "зейнеткер":
    is_vip = False
elif role == "студент":
    is_student = True
elif role == "қалған":
    is_vip = False
else:
    print("Қате мәлімет! Сіз дұрыс мәлімет бермедіңіз.")
    exit()

# Билеттің бағасын көрсету
price = calculate_ticket_price(age, is_vip, is_student)
if is_vip:
    print("Сіз VIP-клиентсіз, сізге билет тегін беріледі!")
else:
    print(f"Сіздің билетіңіз: {price} теңге")
