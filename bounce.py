import math

def ease_out_bounce(x):
  n1 = 7.5625
  d1 = 2.75
  if x < 1 / d1:
    return n1 * x * x;
  elif x < 2 / d1:
    return n1 * pow(x - 1.5 / d1, 2) + .75
  elif x < 2.5 / d1:
    return n1 * pow(x - 2.25 / d1, 2) + .9375
  else:
    return n1 * pow(x - 2.625 / d1, 2) + .984375

def ease_in_bounce(x):
  return 1 - ease_out_bounce(1 - x)

def ease_in_out_bounce(x):
  if x < 0.5:
    return (1 - ease_out_bounce(1 - 2 * x)) / 2
  else:
    return (1 + ease_out_bounce(2 * x - 1)) / 2