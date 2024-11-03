def cocokkan_produk(a, b, c):
    digit_a = a % 10
    digit_b = b % 10
    digit_c = c % 10
    
    return (digit_a == digit_b) or (digit_a == digit_c) or (digit_b == digit_c)

print(cocokkan_produk(900, 10, 38))  # True
print(cocokkan_produk(276, 6, 75))   # True
print(cocokkan_produk(63, 391, 108)) # False
print(cocokkan_produk(654, 24, 74))  # True