import os
import time
import random as r

DIR = '\\texts'
os.chdir(DIR)

class Disorders():

    #blood type not really relevant, remove later.
    bloodType = ['AB+', 'AB-', 'A+', 'A-', 'B+', 'B-', 'O+', 'O-']

    def __init__(self, name, bt, symptoms, disorder):
        self.name = name
        self.bt = bt
        self.symptoms = symptoms
        self.disorder = disorder


    def changedir(self, dir):
        self.dir = os.chdir(dir)

    def getSymptoms(self):
        return self.symptoms

    def getBloodType(self):
        return [self.bloodType[r.randint(0,len(self.bloodType)-1)]]

    def getRandSymptoms(self):
        length = len(self.symptoms)
        numList = r.sample(range(0, length), length)
        symptomList = []
        i = 0
        while len(symptomList) < 4:
            symptomList.append(self.symptoms[numList[i]])     #eliminate repeat symptoms per patient
            i += 1
        return symptomList

    def createObjBipolar(self,nameList, nameLength):
        create = Disorders(nameList[r.randint(0,nameLength)],self.getBloodType(self), self.getRandSymptoms(self), self.description(self))
        return create.name, create.bt, create.symptoms, create.disorder

class Bipolar(Disorders):


    with open('bipolar.txt','r') as f:
        read = f.readlines()
        symptoms = [name.rstrip() for name in read]
        f.close()

    def __init__(self, disorder):
        self.disorder = disorder

    def description(self):
        bi = Bipolar('Bipolar')
        return bi.disorder



class Schitz(Disorders):

    with open('schitz.txt','r') as f:
        read = f.readlines()
        symptoms = [name.rstrip() for name in read]
        f.close()

    def __init__(self,disorder):
        self.disorder = disorder

    def description(self):
        sc = Schitz('Schitzophrenia')
        return sc.disorder



class ADHD(Disorders):

    def __init__(self,disorder):
        self.disorder = disorder

    with open('add.txt', 'r') as f:
        read = f.readlines()
        symptoms = [name.rstrip() for name in read]
        f.close()

    def description(self):
        ad = Schitz('ADHD')
        return ad.disorder

class Depression(Disorders):

    def __init__(self,disorder):
        self.disorder = disorder

    with open('depression.txt', 'r') as f:
        read = f.readlines()
        symptoms = [name.rstrip() for name in read]
        f.close()

    def description(self):
        de = Schitz('Depression')
        return de.disorder

#execution code starts
startTime = time.time()

d = Disorders
length = len(d.getSymptoms(Bipolar)) #move this into appropriate class to determine length of symptom list.
isValid = True
symptomList = []
nameList = []


#go to text file location
DIR = 'D:\\Programming related\\Python Projects\\behaviorAnalysis\\texts'
os.chdir(DIR)
names = open('names.txt','r')


tempList = [name.rstrip() for name in names]
names.close()
#remove empty entries from list of sample names
for name in tempList:
    if '' != name:
        nameList.append(name)

nameLength = len(nameList)-1

#create patients
for x in range(1000):
    print (d.createObjBipolar(Bipolar, nameList, nameLength))
    print (d.createObjBipolar(Depression, nameList, nameLength))
    print (d.createObjBipolar(ADHD, nameList, nameLength))
    print (d.createObjBipolar(Schitz, nameList, nameLength))
#compute run time
print (time.time() - startTime, 'seconds to compute code.')