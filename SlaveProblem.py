# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 17:16:20 2017

@author: atul
"""

from pulp import * ## import pulp-or functions


class SlaveProblem:
    def __init__(self,duals, itemLengths,maxValue):
        self.slaveprob=LpProblem("Slave solver",LpMinimize)
        self.varList=[LpVariable('S'+str(i),0,None,LpInteger) for i,x in enumerate(duals)]
        self.slaveprob+=-lpSum([duals[i]*x for i,x in enumerate(self.varList)])  #use duals to set objective coefficients
        self.slaveprob+=lpSum([itemLengths[i]*x for i,x in enumerate(self.varList)])<=maxValue 

        self.slaveprob.writeLP('slaveprob.lp')
        self.slaveprob.solve() 
        self.slaveprob.roundSolution() #to avoid rounding problems

        

    def returnPattern(self):
        pattern=False
        if value(self.slaveprob.objective) < -1.00001:
            pattern=[]
            for v in self.varList:
                pattern.append(value(v))
        return pattern