# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 17:14:37 2017

@author: atul
"""
from SlaveProblem import SlaveProblem
from pulp import * ## import pulp-or functions


class MasterProblem:
	def __init__(self, maxValue, itemLengths, itemDemands, initialPatterns, problemname):
    		"""
			This class takes all the parameters required to solve a masterproblem and also sends it
			to the slave problem whenever required.
			"""
		
		self.maxValue=maxValue #Length of the sheet
		self.itemLengths=itemLengths #Length of each type of item needed.
		self.itemDemands=itemDemands #Demand of each type of item
		self.initialPatterns=initialPatterns #Initial matrix of patterns created.
		
		self.prob = LpProblem(problemname,LpMinimize)	# set up the problem. 
    
    #It takes the instance of the class LpProblem which is a model of LP which has two arguments, name and Objective:
    # whether minimize or maximize.
    
		
		self.obj = LpConstraintVar("obj1")   # generate a constraint variable that will be used as the objective
        
		self.prob.setObjective(self.obj)
		
		self.PatternVars=[]
		self.constraintList=[]   # list to save constraint variables in
		for i,x in enumerate(itemDemands):		# create variables & set the constraints, in other words: set the minimum amount of items to be produced
			var=LpConstraintVar("C"+str(i),LpConstraintGE,x)  # create constraintvar and set to >= demand for item
			self.constraintList.append(var)
			self.prob+=var
		print self.constraintList
			
		for i,x in enumerate(self.initialPatterns):  #save initial patterns and set column constraints 
			temp=[]
			for j,y in enumerate(x):
				if y>0: 
					temp.append(j)
			print temp
			
			var=LpVariable("Pat"+str(i)	, 0, None, LpContinuous, lpSum(self.obj+[self.constraintList[v] for v in temp]))  # create decision variable: will determine how often pattern x should be produced
			self.PatternVars.append(var)
        

		
	def solve(self):
		self.prob.writeLP('prob.lp')
		self.prob.solve()  # start solve
		
		return [self.prob.constraints[i].pi for i in self.prob.constraints]
		
			
		
	def addPattern(self,pattern):  # add new pattern to existing model
		
		self.initialPatterns.append(pattern)
		temp=[]
		
		for j,y in enumerate(pattern):
			if y>0: 
				temp.append(j)
		print temp
		var=LpVariable("Pat"+str(len(self.initialPatterns))	, 0, None, LpContinuous, lpSum(self.obj+[pattern[v]*self.constraintList[v] for v in temp]))
		self.PatternVars.append(var)
	
	def startSlave(self,duals):  # create/run new slave and return new pattern (if available)
		
		newSlaveProb=SlaveProblem(duals,self.itemLengths,self.maxValue)
				
		pattern=newSlaveProb.returnPattern()
		return pattern
		
	def setRelaxed(self,relaxed):  # if no new patterns are available, solve model as IP problem
		if relaxed==False:
			for var in self.prob.variables():
				var.cat = LpBinary
			
	def getObjective(self):
		return value(self.prob.objective)
		
	def getUsedPatterns(self):
		usedPatternList=[]
		for i,x in enumerate(self.PatternVars):
			if value(x)>0:
				usedPatternList.append((value(x),self.initialPatterns[i]))
		return usedPatternList