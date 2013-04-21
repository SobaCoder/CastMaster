#IMPORT ALL THE MODULES

from rottentomatoes import RT
import json
import re
import string
from collections import defaultdict


#GLOBAL DATA VARIABLES
Documents = defaultdict(list)




def main():

	
	file = open('MovieList.txt', 'r')			#FILE CONTAINS MOVIE NAMES
	Size = 1
	
	for name in file:			

		#print name
		r = RT('c6nttc6uvr4pr6ewr996p6yt').search(name)		#GET INFOR FOR EVERY MOVIE USING API KEY
		w = r[0]
		if 'critics_consensus' in w.keys():					#GET CRITICS REVIEW
			critics = w['critics_consensus']		
		if 'synopsis' in w.keys():							#GET SYNOPSIS
			synopsis = w.get['synopsis']
		word_list = critics + synopsis

		W_out = re.sub('[%s]' % re.escape('!@#$%^&*(){},.:;"~`+=|\?/<>-_'), ' ', word_list)	#REMOVE PUNCTUATION - CANNOT REMOVE THE 'U' 
		W_list = [w.lower() for w in W_out.split()]											#CASE FOLDING AND SPLIT ON WHITE SPACE - TRANSLATE NOT WORKING!!
		#print W_list
		Documents[Size] = W_list															#READ INTO CORPUS
		Size += 1
	
	
	print Documents[20]
	
if __name__ == "__main__":
   main()







