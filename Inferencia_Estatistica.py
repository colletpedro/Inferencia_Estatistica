import random
import string

def gerador_senha(tamanho=12):
    # Definindo os caracteres que podem ser usados na senha
    letras_maiusculas = string.ascii_uppercase  # A-Z
    letras_minusculas = string.ascii_lowercase  # a-z
    numeros = string.digits  # 0-9
    caracteres_especiais = string.punctuation  # !@#$%^&*()

    # Combina todos os caracteres
    todos_os_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais

    # Gerando a senha aleatória
    senha = ''.join(random.choice(todos_os_caracteres) for _ in range(tamanho))
    return senha

# Solicitar o comprimento da senha ao usuário
tamanho = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = gerador_senha(tamanho)
print(f"Senha gerada: {senha_gerada}")
