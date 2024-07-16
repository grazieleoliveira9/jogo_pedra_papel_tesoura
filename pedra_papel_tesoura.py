print("***********************")
print("Pedra, Papel ou Tesoura")
print("***********************")


player1 = input("Player1, escolha Pedra, papel ou tesoura?").lower()
print("***************************************************")
player2 = input("Player2, escolha Pedra, papel ou tesoura?").lower()
print("***************************************************")


if player1 == player2:
    print("Empate, tentem novamente! 👎")

while player1 == "pedra" and player2 == "papel":
    print("Parabéns, Player2! Você ganhou 🙂 ")
    break
while player1 == "papel" and player2 == "pedra":
    print("Parabéns, Player1! você ganhou 🙂 ")
    break
while player1 == "pedra" and player2 == "tesoura":
    print("Parabéns, Player1! voce ganhou 🙂 ")
    break
while player1 == "tesoura" and player2 == "pedra":
    print("Parabéns, Player2! voce ganhou 🙂 ")
    break
while player1 == "papel" and player2 == "tesoura":
    print("Parabéns, Player2! voce ganhou 🙂 ")
    break
while player1 == "tesoura" and player2 == "papel":
    print("Parabéns, Player1! voce ganhou 🙂 ")
    break


