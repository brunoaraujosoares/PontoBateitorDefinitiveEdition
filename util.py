# testa se o arquivo de configurações existe
def testa_arquivo(filePath='variaveis.py'):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        print('O arquivo de configuração não foi encontrado.')
        if criar_arquivo(filePath):
            return True
        else:
            return e
    
#cria o arquivo de configurações
def criar_arquivo(filePath):
    print('Criando o arquivo de configuração.')
    processo = leia_numero_processo()
    with open(filePath, 'a') as f:
        saida = '# Texto que será inserido no campo de texto de evento externo\n'
        saida+= f'texto = \'Trabalho remoto. Processo SEI n, {processo}.\'\n'
        f.write(saida)
    return True

# input para ler o número do processo            
def leia_numero_processo():
    while True:
        processo = str(input('Digite o número do processo de Trabalho Remoto: ')).strip()
        if valida_processo(processo):
            return processo
        else:
            print('Número de processo inválido.')

# validar o nº do processo
def valida_processo(processo):
    # TODO: fazer expressão regular para validar o número do processo
    # 53542.001640/2020-28
    if '53542.' not in processo:
        return False
    else:
        return True
    
# testa se o elemento HTML já foi carregado
def elementoExiste(valor):
    try:
        driver.find_element_by_id(valor)
    except NoSuchElementException:
        return False
    return True

def escreve_arquivo(url, filePath='variaveis.py'):
    with open(filePath, 'a') as f:
        f.write(f'painel_do_servidor = \'{url}\'' + '\n')