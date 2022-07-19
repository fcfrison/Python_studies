'''
The Walrus operator is a way of assign a value to 
a variable.
'''
nums = list()
while(num:=input("Type a number: ").isdigit()): # first, the left hand side is evaluated, then 
                                                # through the walrus operator, the label 'num' 
                                                # points to the boolean value returned by isdigit().                                             
    nums.append(num)
