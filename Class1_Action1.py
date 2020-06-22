# 求2+4+6+8+...+100的求和，用Python该如何写

sum=0
for number in range(51):
    sum=number*2+sum
print(sum)
