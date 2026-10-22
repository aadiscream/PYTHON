s1={1,2,4,5}
s2={4,8,7,4}
s3={10,11}
s4={1,2}
print(s1.union(s2))
print(s1,s2)
print(s1.intersection(s2))
# s1.update(s2)#updates s1 by adding s2
print(s1,s2)
print(s1.symmetric_difference(s2))#those which are not comman in sets
print(s1.isdisjoint(s3))
print(s1.issuperset(s4))
s4.add(3)
print(s4)
s4.remove(3)
print(s4)
# del s4 # used to delete sets
print(s4)