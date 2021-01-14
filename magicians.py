#循环遍历
magicians = ["alice","jone","jack"]
for magician in magicians:
    print(magician)
#编写for 循环时，对于用于存储列表中每个值的临时变量，可指定任何名称。
for magician in magicians:
    print(magician.title() + ", that was a great track!")
    print("I can't wait to see your next performance, " + magician.title() + ".\n")
    #缩进内容将针对列表中每个元素运行一次
print("Thank you everyone. That's a great magic show!")



#练习
#4-1
pizzas = ["Popcorn shrimp pizza","Surf&Turf pizza","New orieans pizza"]
for pizza in pizzas:
    print(pizza.title() + " is delicious!")
    print("I like pepperoni pizza!" + ".\n")
print("I really love pizza!")

    
