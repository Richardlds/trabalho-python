while True:
    marmita = str(input("Digite o tamanho da marmita (p) (m) (g): "))
    type(marmita)
    numero = int
    marmita=str
    type(numero)
    if numero =='p':
        input("Sua marmita é P valor R$12,00")
    elif numero =='m':
        print("Sua marmita é M valor R$14,00")
    elif numero =='g':
        print("Sua marmita é G valor R$16,00")
    else:
        ("Tamanho de marmita inexistente escolha os tamanhos: P ou M ou G")
    lugar = list(input("Sua moradia fica aonde: "))
    type(lugar)
    lugar=list(lugar)
    print("Escolha a loja aonde você deseja retirar seu produto.")
    lojas = ('1-Neves', '2-Belo Horizonte','3-Matozinhos','4-Vespaziano','5-Brumadinho','6-Sair da Loja')
    for i in range(len(lojas)):
        print(lojas[i])
    lojas=int(input("Desejo retirar na loja: "))
    match lojas:
        case 1:
            print("Você escolheu a nossa loja de Neves. ")
            print("Nessa loja temos as opçoes: tropeiro, macarrão, estrogonoff.")
            neves = ['tropeiro', 'macarrao' , 'estrogonoff']
            print(neves[0],"(Preço adicional R$3,00)",neves[1],"(Preço adicional R$2,00)",neves[2],"(Preço adicional R$4,00)")
        case 2: 
            print("Você escolheu a nossa loja de Belo Horizonte. ")
            print("Nessa loja temos as opçoes: tropeiro, macarrão, estrogonoff.")
            belohorizonte = ['tropeiro','macarrão','estrogonoff']
            print(belohorizonte[0],"(Preço adicional R$3,00)",belohorizonte[1],"(Preço adicional R$2,00)",belohorizonte[2],"(Preço adicional R$4,00)")
        case 3:
            print("Você escolheu a nossa loja de Matozinhos. ")
            print("Nessa loja temos as opçoes: tropeiro, macarrão, estrogonoff.")
            matozinhos = ['tropeiro','macarrão','estrogonoff']
            print(matozinhos[0],"(Preço adicional R$3,00)",matozinhos[1],"(Preço adicional R$2,00)",matozinhos[2],"(Preço adicional R$4,00)")
        case 4:
            print("Você escolheu a nossa loja de Vespaziano. ")
            print("Nessa loja temos as opçoes: tropeiro, macarrão, estrogonoff.")
            vespaziano = ['tropeiro','macarrão','estrogonoff']
            print(vespaziano[0],"(Preço adicional R$3,00)",vespaziano[1],"(Preço adicional R$2,00)",vespaziano[2],"(Preço adicional R$4,00)")
        case 5:
            print("Você escolheu a nossa loja de Brumadinho. ") 
            print("Nessa loja temos as opçoes: tropeiro, macarrão, estrogonoff.")
            brumadinho = ['tropeiro','macarrão','estrogonoff']
            print(brumadinho[0],"(Preço adicional R$3,00)",brumadinho[1],"(Preço adicional R$2,00)",brumadinho[2],"(Preço adicional R$4,00)")
        case 6:
            print("Sair da loja")
            break
        
    
print("Vai ficar com fome!!")