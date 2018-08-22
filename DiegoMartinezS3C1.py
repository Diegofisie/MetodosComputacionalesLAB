#######################semana 3 clase 1 ##########################
import numpy as np
import numpy.random as random
def elintegrator10k2018HD(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    w = (x1+x2+x3+x4+x5+x6+x7+x8+x9+x10)**2
    return w
min_val = 0
max_val = 1
n_random = 10000000
random_x1 = random.rand(n_random) * (max_val - min_val) + min_val
random_x2 = random.rand(n_random) * (max_val - min_val) + min_val
random_x3 = random.rand(n_random) * (max_val - min_val) + min_val
random_x4 = random.rand(n_random) * (max_val - min_val) + min_val
random_x5 = random.rand(n_random) * (max_val - min_val) + min_val
random_x6 = random.rand(n_random) * (max_val - min_val) + min_val
random_x7 = random.rand(n_random) * (max_val - min_val) + min_val
random_x8 = random.rand(n_random) * (max_val - min_val) + min_val
random_x9 = random.rand(n_random) * (max_val - min_val) + min_val
random_x10 = random.rand(n_random) * (max_val - min_val) + min_val

random_v = random.rand(n_random)*100

delta = elintegrator10k2018HD(random_x1,random_x2, random_x3,
random_x4,random_x5,random_x6,random_x7,random_x8,random_x9,random_x10) - random_v

inside = np.where(delta>0.0)

interval_integral = (max_val - min_val) **10
integral  = interval_integral * (np.size(inside)/(1.0*np.size(random_v)))*100
print(integral)



