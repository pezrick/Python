def countexercise(sequence, item):
  sum = 0
  for n in sequence:
    if n == item:
      sum += 1
  return sum
