def cek_trio_ajaib(a, b, c):
    return (a + b == c) or (a + c == b) or (b + c == a)

print(cek_trio_ajaib(3, 4, 7))  
print(cek_trio_ajaib(1, 2, 4))
