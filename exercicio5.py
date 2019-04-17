valor = input("informe um valor: ")
print("Tipo primitivo desse valor é ", type(valor))

print("É um número", valor.isnumeric())
print("É uma string", valor.isalnum())
print("É maiúscula", valor.isupper())
print("É minúscula", valor.islower())