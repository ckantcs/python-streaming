import sys

for line in sys.stdin:
	line = line.strip().split(',')  #delimiter is ',' here. change as per your file
	
	
	if line[0] == '1': #student
		print '%s,%s,%s' % (line[2],line[3],line[0])
	else: # subject
		print '%s,%s,%s' % (line[1],line[2],line[0])
	