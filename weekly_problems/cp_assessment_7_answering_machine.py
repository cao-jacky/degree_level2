import cp_assessment_7
import matplotlib as pyplot

x0, y0 = 30, 20             # Initial position of bacteria
r0 = numpy.array((x0,y0))   # Vector form of initial position
k_list = [0, 0.01, 0.001, 0.0001, 0.00001]

for i in k_list:
    cp_assessment_7.bacteria(r0, i)
    
