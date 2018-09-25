# Thanasis Zoumpekas (thanasis.z@hotmail.com)
# Codename : thzou

import numpy as np
import pandas as pd
import sys


def main():
	filename = sys.argv[1]

	if ((filename.endswith('.xlsx')) or (filename.endswith('.xls'))):
		df = pd.read_excel(filename,header=None)

	elif filename.endswith('.csv'):
		df = pd.read_csv(filename,header=None)
	else :
		print ("Please give a suitable file extension :\t xlsx,xls,csv")
		sys.exit(1)


	#print(df.head())

	array = np.array(df)
	print ("Please select which columns to subtract!")
	col1 = input("Column 1:\t")
	col2 = input("Column 2:\t")
	print ("Subtraction : \t Column",col1,"-","Column",col2)
	vec = np.float128(array[:,int(col1)],base=16) - np.float128(array[:,int(col2)],base=16) #convert hex to float 128

	df['Converted'] = vec #make new column in the dataframe

	#print(df.head())

	np.set_printoptions(precision=32,threshold=np.nan) #set numpy print options 

	option = input("Press 1 if you want to save the convertion to a csv file or 0 to print the result:\t")
	print ("Your option : \t", option)

	if int(option)==1:
		option2 = input('Please choose a name for the new file: \t')
		print ("File created : ", option2 + ".csv")
		df.to_csv(option2 + ".csv", encoding='utf-8')
	elif int(option)==0:
		print (vec)


if __name__ == "__main__":
    main()