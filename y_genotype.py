#a copy of "genotype.py"  altered and used to count the genotype of variants on the chrY, and calculate and count the variants,
# grouping them in the 3 bins, Rare, Uncommon and Common. Chr Y genotypes differ from those of the other chromosomes,
#since they are haploid.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


os.remove('new_file')

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
				
					for j in range(9,1233):
						GT = data_raw.iloc[k,j]
						if GT == '1':
							AC = AC + 1
						
						else:
							AC = AC   #the multi-variant positions are ignored
							
        
                     
            
            
					AF = AC / 1233  #since the sample for the chr Y is 1233 men, contributing one chromosome each.
					
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
