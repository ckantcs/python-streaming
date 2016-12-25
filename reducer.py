import sys



countmap = {}
subjecttype = ''
fullsubject = ''
for line in sys.stdin:
	line = line.strip().split(',')
	
	if line[-1] == '1': # student line
		if len(subjecttype) == 0: #first line encountered for a new subjecttype
			subjecttype = line[0]
			countmap[line[1]] = 1
		else:	
			if line[0] == subjecttype:
				try:
					countmap[line[1]] += 1
				except KeyError:
					countmap[line[1]] = 1
			else: #new object
				for key, value in countmap.items():
					print fullsubject , '\t', key, '\t', value
				countmap.clear()
				subjecttype = line[0]
				countmap[line[1]] = 1
				
			
	else: #subjects line
		if len(subjecttype) != 0:
			if line[0] != subjecttype:
				for key, value in countmap.items():
					print fullsubject , '\t', key, '\t', value
				countmap.clear()
		subjecttype = line[0]
		fullsubject =  line[1]
for key, value in countmap.items():
	print fullsubject , '\t', key, '\t', value
			
		
		

	