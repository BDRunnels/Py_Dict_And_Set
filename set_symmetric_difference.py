morning = ["Java", "C", "Ruby", "Lisp", "C#"]
afternoon = ["Python", "C#", "Java", "C", "Ruby"]

# Symmetric difference (items NOT in both sets ie items ONLY in ONE SET)
# possible_courses = morning ^ afternoon  # NOT DEFINED FOR LIST (only set)
possible_courses = set(morning).symmetric_difference(afternoon)
print(possible_courses)

possible_courses = set(afternoon).symmetric_difference(morning)
print(possible_courses)
