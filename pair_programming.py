import numpy as np

def polar_to_cartesian(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return (x, y)
#very concise, should have your own comments though
