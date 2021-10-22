import os
import random

class Hangman():

    def __init__(self):
        self.isright = []
        self.iswrong = []
        self.word = self.get_word().upper()
        #print(self.word)

    # Lê o arquivo Palavras.txt, Salva em uma lista e retorna um item da lista aleatório
    def get_word(self):
        with open("palavras.txt","r",encoding="utf-8") as p:
            words = p.readlines()
        return random.choice(words).strip()

    # inicia o jogo e mantém o loop até game over ou victory
    def game_start(self):
        while(len(self.iswrong) <= 6):   
            os.system('cls') # 'cls' pra limpar terminal windows, 'clear' pra limpar terminal linux  
            self.print_hangman()
            self.print_underline()
            self.info()
            self.check_word()

    # imprime na tela a forca e os erros e verifica se deu game over
    def print_hangman(self):
        pos_a = ['+======+']
        pos_b = ['|','|      O','|      |','|     /|','|     /|\ ','|     /','|     / \ ']

        e = len(self.iswrong)
        print(pos_a[0])  
        if(e <= 1):      
            print(pos_b[e])
            print(pos_b[0])
            print(pos_b[0])
        elif(e<=4):
            print(pos_b[1])
            print(pos_b[e])
            print(pos_b[0])
        elif(e<=6):
            print(pos_b[1])
            print(pos_b[4])
            print(pos_b[e])
        for i in range(3):
            print(pos_b[0])
        
        if(e >= 6):
            print()
            print("       !!! GAME OVER !!!")
            exit()
    
    # imprime na tela os underlines e letras, e verifica se deu victory
    def print_underline(self):
        underline = '       '
        
        for i in self.word:
            if(i in self.isright):
                underline += ' ' + i + ' '
            else:
                underline += ' __ '
        print(underline)

        vic = underline.replace(" ","")
        if(vic == self.word):
            print()
            print("       *** VICTORY ***")
            exit()

    # verificação da letra digitada, se é numero, se tem mais de 1 algarismo, se está na lista de acerto ou erros, e opção de sair
    def check_word(self):
        dig = input("Digite uma Letra ou 'sair' : ").upper() 
        if(dig == 'SAIR'):
            exit()
        elif(dig in self.iswrong or dig in self.isright):
            print("A letra ja foi utilizada")
        elif(len(dig) != 1 or dig.isdigit()):
            print("Letra inválida")
        elif(dig in self.word):
            self.isright.append(dig)
        else:
            self.iswrong.append(dig) 
        print()         
        
    # informa as letra já digitadas e se foram acertos ou erros
    def info(self):
        r = ''
        w = ''
        for i in self.isright:
            r += i + ' '
        for i in self.iswrong:
            w += i + ' '
        print()
        print("Acertos : " + r)
        print("Erros : " + w)
        print()

    

hangman = Hangman()
hangman.game_start()





