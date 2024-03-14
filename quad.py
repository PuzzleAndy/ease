import math

def ease_in_quad(x):
  return math.pow(x, 2)

def ease_out_quad(x):
  return 1 - math.pow(1 - x, 2)

def ease_in_out_quad(x):
  if x < 0.5:
    return 2 * math.pow(x, 2)
  else:
    return 1 - math.pow(-2 * x + 2, 2) / 2