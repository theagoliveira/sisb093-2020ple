passo1_min = 8
passo1_seg = 15

passo2_min = 7
passo2_seg = 12

passo1_seg_total = (passo1_min * 60) + passo1_seg
passo2_seg_total = (passo2_min * 60) + passo2_seg

tempo_total_seg = (2 * passo1_seg_total) + (3 * passo2_seg_total)
tempo_total_min = tempo_total_seg / 60

print(tempo_total_min)
