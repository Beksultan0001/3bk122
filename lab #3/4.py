# Жанаттың жасы, Данияр мен Әселдің жасын есептеу
def find_age():
    for J in range(1, 79):  # Жанаттың жасы 1-ден 78-ге дейін болуы мүмкін
        D = J + 6  # Данияр Жанаттан 6 жас үлкен
        A = 3 * J + 10  # Әселдің жасы 5 жылдан кейін Жанаттың жасынан 3 есе көп
        if A + D + J == 78:  # Жастарының қосындысы 78-ге тең
            return J

# Жанаттың жасы
J = find_age()
print(f"Жанаттың жасы: {J}")