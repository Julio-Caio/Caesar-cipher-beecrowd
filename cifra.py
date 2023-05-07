def criptografar(palavra, valor):
    
    palavra_criptografada = []
    
    for letra in palavra:
        if ord(letra) - valor >= 65:
            letra_criptografada = chr(ord(letra) - valor)
            palavra_criptografada.append(letra_criptografada)
        else:
            letra_criptografada = chr(ord(letra) - (valor - 26))
            palavra_criptografada.append(letra_criptografada)

    return "".join(palavra_criptografada)

qtde = int(input())

for i in range(qtde):
    palavra = input()
    valor = int(input())
    palavra_cripto = criptografar(palavra, valor)
    print(palavra_cripto)