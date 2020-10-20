import time

num = int(input("giv mig et nummer "))

start = time.time()

allNumbers =[]
primeList = []

for number in range(3,num,2): allNumbers.append(number)

while len(allNumbers)>0:
    potPrime = allNumbers.pop(0)
    primeList.append(potPrime)
    for compNum in range(3*potPrime, num, 2*potPrime):
        if(compNum in allNumbers):
            allNumbers.remove(compNum)

primeList.insert(0, 2)

print("Summen af alle primtal under", num, "er", sum(primeList), "og indeholder", len(primeList), "primtal") #to check if the function works
print("programmet tog", time.time() - start, "sekunder")
print("")

print(allNumbers)