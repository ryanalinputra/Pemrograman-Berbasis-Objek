import mypackage.alfa

print(mypackage.alfa.FunctionA())

import mypackage.beta

print(mypackage.beta.FunctionB())

import mypackage.subpackage1.subpackageA.gama as gama

print(gama.FunctionC())

import mypackage.subpackage1.subpackageA.delta as delta

print(delta.FunctionD())

from mypackage.subpackage2 import epsilon

print(epsilon.FunctionE())

from mypackage.subpackage2 import zeta

print(zeta.FunctionF())
