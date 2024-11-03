c_to_f = lambda c: (c * 9/5) + 32
f_to_c = lambda f: (f - 32) * 5/9

celsius = 30
fahrenheit = 86

print(f"{celsius}°C = {c_to_f(celsius)}°F")
print(f"{fahrenheit}°F = {f_to_c(fahrenheit)}°C") 
