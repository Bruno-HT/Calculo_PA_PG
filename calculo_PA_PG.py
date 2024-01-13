print('Vamos calcular e aprender as diferenças entre uma Progressão Aritimética e uma Prograssão Geométrica')

print('Vamos começar pela Prograssão Aritimética (PA):\n')
primeiro_termo_pa = int(input('Digite o primeiro termo: '))
razao_pa = int(input('Digite a razão em que crescerá nossa PA: '))
termos_pa = int(input('Quantos termos terá nossa PA (máximo 50): '))

pa = []
termo_pa = primeiro_termo_pa
for contador in range(0, termos_pa):
    pa.append(termo_pa)
    termo_pa = termo_pa + razao_pa
print('\nEssa será nossa PA: ', pa)

pg = []
termo_pg = primeiro_termo_pa
for contador in range (0, termos_pa):
    pg.append(termo_pg)
    termo_pg = termo_pg * razao_pa
print('Considerando os mesmos números, nossa Progressão Geométrica (PG) ficaria assim: ', pg)
