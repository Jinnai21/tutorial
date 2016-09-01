def compare(list1, list2):
	hitblow = [0, 0]
	for i in range(0, 4):
		if list1.count(list2[i]) == 1:
			if list1[i] == list2[i]:
				hitblow[0] += 1
			else:
				hitblow[1] += 1
	return hitblow

for num in range(123, 9877):
	first = num/1000
	second = num/100 - first*10
	third = num/10 - (first*100 + second*10)
	fourth = num - (first*1000 + second*100 + third*10)
	numlist = [first, second , third , fourth]
	for i in range(0, 10):
		if numlist.count(i) > 1:
			cont = True
			break
		cont = False
	if cont == True:
		continue
	print str(first) + " " + str(second) + " " + str(third) + " " + str(fourth)
	provnum = [0, 1, 2, 3]
	hitblow = compare(numlist, provnum)
	#if hitblow[0] == 4:
	#	continue
	#print str(hitblow[0]) + " " + str(hitblow[1])
	log = []
	log.append([provnum, hitblow])
	provnum = [4, 5, 6, 7]
	hitblow = compare(numlist, provnum)
	#if hitblow[0] == 4:
	#	continue
	log.append([provnum, hitblow])
	hitblowsum = log[0][0] + log[0][1] + log[1][0] + log[1][1]
	print hitblowsum
	break