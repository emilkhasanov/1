a = int(input('vvedite kolichestvo elementov spiska a '))
al = a
x = list()
while a>0:
    q = input('vvedite element spiska ')
    x.append(q)
    a = a-1
b = int(input('vvedite kolichestvo elementov spiska b '))
bl = b
y = list()
while b>0:
    w = input('vvedite element spiska ')
    y.append(w)
    b = b-1
c = int(input('vvedite kolichestvo elementov spiska c '))
cl = c
z = list()
while c>0:
    e = input('vvedite element spiska ')
    z.append(e)
    c = c-1
print('spisok a ',x)
print('spisok b ',y)
print('spisok c ',z)
d = list()
h = list()
i = 0
j = 0
for i in range(0, al):
    if x[i] not in z:
        d.append(x[i])
    i = i + 1
d = sorted(d)
print('sortirovannyi spisok a - c ',d)
for j in range(0, bl):
    if y[j] not in z:
        h.append(y[j])
    j = j + 1
h = sorted(h)
print('sortirovannyi spisok b - c ',h)
