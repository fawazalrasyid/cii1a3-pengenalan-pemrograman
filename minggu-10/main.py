# membuat set
a = {10, 20, 30, 40, 50} 
b = {20, 40, 50}

# mengabungkan 2 set
ab = list(a) + list(b)
ab.sort(key=ab.count)
print(ab)
c = set(ab)

# mencetak set
print(c)