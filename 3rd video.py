# student = ["sarajit",95.5,17,"delhi"]
# print (student[0])
# student[0]="raju"
# print(student)


# mark=[4,5,85,45,52]
# print(mark[1:4])
# print(mark[-3:-1])
# mark.append(54)
# print(mark)
# mark.sort()
# print(mark)
#mark.sort(reverse=True)
# print(mark)

 
# list=["marajit","sarkar","here"]
# list.sort(reverse=True)
# print(list) 


# print("hellow please your favorite 3 move name")
# movies=[]

# m1=input("enter your moves name:")
# m2=input("enter your 2nd move name:")
# m3=input("enter 3rd move name:")

# movies.append(m1)
# movies.append(m2)
# movies.append(m3)

# print(movies)



#palendrom

list1=[1,2,1]
list2=[1,2,1]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list2):
    print("palendrom")
else:
    print("not palendrom")
