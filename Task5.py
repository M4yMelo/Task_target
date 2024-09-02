def inverter_string(s):
    # Cria uma string vazia para armazenar o resultado
    resultado = ""
    
    # Percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    
    return resultado

# Exemplo de uso
entrada = "Olá, TARGET!"
string_invertida = inverter_string(entrada)
print("String original:", entrada)
print("String invertida:", string_invertida)
