#this is derived from a copy of "male_var.py" with the gender selection removed so that the total variant counts can be obtained from 
#counting all the genotypes for the 2504 samples, for comparison with the program "big_data.py" which counts AFs from the INFO line.


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os



rare = 0  #AF<0.005
uncommon = 0   #AF 0.005-0.05
common = 0    #AF > 0.05
n = 0
MV = 0
end_file = False

file = input('file name =')	
	
with open(file,'r') as big:
							
	for h in range(0,5000000):
		l= big.readline()
		if l == '':
			n = 5000
			
			end_file = True
		
		with open('new_file','a') as new:
			new.write(l)
			n = n + 1
			if n > 5000:
				data_raw= pd.read_csv('new_file', sep='\t',header = None, comment='#',low_memory=False)
				row_num= data_raw.shape[0]
				print('h = ',h)
			
			
				for k in range(0,row_num):  #k will iterate each of the rows, which are the variants
					AC = 0  #set the allele count to zero for each variant row
				
					for j in range(9,2513):
						GT = data_raw.iloc[k,j]
						if GT == '0|1' or GT == '1|0':
							AC = AC + 1
						elif GT == '1|1':
							AC = AC + 2
						else:
							AC = AC   #the multi-variant positions are ignored
							
        
                     
            
            
					AF = AC / 5008  #using AN = 5008 for the whole sample of 2504 people
					
					if AF > 0.5:
						AF = 1 - AF
						
					if AF>0.0 and AF<0.005:
						rare = rare + 1
					
					if AF>0.005 and AF<0.05:
						uncommon = uncommon + 1
					
					if AF>0.05:
						common = common + 1
						
					
				print('Rare =', rare, 'uncomm =',uncommon,'common = ',common)
				#print('multi-variants =',MV)
						
				os.remove('new_file')
				n = 0
