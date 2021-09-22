import numpy as np
'''
A code for homogeneous transformation of RRP Scara type manipulator.
'''
def calculate_transformation(q1,q2,p3,l1=1,l2=1):
    # joint 2 and joint 3
    H23 = np.array([[1,0,0,l2],
                    [0,1,0,0 ],
                    [0,0,1,0],
                    [0,0,0,1]])
    # joint 1 and joint 2
    H12 = np.array([[np.cos(q2),-np.sin(q2),0,l1],
                    [np.sin(q2),np.cos(q2),0,0 ],
                    [0,0,1,0],
                    [0,0,0,1]])
    
    # Ground frame and joint 1
    H01 = np.array([[np.cos(q1),-np.sin(q1),0,0],
                    [np.sin(q1),np.cos(q1),0,0 ],
                    [0,0,1,0],
                    [0,0,0,1]])
    
    # [p0 = H01*H12*H13*[p3
    #  1]                1]
    temp = np.matmul(np.matmul(np.matmul(H01,H12),H23),p3)
    p0 = temp[:-1]
    return p0


'''
params -> q1 - joint angle 1 in radians
          q2 - joint angle 2 in radians
          p3 - basically [p3,1].T
          l1 - length of link 1 
          l2 - length of link 2
'''
q1 = 0.1
q2 = 0.2 
dpz = 0.5
p3 = [0,0,dpz,1]

p0 = calculate_transformation(q1,q2,np.transpose(p3))
print(p0)

