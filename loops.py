# emp_id = input("enter the employee id:  ")
# emp_com = input("enter the name of the employee's company:  ")
# emp_loc = input("enter the name of the location:  ")
# print("Person with employee id {2} is working in {0} in {1}".format(emp_id,emp_com,emp_loc))

# a = input("enter the savings account number:  ")
# # print(a.zfill(12))
# num = int(input("Enter the number:  "))
# for i in range(1,num+1):
#     count = 1  
#     count = 
#     #while i <= num:

# a = [1,2,3,[4.5,985,99],"python",105,56,83,67.5]
# a.reverse()
# print(a)

# a = range(1,11)
# print([ j  if j%3==0 else str(j) + " " + "not a multiple of 3" for j in a ])
#print([j%3 for j in range (1,13)])


# append -  add a single value in the end of list
# extend - add multiple values at the end of list - extend(data type==sequence type)
# remove - enter the value to be removed from the list, checks if the value is present and removes.
# pop - removes value - specify the index value 
# insert - facilitate insertion of single value after a particular index
# sort -  arrange sequence of values(homogeneous data type) in ascending order
# sort(reverse = True) - descending order - homogeneous data type
# reverse - print values in a list from right to left - heterogenous datatypes also possible. 
# list comprehension - if, else, for 

# num = int(input("enter the number:  "))
# count = 0
# while count<num:
#     b = num
#     b=num*num
#     count=count+1
#     print(b)   
    
# for i in range (1,101):
#     for j in range(1,11):
#         print(i*j)

# x = int(input("enter the number:-  "))
# s = x
# for i in range(1,x):
#     s = s*x
# print(s)
    
# a = "football"
# inp_ch = input("enter the character:  ")
# count = 0
# for i in a[0::1]:
#     if inp_ch == i:
#         count = count+1
# print(count)        

# a = {"username":"bnagarjun902",(1,2,3):"hello world","password":"nagarjun6#7","topic":"python module 2"}
# a["emailid"] = "nagarjun0607@gmail.com"
# a["city"] = "hyderabad"
# b = {"country":"india","city":"vijayawada","district":"krishna","village":"thimmasamudram"}
# a.update(b),pop,popitem,remove,keys,values,items, 

# a = {1,2,3,'python',3.6,8,9,3}
# a.add((98,99,100))
# print(a)
# a.pop()
# print(a)
# a.discard('bujji')
# print(a)

a = {1,2,3,4,5,6}
b = {3,4}
print(b.issubset(a))
