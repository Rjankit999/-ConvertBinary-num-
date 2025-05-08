def convertBinary (num):

binaryArray = []

while num>0:

binaryArray.append(num%2)

num = num//2

for j in binaryArray:

print(j, end="")

decimal_num = 21

convertBinary(decimal_num)def convertBinary (num):

binaryArray = []

while num>0:

binaryArray.append(num%2)

num = num//2

for j in binaryArray:

print(j, end="")

decimal_num = 21

convertBinary(decimal_num)   # def convertBinary (num):

binary = 0

i, rem = 1,0

while num != 0:

rem = num % 2

num = num // 2

binary += rem

i *= 10

return binary

*

i

decimal_num = 21

print("Binary of", decimal_num, "is : , end="")

print(convertBinary (decimal_num))
