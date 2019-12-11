#a program to extract the segments of chrY from the file Jeanson sent containing the 10 MB regions
#the text file 'f.txt' contains the table of the chrY segments of interest

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#now get the file of segments that are to be analyzed, these could be exons or regions of interest in the DNA
#the file must be in tab separated columns
seg_file = input('segment file name = ')

segs_df =  pd.read_csv(seg_file, sep='\t',header = None, comment='#',low_memory=False)
print(segs_df) #this dataframe is the genome segments of interest

seg_num = len(segs_df)
print('number of segments =', seg_num)

seg_start = {}
seg_end = {}
				
for i in range(0,seg_num):
	seg_start[i] = segs_df.iloc[i,1]
	seg_end[i] = segs_df.iloc[i,2]
	
print('dictionary of start positions =', seg_start)
print()
print('dictionary of end positions =', seg_end)

#now the big data file needs to be opened and chunks read to a new file for analysis
rare = 0  #AF<0.005
uncommon = 0   #AF 0.005-0.05
common = 0    #AF > 0.05


#get the big data file to be analyzed, usually a whole chromosome file from IGSR
file = input('big data file to be analyzed =')


	

data_raw= pd.read_csv(file, sep='\t', header=None,comment='#',low_memory=False)
row_num= data_raw.shape[0]
freq = data_raw.iloc[ : ,7]
position = data_raw.iloc[ : ,1]
print('1st position = ',position[0])
print('number of rows in big file =', row_num)

print('rare =',rare)
print('uncommon =',uncommon)
print('common =', common)

for j in range(0,row_num):

	for k in range(0,seg_num):
		if position[j] >= seg_start[k] and position[j] <= seg_end[k]:
			l = freq[j]
			q = l.replace('I_A','I=A') #replacing element#9, MULTI_ALLELIC corruption
			r = q.replace('X_T','X=T')
			column7 = {}
			column7 = dict(e.split('=') for e in r.split(';'))
			AF_val = column7['AF']
			AF_val_no_comma = AF_val.replace(',0.','') #to overlook multi-allelic position's AF
			AF_num = float(AF_val_no_comma)
			if AF_num > 0.5:
				AF_num = 1 - AF_num
		
			if AF_num < 0.005:
				rare = rare + 1
			if AF_num > 0.005 and AF_num < 0.05:
				uncommon = uncommon + 1
			if AF_num > 0.05:
				common = common + 1
			
	
print('j = ',j)	
print('last position =', position[j])		
print('Total Rare =',rare, 'Total Uncommon =',uncommon,'Total Common =',common)
	
				
			
			
												
						       
        




    



            