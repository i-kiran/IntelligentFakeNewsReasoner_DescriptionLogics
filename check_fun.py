import os

path = 'rdfs/'
def check_quantifiers(myths , facts):
	if not os.path.exists('quantifiers'):
		os.mkdir('quantifiers')

	#print("************************Myth*****************************")

	listforall = ['any' , 'anyone' , 'any type' , 'always']
	thereexist = ['20 degrees' , 'dark' , 'children' , 'old individuals' , 'organ impairment','plasma leakage','mosquito aedes aegypti','mosquito aedes albopictus']
	for i in range(len(myths)):
		myth_quantifier = []
		fact_quantifier = []
		with open(path+'myth'+str(i+1)+'.txt') as file:
			for line in file:
				q = 'quantifier:'
				res = line.partition(q)[2]
				res = res.strip()
				r = 'role:'
				res2 = line.partition(r)[2]
				res2 = res2.strip()
				if(str(res) in listforall):
					#print('myth = ',i+1)
					myth_quantifier.append(res)
					#print('present forall : ',res)
				if(str(res2) in thereexist):
					#print('myth = ',i+1)
					myth_quantifier.append(res2)
					#print('present there exist:',res2)
				if(str(res) in thereexist):
					#print('myth = ',i+1)
					myth_quantifier.append(res)
					#print('present there exist:',res)
		file.close()
		#print("********************FACTS************************")
		with open(path+'fact'+str(i+1)+'.txt','r') as file:
			for line in file:
				spl_word = 'quantifier:'
				res = line.partition(spl_word)[2]
				res = res.strip()
				r = 'role:'
				res2 = line.partition(r)[2]
				res2 = res2.strip()
				if(str(res) in listforall):
					#print('fact = ',i)
					fact_quantifier.append(res)
					#print('present for all: ',res)
				if(str(res2) in thereexist):
					#print('fact = ',i)
					fact_quantifier.append(res2)
					#print('present there exist:',res2)
				if(str(res) in thereexist):
					#print('fact = ',i)
					fact_quantifier.append(res)
					#print('present thereexist: ',res)
		file.close()
		if len(myth_quantifier) > 0 and len(fact_quantifier) > 0:
			file = open('quantifiers/file'+str(i+1)+'.txt','w')
			file.write('Sentence to be checked :\n'+myths[i]+'\n')
			for q in myth_quantifier:
				file.write('Inconsistency detected: '+q+'\n')
			file.write('\nHowever the truth is :\n'+facts[i]+'\n')
			for q in fact_quantifier:
				file.write('Highlighted inconsistency: '+q+'\n')
			file.close()
			
			

def check_modality(myths , facts):
	if not os.path.exists('modalities'):
		os.mkdir('modalities')
		
	#print("************************modality check for myth*****************************")
	for i in range(len(myths)):
		myth_modality = []
		fact_modality = []
		with open(path+'myth'+str(i+1)+'.txt','r') as file:
			for line in file:
				m = 'modality:'
				res = line.partition(m)[2]
				res = res.strip()
				my_string = ''
				if (res != my_string):
	#				print('myth = ',i+1)
					myth_modality.append(res)
	#				print('present modality: ',res)
				a = 'associated with:'
				res = line.partition(a)[2]
				res = res.strip()
				my_string = ''
				if (res != my_string):
					myth_modality.append(res)
	#				print('associated with: ',res)
		file.close()
	#	print("********************modality check for facts****************************")
		
		with open(path+'fact'+str(i+1)+'.txt','r') as m:
			Lines = m.readlines()
			for line in Lines:
				m = 'modality:'
				res = line.partition(m)[2]
				res = res.strip()
				my_string = ''
				if (res != my_string):
	#				print('fact = ',i+1)
					fact_modality.append(res)
	#				print('present modality: ',res)
				a = 'associated with:'
				res = line.partition(a)[2]
				res = res.strip()
				my_string = ''
				if (res != my_string):
					fact_modality.append(res)
	#				print('associated with: ',res)
		file.close()
		if len(myth_modality) > 0 and len(fact_modality) > 0:
			file = open('modalities/file'+str(i+1)+'.txt','w')
			file.write('Sentence to be checked :\n'+myths[i]+'\n')
			k =0
			j =0
			for m in myth_modality:				
				if(k%2 == 0):
					file.write('\nInconsistency detected in modality: '+m+'\n')
				else :
					file.write('associated with : '+m+'\n')
				k+=1
			file.write('\nThe truth is : \n'+facts[i]+'\n')
			
			for m in fact_modality:
				if(j%2 == 0):
					file.write('\nhowever corresponding modality is: '+m+'\n')
				else :
					file.write('associated with : '+m+'\n')
				j+=1
			file.close()
		

def check_negation(myths , facts):
	if not os.path.exists('negations'):
		os.mkdir('negations')
	#print("************************negation check for myth*****************************")
	for i in range(len(myths)):
		myth_negation = []
		fact_negation = []
		with open(path+'myth'+str(i+1)+'.txt','r') as file:
			for line in file:
				q = 'quantifier:'
				ql= 'quality:'
				res = line.partition(q)[2]
				res2= line.partition(ql)[2]
				res = res.strip()
				res2 = res2.strip()	
				if (res == 'can' or res == 'never' ):
	#				print('myth = ',i+1)
					myth_negation.append(res)
	#				print('quantifier: ',res)
				if (res2 == 'never'):
	#				print('fact = ',i+1)
					myth_negation.append(res2)
	#				print('quality: ',res2)
		file.close()
	#	print("********************negation check for facts****************************")
		with open(path+'fact'+str(i+1)+'.txt','r') as file:
			for line in file:
				q = 'quantifier:'
				ql= 'quality:'
				res = line.partition(q)[2]
				res2= line.partition(ql)[2]
				res = res.strip()
				res2 = res2.strip()
				if (res == 'cannot'):
	#				print('fact = ',i+1)
					fact_negation.append(res)
	#				print('quantifier: ',res)
				if (res2 == 'again'):
	#				print('fact = ',i+1)
					fact_negation.append(res2)
	#				print('quality: ',res2)
		file.close()
		if len(myth_negation) > 0 and len(fact_negation) > 0:
			file = open('negations/file'+str(i+1)+'.txt','w')
			file.write('\nSentence to be checked :'+myths[i]+'\n')
			for n in myth_negation:
				file.write('\nInconsistency detected (direct negation) : '+n+'\n')
			file.write('\nTruth is :\n'+facts[i]+'\n')
			for n in fact_negation:
				file.write('\nCorresponding to inconsistency in truth : '+n+'\n')
			file.close()
			
			
