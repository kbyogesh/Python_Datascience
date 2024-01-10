list1 = ['a',1,10.0,"list"]
print(list1)

list2 = ['test',10,11,11,12,13]
print(list2)
print(list2[2])

intlist = [1,2,3,4,5,6,20,10]
strlist = ["name","details","address"]
floatlist = [11.11,12.33,1.11]
#a = int("test")
a = int("15")
print(intlist)
print(strlist)
print(floatlist)
print(a)
print(type(a))

name = "Yogesh"
address = "k.k. nagar"
print(len(name),len(address))

detail = ["name","address","information","S.no","date"]
print(detail[1:4])

include = ["s.no.",1,"Yogesh"]

include.extend(["Remarks"])
print(include)

Newlist = ["s.no.",1,"Yogesh"]
Newlist.extend(["5","Remarks"])
print(Newlist)

Newlist = ["s.no.",1,"Yogesh"]
Newlist.extend(["11"])
print(Newlist)

Newlist1 = ["s.no.", 2, "Mahesh"]
Newlist1.insert(2,"Age")
print(Newlist1)

Newlist1 = ["s.no.", 3, "Akash"]
Newlist1.append("Age")
print(Newlist1)

Newlist1 = ["s.no.", 4, "Ravi"]
print(Newlist1[-1])
print(len(Newlist1))
Newlist2 = ["Address","Picode"]
Newlist1.extend(Newlist2)
print(len(Newlist2))
print(len(Newlist1))
print(Newlist1)
print(Newlist1[-1])
print(Newlist2[-1])
print(Newlist1[:1])
print(Newlist1[1:])

Newlist3 = ["Two Cats and Clever Monkey-Nursery stories to read:-Once upon a time, there were two cats who lived near a house. \n They were very hungry and one day, they found a piece of bread while searching for food. \n But when they tried to divide the bread, they both wanted the bigger piece and started fighting. Then they decided to go to a wise monkey to solve their problem. When they reached the monkey, they told him about their problem.\n However, the monkey was also very hungry and decided to eat the bread himself. The monkey brought a piece of bread and placed it on two plates of a balance scale. He took a bite from the bread on the lower plate and then \nfrom the bread on the higher plate, alternating bites between the two sides. While the monkey was eating, the two cats watched him in amazement. Finally, the monkey finished eating all the bread and said, \n“I have divided the bread into two equal parts. This half is for me and the other half is for you.” The cats were very sad and disappointed because they did not get any bread."]
#print(Newlist3)
#print(len(Newlist3))
#a=Newlist3
a=len(Newlist3)
print(a)

