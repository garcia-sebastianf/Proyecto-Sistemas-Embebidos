# Proyecto-Sistemas-Embebidos

Se realiza una implementación de un sistema embebido utilizando un sensor de aceleración y un módulo convertidor USB a TTL. Se utilizan varios hilos para ejecutar varias tareas al mismo tiempo. Se envían datos al servidor de ThingSpeak.

# ¿Cuál es la diferencia entre una tarea, un proceso y un hilo, (task, process, thread)?

Un proceso es un programa en ejecución que incluye un código ejecutable, los datos asociados a ese código, espacio de memoria y otros recursos. Cada proceso tiene su propio espacio de memoria, lo que significa que los datos de un proceso no son directamente accesibles por otro proceso, sino que se tienen que utilizar otros mecanismos de intercomunicación, aunque esto puede presentar cierta sobrecarga y además hay que tener cuidado para evitar problemas de concurrencia.

Un hilo es la unidad más pequeña de ejecución dentro de un proceso. Los hilos comparten el mismo espacio de memoria y recursos del proceso al que pertenecen. Permiten la ejecución concurrente dentro de un proceso ya que múltiples hilos pueden ejecutarse simultáneamente, lo que puede mejorar la eficiencia. Estos, al compartir recursos dentro de un mismo proceso, facilita la comunicación y el intercambio de datos, sin embargo, al igual que en los procesos, hay que tener cuidado en la gestión de estos para evitar problemas de concurrencia.

El término tarea es a veces utilizado de una forma más general, ya sea para referirse a una unidad de trabajo que deba realizarse ya sea correspondiente a un hilo o a un proceso indistintamente. En otros contextos "tarea" se puede utilizar de formma intercambiable con "hilo" para describir la unidad de ejecución dentro del proceso.

# ¿Cómo se maneja el control de prioridad de un proceso en GNU/Linux, detallando que es el NI y el PR y ¿Cómo se modifica este valor para un proceso?¿Cómo se cambia el valor de este proceso para todos los procesos de un usuario?

En sistemas GNU/Linux, el control de prioridad de un proceso se gestiona mediante el Nice Value (NI) y el Priority (PR). El NI, que varía de -20 a 19, determina la prioridad de un proceso, donde un NI bajo indica mayor prioridad. Para modificar la prioridad de un proceso, se puede usar el siguiente comando: 

    renice -c <nuevo_nice_value> -p <PID_del_proceso>
    
Para cambiar el NI para todos los procesos de un usuario en específico se utiliza el comando **renice** junto con la opción '-u'.

    renice -n <nuevo_nice_value> -u <nombre_de_usuario>

El PR, relacionado inversamente con el NI, a medida que NI aumenta, el PR disminuye y viceversa. Los valores típicos van de 100 a -100.

# Uso del operador '&' al final de una línea de comandos en Bash y la separación de múltiples comandos en una sola línea.

En Bash, el operador "&" al final de una línea de comandos permite ejecutar el comando en segundo plano, liberando la terminal para otros comandos mientras el primero se ejecuta. Para agrupar varios comandos en una sola línea, se emplea el punto y coma.

    #Ejecuta 'mi_comando' en segundo plano
    mi_comando &

    #Ejecuta tres comandos en una línea
    comando1 ; comando2 ; comando3

Comandos asociados:

- **'jobs'**: Muestra los trabajos en segundo plano en la sesión actual de Bash.
- **'$!'**: Representa el PID (identificador de proceso) del último comando ejecutado en segundo plano.
- **'fg'**: Lleva un trabajo en segundo plano al primer plano.

# Diferencia entre & y el comando parallel de bash, no de sh (sudo apt install parallel).

En Bash, el uso del operador **'&'** y del comando **'parallel'** comparten el propósito de ejecutar comandos de manera paralela, pero se diferencian en su implementación y funcionalidad.

**1. '&' en Bash:** 
La utilización del operador **"&"** al final de una línea de comando permite ejecutar ese comando en segundo plano, permitiendo que la terminal esté disponible para otros comandos mientras el primero se ejecuta en segundo plano. 

Este es un componente básico de Bash y opera a nivel de procesos. 

    #Ejecuta 'mi_comando' en segundo plano
    mi_comando &

**2. Comando 'parallel' en Bash:**
Por otro lado, el comando **'parallel'** es una herramienta externa que facilita la ejecución estructurada y controlada de comandos en paralelo.

**'parallel'** divide la entrada en bloques y ejecuta comandos en paralelo utilizando múltiples procesos o hilos, brindando opciones avanzadas para el manejo de la salida y el control del número de procesos simultáneos.

    #Instala parallel (si no está instalado)
    sudo apt install parallel

    #Ejemplo de uso de parallel
    parallel ::: "comando1" "comando2" "comando3"

En resumen, mientras que el operador **"&"** es una característica integrada en Bash para ejecutar comandos en segundo plano, el comando **'parallel'** es una herramienta externa que ofrece una forma más avanzada y estructurada de llevar a cabo operaciones en paralelo, proporcionando mayor control sobre la ejecución concurrente de comandos.

**Funcionamiento del comando time en Bash.**

El comando **'time'** en Bash se emplea para medir el tiempo de ejecución de un comando o un conjunto de comandos. Al utilizarlo, puedes obtener detalles sobre el tiempo que la CPU dedica al usuario y al sistema, así como el tiempo total transcurrido desde el inicio hasta la finalización del comando. La salida proporciona información útil para evaluar el rendimiento de un programa. Es esencial diferenciar entre la palabra clave **'time'** de Bash y el comando externo también llamado **'time'**, que ofrece funcionalidades similares, pero con salidas más resumidas. 

#Proyecto

**Punto 1:**

**Nota. Para este proyecto necesitará un sensor I2C y un conversor USB Serial de 3.3v. (el serial si es posible lleve su portátil a la tienda y verifique que esté bueno, hay muchos clones no funcionales en el mercado).**

Se corrobora que el módulo convertidor USB a TTL sea reconocido por el dispositivo utilizando el administrador de dispositivos (Device Manager). 

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/1345f422-d0a4-4014-aad4-86b7a7b57d1c)

El modulo se encuentra asignado en el puerto COM11, este es el que se utilizará para establecer comunicación hacia la raspberry pi 3B+.

Para comprobar su correcto funcionamiento, se realiza un script en el lenguaje de Python sobre la tarjeta raspberry pi 3B+ para la transmisión de datos. 

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/93ea4020-7791-4da1-b55e-317cd919f3f8)

Con el uso del programa de PuTTY se realiza la configuración de varios parámetros como números de bits de los datos, bit de parada, bits por segundo o baudios, la selección del puerto, etc.

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/274d2d96-1e5f-4258-b169-cb6eadb36534)

Al ejecutar el script se visualiza que se enciende un led azul ubicado sobre el módulo que corresponde a la recepción de los datos, lo que sirve como una comprobación inicial de que se está logrando realizar transmisión de datos. 

Se establece la conexión en Putty y se logra tener el siguiente resultado en pantalla.

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/62db8de2-35e2-413a-af26-ba4ed95f9890)

**Capture datos de un sensor con comunicaciones i2c de su preferencia (temperatura, humedad, presión IMUS, acelerómetros, entre otros) usando un script de Python, para ello debe imprimir en pantalla el valor capturado a una taza de mínimo 1 dato por segundo.**

Se utiliza el acelerómetro I2C ADXL345 y se realiza el siguiente Script de Python para la captura de los datos. 

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/7b56be9d-b478-4f37-85c1-f568578510dc)

Para este módulo, se obtienen tres valores de aceleración, uno por cada eje del espacio en tres dimensiones. También, estas tres aceleraciones pueden presentar valores negativos, lo que ofrece información adicional del sistema donde se encuentre ubicado el módulo. Sin embargo, para este proyecto se requiere optimizar la adquisición y operación para un solo dato, por lo que se opta por el uso de la librería **'math'**. Gracias a esta se pudo obtener un solo dato por medio de la magnitud de las tres componentes de aceleración. 

Para decidir cada cuanto adquirir la lectura, se importa la librería time. En este caso, se agregaa '1' como parámetro de la función time.sleep() para establecer el tiempo de adquisición de los datos para cada segundo, quitar esta línea simplemente hará que se lean los datos a la máxima tasa de datos que pueda generar el módulo. 

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/41e67b36-dd1e-48d5-b5dd-d66fdb1f3d0f)

**Capture los datos de su sensor de temperatura 1 Wire igual que en el proyecto 1.**

A continuación, se presentan las conexiones sobre la raspberry para realizar la captura de estos datos. 

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/69e36c78-ce99-4189-b951-cc5f90fd9985)

**Usando el módulo threading de Python o C (thread.h) implemente un hilo que lea de su sensor i2c a la tasa más alta que permita su sensor. Otro hilo que escriba en un puerto serial a mínimo 115200 bps el promedio de las útlimas N lecturas donde N puede ser configurado por el usuario con una variable de argumento de entrada serial de su programa en su programa (C o Python) y otro hilo que lea del puerto serial a la misma velocidad (115200), una trama así: (##PROMEDIO-NNN-##\n) donde NNN es el tamaño de la ventana de promedio, cualquier otro mensaje debe ser descartado y tomado como no válido.**

Ya se verificó la transmisión de datos y la adquisición de los valores de aceleración, por lo que solamente queda implementar la recepción de los datos. Para ello, se opta por el uso de PyCharm, que es un entorno de desarrollo que permite escribir y ejecutar código realizado en Python. A continuación, se muestra el código para la transmisión de datos ingresados por el usuario a través de la consola. 

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/c07f3899-4326-47e4-84e1-0348b1555cb3)

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/94f09103-b808-48e7-a88e-f16342c360cf)

A partir de diversas pruebas, se determinó que la opción óptima y más sencilla era enviar repetidamente y a la máxima tasa de transmisión los valores ingresados por el usuario. Esto se debe a problemas de sincronización, dado que el usuario puede enviar el dato en cualquier momento, lo que puede ocasionar dificultades ya que el programa en la Raspberry Pi encargado de recibir los datos puede no estar en la línea de código que lee el dato en ese preciso instante, sino ejecutando otras líneas de código. Esta falta de sincronización resultó en problemas inesperados, como la pérdida de información: a veces los datos llegaban incompletos o, en ocasiones, ni siquiera llegaban.

A continuación, se presenta el script de Python utilizado para la recepción de los datos en la Raspberry Pi.

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/1ea132b1-29f5-41e8-bf08-de4b5456c262)

Una vez verificado el correcto funcionamiento de todos los scripts, se procede a unificarlos en un único código, separándolos por hilos de ejecución. La estructura del código se basa en el uso de tres hilos de ejecución, cada uno asociado a una función específica. Para implementar esto, fue necesario establecer una comunicación de datos entre los tres hilos de forma simultánea, lo que significa que los tres hilos se ejecutan al mismo tiempo y comparten datos en tiempo real. En este sentido, el uso de colas FIFO fue crucial, ya que facilitan la comunicación de los datos de manera sencilla y permiten la sincronización entre hilos; es decir, un hilo no puede tomar un dato de la cola hasta que otro hilo haya insertado un valor en la misma.

Es importante destacar que la implementación de hilos en esta aplicación es muy adecuada. A pesar de la alta tasa de adquisición de datos de aceleración y la transmisión de datos por puerto serial a una alta velocidad de baudios, los tiempos de procesamiento son lo suficientemente rápidos como para permitir la realización de otras tareas dentro de las ventanas de tiempo de espera. Además, sin el uso de hilos, no sería posible calcular el promedio de aceleración en tiempo real, ya que tendríamos que detener la recepción de datos, calcular el promedio y luego reanudar la adquisición de datos, lo que resultaría en la pérdida de datos de aceleración. Sin embargo, con el uso de hilos, todos los datos que llegan se utilizan para calcular el promedio de aceleración. 

Para estructurar todo el código, se realiza un esquema que muestra gráficamente cómo debe ser el flujo de los datos a través de los hilos. 

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/32b080a7-3043-4b84-b4d4-190234d5c331)

Los hilos que reciben los datos pueden seguir ejecutándose solamente si la cola ha recibido datos de los otros hilos que los envían. Esta es la razón por la cual se pueden sincronizar los hilos mediante el uso de colas, evitando problemas de concurrencia, como los "glitches", que son muy difíciles, por no decir imposibles de detectar e identificar, esto NO significa que los hilos se estén ejecutando de forma secuencial.

Para promediar los datos en tiempo real, se propone sumar de forma iterativa el dato dividido por el valor de la ventana N e ir acomulando ese valor en el instante en el que llega el dato de la cola enviado por el hilo de adquisición de los datos. Lo que es igual a dividir la fracción de la fórmula de promedio en una soma de fracciones homogéneas. 

A continuación, se presenta la sección del script que realiza el promedio del dato de aceleración.

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/4e2fee3c-8654-4b3d-ad20-1caf1043b0c5)

Integrando todo lo anterior en la estructura de hilos que describimos obtenemos el siguiente script de Python ubicado en el archivo xxx de este proyecto.

Al ejecutar el código obtenemos los siguientes resultados. Cabe mencionar que el usuario va a ser capaz de ingresar en tiempo real una nueva ventana para la 
obtención del promedio con N datos, por lo que ese valor de N se actualizará.

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/79585186-907b-4e23-a97e-39a45d587c2f)
![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/c8c14f0e-65f8-4983-af8b-e1621cded563)
![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/9cdf0299-8144-47f8-bb42-db752df73463)

Se presenta el script de Python que permite que el usuario ingrese el valor de la ventana para la obtención del promedio de los datos:

Valor del promedio de la aceleración en la transmisión. Se realiza la visualización con ayuda de PuTTY.

![image](https://github.com/garcia-sebastianf/Proyecto-Sistemas-Embebidos/assets/76495580/d31d07ba-6953-433e-bd8b-a8468683e521)

# Use el código anterior con un N fijo para subir a la nube de su preferencia cada segundo el promedio de los datos capturados de su sensor, debe ver en la página web de su nube el valor más reciente del sensor en una gráfica. 

# Conclusiones

- En procesos que contienen tiempos de espera, el uso de hilos representa una herramienta que permite optimizar de forma importante los tiempos de ejecución de dicho proceso al aprovechar esos tiempos muertos y ejecutar otros fragmentos del proceso o hilos.

- No es recomendable el uso de variables globales para compartir datos entre hilos. Utilizando este método no se tiene control sobre la sincronización de los hilos, lo que puede causar fallos inesperados y en cualquier instante.

- El uso de las estructuras de colas es una forma muy adecuada para compartir datos entre hilos e incluso para sincronizarlos. El uso de colas va más allá ya que se pueden usar para compartir memoria entre procesos.

- El uso de hilos permite realizar procesos en paralelo. Por lo que se pueden realizar varias tareas de forma simultánea, esto es especialmente importante en algunas aplicaciones, por ejemplo, en este proyecto donde se requerían hacer varias tareas con distintos periféricos y módulos de hardward en tiempo real.

- El uso de hilos no solo se encuadra en un sistema embebido, sino que es posible transmitir los valores obtenidos en una base de datos. Esto ofrece la posibilidad de optimizar procesos en sistemas Iot.


            
                    

                    

                        
                    
