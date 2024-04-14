t = int(input())
while t:
    t -= 1
    c, r = input().split()
    c = int(c)
    r = int(r)
    #Contador de digitos
    List = [0] * 10
    def digitos(numero):
        digits = [int(d) for d in str(numero)]
        return digits

    def maximod(d):
        cuenta = [0] * 10
        for i in d:
            cuenta[i] += 1
        maxi = max(cuenta)
        return maxi

    #Funciones de "buscar a y b"
    def encontrarayb(c,r):
      i = 1000
      while i < 100000:
            a = i
            b = a * c
            m = b + (100000 * a)
            dm = [x for x in digitos(m)]
            if b >= 100000:
                break
            if (maximod(dm) <= r) and (b >= 10000):
                print(str(str(b) + str("/") + str(a) + str(" = ") + str(c)))
            i += 1
            
                

    encontrarayb(c,r)
