import sys
import random

def ID(i):
	x=""
	for p in range(0,i):
		x += str(random.randrange(0,9))
	return x


def Grade():
	number=random.gauss(60,10)
	if number < 40:
		S= "Fail"
	elif number < 60:
		S= "Provisional Pass"
	else:
		S= "Pass"

	return str(round(number,2)), S

print "Student ID,Average,Status"
for K in range(0,100):
	student_ID=ID(5)
	grade, status = Grade()
	print student_ID+","+grade+","+status

#for line in open(sys.argv[1]):
#	line=line.split(",")
#	student_ID=line[0]
#	grade, status = Grade()
#	print student_ID+","+grade+","+status


	#k=""
	#print ">"+random.choice(["CTCF","RAD21","ZNF143"])+"_Peaks_"+str(K)
	#for i in range(0,50):
#		k = k+ random.choice(["A","T","C","G"])
#	print k

