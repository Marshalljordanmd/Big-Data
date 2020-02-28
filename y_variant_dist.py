#revision of the program "std_dev.py" to analyze the 10.4 MB mask on the Y chromosome
#to get mean variant distance and SD.  the 2 large (>1MB) gaps on the Y should not be found in this 10.4 MB mask



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


#these dictionaries of start and end positions for the Y chromosome 10.4 MB mask come from 'y_segs.py'
seg_start = {0: 2655000, 1: 2680000, 2: 6619000, 3: 6726000, 4: 7034000, 5: 7127000, 6: 7144000, 7: 7519000, 8: 8007999, 9: 8976000, 10: 9393000, 11: 9431000, 12: 9798000, 13: 13885000, 14: 13984000, 15: 14447000, 16: 14965000, 17: 15253000, 18: 15303000, 19: 15643000, 20: 15682000, 21: 16015000, 22: 16187000, 23: 18031000, 24: 18554000, 25: 19188000, 26: 19391000, 27: 19493000, 28: 21049000, 29: 21158000, 30: 21746000, 31: 21843000, 32: 21944000, 33: 22541000, 34: 22645000, 35: 23242000, 36: 23746000, 37: 23958000, 38: 24373000, 39: 24388000, 40: 28477000, 41: 28598000}

seg_end = {0: 2674000, 1: 2913000, 2: 6721999, 3: 7016000, 4: 7114000, 5: 7140000, 6: 7431000, 7: 8003000, 8: 8905000, 9: 9156000, 10: 9428000, 11: 9461000, 12: 9895000, 13: 13976000, 14: 14430000, 15: 14960000, 16: 15213000, 17: 15284000, 18: 15636000, 19: 15666000, 20: 16011000, 21: 16067000, 22: 17973000, 23: 18256000, 24: 19163999, 25: 19381999, 26: 19483000, 27: 19551000, 28: 21150000, 29: 21744999, 30: 21828000, 31: 21942000, 32: 22209999, 33: 22628000, 34: 23156000, 35: 23637000, 36: 23898000, 37: 23991999, 38: 24386000, 39: 24480999, 40: 28551000, 41: 28770999}

seg_num = 42

file = input('name of file = ') #this is the Y chromosome file


data_raw= pd.read_csv(file, sep='\t', header=None,comment='#',low_memory=False)
row_num= data_raw.shape[0]
freq = data_raw.iloc[ : ,7]
position = data_raw.iloc[ : ,1]
print('1st position = ',position[0])
print('number of rows in file =', row_num)

last_pos = 0
D = 0
s = 0
next = [] #a list of distances between variant positions
var = 0  #to keep track of the number of variant distances in the distance calculation
z = 0

for j in range(row_num):
	
	for k in range(0,seg_num):
		if position[j] >= seg_start[k] and position[j] <= seg_end[k]:
			
			if last_pos == 0:
				last_pos = position[j]
		
				current_seg = seg_end[k]
				
			elif position[j] <= current_seg:
				distance = position[j] - last_pos
				next.append(distance)
				last_pos = position[j]
				D = D + distance
				var += 1
				
			else:
				last_pos = position[j]
				current_seg = seg_end[k]
		
			
					
print('number of intervals = ',var)
print('D = ',D)					
#now to compute the mean and SD			
mean = D / var #each distance length added to the D has been counted as 'var'
sum = 0

for i in range(1,var):
	s =(abs(next[i] - mean))**2
	sum = sum + s

argument = ((1/(var-1))*sum)	
std_dev = (argument)**(.5)

print('N = ', var)
print('mean of distances = ',mean)
print('standard deviation = ', std_dev)

