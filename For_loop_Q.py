#print the elemaent of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]
"""
nums = [1,4,9,16,25,36,49,64,81,100]

for el in nums:
    print(el)

    """

#Search for a num x in this tup;e using loop:
#[1,4,9,16,25,36,49,64,81,100]
"""
nums = (1,4,91,6,25,36,49,64,81,100,49) 
x = 49

idx = 0
for el in nums:
    if (el == x):
        print("number found at idx ", idx)

    idx += 1  
    """
nums = (1,4,91,6,25,36,49,64,81,100,49) 
x = 49

idx = 0
for el in nums:
    if (el == x):
        print("number found at idx ", idx)
        break

    idx += 1  