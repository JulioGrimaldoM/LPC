#!/bin/bash
#Use mail y se debe configurar un archivo en etc/ssmtp/ssmtp.confif y ahi ponemos nuestra contraseña y correo
read -p "Asunto> " Title
read -p "Mensaje> " Cuerpo
while IFS= read -r line
do
  echo "$Cuerpo" | mail -s "$Title" $line -a From:Julio\<junzsgamerytn@gmail.com\>
done < Destinatarios.txt