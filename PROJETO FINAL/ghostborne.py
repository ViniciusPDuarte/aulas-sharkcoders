def ghostborne():
    from time import sleep
    sleep(1)
    # inicio
    print('-=+> Mike <+=-')
    print('Bem vindo á Ghostborne. Um lugar esquecido. ')
    sleep(3)
    print('Parece ser bem confortável, mas, na realidade, não é.')
    sleep(3)
    print('Mas relaxa, estou a falar que aqui não vai ser o pior possível, mas')
    sleep(1)
    print('aqui provavelmente irá ser uma experiência amedrontadora, e também...')
    sleep(3)

    print(f'=-' * 50)
    print('1 - Não, não me digas isso!')
    print('2 - Ah, irá ser fixe então!')
    print('3 - Ficou pior...')
    print('4 - [Continue a conversa]')
    opc = int(input('Input: '))

    if opc == 1:
        sleep(1)
        print(f'=-' * 50)
        print('-=+> Você <+=-')
        sleep(1)
        print('Não, Mike! Não esteja-me à dizer isto!')
        sleep(1)
        print('-=+> Mike <+=-')
        sleep(1)
        print('Alerta, medrosos!')
        sleep(2)

    if opc == 2:
        sleep(1)
        print(f'=-' * 50)
        print('-=+> Você <+=-')
        sleep(1)
        print('Ei, vai ser até que divertido então...')
        sleep(1)
        print('-=+> Mike <+=-')
        sleep(1)
        print('Bem, quando vim cá pela primeira vez,')
        sleep(2)
        print('Foi divertido... na maioria dos lugares, assim... esquece.')
        sleep(4)

    if opc == 3:
        sleep(1)
        print(f'=-' * 50)
        print('-=+> Você <+=-')
        sleep(1)
        print('Ai, isto não é bom... Ah, não.')
        sleep(1)
        print('-=+> Mike <+=-')
        sleep(1)
        print('Acalma-te, rapaz! Aqui não é assim tão mau!')

    else:
        sleep(1)
        print(f'=-' * 50)
        sleep(1)
        print('-=+> Mike <+=-')
        sleep(1)
        print('E não vás longe, ok?')
        sleep(2)

    # livre
    sleep(1)
    print(f'=-' * 50)
    print('Agora estás livre. ')
    print(f'=-' * 50)
    sleep(3)

    # boss???
    while True:
        print('1 - Entrar no alojamento de jóias')
        print('2 - Atravessar o rio')
        print('3 - Interagir com algo do chão prateado')
        opc = int(input('Input: '))

        if opc == 1:
            sleep(1)
            print(f'=-' * 50)
            print('-=+> Pensamento <+=-')
            sleep(3)
            print('Ha, até parece o presente que dei à minha mãe natal passado!')
            sleep(3)
            print(f'=-' * 50)

        if opc == 2:
            print(f'=-' * 50)
            sleep(3)
            ghostborne_boss_rio()
            break

        if opc == 3:
            print(f'=-' * 50)
            print('-=+> Pensamento <+=-')
            sleep(1)
            print('Esta moeda está-me a dizer para ir ao rio e atravesá-lo.')
            sleep(2)
            print('Vou ver o que se passa lá...')
            sleep(2)
            print(f'=-' * 50)
            sleep(3)
            print('Já estás cansado, mas chegaste ao pé duma árvore grandee.')
            sleep(2)
            print(f'=-' * 50)
            sleep(2)
            ghostborne_boss_rio()
            break

    # pós boss
    print('-=+> Mike <+=-')
    print('Eu avisei-te... ')
    sleep(3)
    print('Pelo menos tu conseguiste sobreviver, mas não deixe a curiosidade te levar, rapaz.')
    sleep(3)
    print('Tenha o que eu falei agora na tua cabeça. Aqui as coisas são muito mais perigosas do que parecem.')
    sleep(4)

    print(f'=-' * 50)
    print('1 - Ok, eu vou tentar.')
    print('2 - Está bem... [Suspiro]')
    print('3 - [Continue a conversa]')
    opc = int(input('Input: '))

    if opc == 1:
        sleep(1)
        print(f'=-' * 50)
        print('-=+> Você <+=-')
        sleep(1)
        print('Vai ser difícil aplicar isso, mas irei tentar.')
        sleep(2)
        print('-=+> Mike <+=-')
        sleep(1)
        print('Ok, não fazes aquilo novamente!')
        sleep(2)
        ghostborne_fim_1()

    if opc == 2:
        sleep(1)
        print(f'=-' * 50)
        print('-=+> Você <+=-')
        sleep(1)
        print('Que chatos!')
        sleep(1)
        print('-=+> Mike <+=-')
        sleep(1)
        print('Ei, não fales assim, as coisas não são como parecem!')
        sleep(2)
        print('Você provavelmente irá acabar num cemitério se não fazer o que falo.')
        sleep(2)
        print('Só estou a falar, também podes ir fazer estas coisas ridículas.')
        sleep(3)
        ghostborne_fim_2()

    if opc == 3:
        sleep(1)
        print(f'=-' * 50)
        sleep(1)
        print('-=+> Mike <+=-')
        sleep(1)
        print('E estou a falar á sério.')
        sleep(2)
        ghostborne_fim_3()

# fins

def ghostborne_fim_1():
    global rndm1, rndm2
    from time import sleep
    while True:
        print(f'=-' * 50)
        print("1 - Entrar numa galeria d'artes")
        print('2 - Ir para uma construção sem nome.')
        print('3 - Pegar o trem para casa')
        opc = int(input('Input: '))

        if opc == 1:
            sleep(2)
            print(f'=-' * 50)
            sleep(3)
            print('O lugar estava cheio de pessoas à ver as pinturas famosas.')
            sleep(3)
            print(f'=-' * 50)
            sleep(2)
            print('-=+> Pensamento <+=-')
            sleep(1)
            print('Uh, aqui é demasiado enorme...')
            sleep(2)
            print('Será que devo ir embora?')
            sleep(3)
            print('Mhm, acho que é melhor antes de não saber onde é a saida.')
            sleep(2)
            break

        if opc == 2:
            casino(opc)
            break

        if opc == 3:
            sleep(2)
            print(f'=-' * 50)
            sleep(3)
            print('Pegaste o trem para casa com sucesso. Todos comemoraram com a sua volta.')
            sleep(3)
            print(f'=-' * 50)
            sleep(2)
            print('PROJETO FINAL-AULAS PYTHON, SHARKCODERS')
            sleep(2)
            print(f'=-' * 50)
            sleep(5)
            break

    print(f'=-' * 50)
    print('1 - Voltar ao rio')
    print('2 - Pegar o trem para casa')
    opc = int(input('Input: '))

    if opc == 1:
        sleep(2)
        print(f'=-' * 50)
        sleep(1)
        print('-=+> Pensamento <+=-')
        sleep(1)
        print('Acho que é melhor eu não ir lá.')
        sleep(2)
        print('Mike irá ficar raivoso comigo, e então acho que é melhor não ir.')
        sleep(2)
        print('Acho que é melhor virar e voltar à Ghostborne antes que algo aconteça...')
        sleep(2)
        print(f'=-' * 50)

    if opc == 2:
        sleep(2)
        print(f'=-' * 50)
        sleep(3)
        print('Pegaste o trem para casa com sucesso. Todos comemoraram com a sua volta.')
        sleep(3)
        print(f'=-' * 50)
        sleep(2)
        print('PROJETO FINAL-AULAS PYTHON, SHARKCODERS')
        sleep(2)
        print(f'=-' * 50)
        sleep(5)

    sleep(3)
    print('E assim ficou por muito tempo. O Mike não queria que você se alejasse, então, decides voltar para casa após disto tudo.')
    sleep(4)
    print(f'=-' * 50)
    sleep(2)
    print('PROJETO FINAL-AULAS PYTHON, SHARKCODERS')
    sleep(2)
    print(f'=-' * 50)
    sleep(5)

def ghostborne_fim_2():
    global rndm1, rndm2
    from time import sleep
    while True:
        print(f'=-' * 50)
        print('1 - Voltar ao rio')
        print('2 - Ir para o casino')
        print('3 - Pegar o trem para casa')
        opc = int(input('Input: '))

        if opc == 1:
            print(f'=-' * 50)
            sleep(2)
            print('-=+> Pensamento <+=-')
            sleep(1)
            print('Vá lá, não veja, Mike!')
            sleep(2)
            print('O rio está com correntes fortes... Ugh!')
            sleep(2)
            print('Acho que é melhor eu me despachar antes que o Mike me veja e dê-me em sarilhos...')
            sleep(2)
            print(f'=-' * 50)
            sleep(2)
            ghostborne_boss_rio2()
            break

        if opc == 2:
            casino(opc)
            break

        if opc == 3:
            sleep(2)
            print(f'=-' * 50)
            sleep(3)
            print('Pegaste o trem para casa com sucesso. Todos comemoraram com a sua volta.')
            sleep(3)
            print(f'=-' * 50)
            sleep(2)
            print('PROJETO FINAL-AULAS PYTHON, SHARKCODERS')
            sleep(2)
            print(f'=-' * 50)
            sleep(5)
            break

    print('1 - Continuar a jornada até o outro lado do rio')
    print('2 - Pegar o trem para casa')
    opc = int(input('Input: '))

    if opc == 1:
        sleep(2)
        print(f'=-' * 50)
        sleep(1)
        print('-=+> Pensamento <+=-')
        sleep(1)
        print('Será que devo ir lá?')
        sleep(2)
        print('Bem, se sobrevivi um animal cinco vezes o meu tamanho, porque não?')
        sleep(2)
        print(f'=-' * 50)
        sleep(1)
        ghostborne_boss_rio_final3()
        sleep(2)
        print(f'=-' * 50)
        sleep(1)
        print('-=+> Alguém? <+=-')
        sleep(1)
        print('Você fez muito bem. Estou feliz.')
        sleep(2)
        print('Salvaste Ghostborne da sua maldição. Podes continuar com felicidade.')
        sleep(2)
        print(f'=-' * 50)
        sleep(2)
        print('PROJETO FINAL-AULAS PYTHON, SHARKCODERS')
        sleep(2)
        print(f'=-' * 50)
        sleep(5)

    if opc == 2:
        sleep(2)
        print(f'=-' * 50)
        sleep(3)
        print('Pegaste o trem para casa com sucesso. Todos comemoraram com a sua volta.')
        sleep(3)
        print(f'=-' * 50)
        sleep(2)
        print('PROJETO FINAL-AULAS PYTHON, SHARKCODERS')
        sleep(2)
        print(f'=-' * 50)
        sleep(5)

def ghostborne_fim_3():
    global rndm1, rndm2
    from time import sleep
    while True:
        print(f'=-' * 50)
        print("1 - Entrar numa galeria d'artes")
        print('2 - Ir para uma construção sem nome.')
        print('3 - Pegar o trem para casa')
        opc = int(input('Input: '))

        if opc == 1:
            sleep(2)
            print(f'=-' * 50)
            sleep(3)
            print('O lugar estava cheio de pessoas à ver as pinturas famosas.')
            sleep(3)
            print(f'=-' * 50)
            sleep(2)
            print('-=+> Pensamento <+=-')
            sleep(1)
            print('Uh, aqui é demasiado enorme...')
            sleep(2)
            print('Será que devo ir embora?')
            sleep(3)
            print('Mhm, acho que é melhor antes de não saber onde é a saida.')
            sleep(2)
            break

        if opc == 2:
            casino(opc)
            break

        if opc == 3:
            sleep(2)
            print(f'=-' * 50)
            sleep(3)
            print('Pegaste o trem para casa com sucesso. Todos comemoraram com a sua volta.')
            sleep(3)
            print(f'=-' * 50)
            sleep(2)
            print('PROJETO FINAL-AULAS PYTHON, SHARKCODERS')
            sleep(2)
            print(f'=-' * 50)
            sleep(5)
            break

    print(f'=-' * 50)
    sleep(1)
    print('E assim ficou por bastante tempo.')
    sleep(1)
    print('Você só ficava fazendo o que o Mike colocava.')
    sleep(2)
    print('E Ghostborne tinha uma maldição de azar,\n que então trouxe a cidade um presente inesperado.')
    sleep(1)
    print(f'=-' * 50)

    sleep(2)
    print('-=+> Você <+=-')
    sleep(1)
    print('Uhm, Mike, o que é aquela coisa no céu?')
    sleep(2)
    print('-=+> Mike <+=-')
    sleep(1)
    print('Ah, Deus, não!')
    sleep(3)
    print(f'=-' * 50)
    sleep(2)
    print('PROJETO FINAL-AULAS PYTHON, SHARKCODERS')
    sleep(2)
    print(f'=-' * 50)
    sleep(5)

# jogo dos fins

def casino(opc):
    from time import sleep
    from random import randint
    if opc == 2:
        sleep(2)
        print(f'=-' * 50)
        sleep(3)
        print('-=+> Mestre <+=-')
        sleep(2)
        print('Bem vindo ao casino de Ghostborne!')
        sleep(1)
        print('Por favor, selecione um jogo:')
        sleep(2)
        listjogo = ['Roulette', 'Lucky draw', 'Number disaster']
        jogo1 = randint(0, 2)
        jogo2 = randint(0, 2)
        print(f'=-' * 50)
        print(f'1 - {listjogo[jogo1]}')
        print(f'2 - {listjogo[jogo2]}')
        opc = int(input('Input: '))

        if opc == 1:
            if jogo1 == 0:
                roleta()
            if jogo1 == 1:
                luckydraw()
            if jogo1 == 2:
                number()

        if opc == 2:
            if jogo2 == 0:
                roleta()
            if jogo2 == 1:
                luckydraw()
            if jogo2 == 2:
                number()

def roleta():
    from time import sleep
    from random import randint
    sleep(1)
    print(f'=-' * 50)
    print('Bem vindo à roleta!\nO jogo funciona da seguinte maneira:\nVocê escolhe um numero e prima ENTER para começar a roleta,\ne se um dos números escolhidos for igual, ganhas 10 pontos!')
    sleep(2)
    num1 = int(input('Selecione o 1º número: '))
    num2 = int(input('Selecione o 2º número: '))
    input('Prima ENTER: ')
    sleep(4)
    print(f'=-' * 50)
    rndm1 = randint(0, 9)
    rndm2 = randint(0, 9)
    for x in range(1, 3):
        print(f'[{rndm1}] [{rndm2}]')

    if num1 == rndm1 or num2 == rndm1:
        sleep(1)
        print(f'=-' * 50)
        print('Você ganhou 10 pontos!')
        sleep(0.5)
        print("=-" * 20)
        sleep(0.5)

    if num1 == rndm1 and num2 == rndm1 or num1 == rndm2 and num2 == rndm2:
        sleep(1)
        print(f'=-' * 50)
        print('Você ganhou 10 pontos!')
        sleep(0.5)
        print("=-" * 20)
        sleep(0.5)

    if num1 == rndm1 and num2 == rndm2 and num1 == rndm2 and num2 == rndm1:
        sleep(1)
        print(f'=-' * 50)
        print('Você ganhou 50 pontos!')
        sleep(0.5)
        print("=-" * 20)
        sleep(0.5)

    if num1 != rndm1 and num2 != rndm1 and num1 != rndm2 and num2 != rndm2:
        sleep(1)
        print(f'=-' * 50)
        print('Você ganhou ganhou nada! Hahaha!')
        sleep(0.5)
        print("=-" * 20)
        sleep(0.5)

def luckydraw():
    from random import randint
    from time import sleep
    py = randint(1, 49 + 1)
    escolha = int(input("Escolha um numero de 1 a 50 e teste a sua sorte!\nInput:"))
    sleep(0.5)
    print("=-" * 20)
    sleep(0.5)
    tent = 0
    while True:
        tent += 1
        if tent == 3:
            print("Ja se foram as tentativas!")
            sleep(0.5)
            print("Foi uma boa rodada.")
            print(f"O numero era {py}.")
            sleep(0.5)
            print("=-" * 20)
            sleep(0.5)
            sleep(0.5)
            break
        if escolha == py:
            print("Nossa senhora! Tu acertaste o numero!\nBem, pelo menos es sortudo...")
            sleep(0.5)
            print("=-" * 20)
            sleep(0.5)

        if escolha != py:
            print(f"Bem, quem esperava em acertares o numero... mais tentativas!")
            sleep(0.5)
            print("=-" * 20)
            sleep(0.5)

        escolha = int(input("Input:"))
        sleep(0.5)
        print("=-" * 20)
        sleep(0.5)

def number():
    from random import randint
    from time import sleep
    for x in range(1, 5+1):
        num = randint(1, 100)
        sleep(1)
        print(f'=-' * 50)
        sleep(1)
        print('1 - Par\n2 - Impar')
        opc = int(input('Selecione entre par ou ímpar: '))
        if opc == 1:
            if num % 2 == 0:
                print('Acertaste o input!')
                print(f'O número era: {num}')
            if num % 2 == 1:
                print('Aw, tu eraste o input...')
                print(f'O número era: {num}')

        if opc == 2:
            if num % 2 == 1:
                print('Acertaste o input!')
                print(f'O número era: {num}')
            if num % 2 == 0:
                print('Aw, tu eraste o input...')
                print(f'O número era: {num}')
        y = x - 6
        print(f'Mais {y} tentativas!')

    sleep(0.5)
    print("=-" * 20)
    sleep(0.5)

# bosses

def ghostborne_boss_rio():
    from time import sleep
    from random import randint
    print('-=+> Pensamento <+=-')
    sleep(1)
    print('Calma, o que é esta árvore tão enorme?')
    print(f'=-' * 50)
    sleep(3)
    print('Dentro da árvore parece ter um buraco. Está escuro, então decides acender um esqueiro para ver melhor.')
    sleep(2)
    print(f'=-' * 50)
    sleep(2)
    boss = randint(0, 1)
    bosses = ['pássaro', 'morcego']
    print(f'Um {bosses[boss]} enorme apareceu!')
    sleep(2)
    print(f'=-' * 50)
    sleep(2)
    vdaranha = 100
    vdpers = 100
    while True:
        pntp = randint(20, 50)
        scprns = randint(10, 25)
        lanc = randint(75, 90)
        atqaranha = randint(1, 45)
        print('1 - Pontapé')
        print('2 - Soco nas pernas')
        print('3 - Lançar seu esqueiro')
        print('4 - Desvio')
        opc = int(input('Input: '))
        print(f'=-' * 50)
        sleep(2)

        # ataques
        if opc == 1:
            print(f'Você deu um pontapé na barriga do {bosses[boss]}!')
            sleep(2)
            vdaranha -= pntp
            print(f'O {bosses[boss]} agora tem', vdaranha, 'de vida!')
            if vdaranha <= 0:
                print(f'Você derrubou o {bosses[boss]}!')
                print(f'=-' * 50)
                sleep(2)
                break
            print(f'=-' * 50)
            sleep(2)
        if opc == 2:
            print(f'Você deu um soco nas pernas do {bosses[boss]}!')
            sleep(2)
            vdaranha -= scprns
            print(f'O {bosses[boss]} agora tem', vdaranha, 'de vida!')
            if vdaranha <= 0:
                print(f'Você derrubou o {bosses[boss]}!')
                print(f'=-' * 50)
                sleep(2)
                break
            print(f'=-' * 50)
            sleep(2)
        if opc == 3:
            print(f'Você lançou seu esqueiro no {bosses[boss]}!')
            sleep(2)
            vdaranha -= lanc
            print(f'O {bosses[boss]} agora tem', vdaranha, 'de vida!')
            if vdaranha <= 0:
                print(f'Você derrubou o {bosses[boss]}!')
                print(f'=-' * 50)
                sleep(2)
                break
            print(f'=-' * 50)
            sleep(2)
        if opc == 1 or opc == 2:
            vdpers -= atqaranha
            print(f'O {bosses[boss]} deu um hit em você! Agora tens', vdpers, 'de vida!')
            print(f'=-' * 50)
            sleep(2)
            if vdpers <= 0:
                print('Você está com pouca vida e decide fugir.')
                print(f'=-' * 50)
                sleep(2)
                break
        if opc == 4:
            print(f'Você desviou o ataque do {bosses[boss]}!')
            sleep(2)
            print('Continuas com', vdpers, 'de vida.')
            print(f'=-' * 50)
            sleep(2)

def ghostborne_boss_rio2():
    from time import sleep
    from random import randint
    print('-=+> Pensamento <+=-')
    sleep(1)
    print('Já estou cansado... Quem me dera estar gordo!')
    print(f'=-' * 50)
    sleep(3)
    print('Já estás no meio do rio.')
    sleep(2)
    print('É muito fundo.')
    sleep(2)
    print(f'=-' * 50)
    sleep(2)
    boss = randint(0, 1)
    bosses = ['peixe', 'crocodilo']
    print(f'Um {bosses[boss]} gigante surgiu!')
    sleep(2)
    print(f'=-' * 50)
    sleep(2)
    vdaranha = 150
    vdpers = 110
    while True:
        pntp = randint(30, 70)
        scprns = randint(10, 25)
        atqaranha = randint(10, 50)
        print('1 - Pontapé')
        print('2 - Soco nas pernas')
        print('3 - Desvio')
        opc = int(input('Input: '))
        print(f'=-' * 50)
        sleep(2)

        # ataques
        if opc == 1:
            print(f'Você deu um pontapé na barriga do {bosses[boss]}!')
            sleep(2)
            vdaranha -= pntp
            print(f'O {bosses[boss]} agora tem', vdaranha, 'de vida!')
            if vdaranha <= 0:
                print(f'Você derrubou o {bosses[boss]}!')
                print(f'=-' * 50)
                sleep(2)
                break
            print(f'=-' * 50)
            sleep(2)
        if opc == 2:
            print(f'Você deu um soco nas pernas do {bosses[boss]}!')
            sleep(2)
            vdaranha -= scprns
            print(f'O {bosses[boss]} agora tem', vdaranha, 'de vida!')
            if vdaranha <= 0:
                print(f'Você derrubou o {bosses[boss]}!')
                print(f'=-' * 50)
                sleep(2)
                break
            print(f'=-' * 50)
            sleep(2)
        if opc == 1 or opc == 2:
            vdpers -= atqaranha
            print(f'O {bosses[boss]} deu um hit em você! Agora tens', vdpers, 'de vida!')
            print(f'=-' * 50)
            sleep(2)
            if vdpers <= 0:
                print('Você está com pouca vida e decide fugir.')
                print(f'=-' * 50)
                sleep(2)
                break
        if opc == 3:
            print(f'Você desviou o ataque do {bosses[boss]}!')
            sleep(2)
            print('Continuas com', vdpers, 'de vida.')
            print(f'=-' * 50)
            sleep(2)

def ghostborne_boss_rio_final3():
    from time import sleep
    from random import randint
    print('-=+> Pensamento <+=-')
    sleep(1)
    print('Acho que essa brincadeira me deixou cansado...')
    print(f'=-' * 50)
    sleep(1)
    print('Quando chegas do outro lado, tem uma floresta enorme. Decides investigar.')
    sleep(3)
    print(f'=-' * 50)
    sleep(2)
    boss = randint(0, 1)
    bosses = ['cobra', 'jiboia']
    print(f'Uma {bosses[boss]} gigante surgiu!')
    sleep(2)
    print(f'=-' * 50)
    sleep(2)
    vdaranha = 160
    vdpers = 140
    while True:
        pntp = randint(30, 70)
        scprns = randint(10, 25)
        atqaranha = randint(10, 50)
        print('1 - Pontapé')
        print('2 - Soco nas pernas')
        print('3 - Desvio')
        opc = int(input('Input: '))
        print(f'=-' * 50)
        sleep(2)

        # ataques
        if opc == 1:
            print(f'Você deu um pontapé na barriga da {bosses[boss]}!')
            sleep(2)
            vdaranha -= pntp
            print(f'A {bosses[boss]} agora tem', vdaranha, 'de vida!')
            if vdaranha <= 0:
                print(f'Você derrubou a {bosses[boss]}!')
                print(f'=-' * 50)
                sleep(2)
                break
            print(f'=-' * 50)
            sleep(2)

        if opc == 2:
            print(f'Você deu um soco nas pernas da {bosses[boss]}!')
            sleep(2)
            vdaranha -= scprns
            print(f'A {bosses[boss]} agora tem', vdaranha, 'de vida!')
            if vdaranha <= 0:
                print(f'Você derrubou a {bosses[boss]}!')
                sleep(2)
                break
            print(f'=-' * 50)
            sleep(2)

        if opc == 1 or opc == 2:
            vdpers -= atqaranha
            print(f'A {bosses[boss]} deu um hit em você! Agora tens', vdpers, 'de vida!')
            print(f'=-' * 50)
            sleep(2)
            if vdpers <= 0:
                print('Você foi morto infelizmente.')
                sleep(1)
                print('Todos vão lembrar de ti e dos momentos bons contigo.')
                sleep(3)
                break

        if opc == 3:
            print(f'Você desviou o ataque da {bosses[boss]}!')
            sleep(2)
            print('Continuas com', vdpers, 'de vida.')
            print(f'=-' * 50)
            sleep(2)
