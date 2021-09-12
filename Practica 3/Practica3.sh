#!/bin/bash

Dominio=$1
ApiKey=$2

# Sirve para buscar correos electronicos con el dominio dado
echo "Domino de Correo Hunter io"
curl "https://api.hunter.io/v2/domain-search?domain=$Dominio&api_key=$ApiKey" | head -n 50 > Result_Dom.txt

# Sirve para encontrar correos electronicos mas probables con el dominio, nombre y apellido o segundo nombre
echo "Buscar correos Hunter io"
read -p "Primer nombre: " Nom
read -p "Apellido: " Ape
curl "https://api.hunter.io/v2/email-finder?domain=$Dominio&first_name=$Nom&last_name=$Ape&api_key=$ApiKey" > Result_Correo.txt

# Sirve para comprobar que existe el correo electronico
echo "Comprobar correo Hunter io"
read -p "Correo electronico: " Correo
curl "https://api.hunter.io/v2/email-verifier?email=$Correo&api_key=$ApiKey" > Status_Correo.txt

#Obtienes tu propio perfil de usuario
echo "Perfil de Github"
read -p "Nombre de Usuario: " User
read -p "Token Actual: " Tok
curl  -i -u $User:$Tok https://api.github.com/user > User.txt

#Listar repositorios de otro usuario
echo "Repositorios de Github"
read -p "Nombre del Usuario: " UUser
curl -i https://api.github.com/users/$UUser/repos >  Repos.txt

