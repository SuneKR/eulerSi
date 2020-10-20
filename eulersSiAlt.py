import time

# Change from local machine

# And with another comment added online via github

start = time.time()

allNumbers =[]
primeList = []

def lenB3(n):
    b3 = []
    pow = 1
    while n:
        rem = n%(3**pow)
        b3.append(rem)
        n -= rem
        pow += 1
    return len(b3)

def squareEliminator(prime):
    for primePot in range (2,pot):
        squNum = prime**primePot
        if (squNum <= num):
            allNumbers.remove(squNum)
            compositeEliminator(squNum, primePot, 0)
        else: break

def compositeEliminator(prime, primePot, rep):
    for kPrime in primeList[rep:]:
        rep += 1
        for kPrimePot in range (1,pot-primePot):
            compNum = prime * kPrime**kPrimePot
            if(compNum <= num):
                allNumbers.remove(compNum)
                compositeEliminator(compNum, primePot+kPrimePot, rep)
            else: break

num = int(input("giv mig et nummer "))
rNum = int(num**0.5)+1
pot = int(lenB3(num))

for number in range(3,num,2): allNumbers.append(number)

print("")

while len(allNumbers)>0:
    prime = allNumbers.pop(0)
    compositeEliminator(prime, 1, 0)
    if(prime < rNum): squareEliminator(prime)
    primeList.append(prime)

primeList.insert(0, 2)

runTime = time.time() - start

print("Summen af alle primtal under", num, "er", sum(primeList), "og indeholder", len(primeList), "primtal")
print("programmet tog", runTime, "sekunder")
print("")

print(primeList)
print("")
