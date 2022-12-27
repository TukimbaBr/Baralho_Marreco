import random, magias, arcanos_maiores
#♦️♠️♥️♣️🃏

baralho = ["as_copas", "dois_copas", "tres_copas", "quatro_copas", "cinco_copas", "seis_copas",
"sete_copas","oito_copas","nove_copas","dez_copas", 'onze_copas', "dama_copas", "valete_copas", "reis_copas",

"as_ouros", "dois_ouros", "tres_ouros", "quatro_ouros", "cinco_ouros", "seis_ouros",
"sete_ouros", "oito_ouros","nove_ouros","dez_ouros", 'onze_ouros', "dama_ouros", "valete_ouros", "reis_ouros",

"as_paus", "dois_paus", "tres_paus", "quatro_paus", "cinco_paus", "seis_paus", "sete_paus",
"oito_paus", "nove_paus","dez_paus", 'onze_paus', "dama_paus", "valete_paus", "reis_paus",

"as_espada", "dois_espada", "tres_espada", "quatro_espada", "cinco_espada", "seis_espada",
"sete_espada", "oito_espada", "nove_espada", "dez_espada", 'onze_espada', "dama_espada", "valete_espada",
"reis_espada"]

copas = ["as_copas", "dois_copas", "tres_copas", "quatro_copas", "cinco_copas", "seis_copas",
"sete_copas","oito_copas","nove_copas","dez_copas", 'onze_copas', "dama_copas", "valete_copas", "reis_copas",]

ouros = ["as_ouros", "dois_ouros", "tres_ouros", "quatro_ouros", "cinco_ouros", "seis_ouros",
"sete_ouros", "oito_ouros","nove_ouros","dez_ouros", 'onze_ouros', "dama_ouros", "valete_ouros", "reis_ouros",]

paus = ["as_paus", "dois_paus", "tres_paus", "quatro_paus", "cinco_paus", "seis_paus", "sete_paus",
"oito_paus", "nove_paus","dez_paus", 'onze_paus', "dama_paus", "valete_paus", "reis_paus",]

espada = ["as_espada", "dois_espada", "tres_espada", "quatro_espada", "cinco_espada", "seis_espada",
"sete_espada", "oito_espada", "nove_espada", "dez_espada", 'onze_espada', "dama_espada", "valete_espada",
"reis_espada"]

coringa = ['CORINGA']

spread = []

limitspread = int(6)

def linha(tl):
    print('-'*tl)


def show_color(card,magic=False):    
    if card in copas[:]:
        print(f'\033[1;36m[{card}]\033[0;0m',end=' ')
            
    if card in espada[:]:
        print(f'\033[1;32m[{card}]\033[0;0m',end=' ')
    
    if card in ouros[:]:
        print(f'\033[1;35m[{card}]\033[0;0m',end=' ')
    
    if card in paus[:]:
        print(f'\033[1;31m[{card}]\033[0;0m',end=' ')
    
    if card in coringa:
        print(f'{card}',end=' ')            

        
def show_color_list(lista):
    if lista == spread:
        print('SPREAD = ',end='')
    if lista == baralho:
        print('DECK = ',end='')
    for carta in range(0,len(lista)):
            show_color(lista[carta])
            

print('')    
linha(50)   
print('-ITS TIME TO DUEL-')
linha(50)

while True:
    opcao = int(input('''\n   ITS MY TURN
    
    [01] EMBARALHAR
    [02] VER ORDEM DO BARALHO
    [03] COMPRAR SPREAD
    [04] VER SPREAD
    [05] MULLIGAN
    [06] ADICIONAR UMA CARTA COM O CORINGA
    [07] USAR UMA CARTA
    [08] ARCANO MAIOR  
    [10] 
     '''))

#embaralha as cartas
    if opcao == 1:
        baralho = random.sample(baralho, len(baralho))
        linha(50)       
        print('{:^50}'.format('EMBARALHADO'))        
        linha(50)

#mostra a ordem do baralho    
    if opcao == 2:
        show_color_list(baralho)            
        
#Compra o spread
    if opcao == 3:            
        print(f'Comprando {limitspread} cartas')        
        for c in range(len(spread),limitspread):
            spread.append(baralho.copy()[c])
        del baralho[0:limitspread]       
        show_color_list(spread)
        print('\n')
        
#Mostra o spread
    if opcao == 4:
        print('')
        show_color_list(spread)        
        print('')
        for c in range(0,len(spread)):
            magias.magia(spread[c])
        
#Muligan    
    if opcao == 5:
        spread.append(baralho.copy()[0])                #FIX THIS!
        show_color_list(spread)
        descarte = str(input('Qual carta vai pro fundo o baralho? '))
        spread.remove(descarte)
        baralho.append(descarte)
        show_color_list(spread)
        for c in range(0,len(spread)):
            magias.magia(spread[c])
        
#Comprar carta com o coringa
    if opcao == 6:
        show_color_list(baralho)
        carta = str(input('Qual dessas cartas você quer em seu spread? '))
        spread.append(carta)
        baralho.remove(carta)
        baralho.append(coringa[:])
        baralho = random.sample(baralho, len(baralho))
        show_color_list(spread)
        for c in range(0,len(spread)):
            magias.magia(spread[c])
#impede que o spread tenha mais que o limite dele
    while len(spread) > limitspread:
        print(f'SPREAD = {str(spread)}')
        print(f'Seu SPREAD excedeu o limite de cartas que é {limitspread}')
        descarte = str(input('Qual carta vai pro fundo o baralho? '))
        while descarte not in spread:
            descarte = str(input('Digite uma carta válida? ')).lower()
        spread.remove(descarte)
        baralho.append(descarte)
        print(f'SPREAD = {str(spread)}')
        print('')

#Usar uma carta
    if opcao == 7:
        show_color_list(spread)        
        use = str(input('Qual carta você vai usar? ')).lower()
        while use not in spread[:]:
            show_color_list(spread)
            use = str(input('Digite uma carta válida? ')).lower()
        spread.remove(use)
        baralho.append(use)
        show_color_list(spread)
        
#Arcanos Maiores

    if opcao == 8:
        arcanos_maiores.sorte()
        
    

                

    
    


    


    




        



        
