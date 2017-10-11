# -*- coding: utf-8 -*-

import random  ## to generate the items
from MasterProblem import MasterProblem

random.seed(2012)


nrItems=12
lengthSheets=20


itemLengths=[]
itemDemands=[]

while len(itemLengths)!=nrItems:
	length=random.randint(5, lengthSheets-2)
	demand=random.randint(5, 100)
	if length not in itemLengths:
		itemLengths.append(length)
		itemDemands.append(demand)
	
print "Item lengts  : %s" % itemLengths
print "Item demands : %s\n\n" % itemDemands


patterns=[]
print "Generating start patterns:"
## generate simple start patterns
for x in range(nrItems):
	temp=[0.0 for y in range(x)]
	temp.append(1.0)
	temp+=[0.0 for y in range(nrItems-x-1)]
	patterns.append(temp)
	print temp


print "\n\nTrying to solve problem"
CGprob=MasterProblem(lengthSheets,itemLengths,itemDemands,patterns,'1D cutting stock')
	
relaxed=True
while relaxed==True:   # once no more new columns can be generated set relaxed to False
	duals=CGprob.solve()
	print "duals are"
	print duals
	
	newPattern=CGprob.startSlave(duals)
	
	print 'New pattern: %s' % newPattern
	
	if newPattern:
		CGprob.addPattern(newPattern)
	else:
		CGprob.setRelaxed(False)
		CGprob.solve()
		relaxed=False

print "\n\nSolution: %s sheets required" % CGprob.getObjective()

t=CGprob.getUsedPatterns()
print "For the number of itms= "+ str(nrItems)
print "And the length of sheet is " +str(lengthSheets)
print "And,"
print "Item lengts  : %s" % itemLengths
print "Item demands : %s\n\n" % itemDemands

for i,x in enumerate(t):
	print "Pattern %s: selected %s times	%s" % (i,x[0],x[1])

