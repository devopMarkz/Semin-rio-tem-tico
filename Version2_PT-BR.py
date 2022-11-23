def porcentagem (respostas_certas,quant_perguntas):
  return  ((respostas_certas/quant_perguntas)*100)


print(f'a quantidade de acertos= {respostas_certas}')
print(f'a quantidade de de perguntas = {len(perguntas)}')
quant_perguntas = len(perguntas)
print()
print(f'a quantidade de resposta certas foi {porcentagem(respostas_certas,quant_perguntas):.2f}%')
