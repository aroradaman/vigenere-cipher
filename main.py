print "Please enter a key\n"
key = raw_input().upper()
print "Please eter plain text\n"
inpt = raw_input().upper()

def move (char,pos) :	
	n = ord(char) + pos 
	if n >= 90 :
		n -= 90
		n += 64
	return chr(n)

def encrypt(string,key) :
	key = key.upper()	
	eString = ''	
	count = 0
	for char in string :		
		if count >= len(key) :
			count = 0	
		pos = ord(key[count]) - 65	
		eString += move(char,pos)
		count += 1
	return eString					
	

print '\n',inpt.upper()' ,'\t' ,encrypt(inpt,key)
	
