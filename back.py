import math

def ease_in_back(x):
  c1 = 1.70158
  c3 = c1 + 1
  return c3 * math.pow(x, 3) - c1 * math.pow(x, 2)

def ease_out_back(x):
  c1 = 1.70158
  c3 = c1 + 1
  return 1 - c3 * math.pow(x - 1, 3) + c1 * math.pow(x - 1, 2)

def ease_in_out_back(x):
  c1 = 1.70158
  c2 = c1 * 1.525
  if x < 0.5:
    return math.pow(2 * x, 2) * ((c2 + 1) * 2 * x - c2) / 2
  else:
    return (math.pow(2 * x - 2, 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2