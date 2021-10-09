import os

class estruturaForca():

    def __init__(self,palavra):
        self.a = '+=====+'
        self.b = ['|','|     O','|     |','|     |\ ','|    /|\ ','|      \ ','|    / \ '] 
        self.c = '_ '
        self.tamanho = 6
        self.erros = [] 
        self.acertos = []  
        self.palavra = palavra  

    def PrintaForca(self):
        print()
        print(self.a) 
        x = len(self.erros)        
        if (x == 0):
            self.PrintaParte(self.tamanho)  
            self.PrintaUnder()          
        elif (x == 1):
            print(self.b[1])            
            self.PrintaParte(self.tamanho-1)
            self.PrintaUnder()
        elif (x > 1 and x < 5):
            print(self.b[1])
            print(self.b[x])
            self.PrintaParte(self.tamanho-2)
            self.PrintaUnder()
        elif (x > 4 and x < 7):
            print(self.b[1])
            print(self.b[4])
            print(self.b[x])
            self.PrintaParte(self.tamanho-3)            
            if(x >= 6):        
                self.GameOver() 
            else:
                self.PrintaUnder()

    def PrintaParte(self,y):
        for i in range(y):
            print(self.b[0])

    def PrintaUnder(self):        
        bc = self.b[0] + '            '

        for i in self.palavra:
            if(i in self.acertos):
                bc += i + ' '             
            else:
                bc += '_ '                     

        print(bc)
        atual = bc.replace(" ","")
        base = self.b[0] + self.palavra
        if(atual == base):
            self.Vitoria()

    def GameMenu(self):
        self.PrintaForca()
        if(len(self.erros) > 0):                
            e = ''
            for i in self.erros:
                e += i + ' '
            print()
            print('### ERROS ###')
            print(e)
        if(len(self.acertos) > 0):
            a = ''
            for i in self.acertos:
                a += i + ' '
            print()
            print('### ACERTOS ###') 
            print(a)
        print()      
        letra = input('Digite uma letra ou "sair" : ')   
        if(letra.upper() == 'SAIR'):
            exit()                
        else:
            self.TestaPalavra(letra.upper())
            
    
    def TestaPalavra(self,letra):
        if(len(letra) != 1 or letra.isdigit()):
            print('AVISO : letra invalida')            
        elif(letra in self.acertos):
            print('AVISO : letra ja utilizada')            
        elif(letra in self.erros):
            print('AVISO : letra ja utilizada')            
        elif(letra in self.palavra):
            self.acertos.append(letra)            
        else:
            self.erros.append(letra)        
        
    def GameOver(self):
        print()
        print('     GAME OVER     ')
        exit()
    def Vitoria(self):
        print()
        print('     PARABENS VOCE VENCEU     ')
        exit()

palavra = ''
while not palavra or palavra.isdigit():
    palavra = input('Digite a palavra para comecar : ')
    if(type(palavra) == str and not palavra.isdigit()):
        jogar = estruturaForca(palavra.upper())
    else:
        print('Palavra inválida')

while (len(jogar.erros) <= 6):
    os.system('clear')
    jogar.GameMenu()










