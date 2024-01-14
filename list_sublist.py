Dataset = { 'Name' : ['Yogesh','Manik','Ravi','Vaidhees'],
           'Age': [43,27,22,12], 
           'Salary' : [30000,35000,25000,0]}
print(Dataset)

for key,value in Dataset.items():
    for i in value:
        print("{} : {}".format(key,i))

#Dataset['Year']=[]
#print(Dataset)

Dataset.update({'Year' : [1979,1997,1992,2011]})
print(Dataset)

L1=list(Dataset['Name'])
print("__________________")
print(L1)




for key in Dataset['Name']:
    if key == 'Manik':
        print("Name exist")
        list(Dataset['Name'] ='Ramesh')
#        print(key)
    else:
        print("Name not matched")
       # print(value)
print(Dataset)