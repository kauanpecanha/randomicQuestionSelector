from random import choice

def getQuestion(i):
    if(i<=24):
        print("\n\nLista 1")
    else:
        print("\n\nLista 2")
    
    
    if(i == 0):
        print("Questão 1 letra a")
    if(i == 1):
        print("Questão 1 letra b")
    
    if(i == 2):
        print("Questão 2 letra a")
    if(i == 3):
        print("Questão 2 letra b")
    if(i == 4):
        print("Questão 2 letra c")
    if(i == 5):
        print("Questão 2 letra d")
    if(i == 6):
        print("Questão 2 letra e")
    if(i == 7):
        print("Questão 2 letra f")
    if(i == 8):
        print("Questão 2 letra g")
    if(i == 9):
        print("Questão 2 letra h")
    
    if(i == 10):
        print("Questão 3")
    
    if(i == 11):
        print("Questão 4")
    
    if(i == 12):
        print("Questão 5")
    
    if(i == 13):
        print("Questão 6")
    
    if(i == 14):
        print("Questão 7 letra a")
    if(i == 15):
        print("Questão 7 letra b")
    
    if(i == 16):
        print("Questão 8 letra a")
    if(i == 17):
        print("Questão 8 letra b")
    if(i == 18):
        print("Questão 8 letra c")
    if(i == 19):
        print("Questão 8 letra d")
    if(i == 20):
        print("Questão 8 letra e")
    if(i == 21):
        print("Questão 8 letra f")
    if(i == 22):
        print("Questão 8 letra g")
    if(i == 23):
        print("Questão 8 letra h")
    if(i == 24):
        print("Questão 9")
    
    # lista 2
        
    if(i == 25):
        print("Questão 1 letra a")
    if(i == 26):
        print("Questão 1 letra b")
    if(i == 27):
        print("Questão 1 letra c")
    if(i == 28):
        print("Questão 1 letra d")
    if(i == 29):
        print("Questão 1 letra e")
    
    if(i == 30):
        print("Questão 2 letra a")
    if(i == 31):
        print("Questão 2 letra b")
    
    if(i == 32):
        print("Questão 3 letra a")
    if(i == 33):
        print("Questão 3 letra b")
    
    if(i == 34):
        print("Questão 4")
    
    if(i == 35):
        print("Questão 5 letra a")
    if(i == 36):
        print("Questão 5 letra b")
    if(i == 37):
        print("Questão 5 letra c")
    
    if(i == 38):
        print("Questão 6 letra a")
    if(i == 39):
        print("Questão 6 letra b")
    if(i == 40):
        print("Questão 7")
    if(i == 41):
        print("Questão 8")

def random():
    i = choice(range(0, 41+1))

    getQuestion(i)

while(True):
    c = int(input("\n\nEntre com 0 para finalizar o programa, ou 1 para gerar outra questão: "))

    if(c == 0):
        print("\n\nPrograma finalizado.")
        break

    elif(c == 1):
        random()
    
    else:
        print("Número inválido.")