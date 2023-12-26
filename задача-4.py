V = int(input("введите скорость:"))
S = int(input("введите расстояние:"))

t = (S/V) % 24
if t < 8:
    print("1 пилот")
elif t < 16:
     print("2 пилот")
else:
     print("3 пилот")