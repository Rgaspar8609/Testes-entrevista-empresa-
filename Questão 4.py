def calcular_percentual_faturamento(dados):
  """Calcula o percentual de faturamento por estado.

  Args:
    dados (dict): Um dicionário onde as chaves são os estados e os valores são os faturamentos.

  Returns:
    dict: Um dicionário com os estados e seus respectivos percentuais de faturamento.
  """

  faturamento_total = sum(dados.values())
  percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in dados.items()}
  return percentuais

# Dados de exemplo (substitua pelos seus dados)
faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calculando os percentuais
percentuais = calcular_percentual_faturamento(faturamento_por_estado)

# Imprimindo os resultados
for estado, percentual in percentuais.items():
  print(f"{estado}: {percentual:.2f}%")