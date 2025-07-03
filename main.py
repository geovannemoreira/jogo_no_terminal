import os

# Tamanho do mapa
LARGURA = 10
ALTURA = 5

# Posição inicial do jogador
player = {'nome': 'python', 'x': 0, 'y': 0}

def andar(direcao):
  if direcao == 'd' and player['x'] < LARGURA - 1:
    player['x'] += 1
  elif direcao == 'a' and player['x'] > 0:
    player['x'] -= 1
  elif direcao == 'w' and player['y'] > 0:
    player['y'] -= 1
  elif direcao == 's' and player['y'] < ALTURA - 1:
    player['y'] += 1

while True:
  os.system('clear' if os.name == 'posix' else 'cls')  # Compatível com Windows e Linux/Mac

  print('------------------------')
  for y in range(ALTURA):
    for x in range(LARGURA):
        if player['x'] == x and player['y'] == y:
          print('👺', end='')
        else:
          print('🟩', end='')
    print()  # Nova linha após cada linha do mapa
  print('------------------------')

  direcao = input('Próxima direção (w, a, s, d): ').lower()
  
  andar(direcao)
