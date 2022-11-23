def porcentagem (respostas_certas,quant_perguntas):
  return  ((respostas_certas/quant_perguntas)*100)


print()
print()
print()
print("                    :!@:                         !!#@@#!.                                                               ")
print("                  !@@@@@   .!@@:               !@@@@@@@@@!.                    :@@#.                                    ")
print("                 !@@@@@@!  !@@@@              @@@@@@@@@@@@#.                   @@@@#                                    ")
print("                :@@@@@##!  :@@@@             @@@@@@@@@@@@@@@.                  @@@@#                                    ")
print("                !@@@@#      !##:      ..    !@@@@@#: .#@@@@@@                  .###                                     ")
print("                !@@@@#      ....    .@@@@   @@@@@#     .@@@@@.  ....    .....  .....  .:........                        ")
print("                !@@@@@     !@@@@   #@@@@@! .@@@@#       #@@@@:  @@@@:   @@@@#  @@@@#  :@@@@@@@@@!                       ")
print("                 #@@@@@    :@@@@  :@@@@@.  #@@@@!        @@@@!  @@@@:   @@@@#  @@@@#  @@@@@@@@@@!                       ")
print("                  @@@@@@   :@@@@  :@@@@    #@@@@!        @@@@! !@@@@:   @@@@#  @@@@#  @@@@@@@@@@!                       ")
print("                   #@@@@!  :@@@@  :@@@@#   !@@@@!        @@@@: #@@@@:   @@@@#  @@@@#  .   #@@@@:                        ")
print("                   !@@@@@  :@@@@   :@@@@#   @@@@#       #@@@@: #@@@@:   @@@@#  @@@@#     #@@@@:                         ")
print("                   #@@@@@  :@@@@    :@@@@:  #@@@@!     :@@@@@. !@@@@:   @@@@#  @@@@#    #@@@@:                          ")
print("                 .!@@@@@#  :@@@@     @@@@!  :@@@@@@!!!#@@@@@!  .@@@@!  :@@@@#  @@@@#  !@@@@@.  .:                       ")
print("                @@@@@@@@:  :@@@@  ::#@@@@!   !@@@@@@@@@@@@@@    @@@@@@@@@@@@#  @@@@# :@@@@@@@@@@#                       ")
print("                !@@@@@@.   :@@@@  #@@@@@#     !@@@@@@@@@@@#     #@@@@@@@@@@@#  @@@@#  @@@@@@@@@@!                       ")
print("                @@@@!     :@@@@  .@@@@#    O   .#@@@@@@@#.      .#@@@@# @@@@#  @@@@# .@@@@@@@@@@!                       ")
print("                 :#:               .!.            #@@@@                                                                 ")
print("                                                  #@@@@#                                                                ")
print("                                                  #@@@@@@                                                               ")
print("                                                                                                                        ")
print("                                                                                                                        ")
print("                                                                                                                        ")
print("                                           .#@@@@@!.           ..#@@@@@!.                                               ")
print("                                         :@@@@@@@@@@!         .@@@@@@@@@@:                                              ")
print("                                         :@@@@@@@@@@@.        .@@@@@@@@@@@.                                             ")
print("                                         .@@@: #@@@@@:        .@@#. #@@@@@.                                             ")
print("                                          !     :@@@@:        .!     :@@@@.                                             ")
print("                                                :@@@@.               .@@@@.                                             ")
print("                                                #@@@#                @@@@#                                              ")
print("                                               !@@@#                !@@@#                                               ")
print("                                              !@@@@.     .!.       #@@@#                                                ")
print("                                             !@@@@.     !@@@!     !@@@@.                                                ")
print("                                          .:!@@@@##@@@::@@@@@: .:!@@@@###@@:                                            ")
print("                                         :@@@@@@@@@@@@::@@@@@:.@@@@@@@@@@@@:                                            ")
print("                                          @@@@@@@@@@@@:.@@@@@..@@@@@@@@@@@@:                                            ")
print("                                          ###########@:  #@#.  ###########@:                                            ")
print()


#dicionários dentro de dicionários



perguntas = {                

     '---PORTUGUÊS--- \n'

     'pergunta1 :\n': {
        'pergunta':'\n Esta vida é uma viagem \n pena eu estar \n só de passagem \n'' (Paulo Leminki) \n''No poema, o poeta lamenta-se: \n',

        'resposta':{ 'a':'da fugacidade da vida','b': 'revolta-se contra seu destino','c': 'sugere que a vida não tem sentido', 'd': 'abomina a agitação da vida ' },
        'resposta_certa': 'a',
    },
    '---CÁLCULO--- \n'
    'pergunta2 \n': {
    
        'pergunta': '\n A integrau da função, ∫ x^7 dx :',

        'resposta':{ 'a':'7x^7/7+C ','b': 'x^8/8+C','c': '7x/7+C', 'd': '7x^8+C' },
        'resposta_certa': 'b',  
    },
    '---INGLÊS--- \n'
    'pergunta3 \n': {
    
        'pergunta': '\n Qual é a estratégia de leitura rápida :',

        'resposta':{ 'a':'Scanning ','b': 'Main idea', 'c': 'Skimming', 'd': 'Nominal groups' },
        'resposta_certa': 'c',  
    },
    '---METÓDOS E TECNICAS DE PESQUISA--- \n'

    'pergunta4 \n': {
    
        'pergunta': '\n Quais as citações se enquadram no parâmetros da ABNT:',

        'resposta':{ 'a':'(NASCIMENTO,1996,p.123)','b': '(nascimento,1999,p.122)','c': '(NASCIMENTO,1999,P.12)', 'd': 'NASCIMENTO(1996,p.13)' },
        'resposta_certa': 'a',  
    },
    '---ORGANIZAÇÃO SISTEMAS E METODOS--- \n'

    'pergunta5 \n': {
    
        'pergunta': '\n A ferramneta que produz checklist adiminitrativo, prazos e responsabilidades por todos os envolvidos em um projeto:',

        'resposta':{ 'a':'5W2H ','b': 'diagrama de ishikawa','c': 'caban', 'd': 'WPA2' },
        'resposta_certa': 'a',  
    },
    '---LÓGICA E ALGORITMO DE PROGAMAÇÃO--- \n'
    'pergunta6 \n': {
        'pergunta': '\n I)  n1 = float(input("digite um numero: ")) \n'
                        'II)  n2 = float(input("digite outro numero: ")) \n'
                        'III) media = n1 + n2 / 2 \n'
                        'IV)  print(media) \n'

                        'Encontre o(s) erro(s) no código e marque a opção correta: ',

        'resposta':{ 'a':'I e III','b': 'IV','c':'III e II', 'd':'III' },
        'resposta_certa': 'd',  
    },
    '---GEOMETRIA ANALÍTICA---'
    'pergunta7 \n': {
        'pergunta': '\n Qual a condição para encontrar a  matriz inversa de uma matriz quadrada:',

        'resposta':{ 'a':'Usar a regra de Sarrus','b': 'Tudo que é linha vira coluna','c': 'A determinante ser diferente de 0', 'd': 'a determinante ser 0' },
        'resposta_certa': 'c',  
    },
     
    '---LÓGICA E ALGORITMO DE PROGAMAÇÃO--- \n'
    'pergunta8 \n': {
        'pergunta': '\n a = round(5.5) \n'
                        ' b = round(6.5) \n'
                        ' print(a,b) \n'
                        

                        'De acordo com o código acima, qual será a saida: ',

        'resposta':{ 'a':'5 6','b': '6 6','c':'6 7', 'd':'66' },
        'resposta_certa': 'b',  
    },

     
    '---LÓGICA E ALGORITMO DE PROGAMAÇÃO--- \n'
    'pergunta9 \n': {
        'pergunta': '\n   x = -4 \n'
                        '   if bool (x) \n'
                        '    print(x) \n'
                        '   else: \n'
                        '    print(0) \n ' 
                     
                         'Qual será a saida do progama:'  ,

        'resposta':{ 'a':'0','b': '-4','c':'none', 'd':'error' },
        'resposta_certa': 'b',  
    },


}




respostas_certas = 0

#iterações com chaves e valores

for perguntas_chaves,perguntas_valor in perguntas.items():
  print()
  print(f'{perguntas_chaves}  {perguntas_valor["pergunta"]}')

  print()

  print('escolha as opções abaixo'.capitalize())
  for respostas_chaves, respostas_valor in perguntas_valor ['resposta'].items():
    print (f'({respostas_chaves}) : {respostas_valor } ')
  
  
#caso o usário digite uma letra diferente de a, b , c ou d
  while True:
    print()
    sua_resposta = input('digite sua resposta: ').lower()
    if sua_resposta != 'a' and sua_resposta != 'b' and sua_resposta != 'c' and sua_resposta != 'd':
      print()
      print('digite uma letra válida \U0001F642 ')
      print()
      
    else:

      break

#verificação da resposta  

  if sua_resposta == perguntas_valor ['resposta_certa'] :
     print()
     print('UHOUUU, VOCÊ ACERTOU !!! \U0001F603 ')
     respostas_certas+=1
  else:
      print('INFELIZMENTE VOCÊ ERROU \U0001F614. ')
      print()

print(f'a quantidade de acertos= {respostas_certas}')
print(f'a quantidade de de perguntas = {len(perguntas)}')
quant_perguntas = len(perguntas)
print()
print(f'a quantidade de resposta certas foi {porcentagem(respostas_certas,quant_perguntas):.2f}%')
