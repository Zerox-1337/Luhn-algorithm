import numpy as np
import scipy as sp
import time
import random




def lineToKeyArray(line):
	print([values for values in line]);
	return [values for values in line];

def luhn(key): 
	doubleOrNot = 0;
	sumOfKey = 0;
	factorX = 1;

	for numIndex in range(len(key) - 1, -1, -1):
		print(key[numIndex]);
		if (key[numIndex] == 'X'):
			if (doubleOrNot == 1):
				factorX = 2;
				
		
		else:
			
			if (doubleOrNot == 1): 
				dubvalue = 2*int(key[numIndex]);
				if (dubvalue > 9):
					sumOfKey += (dubvalue - 9);
				else:
					sumOfKey += dubvalue;
			else: 
				sumOfKey += int(key[numIndex]);
		doubleOrNot = 1- doubleOrNot;
	for xGuess in range(0, 10):
		print(sumOfKey);
		xValue = xGuess;
		if (factorX == 2):
			xValue *= 2;
			if (xValue > 9):
				xValue -= 9;
			
			
			
		if ((xValue + sumOfKey) % 10 == 0):
			return str(xGuess) # Returns it as a string. 
	return "?"

file_luhn = open("key", 'r');
correctValue = "";
for line in file_luhn:
	print(line.strip());
	key = lineToKeyArray(line.strip());
	correctValue += luhn(key);
print("final value: " + correctValue);	
#luhn("test")

