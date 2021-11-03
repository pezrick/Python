import math
import random

def random_pi():
    return math.ceil(random.randint(1, 10) * math.pi)

for _ in range(5):
    print(random_pi())