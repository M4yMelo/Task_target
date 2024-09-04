faturamento = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.8318},
    {"dia": 28, "valor": 1718.1221},
    {"dia": 29, "valor": 13220.495},
    {"dia": 30, "valor": 8414.61}
]

def calcular_estatisticas(faturamento):
    # Filtra os dias com faturamento positivo
    valores_com_faturamento = [item["valor"] for item in faturamento if item["valor"] > 0]

    # Calcula as métricas
    menor_valor = min(valores_com_faturamento)
    maior_valor = max(valores_com_faturamento)
    dias_sem_faturamento = len(faturamento) - len(valores_com_faturamento)
    media_faturamento = sum(valores_com_faturamento) / len(valores_com_faturamento)

    return menor_valor, maior_valor, dias_sem_faturamento, media_faturamento

# Executa a função e armazena os resultados
menor_valor, maior_valor, dias_sem_faturamento, media_faturamento = calcular_estatisticas(faturamento)
# Filtra os valores de faturamento excluindo os dias com 0
valores_com_faturamento = [item["valor"] for item in faturamento if item["valor"] > 0]

# Calcula o menor valor de faturamento
menor_valor = min(valores_com_faturamento)

# Calcula o maior valor de faturamento
maior_valor = max(valores_com_faturamento)

# Calcula o número de dias sem faturamento
dias_sem_faturamento = len([item for item in faturamento if item["valor"] == 0])

# Calcula a média de faturamento
media_faturamento = sum(valores_com_faturamento) / len(valores_com_faturamento)

# Exibe os resultados
print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
print(f"Dias sem faturamento: {dias_sem_faturamento}")
print(f"Média de faturamento (excluindo dias sem faturamento): R$ {media_faturamento:.2f}")
