# Жүйеде сақталған логин мен пароль
correct_login = "admin"
correct_password = "12345"

# Пайдаланушыдан логин мен пароль енгізуді сұраймыз
user_login = input("Логинді енгізіңіз: ")
user_password = input("Құпиясөзді енгізіңіз: ")

# Тексеру
if user_login == correct_login and user_password == correct_password:
    print("Қош келдіңіз!")
else:
    print("Қате логин немесе пароль!")
