# Ransomware
Ranson-py  es un proyecto que fue escrito para mostrar lo fácil que es crear código extremadamente malicioso,el ransomware está diseñado para secuestrar los archivos más queridos de la víctima demandando grandes cantidades de dinero para desbloquearlos.

# Advertecia
Este software se crea SOLAMENTE para fines educativos. No soy responsable de su uso.
Úselo con extrema precaución.

# Para la POC se necesita instalar lo siguiente

# Instalar Servidor Apache:
sudo apt -get update
sudo apt -get install apache2

# Instalar Servidor Mysql
sudo apt-get install mysql-server

# Instalar PHP5
sudo apt-get install libapache2-mod-php5 php5 php5-mcrypt php5-mysql

# Crear base de datos

CREATE DATABASE ransomware_db;
USE ransomware_db;
CREATE TABLE victimas (ID int NOT NULL AUTO_INCREMENT,
                       IDD varchar(35),
                       PASS varchar(35),
                       PRIMARY KEY (ID));


# Pasos a Seguir
Paso 1:

Se crea un código que cifre datos de una computadora, escogí hacerlo en python por su versatilidad y facilidad de aprendizaje.

Paso 2:

Se debe infectar una maquina con el código, en este ejemplo no voy a mostrar ningún vector de ataque para hacerlo mas simple y decidí instalarlo directamente en la computadora.

Paso 3:

Al infectar la maquina, esta busca ciertos directorios que nosotros le indiquemos, va a cifrar con una contraseña aleatoria y cuando este todo listo las va a enviar a un servidor Web. El servidor Web va a recibir un Id y un password, lo va a guardar en una base de datos.

Paso 4:

La maquina infectada va a tener solo un script para recuperar los archivos cifrados y se le va a solicitar un pago.

Paso 5:

El usuario paga por medio de bitcoin.

Paso 6:

Se procede a ejecutar el script con la contraseña obtenida después del pago.


