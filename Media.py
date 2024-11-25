# Descrição: Calcular a média de três notas
# Fornecida pelo usúario.

listas_notas = []

for media in range(1, 4):

    nota = float(input(f"Digite a {media} nota: "))
    listas_notas.append(nota)

    if media == 3:
        media_notas = (listas_notas[0] + listas_notas[1] + listas_notas[2]) / media
        print(f"A media é: {media_notas}")    
    
    
    