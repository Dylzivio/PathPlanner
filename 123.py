import random

def getName():
    alfawit = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    my_name = random.choice(alfawit)
    for i in range(3):
        my_name += random.choice(alfawit)
    for i in range(4):
        my_name += random.choice(numbs)
    return my_name

# listik = []
# newname = '777'
# iteration = 1
# while newname not in listik:
#     print(iteration)
#     iteration +=1
#     listik.append(newname)
#     newname = getName()
#     print(newname)
dict_sample = {
  "Company": "Mitsubishi",
  "model": "Outlander",
  "year": 2011
}
dict_sample2 = {
  "Company": "Hynday",
  "model": "Accent",
  "year": 2007
}
dict_sample3 = {
  "Company": "Ford",
  "model": "Focus",
  "year": 2010
}
my_cars = {}
my_cars['Dina']=dict_sample
my_cars['Me']=dict_sample2
my_cars['Dad']=dict_sample3

case = 2007
for NodeName in my_cars.keys():
    print(my_cars.keys())
    for childNode in my_cars.get(NodeName):
        # print('c--',childNode)
        # print(my_cars.get(NodeName))
        if childNode != 'year':
            print(my_cars.get(NodeName).get(childNode))
            print('===============')
