# # # # # # # # a=10
# # # # # # # # b=10
# # # # # # # # name=input("Enter name")
# # # # # # # # print(name)
# # # # # # # # print("Enter age")
# # # # # # # # d=21
# # # # # # # # print(d)
# # # # # # # # e=22.5
# # # # # # # # print("float:",e)
# # # # # # # # f=True
# # # # # # # # print("bool:",f)

# # # # # # # # side = int(input("value"))
# # # # # # # # area = side*side
# # # # # # # # # print("Area of square:", area)

# # # # # # # subject1 = float(input("Enter marks of subject1: "))
# # # # # # # subject2 = float(input("Enter marks of subject 2: "))
# # # # # # # subject3 = float(input("Enter marks of subject 3: "))
# # # # # # # subject4 = float(input("Enter marks of sub4: "))
# # # # # # # subject5 = float(input("Enter marks of sub5: "))

# # # # # # # total = subject1+subject2+subject3+subject4+subject5
# # # # # # # avg = total/5
# # # # # # # print("Total marks: ",total)
# # # # # # # print("average marks",avg)

# # # # # # itemname = str(input("Enter name: "))
# # # # # # quantity = float(input("Enter quantity:"))
# # # # # # price_per_item = float(input("Enter price per item: "))
# # # # # # total_cost = quantity * price_per_item
# # # # # # gst = total_cost * 0.18
# # # # # # final_cost = total_cost + gst
# # # # # # print("Total cost: ",final_cost)

# # # # # food = float(input("food expenses: "))
# # # # # travel = float(input("travel expenses: "))
# # # # # other = float(input("other expenses: "))

# # # # # print("Total expenses: ",food + travel + other)

# # # # a = int(input("Enter first number: "))
# # # # b = int(input("Enter second number: ")) 
# # # # operation = input("Enter operation (+,-,*,/): ")
# # # # if operation == '+':
# # # #     print(a+b)
# # # # elif operation == '-':
# # # #     print(a-b)
# # # # elif operation == '/':
# # # #     print(a/b)
# # # # elif operation == '*':
# # # #     print(a*b)

# # # p = float(input("principle amt: "))

# # # r = float(input("rate: "))
# # # t = float(input("time: "))
# # # si = (p*r*t)/100 
# # # print("simple interest : ",si)

# # key = str(input("password: "))
# # if key == 'abcd123':
# #     print("Access granted")
# # else:
# #     print("Re enter password")

# #ATM DISPATCH only 500 and 200 notes available                           1

# # amt = float(input("Enter amount: "))
# # if amt >= 200 and amt % 100==0 and amt != 300: 
# #     print("discharging card")
# # else:
# #     print("nooooooo")

# # #TIME DAY AFTER NIGHT                                                    2

# t = str(input("Enter time: "))
# if "04:00" <= t <="11:59":
#     print("Good morning")
# elif "12:00" <= t <= "15:59":
#     print("Good afternoon")
# elif "16:00" <=t <= "18:59":
#     print("Good evening")
# else:
#     print("Good night")



num = int(input("Table of the number: "))
for i in range(1,11):
    print(num*i)
