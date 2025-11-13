print("MOSTRANDO O TIPO PRIMITIVO")

n = input("Digite algo:")

print(f" É númerico?", n.isnumeric())
print(f"É alfanúmerico?", n.isalnum())
print(f"São todos letras?", n.isalpha())
print(f"É decimal?", n.isdecimal())
print(f"São todos dígitos?", n.isdigit())
print(f"Todos os caracteres alfabéticos estão em maiúsculas?", n.isupper())
print(f"Todos os caracteres alfabéticos estão em minúsculas?", n.islower())


