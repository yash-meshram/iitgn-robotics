import numpy as np
'''
Jacobian for scara
'''

def compute_jacob(l1,l2,q1,q2):
    J = np.array([[-l1*np.sin(q1) - l2*np.sin(q1+q2), -l2*np.sin(q1+q2), 0],
                  [l1*np.cos(q1) + l2*np.cos(q1+q2), l2*np.cos(q1+q2), 0],
                  [0                               ,0                  ,-1],
                  [0                               ,0                  , 0],
                  [0                               ,0                  , 0],
                  [1                               ,1                  , 0],                  
                 ])
    
    return J
l1 = 1
l2 = 1
q1 = 0
q2 = 0
jacobian = compute_jacob(l1,l2,q1,q2)
print(jacobian)