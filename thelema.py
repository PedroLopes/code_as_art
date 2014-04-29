import shlex
import sys
import re

chapter1_data_split=[]

greetings=[]
greetings.append("hello")
greetings.append("hallo")
greetings.append("hy")
greetings.append("hi")
greetings.append("you")
greetings.append("are")
greeting = 0
goodbyes=[]
goodbyes.append("see")
goodbyes.append("ya")
goodbyes.append("you")
goodbyes.append("thanks")
goodbyes.append("later")
goodbyes.append("soon")
goodbyes.append("out")
goodbyes.append("away")
goodbyes.append("disconnect")
goodbyes.append("logout")
goodbyes.append("exit")
goodbyes.append("close")
goodbyes.append("die")
goodbye = 0
doasthouwilts=[] #what should I do? choose? which? 
doasthouwilts.append("?")
doasthouwilts.append("should")
doasthouwilts.append("what")
doasthouwilts.append("which")
doasthouwilts.append("do")
doasthouwilts.append("make")
doasthouwilts.append("ask")
doasthouwilts.append("I")
doasthouwilts.append("will")
doasthouwilts.append("want")
doasthouwilts.append("did")
doasthouwilts.append("that")
doasthouwilt=0
loveisthelaws=[] #love is the law, what is love?
loveisthelaws.append("love")
loveisthelaw=0

#take out irrelevant words first
#cound term frequency
#check most frequent
#check if it was also the last one, if yes, random but not much, if twice, yes more random

bookofthelaw="texts/bookofthelaw/bookofthelaw.text"
chapter1="texts/bookofthelaw/chapter1.text"
chapter2="texts/bookofthelaw/chapter2.text"
chapter3="texts/bookofthelaw/chapter3.text"

if len(sys.argv) != 2:
    print 'Please specify one filename on the command line.'
    sys.exit(1)

with open(bookofthelaw) as f:
    bookofthelaw_data = f.readlines()

print bookofthelaw_data

#for s in chapter1_data:
	#print s
	#t = re.findall("\d+.", s)
	#my_text = s.replace(t[1], 'a')
	#print my_text
 	#t2 = re.search("\d+.", s)
        #print t2.group(1)
	#chapter1_data_split.append(t)

#print chapter1_data_split
filename = sys.argv[1]
body = file(filename, 'rt').read()
print 'ORIGINAL:', repr(body)
print

print 'TOKENS:'
lexer = shlex.shlex(body)
for token in lexer:
    if token in greetings:
    	greeting+=1
    elif token in goodbyes:
    	goodbye+=1
    elif token in doasthouwilts:
    	doasthouwilt+=1
    elif token in loveisthelaws:
    	loveisthelaw+=1
    print repr(token)

#find max here and output it

if doasthouwilt > greeting and doasthouwilt > goodbye:
	print("do as thou wilt shall be the whole of the law")
elif greeting > goodbye:
	print("how are you?")
elif goodbye > greeting:
	print("see yah later!")
#else print("random")
