import math
import fractions as fr
# YO, search Pell's equation

def recurrentFraction(a):
	A = a**2
	# A is nearest square below n (this can be allocated smarter beforehand)
	b = n - A
	

def findRecFrac(n):
	# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
	a0 = int(math.floor(math.sqrt(n)))
	#print a0
	d0 = 1
	m0 = 0
	l = [a0]
	d = d0
	m = m0
	a = a0
	encountered = [(a0,d0,m0)]
	while True:
		m = (d*a) - m
		d = (n - m*m)/d
		a = (a0 + m) / d
		l.append(a)
		if (a,d,m) in encountered:
			break
		else:
			encountered.append((a,d,m))
		if a == 2*a0:
			break
	print l
	return l
	#A = recurrentFraction(a)
	# n^.5  = a + 1/x
	# x = 1 / (n^.5 - a)

def calcfrac(l):
	l.reverse()
	first = l.pop()
	if len(l) < 3:
		print "hooo"
		return first + fr.Fraction(1,l.pop())
	#print "ho: " + str(l)
	ans = first + rec(l)
	return ans

def rec(l):
	print l
	if len(l) == 2:#hier gaat fout
		#return fr.Fraction(1,l[1])
		#print "stop :  " + str(l)
		#print l[1]
		return l[1]
	if len(l) == 1:
		#return fr.Fraction(1,l[0])
		return l[0]
	#print fr.Fraction (1, (l.pop() + fr.Fraction(1,rec(l) )))
	return fr.Fraction (1, (l.pop() + fr.Fraction(1,rec(l) )))

def main():
	res = 0
	resD = 0
	for x in range(2,1001):
		print "x  " + str(x)
		if math.sqrt(x)**2 == x:
			continue
		ans = fr.Fraction(calcfrac(findRecFrac(x)))
		print ans.numerator, ans.denominator
		if ans.numerator > res:
			res = ans.numerator
			resD = x
			#print resD
	return resD


lx = findRecFrac(7)
print lx
print fr.Fraction(calcfrac(lx))
#print main()
