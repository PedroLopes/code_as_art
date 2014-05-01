import shlex
import sys
import re
from random import randint

bookofthelaw_crowley=[] 
bookofthelaw_parser=[]

#to do
#make case insensitive
#count the words that appear inside the sentence thelema*2, and the sentence parser itself * factor of size
#cound term frequency -- done
#check most frequent
#check if it was also the last one, if yes, random but not much, if twice, yes more random

bookofthelaw="texts/bookofthelaw/bookofthelaw.text"
#chapter1="texts/bookofthelaw/chapter1.text" #if you want the complete chapter, see here


with open(bookofthelaw) as f:
    bookofthelaw_data = f.readlines()

crowley=False
for prophetic_statement in bookofthelaw_data:
	if (prophetic_statement[0] != '-'):
		crowley = not crowley 
		if crowley:
			#print ("mr crowley said:")
			#print prophetic_statement
			bookofthelaw_crowley.append(prophetic_statement)
		else:
			prophetic_statement_parser=prophetic_statement.split(',')
			#print ("we parse it by:")
			#print prophetic_statement_parser
			bookofthelaw_parser.append(prophetic_statement_parser)

while True:
	yourwill = raw_input("What is your will?")


#this is if you want to read your will from a file			
#if len(sys.argv) != 2:
    #print 'Please specify one filename on the command line.'
#    sys.exit(1)
#filename = sys.argv[1]
#yourwill = file(filename, 'rt').read()
#print 'ORIGINAL:', repr(yourwill)
#print

	thelemic_power = [0] * len(bookofthelaw_parser)
	#print 'TOKENS:'
	dissecting_yourwill = shlex.shlex(yourwill)
	for will in dissecting_yourwill:
		#print repr(will)
		i=-1
		for prophetic_statement in bookofthelaw_parser:
			i+=1
			#print i
			#print "this is to match"
			#print prophetic_statement
			#token_essence  = re.search("\d+.", prophetic_statement) #we can't really do this because its a match 1:1 now
			for thelemic_will in prophetic_statement:
				#print "we are now looking at the small token"
				#print thelemic_token
				if (will == thelemic_will):
					#print ("match---------------------------------------------------------------------")
					thelemic_power[i]+=1
					
	#print thelemic_power	
	maximal_frequency = 0
	maximal_index = -1
	resonant_index=-1
	for resonant_frequency in thelemic_power:
		resonant_index+=1
		if (resonant_frequency > maximal_frequency):
			maximal_frequency = resonant_frequency
			maximal_index = resonant_index
	#print maximal_index
	if (maximal_index == -1 or maximal_index == 0):
		the_answer = randint(0,len(bookofthelaw_crowley)-2)
	else:	
		the_answer = maximal_index
	print bookofthelaw_crowley[the_answer]
	if (maximal_index == len(bookofthelaw_crowley)-1):
		sys.exit()
	#print bookofthelaw_crowley
