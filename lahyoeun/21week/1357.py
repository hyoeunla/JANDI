a, b = input().split()
a = list(a)
b = list(b)
if len(a) < 2:
    a.append('0')
    a.append('0')
    a.append('0')
elif 2 <= len(a) < 3:
    a.append('0')
    a.append('0')
elif 3 <= len(a) < 4:
    a.append('0')

if len(b) < 2:
    b.append('0')
    b.append('0')
    b.append('0')
elif 2 <= len(b) < 3:
    b.append('0')
    b.append('0')
elif 3 <= len(b) < 4:
    b.append('0')
a.reverse()
b.reverse()
a = int(a[0])*1000+int(a[1])*100+int(a[2])*10+int(a[3])
b = int(b[0])*1000+int(b[1])*100+int(b[2])*10+int(b[3])
c = a + b
c = str(c)
c = list(c)
if len(c) < 2:
    c.append('0')
    c.append('0')
    c.append('0')
elif 2 <= len(c) < 3:
    c.append('0')
    c.append('0')
elif 3 <= len(c) < 4:
    c.append('0')
c.reverse()
c = int(c[0])*1000+int(c[1])*100+int(c[2])*10+int(c[3])
print(c)
