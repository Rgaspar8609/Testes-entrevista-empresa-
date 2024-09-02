import json

def analisar_faturamento(arquivo):
    """Analisa os dados de faturamento de um arquivo JSON.

    Args:
        arquivo (str): Nome do arquivo JSON.

    Returns:
        tuple: Uma tupla contendo o menor valor, o maior valor, a média e a quantidade de dias acima da média.
    """

    with open(arquivo, 'r') as f:
        dados = json.load(f)

    faturamentos = [dado['valor'] for dado in dados if dado['valor'] > 0]
    menor_valor = min(faturamentos)
    maior_valor = max(faturamentos)
    media = sum(faturamentos) / len(faturamentos)
    dias_acima_media = len([valor for valor in faturamentos if valor > media])

    return menor_valor, maior_valor, media, dias_acima_media

# Exemplo de uso
arquivo_json = 'faturamento.json'  # Substitua pelo nome do seu arquivo
menor, maior, media, dias_acima = analisar_faturamento(arquivo_json)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Média: {media:.2f}")
print(f"Dias acima da média: {dias_acima}")