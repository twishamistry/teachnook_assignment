# assignment 1
# create examples of list ,touple and dictionary
# --> list [] , mutable-- changable
grocery =["bread",1,"eggs",12,"peanut butter",1,"chicken",2]
print(grocery)

#insert element
grocery.insert(2,"paneer")
print(grocery)

#add or extend element
grocery.append("maggie masala")
print(grocery)

#delete element
del grocery[1]
print(grocery)

#remove element
grocery.remove("eggs")
print(grocery)

#-->tuple (), immutable
marks = ("maths 12/15","english 10/15","hindi 13/15")
print(marks)

#-->dictionary {},mutable
insta = {
    "instagram id":"_sooraj_sj_007",
    "password":"suraj1234",
    "followers":"1k",
    "posts":"60"}
print(insta)

# delete element
del insta["posts"]
print(insta)

#add or update element
insta.update({"likes":"10800"})
print(insta)
insta.update({"followers":"1.1k"})
print(insta)
insta["posts"] = "35"
print(insta)

#sclicing and step indexing
brand = "blackpipers"
print(brand[:])
print(brand[:5])
print(brand[-6:-1])
print(brand[::])
print(brand[::2])
print(brand[::-1])
print(brand[-8::-1])
