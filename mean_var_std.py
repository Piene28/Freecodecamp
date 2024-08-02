import numpy as np
import sys
from collections import OrderedDict
import pprint

def cleaned(string):
    return string.strip().replace(" ","").replace(",","").replace(".","")

def calculate(list):
    #make array, as a float in a 3x3 construction
    a = np.array(list).astype(np.float32).reshape(3,3)
    b = [j for sub in a for j in sub]
    #create dict
    stats=OrderedDict()
    #mean
    stats["mean"]=[]
    mean1=np.mean(a, axis=0).tolist()
    mean2=np.mean(a, axis=1).tolist()
    mean3=np.mean(b).tolist()
    stats["mean"].append(mean1)
    stats["mean"].append(mean2)
    stats["mean"].append(mean3)
    #variance
    stats["variance"]=[]
    variance1=np.var(a, axis=0).tolist()
    variance2=np.var(a, axis=1).tolist()
    variance3=np.var(b).tolist()
    stats["variance"].append(variance1)
    stats["variance"].append(variance2)
    stats["variance"].append(variance3)
    #std
    stats["standard deviation"]=[]
    std1=np.std(a, axis=0).tolist()
    std2=np.std(a, axis=1).tolist()
    std3=np.std(b).tolist()
    stats["standard deviation"].append(std1)
    stats["standard deviation"].append(std2)
    stats["standard deviation"].append(std3)
    #max
    stats["max"]=[]
    max1=np.max(a, axis=0).tolist()
    max2=np.max(a, axis=1).tolist()
    max3=np.max(b).tolist()
    stats["max"].append(max1)
    stats["max"].append(max2)
    stats["max"].append(max3)
    #min
    stats["min"]=[]
    min1=np.min(a, axis=0).tolist()
    min2=np.min(a, axis=1).tolist()
    min3=np.min(b).tolist()
    stats["min"].append(min1)
    stats["min"].append(min2)
    stats["min"].append(min3)
    #sum
    stats["sum"]=[]
    sum1=np.sum(a, axis=0).tolist()
    sum2=np.sum(a, axis=1).tolist()
    sum3=np.sum(b).tolist()
    stats["sum"].append(sum1)
    stats["sum"].append(sum2)
    stats["sum"].append(sum3)
    #results
    pprint.pprint(stats)    

#input is list of 9 digits
#if <9 ValueError
list=[]

#get input and clean away all other symbols
numbers=input("Type your 9 numbers: ")
numbers =cleaned(numbers)

#loop over the input, check if number and if yes append to list. If no raise error
n=0
for i in numbers:
    try:
        int(i)
        n+=1
        list.append(i)
    except (ValueError,TypeError):
        print("List must contain nine numbers.")
        sys.exit()

#check if input is 9 numbers

#TO DOO: Value Erro klopt nog niet. Kijken of dit onderste gedeelte in de for loop hierboven kan!
#To DOO: 3. moet 3.0 worden
if n != 9:
    raise ValueError("List must contain nine numbers.")
    sys.exit()
else:
    pass

stat = calculate(list)

#convert list into 3x3 numpy array in function called calculate
#return dict with statisti