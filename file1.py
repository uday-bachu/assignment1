#Assignment 
# let us define few variables globally for our assaignment
name = "divya" 
age = 22
a = "Good Evening"
a1 = 3
var1 = ["He", "is" , "my" , "assistant"]
var2 = ("I", "think" , "is" , "tupple")
l1 = [1,3,5,7]
s1 = {11,33,55,77}
s2 = {"hello","world",22.43,56}
# let us get into the assignment part
def assignment():
  # we can start with the basic program
  print("Hello " + a +" " + name +"!")
  print("let us perform some basic python programs")
  print("name = " + name)
  print("age = " ,age)
  print("After three years " + name + " age will be: "+ str(age+a1))
  print("name class is", type(a),"and " + "age class is" ,type(age))
#we need to get more deatail in our var1 list
  
  print("As we considered list called var1: ", var1)
  print("Class of var1:",type(var1))
  var1.insert(4,"at")
  var1.append("work")
  var1.append(True)
  var1.append(8)
  print("By updating the data we get: ",var1)
# printing data in a list by using index number
  print("Print how many data are present in var1 list",var1[7])
# by using negative indexing let us print data in the list
  print("We are printing number of data prsent in var1 list using negative indexing",var1[-1])
#Updating the data in list
  var1.insert(7,l2)
  print(var1)
  del var1[7]
  print(var1)

  #Now let us see examples on tuple
  tup1=("tv","ac","bed",33,54.56)
  print(tup1)
  print("length of tuple",len(tup1))
  #We can also find length using a for loop
  i=0
  for t in tup1:
  	i=i+1
  print("Length of the tuple using a for loop is",i)

  #Now lets see some examples on dictionary 
  dica={"clock":"hand","bed":"pillow","ceiling":"fan"}
  print(dica)
  #updating the dictionary 
  dica["phone"]="Narzo 30 pro"
  print(dica)
  del dica["bed"]
  print(dica)

  #sets
  print(s1)
  print(s2)
  # let us union the sets
  s3=s1|s2
  print("union of both the sets",s3)
  # let us see the intersection operation on the above sets
  print(s1.intersection(s2))
  #updating the sets
  s1.add(23)
  print(s1)

  #slicing 
  print(a[0])
  print(a[:])
  print(a[0:4])
  print(a[2:])
  #slicing using negative indexing
  print(a[-3])
  print(a[:-1])
  print(a[-5:])
  print(a[-3:-7])

  #functions
  def Greet():
    for i in range(1):
      print("HI")
  Greet()  
  def add(a,b):
    print("Age of "+ name + " after ",a1,"years is",a+b)
  add(age,a1)

assignment()
