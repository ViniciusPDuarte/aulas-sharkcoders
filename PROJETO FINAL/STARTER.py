def starter():
    lista_nome = ['Farlight', 'Ghostborne']
    from random import randint
    from time import sleep

    # games vvv
    import farlight
    import ghostborne

    print(f'=-'*50)
    sleep(1)
    nome = randint(0, 1)
    print(lista_nome[nome])
    sleep(1)
    print(f'=-'*50)
    sleep(1)

    if nome == 0:
        farlight.farlight()

    if nome == 1:
        ghostborne.ghostborne()

starter()
