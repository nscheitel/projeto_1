global pontos
pontos = 0
resposta1 = []
resposta2 = []
resposta3 = []
resposta4 = []
resposta5 = []
resposta6 = []
resposta7 = []
resposta8 = []
resposta9 = []
resposta10 = []
gabarito1 = ['d']
gabarito2 = ['e']
gabarito3 = ['c']
gabarito4 = ['a']
gabarito5 = ['c']
gabarito6 = ['d']
gabarito7 = ['c']
gabarito8 = ['c']
gabarito9 = ['b']
gabarito10 = ['a']
explicacao1 = ['Caso ocorra, a Olímpiada de 2021 será realizada no Japão, sendo a sede a cidade de Tóquio.']
explicacao2 = ['Os jogos Olímpicos de 2016, conhecido mais comumente como Rio 2016, foi realizado no segundo semestre de 2016, na cidade do Rio de Janeiro, no Brasil. Essa foi a oitava vez que o Brasil sediou um grande evento multiesportivo.']
explicacao3 = ['Atenas, A primeira Olimpíada da Era Moderna foi disputada entre 6 e 15 de abril de 1896, com delegações de 14 países, que somavam 241 atletas. Eles competiram em 43 eventos, de nove modalidades.']
explicacao4 = ['São 32 provas, 26 individuais e seis de revezamento.']
explicacao5 = ['5 anéis intrelaçados, que representam a união dos cinco continentes.']
explicacao6 = ['Em 1896, com a disputa da primeira edição dos Jogos Olímpicos da Era Moderna, o atletismo ganhou força e sua prática difundiu-se em todo o mundo nas décadas seguintes']
explicacao7 = ['Há 100 anos, no dia 3 de agosto de 1920, o Brasil subia ao topo do pódio olímpico pela primeira vez. O feito veio na categoria do tiro esportivo, nos Jogos da Antuépia, na Bélgica. Nesse dia, Guilherme Paraense conquistava a primeira medalha de ouro do Brasil na história dos Jogos Olímpicos']
explicacao8 = ['Serão 5 novos esportes, beisebol/softbol, karatê, escalada, surfe e skate.']
explicacao9 = ['O hino foi composto por Spirou Samara, com a letra do grego Cositis Palama, em 1986.']
explicacao10 = ['O neozelandês Mahe Drysdale venceu a prova do skiff simples de remo nos Jogos Olímpicos do Rio.']
               
def pergunta1():
    print('Olimpíadas')
    print('1. [Nível Fácil] Onde será realizada a próxima Olimpíada?')
    print('a)Alemanha \nb)Rússia \nc)Portugal \nd)Japão \ne)Islândia')
    resp1 = input()
    resposta1.append(resp1)  

def correcao1():
    global pontos
    for i in range(len(gabarito1)):
        if gabarito1[i]==resposta1[i]:    
            print('Parabéns, você acertou e ganhou 10 pontos!')
            pontos+=10
        else:
            print('Você errou e não ganhou pontos! A alternativa correta é a d)Japão.')
            print(explicacao1[i])


def pergunta2():
    print(' ')
    print('2. [Nível Fácil] Qual foi o último país e cidade sede das Olímpiadas (2016)?')
    print('a)Canadá, Vancouver \nb)Espanha, Madrid \nc)Chile, Santiago \nd)China, Pequim \ne)Brasil, Rio de Janeiro')
    resp2 = input()
    resposta2.append(resp2)  

def correcao2():
    global pontos
    for i in range(len(gabarito2)):
        if gabarito2[i]==resposta2[i]:    
            print('Parabéns, você acertou e ganhou mais 10 pontos!')
            pontos+=10
        else:
            print('Você errou e não ganhou pontos! A alternativa correta é a e)Brasil, Rio de Janeiro.')
            print(explicacao2[i])


def pergunta3():
    print(' ')
    print('3. [Nível Médio] Onde foi disputada a primeira Olimpíada da Era moderna?')
    print('a)Munique (Alemanha) \nb)Madrid (Espanha) \nc)Atenas (Grécia) \nd)Paris (França) \ne)Estocolmo (Suécia)')
    resp3 = input()
    resposta3.append(resp3)  

def correcao3():
    global pontos
    for i in range(len(gabarito3)):
        if gabarito3[i]==resposta3[i]:    
            print('Parabéns, você acertou e ganhou mais 15 pontos!')
            pontos+=15
        else:
            print('Você errou e não ganhou pontos! A alternativa correta é a c)Atenas (Grécia)')
            print(explicacao3[i])
            

def pergunta4():
    print(' ')
    print('4. [Nível Médio] Quantas provas existem dentro do programa olímpico?')
    print('a)32 \nb)30 \nc)42 \nd)36 \ne)36')
    resp4 = input()
    resposta4.append(resp4)  

def correcao4():
    global pontos
    for i in range(len(gabarito4)):
        if gabarito4[i]==resposta4[i]:    
            print('Parabéns, você acertou e ganhou mais 15 pontos!')
            pontos+=15
        else:
            print('Você errou e não ganhou pontos! A alternativa correta é a a)32')
            print(explicacao4[i])

            
def pergunta5():
    print(' ')
    print('5. [Nível Médio] Por quantos anéis entrelaçados é composto o símbolo das Olimpíadas?')
    print('a)8 \nb)6 \nc)5 \nd)3 \ne)9')
    resp5 = input()
    resposta5.append(resp5)  

def correcao5():
    global pontos
    for i in range(len(gabarito5)):
        if gabarito5[i]==resposta5[i]:    
            print('Parabéns, você acertou e ganhou mais 15 pontos!')
            pontos+=15
        else:
            print('Você errou e não ganhou pontos! A alternativa correta é a c)5')
            print(explicacao5[i])


def pergunta6():
    print(' ')
    print('6. [Nível Médio] Quando o atletismo passou a integrar o programa dos Jogos Olímpicos?')
    print('a) 1990 \nb) 1996 \nc) 1984 \nd) 1986 \ne) 1980')
    resp6 = input()
    resposta6.append(resp6)  

def correcao6():
    global pontos
    for i in range(len(gabarito6)):
        if gabarito6[i]==resposta6[i]:    
            print('Parabéns, você acertou e ganhou mais 15 pontos!')
            pontos+=15
        else:
            print('Você errou e não ganhou pontos! A alternativa correta é a d)1986')
            print(explicacao6[i])


def pergunta7():
    print(' ')
    print('7. [Nível Médio] Em qual Olimpíada o Brasil conquistou sua primeira medalha de ouro?')
    print('a) 1926, em Londres \nb) 2016, no Rio de Janeiro \nc) 1920, em Antuerpia \nd) 1996, em Atlanta \ne) 2008, em Sydney')
    resp7 = input()
    resposta7.append(resp7)  

def correcao7():
    global pontos
    for i in range(len(gabarito7)):
        if gabarito7[i]==resposta7[i]:    
            print('Parabéns, você acertou e ganhou mais 15 pontos!')
            pontos+=15
        else:
            print('Você errou e não ganhou pontos! A alternativa correta é a c)1920, em Antuerpia')
            print(explicacao7[i])


def pergunta8():
    print(' ')
    print('8. [Nível Médio] Quantos novos esportes teremos nas olimpiadas de 2021?')
    print('a)2 \nb)4 \nc)5 \nd)6 \ne)7 ')
    resp8 = input()
    resposta8.append(resp8)  

def correcao8():
    global pontos
    for i in range(len(gabarito8)):
        if gabarito8[i]==resposta8[i]:    
            print('Parabéns, você acertou e ganhou mais 15 pontos!')
            pontos+=15
        else:
            print('Você errou e não ganhou pontos! A alternativa correta é a c)5')
            print(explicacao8[i])

            
def pergunta9():
    print(' ')
    print('9. [Nível Difícil] Sobre o hino olímpico atual, está correto apenas:')
    print('a)Foi composto por Cositis Palamas em 1800 \nb)Foi composto por Spirou Samara em 1896 \nc)Foi composto por Cositis Palamas em 1896 \nd)Foi composto por Spirou Samara em 1800 \ne)Foi composto por Josh Williams em 2012')
    resp9 = input()
    resposta9.append(resp9)  

def correcao9():
    global pontos
    for i in range(len(gabarito9)):
        if gabarito9[i]==resposta9[i]:    
            print('Parabéns, você acertou e ganhou mais 20 pontos!')
            pontos+=20
        else:
            print('Você errou e não ganhou pontos! A alternativa correta é a b)Foi composto por Spirou Samara em 1896')
            print(explicacao9[i])


def pergunta10():
    print(' ')
    print('10. [Nível Difícil] Quem foi o ultimo campeao olímpico em remo skiff simples?')
    print('a)Mahé Drysdale (Nova Zelandia) \nb)Ondřej Synek (Republica Checa) \nc)Damir Martin (Croácia) \nd)Alan Campbell (Grã-Bretanha) \ne)Jhonatan Esquivel (Uruguai)')
    resp10 = input()
    resposta10.append(resp10)  

def correcao10():
    global pontos
    for i in range(len(gabarito10)):
        if gabarito10[i]==resposta10[i]:    
            print('Parabéns, você acertou e ganhou mais 20 pontos!')
            pontos+=20
        else:
            print('Você errou e não ganhou pontos! A alternativa correta é a a)Mahé Drysdale (Nova Zelandia)')
            print(explicacao10[i])

            
def main():
    pergunta1()
    correcao1()
    pergunta2()
    correcao2()
    pergunta3()
    correcao3()
    pergunta4()
    correcao4()
    pergunta5()
    correcao5()
    pergunta6()
    correcao6()
    pergunta7()
    correcao7()
    pergunta8()
    correcao8()
    pergunta9()
    correcao9()
    pergunta10()
    correcao10()
    print('Pontuação: ', pontos)
    if pontos <10:
        print('Errou todas!! Concentração, e mais sorte na próxima vez.')
    if pontos >=10 and pontos <=20:
        print('Garantiu o básico!! Tente mais uma vez.')
    if pontos >=25 and pontos <=40:
        print('Parece que você não conhecia muito sobre as Olimpíadas. Mais sorte na próxima!')
    if pontos >=45 and pontos <=60:
        print('Quase lá… Talvez na próxima você se saia melhor!')
    if pontos >=65 and pontos <=80:
        print('Mediano! Nada mal, hein?')
    if pontos >=85 and pontos <=100:
        print('Bom! Se saiu bem, aposto que pode ir ainda melhor!')
    if pontos >=105 and pontos <=120:
        print('Muito bom! Faltou pouquinha coisa, mandou bem!!')
    if pontos >=125 and pontos <=140:
        print('Mandou bem! Mostrou bastante conhecimento sobre as Olimpíadas, é isso aí!')
    if pontos >=145 and pontos <=150:
        print('Incrível!! Você domina mesmo o assunto, meus parabéns!!!')
main()

