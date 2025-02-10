def university_admission():
  ubt_score = int(input("ҰБТ балыңызды енгізіңіз: "))
  has_sports_achievements = input("Спорттық жетістіктеріңіз бар ма? (иә/жоқ): ").strip().lower() == "иә"
  has_disciplinary_action = input("Тәртіптік жазасы бар ма? (иә/жоқ): ").strip().lower() == "иә"

  if has_disciplinary_action:
      return "Қабылданбады: Тәртіптік жазасы бар."

  if ubt_score > 90 or (ubt_score >= 75 and has_sports_achievements):
      return "Құттықтаймыз! Сіз университетке қабылдандыңыз!"

  return "Қабылданбады: ҰБТ балы жеткіліксіз."

# Тестілеу
print(university_admission())
