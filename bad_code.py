n = int(input("Number: "))
s = [0, 1]
s += [(s := [s[1], s[0] + s[1]]) and s[1] for k in range(n-2)]
print(s)
