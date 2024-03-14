import math

def ease_in_quint(x):
  return math.pow(x, 5)

def ease_out_quint(x):
  return 1 - math.pow(1 - x, 4)

def ease_in_out_quint(x):
  if x < 0.5:
    return 16 * math.pow(x, 5)
  else:
    return 1 - math.pow(-2 * x + 2, 5) / 2