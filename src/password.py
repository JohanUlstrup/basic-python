import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
#print(password)
lower= False
upper = False
numb = False
special =False
minmax = False
for n in password:
    if n.islower():
        lower = True
    elif n.isupper():
        upper = True
    elif n.isnumeric():
        numb =True
    elif n=="$" or n=="#" or n=="@":
        special= True
    
if len(password)>=6 and len(password)<=16:
    minmax=True
"""     
print(lower)
print(upper)
print(numb)
print(special)
print(minmax)
 """
if lower and upper and numb and special  and minmax:
    is_valid = True
print(is_valid)
