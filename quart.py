import math

def ease_in_quart(x):
  return math.pow(x, 4)

def ease_out_quart(x):
  return 1 - math.pow(1 - x, 4)

def ease_in_out_quart(x):
  if x < 0.5
    return 8 * math.pow(x, 4)
  else:
    return 1 - math.pow(-2 * x + 2, 4) / 2