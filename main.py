print("Hello World")
name="Duncan"
print("My name is "+name)
print("I am 20+ years of age. Young, right?"+"\N{Slightly smiling face}")
list1=[12, 4, 56, 17, 8, 99]
print("The maximum number in this list:"+str(list1)+" is "+str(max(list1)))
sum=0
for i in list1:
    sum+=i
print("The mean: "+str(list1)+"is "+str(sum/float(len(list1))))

Var = ['A for Apple','B for Boy','C for Cat','D for Dog','E for Elephant','F for Fish','G for Girl','H for Hen','I for Ice cream','J for Jug','K for Kettle','L for Lion','M for Man','N for Nurse','O for Ostrich','P for Puppy','Q for Queen','R for Rabbit','S for Ship','T for Tree','U for Umbrella','V for Van','W for Woman','X for X-mass tree','Y for Yatch','Z for Zebra']
for n in Var:
    print(n)