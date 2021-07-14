import time

total_segundos = int(time.time())
dia_em_s = 60 * 60 * 24
hora_em_s = 60 * 60
min_em_s = 60

dias = total_segundos // dia_em_s
total_segundos = total_segundos % dia_em_s
horas = total_segundos // hora_em_s
total_segundos = total_segundos % hora_em_s
mins = total_segundos // min_em_s
segs = total_segundos % min_em_s

print(
    str(dias)
    + " dias, "
    + str(horas)
    + " horas, "
    + str(mins)
    + " minutos, "
    + str(segs)
    + " segundos."
)
