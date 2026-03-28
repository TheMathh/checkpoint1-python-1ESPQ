#Checkpoint 1 - Mateus Alves Borges

ajuda = str(input("Você quer que a câmera da JOVI faça ajustes automáticos para ajudar nessa captura? Responda sim ou nao."))

importancia = str(input("Essa captura é importante para estudo, trabalho, compartilhamento ou registro com outras pessoas? Responda sim ou nao."))

dificuldade = int(input("Como você avalia a dificuldade desta cena? Digite 1 para dificuldade baixa, 2 para dificuldade média ou 3 para dificuldade alta: "))

tentativas = int(input("Quantas tentativas você já fez para conseguir uma boa foto nessa situação? Digite apenas um número: "))


if ajuda == "nao":
    classificacao = "Modo padrão."
    acao_sistema = "O programara manterá interface simples e seguirá com uma captura comum"

elif ajuda == "sim" and dificuldade == 3 and importancia == "sim":
    classificacao = "Modo Inteligente Primário"
    acao_sistema = "O programa ativará a recomendação avançada de apoio à captura"

elif ajuda == "sim" and importancia == "sim" and dificuldade == 3 and tentativas >= 5:
    classificacao = "Ajuste Recomendado"
    acao_sistema = "O sistema irá sugerir recurso apropriado para melhorar o resultado"

else:
    classificacao = "Captura guiada"
    acao_sistema = "O sistema irá exibir orientação básica para o usuário antes da foto"

print("Classificação:", classificacao)
print("Ação sistema:", acao_sistema)