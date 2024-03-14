import math

def ease_in_circ(x):
  return 1 - math.sqrt(1 - math.pow(x, 2))

def ease_out_circ(x):
  return sqrt(1 - math.pow(x - 1, 2))

def ease_in_out_circ(x):
  if x < 0.5:
    return (1 - math.sqrt(1 - math.pow(2 * x, 2))) / 2
  else
    return (math.sqrt(1 - math.pow(-2 * x + 2, 2)) + 1) / 2