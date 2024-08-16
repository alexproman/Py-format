#string formating in python
###############################
name ="hamid"
age = 27
rank = 12.4
# old way of string formating 
###############################
#print("my name is "+name + "and my age is " +age) #########TypeError: can only concatenate str (not "int") to str
print("my name is "+str(name) + " and my age is " +str(age) + " my rank is " +str(rank)) 
## output : my name is hamid and my age is 44 my rank is 12.4
###############################
# in this way we will use placeholder (%s)==> string ,(%d)==> digit,(%f)==>float
print("my name is %s and my age is %d my rank is %.1f" % (name,age,rank) )
## output : my name is hamid and my age is 44 my rank is 12.4
###############################
# New ways to format strings
# 1- first Way
# in this way we will use placeholder {:s}==> string ,{:d}==> digit,{:f}==>float
print("my name is {} and my age is {} my rank is {}" .format (name,age,rank) )
print("my name is {:s} and my age is {:d} my rank is {:.1f}" .format (name,age,rank) )

#2 - format in version 3.6+
salary = 34653
print("************")
print(f"Hello, my name is {name}\nI'm {age} years old\nMy rank is {rank}\nand my salary is {salary:,d} LE")
print("************")
# output :
# Hello, my name is hamid
# I'm 27 years old
# My rank is 12.4
# and my salary is 34,653 LE
###############################
# format mony
#use placeholder {:,d} or {:_d}
mony = 1539754
print("my mony is : {:,d}".format(mony))
###############################
# Rearrang items 
a , b , c = "one","two","three"
print("my items is : {} {} {}".format(a,b,c)) # output : one two three
print("my items is : {1} {0} {2}".format(a,b,c)) # output :  two one three
print("my items is : {2} {1} {0}".format(a,b,c)) # output :  three two one

d, i ,f = 10,14,17
print("my items is : {} {} {}".format(d,i,f)) # output : 10 14 17
print("my items is : {1:d} {0:d} {2:d}".format(d,i,f)) # output :  14 10 17
print("my items is : {2:.2f} {1:.2f} {0:.2f}".format(d,i,f)) # output :  17.00 14.00 10.00


###########################
###### pyformat.info ######
###########################