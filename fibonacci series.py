nterms = int ( input ( "ENTER N: " ) )

n1 = 0
n2 = 1
count = 2
if nterms <= 0 :
	print "ERROR"
elif nterms == 1 :
	print n1
else :
	print n1
	print n2
	while count < nterms :
		nth = n1 + n2
		print nth
		n1 = n2
		n2 = nth
		count += 1
ax = raw_input("")
