# def calc_sum(a,b):
#     sum = a+b
#     return sum

# print(calc_sum(5,8))
# print(calc_sum(4,3))


# average of 3 number

# def cal_average(a=1,b=3,c=1):
#     ave=(a+b+c)/2
#     print(ave)

# cal_average()




# cities = ["delhi","gurgaon","noida","mumbai","chennai"]
# heroes =["thor","ironman","captain america","shaktiman"]


# def print_len(list):
#     print(len(list))

# # print_len(cities)
# # print_len(heroes) 

# def print_list(list):
#     for item in list:
#         print(item, end =" ")

# print_list(heroes)
# print_list(cities)


# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)


# n=5
# def cal_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *=i
#     print(fact)

# cal_fact(5)


# def conveter(usd_val):
#     inr_val=usd_val*96
#     print(usd_val,"USD =",inr_val,"INR")

# conveter(100)   



# def fun(a):
#     if(a/2==0):
#         print("string ODD")
#     else:
#         print("string EVEN")


# fun(5)


def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n

print(fact(5))




