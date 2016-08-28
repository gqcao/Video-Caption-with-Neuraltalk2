import math
from numpy import *

def eucl_dist(col1, col2):
    col1 = mat(col1); col2 = mat(col2)
    return linalg.norm(col1 - col2)

def cosine_dist_rev(col1, col2):
    col1 = mat(col1); col2 = mat(col2)
    return float(inner(col1, col2) / (linalg.norm(col1) * linalg.norm(col2)))

def cosine_dist(col1, col2):
    col1 = mat(col1); col2 = mat(col2)
    dist = 1 - inner(col1, col2) / (linalg.norm(col1) * linalg.norm(col2))
    return float(dist)
