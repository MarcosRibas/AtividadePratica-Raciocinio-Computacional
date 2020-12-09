def obter_limite():
    global credito
    global idade
    from datetime import date
    print('Esta é a Loja Destini, bem-vindo! Aqui quem fala é Marcos Ribas.')
    print('Precisamos fazer para você uma análise de crédito. Para isso precisamos de alguns de seus dados.')
    cargo = str(input('Por favor digite seu cargo: '))
    salario = float(input('Agora digite o seu salário: R$ '))
    ano = date.today().year
    nascimento = int(input('Para finalizar, digite o ano em que você nasceu: '))
    print(
        'Obrigado! Registramos suas informações. Seu cargo é {}, seu salário é de {:.2f}, e o ano de seu nascimento é {}.'.format(
            cargo, salario, nascimento))
    print('Estamos processando sua análise de crédito...')
    idade = ano - nascimento
    credito = salario * (idade / 1000) + 100
    print('Em 2020, você completa {} anos.'.format(idade))
    return credito


def verificar_produto():
    meu_nome_completo = ('Marcos Rafael Marcondes Ribas')
    meu_primeiro_nome = ('Marcos')
    caracteres = len(meu_nome_completo)
    desconto = len(meu_primeiro_nome)
    produto = str(input('Digite o nome do produto que você quer comprar: '))
    preço = float(input('Digite o valor do produto que você deseja comprar:R$ '))
    if preço <= credito * 60 / 100:
        print('Liberado!')
    elif preço >= credito * 61 / 100 and preço < credito * 90 / 100:
        print('Liberado! Você pode parcelar em até duas vezes')
    elif preço >= credito * 90 / 100 and preço <= credito * 100 / 100:
        print('Liberado! você pode parcelar em três vezes ou mais vezes')
    else:
        print('Bloqueado')
    if preço >= caracteres and preço < idade or preço <= caracteres and preço > idade:
        print('Você ganhou o desconto de: {}%'.format(preço - desconto))


print('------------ LOJA DESTINI---------------')
obter_limite()
print('E o seu crédito de compra é de: {:.2f} '.format(credito))
print('----------- VERIFICAÇÃO DE PRODUTO -----------')
quantidade = int(input('Digite quantos produtos você deseja cadastrar: '))
for quantidade in range(quantidade):
    verificar_produto()
print('FIM')
