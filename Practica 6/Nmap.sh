#!/bin/bash
#ESTE SCRIPT NECESITA PARAMETROS PARA QUE FUNCIONE EJEMPLO ./Nmap.sh (IP_PRIVADA) (IP_PUBLICA)
#Lo hice de esta forma ya que no queria mostrar mi ip
ip=$1
ipu=$2

echo "===Obtenemos la ip privada==="|base64>>Nmap.txt
hostname -I |base64>>Nmap.txt

echo "===Obtenemos la ip publica==="|base64>>Nmap.txt
curl ifconfig.me | base64 >> Nmap.txt

echo "===Nmap segmento a la red privada==="|base64 >>Nmap.txt
nmap -sP "$ip"|base64 >>Nmap.txt
nmap "$ip"|base64 >>Nmap.txt

echo "===Nmap segmento con un script==="|base64>>Nmap.txt
nmap --script=acarsd-info "$ip"|base64 >>Nmap.txt
nmap --script=firewall-bypass "$ipu"|base64 >>Nmap.txt

echo "===Nmap segmento a la red public==="|base64>>Nmap.txt
nmap -sP "$ipu"|base64 >>Nmap.txt
nmap "$ipu"|base64 >>Nmap.txt

