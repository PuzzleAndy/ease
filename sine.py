import math

def ease_in_sine(x):
  return 1 - math.cos((x * math.pi) / 2)

def ease_out_sine(x):
  return math.sin((x * math.pi) / 2)

def ease_in_out_sine(x):
  return -(math.cos(x * math.pi) - 1) / 2