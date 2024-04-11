# Proyecto-Sistemas-Embebidos

Se realiza una implementación de un sistema embebido utilizando un sensor de aceleración y un modulo convertidor USB a TTL. Se utilizan varios hilos para ejecutar varias tareas al mismo tiempo. Se envían datos al servidor de ThingSpeak.

# ¿Cuál es la diferencia entre una tarea, un proceso y un hilo, (task, process, thread)?

Un proceso es un programa en ejecución que incluye un código ejecutable, los datos asociados a ese código, espacio de memoria y otros recursos. Cada proceso tiene su propio espacio de memoria, lo que significa que los datos de un proceso no son directamente accesibles por otro proceso, sino que se tienen que utilizar otros mecanismos de intercomunicación, aunque esto puede presentar cierta sobrecarga y además hay que tener cuidado para evitar problemas de concurrencia.

Un hilo es la unidad más pequeña de ejecución dentro de un proceso. Los hilos comparten el mismo espacio de memoria y recursos del proceso al que pertenecen. Permiten la ejecución concurrente dentro de un proceso ya que múltiples hilos pueden ejecutarse simultáneamente, lo que puede mejorar la eficiencia. Estos, al compartir recursos dentro de un mismo proceso, facilita la comunicación y el intercambio de datos, sin embargo, al igual que en los procesos, hay que tener cuidado en la gestión de estos para evitar problemas de concurrencia.

El término tarea es a veces utilizado de una forma más general, ya sea para referirse a una unidad de trabajo que deba realizarse ya sea correspondiente a un hilo o a un proceso indistintamente. En otros contextos "tarea" se puede utilizar de formma intercambiable con "hilo" para describir la unidad de ejecución dentro del proceso.

# ¿Cómo se maneja el control de prioridad de un proceso en GNU/Linux, detallando que es el NI y el PR y ¿Cómo se modifica este valor para un proceso?¿Cómo se cambia el valor de este proceso para todos los procesos de un usuario?

En sistemas GNU/Linux, el control de prioridad de un proceso se gestiona mediante el Nice Value (NI) y el Priority (PR). El NI, que varía de -20 a 19, determina la prioridad de un proceso, donde un NI vajo indica mayor prioridad. Para modificar la prioridad de un proceso, se puede usar el siguiente comando: 

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


