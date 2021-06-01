# LIST Basics : ordered , indexed , mutable and duplicate values allowed
# List can contain other built in types as its element

#CREATION --> with []
empty_list=[]
single_list=[1,2,3,4,5,6,7,8,9,10]
mixed_list=[6.7,3,True,'a',"Kashish"]
nested_list=[(4,6,7),['x','y',0],{67,9,0},True,empty_list,empty_list]
print("CREATING NESTED LIST : ",nested_list)
print()

#type() : Returns the type of data type
print("DATA TYPE : ",type(single_list))
print()

#ACCESSING ELEMENTS OF LIST :
#METHOD 1 :
print("ACCESSING ELEMENTS OF LIST : ")
print("First element of nested_list : ",nested_list[0])
print("Third element of list in nested_list : ",nested_list[1][2])
#Empty list cannot have indexing i.e. nested_list[4][0] not possible
print("Fourth element of nested_list i.e. Empty list : ",nested_list[4])
#METHOD 2 : Using Negative Indexing
print("Last second element of nested_list : ",nested_list[-2])
print()

#SLICING IN LIST : Using slicing operator ":" i.e. colon
#single_list=1,2,3,4,5,6,7,8,9,10
#METHOD 1 : start/initial index not included
print("SLICING IN LIST : ")
print("Elements at 2 to 5 index : ",single_list[1:5])
print("Start index not given : ",single_list[:6])
print("End index not given : ",single_list[4:])
#METHOD 2 : Using Negative Indexing -> goes from left to right always while accessing elements , final/end index not included
print("Elements between 2-5 index : ",single_list[-5:-1])          #not simple_tuple[-1:-5]
print("Start index not given : ",single_list[:-4])                 #elements from -10 to -3
print("End index not given : ",single_list[-4:])                   #elements from -4 to -1
print()

#CHANGING IN LIST : List are mutable
print("CHANGING IN LIST : ")
#METHOD 1 : Using "=" operator for item assignment
nested_list[3]=(0,'u')
print("1 . Modifying an item at a particular index in list  : ",nested_list)
#METHOD 2 : Using ":" slicing operator for item assignment
single_list[1:4]=[20,30,40]                 #changes items at index 2,3,4 in single_list
print("2 . Modifying items using slicing in list  : ",single_list)
#METHOD 3 : Using append() method --> adds an element at the end
single_list.append([11,12,13])
print("3 . Appending in list : ",single_list)
#METHOD 4 : Using extend() method --> adds all elements at the end
single_list=[1,2,3,4,5,6,7,8,9,10]
single_list.extend([11,12,13])
print("4 . Extending in list : ",single_list)
#METHOD 5 : Concatenation using "=" operator --> for similar built in type
single_tuple=10,20,30,40,50,60,70,80,90,100
#print("5.1 . Concatenation of simple_tuple and nested_tuple : ",single_list+(14,15)) --> INVALID
print("5 . Concatenation of simple_tuple and nested_tuple : ",single_list+[14,15])
#METHOD 6 : Repeatition using "*" operator
print("6 . Repeatition in simple_tuple : ",["hello"]*5)
print()

#SPECIAL FEATURES OF LIST or LIST COMPREHENSIONS :
print("SPECIAL FEATURES OF LIST :",end="")
# 1 . Use of for statement within list brackets
print("1. Use of 'for' statement within list brackets : ")
power=[ 2 ** x for x in range(5) ]          #prints square of 0 to 4
print(power)
#1 Another way :
#power=[]
#for x in range(5):
    #power.append(2**x)

# 2 . Use of for and if statement within list brackets
power1=[ 2 ** x for x in range(10) if x>5 ]                         #the entire list gets stored in power1
print("2.1 Use of 'for' and 'if' statement within list brackets : ",power1)

multiply=[ x for x in range(10) if x%2==0 ]
print("2.2 Use of 'for' and 'if' statement within list brackets (even numbers): ",multiply)

concate=[ x+y for x in ['a','b'] for y in ['c','d'] ]
print("2.3 Use of concatenation of two lists using 'for' statement within list brackets : ",concate)
print()

#DELETING IN LIST :
print("DELETING IN LIST :")
#METHOD 1 :  Item deletion
single_list=[10,20,30,40,50,60,70,80,90,100]
del single_list[2]
print("1. Deleting item using its index : ",single_list)

#METHOD 2 : To delete item in list -> Delete nested item
del nested_list[1][2]
print("2. Deleting element from mutable member of list via index : ",nested_list)

#METHOD 3 : Using pop(index) method : Removes and returns an element at given index
single_list.pop()
print("3.1. Deleting element from last using pop() : ",single_list)
single_list.pop(4)
print("3.2 Deleting element from at index 4 using pop(4) : ",single_list)

#METHOD 4 : Using remove(value) method : Removes an element of given value
single_list.remove(10)
print("4. Deleting element using remove() : ",single_list)

#METHOD 5 : Assigning an empty list to a slice of elements
single_list[:3]=[]
print("5. Assigning an empty list to a slice of elements (removes elements from index 1 to 3): ",single_list)

#METHOD 6 : Using clear() method : Removes all elements of list
mixed_list.clear()
print("6. Deleting all elements using clear() : ",mixed_list)
#print("6. Checking whether the list got cleared or not using len() : ",len(mixed_list))

#METHOD 7 : Deleting entire list
del empty_list
print("7. Entire empty_list deleted :")
#print(empty_list) --> gives NameError : empty_list not defined