min1 = int(input("Quantos minutos tem a musica 1:  "))
seg1 = int(input("Quantos segundos tem a musica 1:  "))

min2 = int(input("Quantos minutos tem a musica 2:  "))
seg2 = int(input("Quantos segundos tem a musica 2:  "))

min3 = int(input("Quantos minutos tem a musica 3:  "))
seg3 = int(input("Quantos segundos tem a musica 3:  "))

min4 = int(input("Quantos minutos tem a musica 4:  "))
seg4 = int(input("Quantos segundos tem a musica 4:  "))

min5 = int(input("Quantos minutos tem a musica 5:  "))
seg5 = int(input("Quantos segundos tem a musica 5:  "))

totalMin = min1+min2+min3+min4+min5
totalSeg = seg1+seg2+seg3+seg4+seg5

extraMin = int(totalSeg/60)
extraHoras = int(totalMin/60)

segundos = totalSeg - (extraMin * 60)
minutos = extraMin + totalMin - (extraHoras * 60)
horas = extraHoras



print("O total de tempo do album é:", horas, "Horas", minutos, "Minutos", segundos, "Segundos")