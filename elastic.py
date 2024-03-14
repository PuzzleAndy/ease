import math

def ease_in_elastic(x):
  c4 = 2 * math.pi / 3
  if x == 0:
    return 0
  elif x == 1:
    return 1
  else:
    return -math.pow(2, 10 * x - 10) * math.sin((x * 10 - 10.75) * c4)

def ease_out_elastic(x):
  c4 = (2 * math.pi) / 3
  if x == 0:
    return 0
  elif x == 1:
    return 1
  else:
    return math.pow(2, -10 * x) * math.sin((x * 10 - 0.75) * c4) + 1

def ease_in_out_elastic(x):
  c5 = 2 * math.pi / 4.5
  if x == 0:
    return 0
  elif x == 1:
    return 1
  elif x < 0.5:
    return -(math.pow(2, 20 * x - 10) * math.sin((20 * x - 11.125) * c5)) / 2
  else:
    return (math.pow(2, -20 * x + 10) * math.sin((20 * x - 11.125) * c5)) / 2 + 1