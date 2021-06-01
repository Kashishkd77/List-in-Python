# LIST Operations illustration : (only 2 operations are in list)

list1=(-11,56.8,True,'a','b','c',67,33,1,True,)

#OPERATION 1 -> Using "in" and "not in" keyword : Returns True/False
print("OPERATION 1 : Using 'in' and 'not in' keyword")
#"in" keyword
print("Is 'Kashish' present in list? : ",'Kashish' in list1)
print("Is 'True' present in list? : ",True in list1)
#"not in" keyword
print("Is 'Kashish' not present in list? : ",'Kashish' not in list1)
print("Is 'True' not present in list? : ",True not in list1)
print()

#OPERATION 2 -> Iterating through a list
print("OPERATION 2 : Iterating through a list using for loop")
#accessing the elements of list by value and not index , using for loop to iterate through list
print("Example 1 : ")
for i in list1:
    print(i)
print("Example 2 : ")
for i in [7,89,'d']:
    print(i)