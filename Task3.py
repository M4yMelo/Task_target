faturamento = [2000, 2500, 1800, 0, 3200, 2900, 0, 4000, 3300, 487, 1000, 0, 8631]

def calcular_estatisticas(faturamento):
    faturamento_valido = [valor for valor in faturamento if valor > 0]
    menor_valor = min(faturamento_valido)
    maior_valor = max(faturamento_valido)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_da_media

menor_valor, maior_valor, dias_acima_da_media = calcular_estatisticas(faturamento)
print(f"Menor valor: R${menor_valor}")
print(f"Maior valor: R${maior_valor}")
print(f"Dias acima da média: {dias_acima_da_media}")
