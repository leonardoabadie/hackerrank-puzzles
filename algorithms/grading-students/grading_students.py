def multiples(initial):
  return [n for n in range(initial, 100+1) if n % 5 == 0]

def gradingStudents(grades) -> int:
  for i,grade in enumerate(grades):
    five_multiples = multiples(grade)
    if (grade >= 38) and (five_multiples[0] - grade < 3):
      grades[i] = five_multiples[0]

  return grades
