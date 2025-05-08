import os
os.system("cls")
os.system("color 3")
#aula 02 -> variaveis, tipos e input
#Tipos de Dados 
#String -> Texto 
#Int -> Inteiro
#Float -> quebrado (flutuante)

#declaração de variaveis
#escola = "senai"
#mostrando o valor da variavel no print
#concatenando com o +
#print("o nome da minha escola é" + escola)
#separando por parametro ,
#print("o nome da minha escola é" , escola)
#f strind {} -> mostra o valor da variavel detro das aspas
#print(f"o nome da minha escola é  {numero}")

#exemplo de variavel int
#numero =100
#print("somando com 10 = ",numero+10)
#print("subtraindo 5 = ", numero -5 )
#print("dividindo por 2 = ", numero/2)
#print("multiplicando por 10 =", numero *10) 

#!!!atividade!!!

#print(">"*5,"DADOS CADASTRAIS","<"*5)
#nome= "Nome: Kauã\n"
#idade= "Idade: 16 \n"
#cpf= "CPF: 47762424865 \n"
#print(nome," ",idade," ",cpf )

#!!!atividade 2!!!
#input
#texto = input("digite algo: ")
#print("voce digitou ..." ,texto)

print(">"*5,"DADOS CADASTRAIS","<"*5)
nome = input("Digite seu Nome: ")
cpf = input("Digite seu CPF: ")
rg = input("Digite seu RG: ")
os.system("cls")
print(">"*3,"DADOS CADASTRADOS","<"*3)
print("Nome: " ,nome)
print("CPF: " ,cpf)
print("RF: " ,rg)