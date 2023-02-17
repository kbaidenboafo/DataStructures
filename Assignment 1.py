L = 12
w = 10
x = [0, 6, 12]
M = w*(-6*x[0]**2+6*L*x[0]-L**2)/12
V = w*(0.5*L-x[0])

# Question 1
print('ai. Bending moment at ends = ' + str(M) + 'kNm')
print('ii. Shear force at the ends = ' + str(V) + 'kN')
print('')

from math import sqrt

sqrt(9)
# Question 2
x_one = L/2 + L/sqrt(12)
x_two = L/2 - L/sqrt(12)
print('b. Bending moment will be zero at x =:')
print(str(x_one) + 'm and ' + str(x_two) + 'm')
print('')

# Question 3
x = L/2
print('c. Shear force is zero at x = ' + str(x) + 'm')
print('')


import numpy as np
# Question 4
r = np.linspace(0,12,1200)
M_one = w*(-6*r**2+6*L*r-L**2)/12
print('d. Bending moment at each step:')
print(M_one)
print('')

# Question 5
V_one = w*(0.5*L-r)
print('e. Shear force at each step:')
print(V_one)
print('')

#Question 6
min_M = np.min(abs(M_one))
print('f. The minimum absolute bending moment = ' + str(min_M) + ' and occurs at:')
x_three = L/2 + L/sqrt(12)  + sqrt((min_M*L/w)/6) 
x_four =  L/2 - L/sqrt(12) - sqrt((min_M*L/w)/6)  
print(str(x_three) + 'm and ' + str(x_four))
print('')

#Question 7
relative_error1 = (x_three - x_one)/x_three * 100
relative_error2 = (x_two - x_four)/x_two*100
print('g. ' + str(relative_error1) + '%')
print(str(relative_error2) + '%')
print('')

#Question 8
max_M = max(M_one)
a = 1
b = -L
c = (L**2/6)+(2*max_M)/w
D = b**2 - 4*a*c
root_1 = (-b + np.sqrt(D))/2*a
root_2 = (-b - np.sqrt(D))/2*a
print('h. The points at which the maximum bending moment occur are')
print(root_1)
print(root_2)
print('')

min_M = min(M_one)
a = 1
b = -L
c = (L**2/6)+(2*min_M)/w
D = b**2 - 4*a*c
root_1 = (-b + np.sqrt(D))/2*a
root_2 = (-b - np.sqrt(D))/2*a
print('The points at which the minimum bending moment occur are')
print(root_1)
print(root_2)

#https://github.com/kbaidenboafo



