texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nunc dolor, pretium sed laoreet in, efficitur eget leo. In elementum commodo mauris, eget pellentesque nibh semper sed. Maecenas eu nisl nulla. Nunc varius orci eget dolor vestibulum, at pulvinar quam posuere. Ut sit amet gravida ante. Vestibulum vel varius nulla, vitae dapibus purus. Aliquam blandit ultricies tellus eu elementum. Pellentesque at tempor tortor. Nullam vehicula aliquet magna in rutrum. Quisque ante diam, malesuada id sapien vitae, hendrerit tempor elit. Pellentesque vel eros ut odio commodo faucibus accumsan nec massa. Aliquam pulvinar, dolor ac accumsan pulvinar, ligula justo auctor diam, ac consequat arcu erat id nunc. Praesent vel pulvinar justo. Ut congue mauris vitae turpis euismod tristique. Aliquam nec sapien non metus tincidunt fringilla vel a mi. Integer at consectetur magna"

contadorA = 0
contadorE = 0
contadorI = 0
contadorO = 0
contadorU = 0

for letra in texto:
    if(letra.upper() == "A"):
        contadorA = contadorA + 1
    elif(letra.upper() == "E"):
        contadorE = contadorE + 1
    elif(letra.upper() == "I"):
        contadorI = contadorI + 1
    elif(letra.upper() == "O"):
        contadorO = contadorO + 1
    elif(letra.upper() == "U"):
        contadorU = contadorU + 1

print(f"Cantidad de A: {contadorA}")
print(f"Cantidad de E: {contadorE}")
print(f"Cantidad de I: {contadorI}")
print(f"Cantidad de O: {contadorO}")
print(f"Cantidad de U: {contadorU}")
print(f"Total de vocales: {contadorA+contadorE+contadorI+contadorO+contadorU}")
