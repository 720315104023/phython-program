i = 65;
k = 120;
print("before swapping\ni=", i,"k=",k);
i = i ^ k;
k = i ^ k;
i = i ^ k;
print("after swapping\ni=", i,"k=",k);
