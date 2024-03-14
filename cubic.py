import math

def ease_in_cubic(x):
  return math.pow(x, 3)

def ease_out_cubic(x):
  return 1 - math.pow(1 - x, 3)

def ease_in_out_cubic(x):
  if x < 0.5:
    return 4 * math.pow(x, 3)
  else:
    return 1 - math.pow(-2 * x + 2, 3) / 2