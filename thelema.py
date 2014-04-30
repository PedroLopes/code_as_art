import shlex
import sys
import re

chapter1_data_split=[]

bookofthelaw_crowley=[] 
bookofthelaw_parser=[]

#to do
#take out irrelevant words first
#cound term frequency
#check most frequent
#check if it was also the last one, if yes, random but not much, if twice, yes more random

bookofthelaw="texts/tests/bookofthelaw_small.text"
#chapter1="texts/bookofthelaw/chapter1.text" #if you want the complete chapter, see here
#chapter2="texts/bookofthelaw/chapter2.text" #if you want the complete chapter, see here
#chapter3="texts/bookofthelaw/chapter3.text" #if you want the complete chapter, see here

if len(sys.argv) != 2:
    print 'Please specify one filename on the command line.'
    sys.exit(1)

with open(bookofthelaw) as f:
    bookofthelaw_data = f.readlines()

#print bookofthelaw_data[1]

crowley=False
for prophetic_statement in bookofthelaw_data:
	#prophetic_statement_no_blank_lines = re.findall("-.", prophetic_statement)
	if (prophetic_statement[0] != '-'):
		crowley = not crowley #make the code more literary
		if crowley:
			print ("mr crowley said:")
			print prophetic_statement
			bookofthelaw_crowley.append(prophetic_statement)
		else:
			prophetic_statement_parser=prophetic_statement.split(',')
			print ("we parse it by:")
			print prophetic_statement_parser
			bookofthelaw_parser.append(prophetic_statement_parser)
			
filename = sys.argv[1]
body = file(filename, 'rt').read()
print 'ORIGINAL:', repr(body)
print

thelemic_power = [0] * len(bookofthelaw_parser)
print 'TOKENS:'
lexer = shlex.shlex(body)
i=-1
for token in lexer:
	print repr(token)
	i+=1
	print i
	for prophetic_statement in bookofthelaw_parser:
		print "this is to match"
		print prophetic_statement
		#token_essence  = re.search("\d+.", prophetic_statement) #we can't really do this because its a match 1:1 now
		for thelemic_token in prophetic_statement:
			print "we are now looking at the small token"
			print thelemic_token
			if (token == thelemic_token):
				print ("match---------------------------------------------------------------------")
				thelemic_power[i]+=1
					
print thelemic_power			
