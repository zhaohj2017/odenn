from scipy.integrate import solve_ivp
import numpy as np
import superpara

#solve ode using RK45 for sampling points
#this file is currently not used

def myode(t, y):
    return np.exp(y)

def tsample():
    # sol = solve_ivp(myode, [0, 0.3], [superpara.RANGE_Y[0]])
    # res.extend(sol.t) #extend

    # sol = solve_ivp(myode, [0, 0.3], [(superpara.RANGE_Y[0] + superpara.RANGE_Y[1]) / 2])
    # res.extend(sol.t) #extend

    sol = solve_ivp(myode, [0, 0.36], [superpara.RANGE_Y[1]])
    
    return sol.t, sol.y

print tsample()


"""
scipy.integrate.solve_ivp(fun, t_span, y0, method='RK45', t_eval=None, dense_output=False, events=None, vectorized=False, **options)
"""

"""
sample_y = np.arange(superpara.RANGE_Y[0] - superpara.EPS_Y, superpara.RANGE_Y[1] + superpara.EPS_Y + superpara.MESH_SIZE_Y, superpara.MESH_SIZE_Y)
"""