from collections import Counter
diagnoses = ["Diabetes", "Flu", "Covid", "Flu", "Covid", "Flu"]
disease_count = Counter(diagnoses)
most_common = disease_count.most_common(1)[0][0]
print("Most common disease:", most_common)
