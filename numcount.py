s = input("Input a string")
d=0
for c in s:
    if c.isdigit():
        d=d+1
     else:
        pass
print("digits", d)
