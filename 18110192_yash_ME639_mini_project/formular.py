import math

"""
m1 = mass of rod 1
l1 = length of rod 1
q1 = angle of rod 1

m2 = mass of rod 2
l2 = lenth of rod 2
q2 = angle of rod 2
"""

def deg(theta):
    rad = (math.pi/180)*theta
    return rad

def cos(q):
    return math.cos(deg(q))

def sin(q):
    return math.sin(deg(q))

def tan(q):
    return math.tan(deg(q))

def pos_x(l1, l2, q1, q2):
    x = l1*cos(q1) + l2*cos(q2)
    return x

def pos_y(l1, l2, q1, q2):
    y = l1*sin(q1) + l2*sin(q2)
    return y

def pos_x1(l1, q1):
    x1 = l1*cos(q1)
    return x1

def pos_y1(l1, q1):
    y1 = l1*sin(q1)
    return y1

def ang_q1(x, y, l1, l2):
    theta = math.acos((x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2)) * 180/math.pi
    if (x>=0 and y>=0):
        q1 = (math.atan(abs(y)/abs(x)) - math.atan((l2*sin(theta))/(l1 + l2*cos(theta)))) * 180/math.pi
    elif (x<=0 and y>=0):
        q1 = (math.pi - math.atan(abs(y)/abs(x)) - math.atan((l2*sin(theta))/(l1 + l2*cos(theta)))) * 180/math.pi
    elif (x<=0 and y<=0):
        q1 = (math.pi + math.atan(abs(y)/abs(x)) - math.atan((l2*sin(theta))/(l1 + l2*cos(theta)))) * 180/math.pi
    else:
        q1 = (2*math.pi - math.atan(abs(y)/abs(x)) - math.atan((l2*sin(theta))/(l1 + l2*cos(theta)))) * 180/math.pi

    
    return q1

def ang_q2(x, y, l1, l2):
    theta = math.acos((x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2)) * 180/math.pi
    if (x>=0 and y>=0):
        q1 = (math.atan(abs(y)/abs(x)) - math.atan((l2*sin(theta))/(l1 + l2*cos(theta)))) * 180/math.pi
    elif (x<=0 and y>=0):
        q1 = (math.pi - math.atan(abs(y)/abs(x)) - math.atan((l2*sin(theta))/(l1 + l2*cos(theta)))) * 180/math.pi
    elif (x<=0 and y<=0):
        q1 = (math.pi + math.atan(abs(y)/abs(x)) - math.atan((l2*sin(theta))/(l1 + l2*cos(theta)))) * 180/math.pi
    else:
        q1 = (2*math.pi - math.atan(abs(y)/abs(x)) - math.atan((l2*sin(theta))/(l1 + l2*cos(theta)))) * 180/math.pi

    q2 = q1 + theta
    return q2

def Torque_1(Fx, Fy, l1, q1):
    T1 = Fy*l1*cos(q1) - Fx*l1*sin(q1)
    return T1

def Torque_2(Fx, Fy, l2, q2):
    T1 = Fy*l2*cos(q2) - Fx*l2*sin(q2)
    return T1

def Torque_s1(l1, l2, q1, q2, k):
    Ts1 = k*(l1*sin(q1) + l2*sin(q2))*l1*cos(q1) - k*(l1*cos(q1) + l2*cos(q2))*l1*sin(q1)
    return Ts1

def Torque_s2(l1, l2, q1, q2, k):
    Ts2 = k*(l1*sin(q1) + l2*sin(q2))*l2*cos(q2) - k*(l1*cos(q1) + l2*cos(q2))*l2*sin(q2)
    return Ts2


    

