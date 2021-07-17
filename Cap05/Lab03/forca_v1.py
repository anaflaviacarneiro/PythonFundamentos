# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.missing_letter = []
		self.guessed_letter = []

	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in word and letter not in guessed_letter:
			guessed_letter.append(letter)
		elif letter not in word and letter not in missing_letter:
			missing_letter.append(letter)
		else:
			return False
		return True

	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return self.hangman_won() or (len(self.missed_letters) == 6)

	# Método para verificar se o jogador venceu
	def hangman_won(self):

		if len(self.word) == len(guessed_letter):
			return True
		else:
			return False

	# Método para não mostrar a letra no board
	def hide_word(self):
		rtn = ''
		for letter in self.word:
			if letter not in guessed_letter:
				rtn += '_'
			else:
				rtn += letter

	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[len(missing_letter)])
		print("Palavra: \n")
		print ("Letras erradas: ")
		for letter in  missing_letter:
			print(letter)
		print ("Letras corretas: ")
		for letter in guessed_letter:
			print(letter)

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

	while not game.hangman_over():
		game.print_game_status()
		input_user = ("Digite uma letra \n")
		game.guess(input_user)

	# Verifica o status do jogo
	game.print_game_status()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
