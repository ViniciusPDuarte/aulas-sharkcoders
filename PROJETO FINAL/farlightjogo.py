def farlight():
    from time import sleep
    from random import randint
    sleep(1)
    # inicio
    print('-=+> Britte <+=-')
    f1 = ['Bem vindo à Farlight. Um lugar temido.', 'Seja bem-vindo à esta aldeia chamada Farlight. Agradecimentos.']
    r1 = randint(0, 1)
    print(f1[r1])
    sleep(3)
    print('Eu sei que aqui é um lugar pequeno, mas não deixe este olhar te enganar.')
    sleep(3)
    f1 = ['Aqui será divertido, ambo do jeito assustador, e do je-', 'Tenha cuidado onde pisas.', 'Já tive muitos casos aterrorizantes aqui.']
    r1 = randint(0, 2)
    print(f1[r1])
    sleep(3)
    print(f'=-' * 50)
    print('1 - Como assim? Eu fui para um lugar perigoso sem saber?')
    print('2 - Ou seja, eu posso morrer em qualquer sítio?')
    print('3 - Ah, não...')
    print('4 - [Continue a conversa]')
    opc = int(input('Input: '))

    if opc == 1:
        sleep(1)
        print(f'=-' * 50)
        print('-=+> Você <+=-')
        sleep(1)
        print('Como assim, Britte? Eu fui para um lugar perigoso sem saber?')
        sleep(1)
        print('-=+> Britte <+=-')
        sleep(1)
        print('Não, não é isso... ')
        sleep(2)
        print('É difícil de explicar á pessoas como você; não estou a falar\nque és burro, não, mas... é algo complicado.')
        sleep(4)

    if opc == 2:
        sleep(1)
        print(f'=-' * 50)
        print('-=+> Você <+=-')
        sleep(1)
        print('Então, eu posso morrer em algures?')
        sleep(1)
        print('-=+> Britte <+=-')
        sleep(1)
        print('Depende em este "algures": ')
        sleep(2)
        print('Tem lugares que realmente podes falecer, e outros praticamente impossivéis de fazer tal coisa.')
        sleep(4)

    if opc == 3:
        sleep(1)
        print(f'=-' * 50)
        print('-=+> Você <+=-')
        sleep(1)
        print('Ai, isto não é bom... Ah, não.')
        sleep(1)
        print('-=+> Britte <+=-')
        sleep(1)
        print('Acalma-te, rapaz! O mundo não vai acabar!')

    if opc == 4:
        sleep(1)
        print(f'=-' * 50)
        sleep(1)
        print('-=+> Britte <+=-')
        sleep(1)
        print('E repito, só tem cuidado onde pisas, ok?')
        sleep(2)

    # livre
    sleep(1)
    print(f'=-' * 50)
    print('Agora estás livre. ')
    print(f'=-' * 50)
    sleep(3)

    # boss???
    while True:
        f1 = ['Entrar no museu de música', 'Entrar na loja de instrumentos músicais']
        r1 = randint(0, 1)
        print(f'1 - {f1[r1]}')
        print('2 - Caminhar até a montanha')
        print('3 - Interagir com algo do chão prateado')
        opc = int(input('Input: '))

        if opc == 1:
            sleep(1)
            print(f'=-' * 50)
            print('-=+> Pensamento <+=-')
            sleep(3)
            print('Olha só, até parece a minha guitarra antiga!\nMas está demasiado caro, meu deus... também, para quem iria tocar a \nguitarra no meio do deserto?')
            sleep(3)
            print(f'=-' * 50)

        if opc == 2:
            print(f'=-' * 50)
            sleep(3)
            farlight_boss_mtnh()
            break

        if opc == 3:
            print(f'=-' * 50)
            print('-=+> Pensamento <+=-')
            sleep(1)
            print('Esta moeda está-me a dizer para ir á montanha ao fundo.')
            sleep(2)
            print('Vou ver o que se passa lá...')
            sleep(2)
            print(f'=-' * 50)
            sleep(3)
            print('Já estás cansado, mas chegaste ao pé da montanha gigante.')
            sleep(2)
            print(f'=-' * 50)
            sleep(2)
            farlight_boss_mtnh()
            break

    # pós boss
    print('-=+> Britte <+=-')
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
        print('-=+> Britte <+=-')
        sleep(1)
        print('Boa! Continue assim!')
        sleep(2)
        farlight_fim_1()

    if opc == 2:
        sleep(1)
        print(f'=-' * 50)
        print('-=+> Você <+=-')
        sleep(1)
        print('Ok, Britte...')
        sleep(1)
        print('-=+> Britte <+=-')
        sleep(1)
        print('Ei, não fales assim, as coisas não são como parecem!')
        sleep(2)
        print('Você provavelmente irá acabar num cemitério se não fazer o que falo.')
        sleep(2)
        print('Só estou a falar, também podes ir fazer estas coisas ridículas.')
        sleep(3)
        farlight_fim_2()

    if opc == 3:
        sleep(1)
        print(f'=-' * 50)
        sleep(1)
        print('-=+> Britte <+=-')
        sleep(1)
        print('E estou a falar á sério.')
        sleep(2)
        farlight_fim_1()

# fins

def farlight_fim_1():
    global rndm1, rndm2
    from time import sleep
    while True:
        print(f'=-' * 50)
        print('1 - Entrar num bar')
        print('2 - Ir para o casino')
        print('3 - Pegar o trem para casa')
        opc = int(input('Input: '))

        if opc == 1:
            sleep(2)
            print(f'=-' * 50)
            sleep(3)
            print('Havia muitas pessoas bebadas. O verão já estáva aí, então está é uma razão...')
            sleep(3)
            print(f'=-' * 50)
            sleep(2)
            print('-=+> Pensamento <+=-')
            sleep(1)
            print('Eles estão loucos, de certeza. Jesus Cristo!')
            sleep(2)
            print('Pelo menos não estou que nem á eles!')
            sleep(2)
            print('Acho que é melhor eu sair daqui antes que algo aconteça...')
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
    print('1 - Voltar à montanha')
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
        print('A Britte irá ficar raivosa comigo, e então acho que é melhor não ir.')
        sleep(2)
        print('Acho que é melhor virar e voltar à Farlight antes que algo aconteça...')
        sleep(2)

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
    print('E assim ficou por muito tempo. A Britte não queria que você se alejasse, então, decides voltar para casa após disto tudo.')
    sleep(4)
    print(f'=-' * 50)
    sleep(2)
    print('PROJETO FINAL-AULAS PYTHON, SHARKCODERS')
    sleep(2)
    print(f'=-' * 50)
    sleep(5)

def farlight_fim_2():
    global rndm1, rndm2
    from time import sleep
    while True:
        print(f'=-' * 50)
        print('1 - Voltar à montanha')
        print('2 - Ir para o casino')
        print('3 - Pegar o trem para casa')
        opc = int(input('Input: '))

        if opc == 1:
            sleep(2)
            print(f'=-' * 50)
            sleep(3)
            print('Pensaste 2 vezes, e ainda decides fazer o ruim.')
            sleep(3)
            print(f'=-' * 50)
            sleep(2)
            print('-=+> Pensamento <+=-')
            sleep(1)
            print('Deus me abençoe agora!')
            sleep(2)
            print('A montanha está escorregadia...')
            sleep(2)
            print('Acho que é melhor eu me despachar antes que a Britte me veja e algo aconteça...')
            sleep(2)
            print(f'=-' * 50)
            sleep(2)
            farlight_boss_mtnh2()
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

    print('1 - Continuar a jornada até o outro lado da montanha')
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
        print('A Britte irá ficar raivosa comigo, e então acho que é melhor não ir.')
        sleep(2)
        print('Haha! Estou a brincar! Se sobrevivi um animal cinco vezes o meu tamanho, porque não?')
        sleep(2)
        print(f'=-' * 50)
        sleep(1)
        farlight_boss_mtnh_final3()
        sleep(2)
        print(f'=-' * 50)
        sleep(1)
        print('-=+> Alguém? <+=-')
        sleep(1)
        print('Você fez muito bem. Estou feliz.')
        sleep(2)
        print('Salvaste Farlight da sua maldição. Podes continuar com felicidade.')
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

# jogos dos fins

def casino(opc):
    from time import sleep
    from random import randint
    if opc == 2:
        sleep(2)
        print(f'=-' * 50)
        sleep(3)
        print('-=+> Mestre <+=-')
        sleep(2)
        print('Bem vindo ao casino de Farlight')
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

def farlight_boss_mtnh():
    from time import sleep
    from random import randint
    print('-=+> Pensamento <+=-')
    sleep(1)
    print('Queria ter mais energia...\nEspere, o que é esta caverna?')
    print(f'=-' * 50)
    sleep(3)
    print('Dentro da caverna parece ter um ninho com seis ovos dentro. Está escuro, então decides acender um esqueiro.')
    sleep(2)
    print(f'=-' * 50)
    sleep(2)
    boss = randint(0, 2)
    bosses = ['rato venenoso', 'morcego', 'urso']
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

def farlight_boss_mtnh2():
    from time import sleep
    from random import randint
    print('-=+> Pensamento <+=-')
    sleep(1)
    print('Já estou cansado... Pelo menos cheguei ao topo!')
    print(f'=-' * 50)
    sleep(3)
    print('Lá tem uma cratera com algo brilhante dentro. Parece ser lava.')
    sleep(2)
    print('No fim, a curiosidade te leva. Decides tocar este objeto.')
    sleep(2)
    print(f'=-' * 50)
    sleep(2)
    boss = randint(0, 1)
    bosses = ['dragão', 'macaco']
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

def farlight_boss_mtnh_final3():
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
    bosses = ['cobra', 'aguia']
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
        pontos = 0
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
                pontos += 75
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
                pontos += 75
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

