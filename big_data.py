#a program to open a large file on my hard drive and extract data. 
#8.28.19

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os



#os.remove('new_file')
#this above line needed to ensure new_flie is empty to start. Error occurs if there is no new_file in storage.

file = input('file name = ')
#this is a big file, too large to open in my RAM
#so now a small chunk of the big file is put into a new working file

#start = int(input("Enter start position: "))
#end = int(input("Enter end position: "))

rare = 0  #AF<0.005
uncommon = 0   #AF 0.005-0.05
common = 0    #AF > 0.05
rare_ex = 0
uncommon_ex = 0
common_ex = 0

n = 0
end_file = False

with open(file,'r') as big:
	
	for j in range(0,50000000):
		l= big.readline()
		if l == '':
			n = 5000
			end_file = True
			
		with open('new_file','a') as new:
			new.write(l)
			n = n + 1
			if n > 5000:
				data_raw= pd.read_csv('new_file', sep='\t', header=None,comment='#',low_memory=False)
				row_num= data_raw.shape[0]
				freq = data_raw.iloc[ : ,7]
				position = data_raw.iloc[ : ,1]
				print('1st position = ',position[0])
				


				for i in range(0,row_num):
				#if data_raw.iloc[i,1] >= start and data_raw.iloc[i,1] <= end:  #column 1 contains the location on the chromosome
					#use the above line if a start and end positon is needed to look at a part of the file.
						
					#if data_raw.iloc[i,1] >= start and data_raw.iloc[i,1] <= end:		
						
						z = freq[i]
						l = z.replace('CDX','CDZ')
						
						#if j > 4007 and i > 307:
							#print(position[i])
			#Now to distinguish the exon part of the gene from the regulatory part and to put a 'EX' key into the dictionary called column7, 
			#each letter of the slice is examined to see if it is 'X', which would be part of 'EX_TARGET', making this an exon variant 
			#and if no 'X' is found in l then the last part of the column is changed from VT=SNP to EX=SNP, so the dictionary will have a key 'EX'
						is_exon = False
						for k in range(0,len(l)):
							if l[k] =='E' and l[k+1] == 'X':
								is_exon = True
	
						if is_exon != True:
							m = l.replace('VT','EX') 

						else:
							m=l      

						q = m.replace('I_A','I=A') #replacing element #9 'MULTI_ALLELIC' corruption. If the data has multi allelic SNP, then you must check to be sure a common variant has not been missed.

						p = q.replace('IMPRECISE','IMPR=CISE')
			#next the string 'l' cleaned up to remove a '_' and replace it with an '=' so all elements contain '=' separating key from value
						r= p.replace('X_T','X=T')  #this puts the EX_TARGET variants into the dictionary as EX : TARGET
					#print(r)




			#now the cleaned up string 'r' will be made into a dictionary of key:value pairs, called 'column7'
						column7={}
						#print('i = ', i)
						
						#these next line used to look for corrupt positions
						#if j > 1001 and i > 254:
							#print('position = ', position[i])
							#print(l)

			#there are 14 results in column index=7 of the 'data' DataFrame, the INFO column, so j is set to range (0,13)
			#need to make this string l into a dictionary or 14 key:value pairs.  but if NOT EX_T there are only 13 key:value pairs. 

						column7= dict(e.split('=') for e in r.split(';'))

					#print(column7['EUR_AF'])
			# the above dictionary 'column7' has only string values, so these must be converted to floats for calculations.
			#the particular datum I am interested in is the key 'AF' in the dictionary 'column7', the value is a string.
						AF_val=column7['AF']
						EXON = column7['EX']

					#print(AF_val)
					#print(type(AF_val))
					#need to eliminate commas from AF_val
						AF_val_no_comma = AF_val.replace(',0.','')
						AF_val_no_comma2 = AF_val_no_comma.replace(',0','')

			#now the string value is converted to a float, 'AF_num', which can be used in calculations.
						AF_num=float(AF_val_no_comma2)        
	
						if AF_num > 0.5:
							AF_num = 1 - AF_num 

			#now the EX_TARGET region variants are counted separately to the whole gene variant counts. Note that EX_TARGET regions contain more
			#than the exon sequences. they include splice regions and they include esv variants which are structural variants. These inclusions tend to
			#inflate the rare variants bin for the coding sequence variants.
	
						if AF_num < 0.005:
							rare = rare +1
							if EXON =='TARGET':
								rare_ex = rare_ex + 1
		   
						if AF_num >= 0.005 and AF_num < 0.05:
							uncommon = uncommon +1
							if EXON =='TARGET':
								uncommon_ex = uncommon_ex +1

						if AF_num >= 0.05 and AF_num < 0.5:
							common = common +1
							if EXON == 'TARGET':
								common_ex = common_ex + 1
							
						#print('i =',i)
						
				print('j = ',j)
							
				print('whole chromosome variants = ',rare, uncommon, common)
				print('EX_TARGET variants = ',rare_ex,uncommon_ex,common_ex)

				n = 0
				os.remove('new_file')
				if end_file == True:
				    print('end of file')
				    print('last position = ', position[row_num - 1])
				    print('')
				    print('')
				    j = 50000000
				    



