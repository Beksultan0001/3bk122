# Пайдаланушыдан үш қабырғаны енгізуді сұраймыз
a = int(input("Бірінші қабырғаны енгізіңіз: "))
b = int(input("Екінші қабырғаны енгізіңіз: "))
c = int(input("Үшінші қабырғаны енгізіңіз: "))

# Үшбұрыш болу шартын тексеру (екі қабырғаның қосындысы үшінші қабырғадан үлкен болуы керек)
if a + b > c and a + c > b and b + c > a:
    # Үшбұрыштың түрін анықтау
    if a == b == c:
        print("Теңқабырғалы үшбұрыш")
    elif a == b or a == c or b == c:
        print("Теңбүйірлі үшбұрыш")
    else:
        print("Әртүрлі қабырғалы үшбұрыш")
else:
    print("Бұл үш қабырғадан үшбұрыш құру мүмкін емес!")
