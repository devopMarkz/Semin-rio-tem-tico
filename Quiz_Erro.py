def porcentagem (respostas_c,q):
  return  ((respostas_c/q)*100)
  
perguntas = {
    'pergunta1': {
        'pergunta': 'QUANTO E 3*3 ?',
        'resposta':{ 'a':'6 ','b': '9','c': '0', },
        'resposta_certa': 'b',
    },
    'pergunta2': {
        'pergunta': 'QUANTO E a raiz quadrada de 144?',
        'resposta':{ 'a':'6 ','b': '9','c': '12', },
        'resposta_certa': 'c',  
    }


}
respostas_c = 0
for perguntas_k,perguntas_v in perguntas.items():
  print()
  print(f'{perguntas_k} ) {perguntas_v["pergunta"]}')

  print('escolha as opções abaixo'.capitalize())
  for respostas_k, respostas_v in perguntas_v ['resposta'].items():
    print (f'({respostas_k}) : {respostas_v } ')
  
  sua_resposta = input('digite sua resposta: ').lower()
  while sua_resposta != 'a' or 'b' or 'c':
      print('digite uma letra valida!!!')
      sua_resposta = input('digite sua resposta: ').lower()
      break
  if sua_resposta == perguntas_v ['resposta_certa'] :
        print('uhouuu, voce acertou')
        respostas_c+=1
  else:
        print('infelizmente voce errou')


print(f'a quantidade de acertos= {respostas_c}')
print(f'a quantidade de de perguntas = {len(perguntas)}')
quant_perguntas = len(perguntas)
print()
print(f'a quantidade de resposta certas foi {porcentagem(respostas_c,quant_perguntas)}%')