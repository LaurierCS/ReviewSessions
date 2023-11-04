# two ways to make a list
a = list(1,2,3)
a = [1,2,3]

# List indices
print(a[0])
print(a[-1])

# List slicing
print(a[0:2])

# List methods
a.append(4)
a.insert(0,0)
a.remove(0)
a.pop(0)
a.sort()
a.reverse()

# list traversal
for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])

i = 0
while i < len(a):
    print(a[i])
    i = i + 1

# strings
s = "Hello World"

# string indices
print(s[0])

# string slicing
print(s[0:5])


# string traversal
for i in s:
    print(i)

for i in range(len(s)):
    print(s[i])

i = 0
while i < len(s):
    print(s[i])
    i = i + 1