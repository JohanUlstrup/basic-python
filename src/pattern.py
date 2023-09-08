
# Print the pattern
y=10
x=[]
for number in range(y-1):
    if number <= y//2-1:
    
        x.append("*")
        print(' '.join(x))
    else:
        x.pop()
        print(' '.join(x))