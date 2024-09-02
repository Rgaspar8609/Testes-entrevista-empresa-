def fibonacci(n):
  """Calcula a sequência de Fibonacci até o n-ésimo termo.

  Args:
    n: O número até onde a sequência será calculada.

  Returns:
    Uma lista com os números da sequência de Fibonacci.
  """

  fib = [0, 1]
  while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])
  return fib

def pertence_fibonacci(num):
  """Verifica se um número pertence à sequência de Fibonacci.

  Args:
    num: O número a ser verificado.

  Returns:
    True se o número pertence à sequência, False caso contrário.
  """

  seq_fib = fibonacci(num)
  return num in seq_fib

# Obtendo o número do usuário
numero = int(input("Digite um número: "))

# Verificando se o número pertence à sequência
if pertence_fibonacci(numero):
  print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence à sequência de Fibonacci.")