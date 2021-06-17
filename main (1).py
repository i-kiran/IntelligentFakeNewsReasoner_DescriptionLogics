import random
import os
import logging
import check_fun
import fuzzify
from fuzzify import fuzzify_fun
from check_fun import check_quantifiers
from check_fun import check_modality
from check_fun import check_negation
root1     = ['cause','causes','indication','cured','bite','ensures','attract','cures','cure','do','suffer','affect','parents','prevention','affects','prevents','drinking']
root2     = ['drink','exist','prove']
role1     = ['mosquito','mosquito aedes aegypti','clothes' ,'dengue','person1','papaya leaves','house','people','mosquitos']
role2     = ["goat's milk",'temperature','dengue','mosquito aedes albopictus','person2','platelet count','harm','organ impairment','children','temperature','one','mosquitos']
role3 	  = ['dengue','plasma leakage','old individuals']
quantifier1 = ['can','any','anyone','low','no evidence','always','only','cannot','severe','clean','cleanliness','dark','any type','20 degrees','can be','do','irrespective of','doesnot gurantee']
modality   = ['necessary','possible','restricted','wide','sure','unsure','surely not']
quality1 = ['only' , 'once' , 'again','less than','never','vigilant']
situation = ['vigilant']

m1  = 'Any mosquito can cause Dengue'
f1  = 'Mosquito aedes aegypti and mosquito aedes albopictus causes dengue'
m2  = 'Low platelet count ensures dengue'
f2  = 'A low platelet count can be an indication of dengue'
m3  = 'Papaya leaves can cure dengue'
f3  = 'Papaya leaves cannot cure dengue'
m4  = 'Dengue fever cannot do any harm'
f4  = 'Severe Dengue can cause organ impairment and plasma leakage'
m5  = 'Dengue only affects children and old individuals'
f5  = 'Dengue can affect anyone irrespective of age'
m6  = 'Clean house prevents dengue'
f6  = 'Cleanliness doesnot gurantee prevention from dengue'
m7  = "Dengue can be cured by drinking goat's milk"
f7  = "No evidence exist which can prove that goat's milk cures dengue"
m8  = 'Dark clothes attract mosquitos'
f8  = 'Any type of clothes cannot attract mosquitos'
m9  = 'If you suffer from dengue once , you will never get it again'
f9  = 'People can suffer from dengue again and again'
m10 = 'People should always be vigilant'
f10 = 'Mosquitos bite only at a temperature less than 20 degrees'

def write_dependencies(sentence, file):
	role = 0
	sentence = sentence.lower()
	sentence = sentence.strip().split(' ')
	s_list = []
	for i in range(len(sentence)):
		if not (sentence[i] == 'mosquito' and sentence[i+1] == 'aedes'):
			s_list.append(sentence[i])
		if i+1 < len(sentence):
			s_list.append(sentence[i]+' '+sentence[i+1])
		if i+2 < len(sentence):
			s_list.append(sentence[i]+' '+sentence[i+1]+' '+sentence[i+2])
	
	for word in s_list:
		if word in root1:
			if(word == 'ensures' or word == 'prevents'):
				file.write('modality: sure\n')	
				file.write('associated with: '+word+'\n')	
			file.write('root: '+word+'\n')
		if word in root2:
			if(word == 'ensures' or word == 'prevents'):
				file.write('modality: sure\n')
				file.write('associated with: '+word+'\n')				
			file.write('root: '+word+'\n')
		if word in role1 or word in role2 or word in role3:
			file.write('role: '+word+'\n')
			role += 1
		if word in quantifier1:
			if(word == 'can be' or word == 'doesnot gurantee'):
				file.write('modality: unsure\n')	
				file.write('associated with: '+word+'\n')			
			file.write('quantifier: '+word+'\n')
			if(word == 'no evidence'):
				file.write('modality: surely not\n')	
				file.write('associated with: '+word+'\n')			
			
		if word in modality:
			file.write('modality: '+word+'\n')
		if word in quality1:
			file.write('quality: '+word+'\n')

		if word in situation:
			file.write('situation: '+word+'\n')
			
			

#************************main*************************
myths = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]
facts = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]

if not os.path.exists('rdfs'):
	os.mkdir('rdfs')
path = 'rdfs/'
p = 'negations/'
i = 0
for myth in myths:
	i+=1
	file = open(path+'myth'+str(i)+'.txt','w')
	write_dependencies(myth, file)
	file.close()
	
i = 0
for fact in facts:
	i+=1
	file = open(path+'fact'+str(i)+'.txt','w')
	write_dependencies(fact, file)
	file.close()

check_quantifiers(myths , facts) 
check_modality(myths , facts) 	  
check_negation(myths , facts)     
fuzzify_fun()
print('\n')


quantifier_path = "quantifiers/"
modalities_path = "modalities/"
negations_path = "negations/"
list1 = [1,4,5,8,10]
list2 = [2,6,7]
list3 = [3,9]
def display(i):
	if(i in list1):
		filename= quantifier_path+'file'+str(i)+'.txt'
		with open(filename) as file:
				Lines = file.readlines()
				for line in Lines:
					print(line)
		file.close()
	if(i in list2):
		filename= modalities_path+'file'+str(i)+'.txt'
		with open(filename) as file:
				Lines = file.readlines()
				for line in Lines:
					print(line)
		file.close()

	if(i in list3):
		filename= negations_path+'file'+str(i)+'.txt'
		with open(filename) as file:
				Lines = file.readlines()
				for line in Lines:
					print(line)
		file.close()



loop = 1
while loop ==1:
	print("\n\n************MAIN MENU**************")

	choice = input("""
		1: Any mosquito can cause Dengue.
		2: Low platelet count ensures dengue.
		3: Papaya leaves can cure dengue.
		4: Dengue fever cannot do any harm.
		5: Dengue only affects children and old individuals.
		6: Clean house prevents dengue.
		7: Dengue can be cured by drinking goat's milk.
		8: Dark clothes attract mosquitos.
		9: If you suffer from dengue once , you will never get it again.
		10: People should always be vigilant.
		Q: Quit/Log Out

		Please enter your choice: \n\n""")
	choice=str(choice)

	if choice == "1":
		display(1)
	elif choice == "2":
		display(2)
	elif choice == "3":
		display(3)
	elif choice == "4":
		display(4)
	elif choice == "5":
		display(5)
	elif choice == "6":
		display(6)
	elif choice == "7":
		display(7)
	elif choice == "8":
		display(8)
	elif choice == "9":
		display(9)
	elif choice == "10":
		display(10)
	elif choice=="Q" or choice=="q":
		loop=0
	else:
		print("Please Select a valid option.")
		print("And Try Again!!!")
		
