from dimod import ConstrainedQuadraticModel, Integer
i=Integer('i',upper_bound=4)
j=Integer('j',upper_bound=4)
cqm=ConstrainedQuadraticModel()
cqm.set_objective(-i*j) #we wish to maximize the area of a rectangle given a limit on the perimeter
cqm.add_constraint((2*i+2*j)<=8,"Max perimeter")
from dwave.system import LeapHybridCQMSampler
sampler=LeapHybridCQMSampler() #importing the hybrid sampler
sampleset=sampler.sample_cqm(cqm)
print(sampleset.first)
