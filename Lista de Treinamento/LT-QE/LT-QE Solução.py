nt = float(input())
oa = 10
ol = 30
op = 100
if nt<=oa and nt<ol and nt<op:
    print('Arthur')
elif nt>oa and nt<=ol and nt<op:
    print('Luiz')
elif nt>oa and nt>ol and nt<=op:
    print('Pedro')
else:
    print('Nenhum')