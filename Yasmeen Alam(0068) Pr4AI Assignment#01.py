#!/usr/bin/env python
# coding: utf-8

# In[ ]:


student=[]
for i in range(1,6):
    n=input("Enter name of student:")
    rn=int(input("Enter roll no:"))
    py=int(input("Enter marks of python:"))
    ai=int(input("Enter marks of Artificial Intelligence:"))
    ma=int(input("Enter marks of Mathematics:"))
    stu={
        "Name":n,
        "Roll No":rn,
        "Marks":{"Python":py,
                 "AI":ai,
                 "Math":ma
                }
    }
    student.append(stu)
def calculation(stu):
    p=stu["Marks"]["Python"]
    a=stu["Marks"]["AI"]
    m=stu["Marks"]["Math"]   
    t=p+a+m
    pr=(t/300)*100
    if(pr>=80 and pr<=100):
        g='A'
    elif(pr>=70 and pr<=79):
        g="B"
    elif(pr>=60 and pr<=69):
        g="C"
    elif(pr>=50 and pr<=59):
        g="D"
    elif(pr>=0 and pr<50):
        g="F"
    else:
        print("Invalid Percentage")
    print("Name:",stu["Name"])
    print("Roll No:",stu["Roll No"])
    print("Total Marks:",t)
    print("Percentage:",pr)
    print("Grade:",g)
    stu["Total Marks"]=t
    stu["Percentage"]=pr
    stu["Grade"]=g
print("====DATA OF 5 STUDENTS====")
for stu in student:
    calculation(stu)
highest=student[0]
for stu in student:
    if(stu["Percentage"]>highest["Percentage"]):
        highest=stu
print("=====Student with HIGHEST PERCENTAGE=====")
print("Name:",highest["Name"])
print("Roll No:",highest["Roll No"])
print("Percentage:",highest["Percentage"])
print("Grade:",highest["Grade"])
f=open("result.txt","a")
f.write("Name:"+stu["Name"]+"\n")
f.write("Roll No:"+str(stu["Roll No"])+"\n")
f.write("Total Marks:"+str(stu["Total Marks"])+"\n")
f.write("Percentage:"+str(stu["Percentage"])+"\n")
f.write("Grade:"+stu["Grade"]+"\n")
f.close()


# In[ ]:


s=input("Enter a sentence:")
words=s.split()
tw=len(words)
print("Total no of words :",tw)
c=len(s)
print("Total no of characters:",c)
lw=max(words,key=len)
print("Longest Word:",lw)
sw=min(words,key=len)
print("Shortest Word:",sw)
vowels="aeiouAEIOU"
v=sum(s.count(char)for char in vowels)
print("Total no of vowels:",v)
tw=s.split()
l=list()
for i in tw:
    if i not in l:
        l.append(i)
g=str(l)
print("Set of unique words:",l)
sw=sorted(words)
print("Sorted Sentence:",sw)
f=open("analysis.txt","a")
f.write(s+"\n")
f.write("Total Words:"+str(tw)+"\n")
f.write("Total No Of Characters:"+str(c)+"\n")
f.write("Longest Word:"+str(lw)+"\n")
f.write("Shortest Word:"+str(sw)+"\n")
f.write("Total no of Vowels:"+str(v)+"\n")
f.write("Set of Unique Words:"+g+"\n")
f.write("Sorted Sentence:"+str(sw)+"\n")
f.close()


# In[ ]:


products=[]
for i in range(1,6):
    pn=input("Enter product name:")
    pr=float(input("Enter price:"))
    qu=int (input("Enter quantity:"))
    product={
        "Name":pn,
        "Price":pr,
        "Quantity":qu
    }
    products.append(product)
def calculate_bill(product):
    p=product["Price"]
    q=product["Quantity"]
    tp=p*q
    product["Total Price"]=tp
    return tp
tb=0;
for product in products:
    tb+=calculate_bill(product)
if(tb>10000):
    d=tb*0.10
    fb=tb-d
    print("Final Bill After Discount:",fb)
highest=products[0]
for product in products:
    if(product["Price"]>highest["Price"]):
        highest=product
print("====MOST EXPENSIVE PRODUCT====")
print("Name:",highest["Name"])
print("Price:",highest["Price"])
print("Quantity:",highest["Quantity"])
print("Total Price:",highest["Total Price"])
f=open("bill.txt","a")
f.write("Product Name:"+product["Name"]+"\n")
f.write("Price:"+str(product["Price"])+"\n")
f.write("Quantity:"+str(product["Quantity"])+"\n")
f.write("Total Price:"+str(product["Total Price"])+"\n")
f.close()
f=open("bill.txt","a")
f.write("Total Bill:"+str(tb)+"\n")
f.close()


# In[ ]:


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
i=1
while(i==1):
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    c=int(input("Enter your choice:"))
    if(c==1):
        r=add(num1,num2)      
    elif(c==2):
        r=sub(num1,num2)            
    elif(c==3):
        r=mul(num1,num2)      
    elif(c==4):
        r=div(num1,num2)      
    elif(c==5):
        r=mod(num1,num2)      
    else:
        print("Invalid Choice")
    print("Result=",r)
    ch=int(input("Press 1 if you want to perform another operation otherwise press 0 for exit:"))
    if(ch==1): 
        i=1
    else:
        print("Program Exit")
        break;


# In[ ]:


fb=0
i=1
while(i==1):
    print("1. Item:Burger  Price:500")
    print("2. Item:Pizza  Price:800")
    print("3. Item:Fries  Price:250")
    print("4. Item:Drink  Price:150")
    c=int(input("Enter your choice : "))
    q=int(input("Enter quantity:"))
    if(c==1):
        bill=500*q
    elif(c==2):
        bill=800*q
    elif(c==3):
        bill=250*q
    elif(c==4):
        bill=150*q
    else:
        print("Invalid choice")
    fb+=bill 
    ch=int(input("Press 1 for more order otherwise 0"))
    if(ch==1):
        i=1
    else:
        break; 
print("Final bill = ",fb)
f=open("order.txt","a")
f.write("Final Bill = " + str(fb) + "\n")
f.close()

