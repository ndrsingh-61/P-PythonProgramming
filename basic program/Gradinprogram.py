student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

# Scores 91 - 100: Grade = "Outstanding"
#
# Scores 81 - 90: Grade = "Exceeds Expectations"
#
# Scores 71 - 80: Grade = "Acceptable"
#
# Scores 70 or lower: Grade = "Fail"

for key in student_scores:
    values = student_scores[key]
    if 91 <= values <= 100:
        student_scores[key] = "Outstanding"
    elif 81 <= values <= 90:
        student_scores[key] = "Exceeding Expectations"
    elif 71 <= values <= 80:
        student_scores[key] = "Acceptable"
    elif 70 >= values:
        student_scores[key] = "Fail"

print(student_scores)




