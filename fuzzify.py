import random
def fuzzify_fun():
	p = 'negations/'
	check = [3,9]
	for i in check:
		with open(p+'file'+str(i)+'.txt','a') as file:
			file.write('\nTruth rate : 0 (because direct negation)')
			file.close()

	pth = 'modalities/'
	check2 = [2,6,7]
	m=[]
	f=[]
	for i in check2:
		with open(pth+'file'+str(i)+'.txt','r+') as file:
			for line in file:
				p1 = 'Inconsistency detected in modality: '
				p2 = 'however corresponding modality is: '
				res1 = line.partition(p1)[2]
				res2= line.partition(p2)[2]
				res1 = res1.strip()
				res2 = res2.strip()
				if(res1 != ''):
					m.append(res1)
				if(res2 != ''):
					f.append(res2)
			i=m[-1]
			j=f[-1]
			if(i == 'sure' and j == 'unsure'):
				while(1):
					n = random.randint(100,200)
					if(n<=120 and n>=110):
						#print(n)
						ptval = (120-n)/(120-100)
						ptval = str(ptval)
						file.write('truth rate : '+ptval+'\n')
						break
					elif(n>159):
						#print(n)
						ptval = (200-n)/(200-120)
						ptval = str(ptval)
						file.write('truth rate : '+ptval+'\n')
						break
			
			if(i == 'unsure' and j == 'surely not'):
				while(1):
					n = random.randint(1,99)
					if(n<=20 and n>=9):
						#print(n)
						ptval = (20-n)/(100-20)
						ptval = str(ptval)
						file.write('truth rate : '+ptval+'\n')
						break
					elif(n>59):
						#print(n)
						ptval = (100-n)/(100-20)
						ptval = str(ptval)
						file.write('truth rate : '+ptval+'\n')
						break
		file.close()


	pth_ = 'quantifiers/'
	check_ = [1,4,5,8,10]
	m = []
	f = []
	for i in check_:
		with open(pth_+'file'+str(i)+'.txt','r+') as file:
			for line in file:
				p1 = 'Inconsistency detected: '
				p2 = 'Highlighted inconsistency: '
				res1 = line.partition(p1)[2]
				res2= line.partition(p2)[2]
				res1 = res1.strip()
				res2 = res2.strip()
				if(res1 != ''):
					m.append(res1)
				if(res2 != ''):
					f.append(res2)
			i=m[-1]
			j=f[-1]
			#fdl(0 , 41 , 16 , 17)
			if(i == 'any' or j == 'anyone'):
				ptval = (15-1)/(41-1)
				#print('++++++++++++++',ptval)
				ptval2 = (41-18)/(41-1)
				#print('++++++++++++++',ptval2)
				falseval = ptval + ptval2
				truthval = 1-falseval
				truthval = str(truthval)
				#print('_++++++++',falseval)
				#print('_________',truthval)
				file.write('truth rate : '+truthval+'\n')
			if(i == 'dark'):
				ptval = (15-1)/(41-1)
				#print('++++++++++++++',ptval)
				#ptval2 = (41-)/(41-1)
				#print('++++++++++++++',ptval2)
				falseval = ptval 
				truthval = 1-falseval
				truthval = str(truthval)
				#print('_++++++++',falseval)
				#print('_________',truthval)
				file.write('truth rate : '+truthval+'\n')
			if(i == 'always'):
				ptval = (20-(-5))/(25-(-5))
				#print('++++++++++++++',ptval)
				#ptval2 = (41-)/(41-1)
				#print('++++++++++++++',ptval2)
				falseval = ptval 
				truthval = 1-falseval
				truthval = str(truthval)
				#print('_++++++++',falseval)
				#print('_________',truthval)
				file.write('truth rate : '+truthval+'\n')
		file.close()
