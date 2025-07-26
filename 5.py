# Student Marks
students={'sonu':40,'monu':45,'tonu':50}
a=input('Enter the student name: ')
if a in students:
    print("{}'s marks: {}".format(a,students[a]))
else:
    print('Name not found')

# List Slicing
a=[1,2,3,4,5,6,7,8,9,10]
print('original list:',a)
b=a[:5]
print('Extracted first five elements:',b)
b.reverse()
print('Reversed Extracted elements:',b)

