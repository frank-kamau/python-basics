#dictionary
#list [], tuple (), dictionary {}

student = {'name':'Jane Sarah', 'id':1234, 'age':21, 'gender': 'F'}

print(student['name']) #key

print(student['id'])

print(student['age'])

print(student['gender'])

print(student)

student['weight'] = 61
print(student)

#set -- only one existence per item
people = {'Jane', 'Bill', 'Kevo', 'Said', 'Jane'}
print(people)
people.add('willy')
print(len(people)) #count
people.discard('Kevo')
print(people)

#git init
#git add
#git commit -m "Python basics"
#git remote add origin https://github.com/fran-kamau/python-basics.git
#git push -u origin master


#loops and functions in python