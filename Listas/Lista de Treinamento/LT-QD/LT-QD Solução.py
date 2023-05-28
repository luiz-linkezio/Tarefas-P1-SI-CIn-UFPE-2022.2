a = float(input())
l = float(input())
p = float(input())
h = float(input())
al = (a + l + (abs(a - l))) / 2
pal = (p + al + (abs(p - al))) / 2
if h >= 1:
    pal = int(pal*h)
    print(pal)