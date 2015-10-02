import sys

def pInTriangle(tri):
	tri = [ int(x) for x in tri ]
	(x,y) = (0,0)

	tx1 = tri[0]
	ty1 = tri[1]
	tx2 = tri[2]
	ty2 = tri[3]
	tx3 = tri[4]
	ty3 = tri[5]

	y23 = ty2 - ty3
	x32 = tx3 - tx2
	y31 = ty3 - ty1
	x13 = tx1 - tx3
	det = y23 * x13 - x32 * y31

	minD = min(det,0)
	maxD = max(det,0)

	dx = -tx3
	dy = -ty3
	a = y23 * dx + x32 * dy

	if  (a < minD or a > maxD):
		return 0
	b = y31 * dx + x13 *dy
	if  (b < minD or b > maxD):
		return 0
	c = det - a - b
	if  (c < minD or c > maxD):
		return 0
	return 1

	#print tx1,ty1,tx2,ty2,tx3,ty3



	return

def main():
	file = open('p102_triangles.txt')
	triangles = []
	for line in file:
		triangles.append(line.split(','))
	som = 0
	for triangle in triangles:
		som = som + pInTriangle(triangle)
	print som
if __name__ == '__main__':
	main()