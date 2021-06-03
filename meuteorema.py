e = float(input('lado 1: '))
y = float(input('lado 2: '))
s = float(input('lado 3: '))
x = 180/(e + y + s)
if e == y == s:
    print('o valor dos ângulos é: 60º')
elif s > y and e:
    a = s * x + x
    b = y * x - (x/2)
    c = e * x - (x/2)
    print('''o valor dos ângulos são:
      {:.2f}º, {:.2f}º, {:.2f}º'''.format(a, b, c))
elif y > e and s:
    a = y * x + x
    b = s * x - (x/2)
    c = e * x - (x/2)
    print('''o valor dos ângulos são:
      {:.2f}º, {:.2f}º, {:.2f}º'''.format(a, b, c))
elif e > y and s:
    a = e * x + x
    b = y * x - (x/2)
    c = s * x - (x/2)
    print('''o valor dos ângulos são:
      {:.2f}º, {:.2f}º, {:.2f}º'''.format(a, b, c))