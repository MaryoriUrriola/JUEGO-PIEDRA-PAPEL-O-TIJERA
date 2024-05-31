# JUGUEMOS PIEDRA, PAPEL O TIJERAS

import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

while True:

  print("*" * 50)
  print('ROUND' , rounds)
  print("*" * 50)

  print('computer_wins', computer_wins)
  print('user_wins', user_wins)  
  print("*" * 50)

  user_option = input('piedra, papel o tijera => ')
  user_option = (user_option.lower())

  rounds += 1
  
  if not user_option in options:
    print('Esa Opción no es Valida')
    print('Vuelve a intentarlo')
    continue
  
  computer_option = random.choice(options)
  
  print('User Option =>', user_option)
  print('Computer Option =>', computer_option)
  
  
  if user_option == computer_option:
    print("Empate!")
    
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print("Piedra gana a Tijera")
      print("User Gana!")
      user_wins += 1
    else:
      print("Papel gana a Piedra")
      print("Computer Gana!")
      computer_wins += 1
      
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print("Papel gana a Piedra")
      print("User Gana!")
      user_wins += 1
    else:
      print("Tijera gana a Papel")
      print("Computer Gana!")
      computer_wins += 1
  
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print("Tijera gana a Papel")
      print("User Gana!")
      user_wins += 1
    else:
      print("Piedra gana a Tijera")
      print("Computer Gana!")
      computer_wins += 1

  if computer_wins == 2:
    print('El ganador es la computadora')
    break

  if user_wins == 2:
    print('El ganador es el Usuario')
    break