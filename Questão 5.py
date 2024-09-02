def inverter_string():
  """Inverte uma string fornecida pelo usuário."""
  
  texto = input("Digite a palavra ou frase: ")
  texto_invertido = ""
  
  for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]
  
  print("A string invertida é:", texto_invertido)

# Chamando a função para inverter a string
inverter_string()