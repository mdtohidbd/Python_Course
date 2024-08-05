#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
#WAP to check if a list contains a aplindrome of elements .(hint use copu() method)
 
"""
movies = []
mov1 = input(" enter 1st movie :")
mov2 = input(" enter 2st movie :")
mov3 = input(" enter 3st movie :")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

"""
"""

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")
    """

#WAP to ciun the number of students with the "A" grade in the followwing tuple.
#["C","D","A","A","B","B","A"]
#store The above values in a list & sort them from "A"to "D"
"""
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))
"""

grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)

