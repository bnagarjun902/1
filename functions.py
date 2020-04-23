# positional arguments.....

# def details(username,password,country="India"):
#     print(" user {} with password {} accessed from {}".format(username,password,country))

# details("ji","li")

#arbitrary positional arguments

# def transaction(*a):
#     count = 0 
#     for i in a: 
#         count = count + i 
#     print("{} is the sum".format(count))
# transaction(10,20,30,40,50)


# def trans(*a,name):
#     print("{} amount withdrawn from account of {}".format(sum(a[0]),name))
# num = int(input("enter the number of transactions: "))
# b= [] 
# for i in range (num):
#     amount = float(input("enter the amount: "))
#     b = b + [amount] 


# print(b)               
# trans(b,name = input("enter the name of account holder: "))    
    
# def multiplication_table(a):
#     for i in range(1,21):
#         print('{}  *  {} = {}'.format(a,i,a*i))
       
# multiplication_table(a = int(input("enter the number : ")))

    