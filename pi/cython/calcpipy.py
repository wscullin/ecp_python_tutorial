import random

def calcpi_py(samples):
    """serially calculate Pi using only standard library functions"""
    inside = 0
    random.seed(0)
    for i in range(int(samples)):
        x = random.random()
        y = random.random()
        if (x*x)+(y*y) < 1:
            inside += 1
    return (4.0 * inside)/samples
