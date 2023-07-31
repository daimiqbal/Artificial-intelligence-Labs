from constraint import*
P = Problem()
P.addVariable("a",[1,2,3])
P.addVariable("b",[4,5,3])
print("Without Constraints!");
print(P.getSolutions())
P.addConstraint(lambda a,b:a*2==b,("a","b"))
print("Constraints")
print(P.getSolutions())


from constraint import*
P = Problem()
P.addVariable("a",[1,2,3])
P.addVariable("b",[4,5,3])
print("Without Constraints!");
print(P.getSolutions())
P.addConstraint(lambda a,b:a+1==b,("a","b"))
print("Constraints")
print(P.getSolutions())



from constraint import*
P = Problem()
P.addVariable("a",[3,7,9,3,6])
P.addVariable("b",[7,8,9,10])
P.addVariable("c",[4,58,9,10])
print("Without Constraints!")
print(P.getSolutions())
P.addConstraint(lambda a,b:a+1==b,("a","b"))
P.addConstraint(lambda a,c:a!=c,("a","c"))
print("Constraints")
print(P.getSolutions())


from constraint import*
P = Problem()
P.addVariable("a",[1,2,3])
P.addVariable("b",[4,5,3])
print("Without Constraints!")
print(P.getSolutions())
P.addConstraint(lambda a,b:a!=b,("a","b"))
print("Constraints")
print(P.getSolutions())



from constraint import*
P = Problem()
P.addVariable("a",[2,4,6,8,10,12])
P.addVariable("b",[3,6,12,15])
print("Without Constraints!")
print(P.getSolutions())
P.addConstraint(lambda a,b:a==b,("a","b"))
P.addConstraint(lambda a,b:a==6,("a","b"))
print("Constraints")
print(P.getSolutions())




from constraint import*
P = Problem()
P.addVariable("WA",["red", "green", "blue"])
P.addVariable("NT",["red", "green", "blue"])
P.addVariable("Q",["red", "green", "blue"])
P.addVariable("NSW",["red", "green", "blue"])
P.addVariable("V",["red", "green", "blue"])
P.addVariable("SA",["red", "green", "blue"])
print("Without Constraints!")
print(P.getSolutions())
P.addConstraint(lambda WA,NT:WA!=NT,("a","b"))
P.addConstraint(lambda WA,SA:WA!=SA,("a","b"))
P.addConstraint(lambda NT,SA:NT!=SA,("a","b"))
print("Constraints")
print(P.getSolutions())



from constraint import*

P = Problem()

P.addvariable("a",["R","G","B"])
P.addvariable("b",["R","G","B"])
P.addvariable("c",["R","G","B"])
P.addvariable("d",["R","G","B"])
print("Without Constraints:")

print(P.getsolution())

P.addconstraint(lambda a,b:a!=b,("a","b"))
P.addconstraint(lambda a,c:a!=c,("a","c"))
P.addconstraint(lambda a,d:a!=d,("a","d"))
P.addconstraint(lambda d,b:d!=b,("d","b"))
P.addconstraint(lambda c,d:c!=d,("c","d"))
print("Constraints")

print(P.getsolution())
