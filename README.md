# Proyecto-Sistemas-Embebidos

Se realiza una implementación de un sistema embebido utilizando un sensor de aceleración y un modulo convertidor USB a TTL. Se utilizan varios hilos para ejecutar varias tareas al mismo tiempo. Se envían datos al servidor de ThingSpeak.

# ¿Cuál es la diferencia entre una tarea, un proceso y un hilo, (task, process, thread)?

Un proceso es un programa en ejecución que incluye un código ejecutable, los datos asociados a ese código, espacio de memoria y otros recursos. Cada proceso tiene su propio espacio de memoria, lo que significa que los datos de un proceso no son directamente accesibles por otro proceso, sino que se tienen que utilizar otros mecanismos de intercomunicación, aunque esto puede presentar cierta sobrecarga y además hay que tener cuidado para evitar problemas de concurrencia.

Un hilo es la unidad más pequeña de ejecución dentro de un proceso. Los hilos comparten el mismo espacio de memoria y recursos del proceso al que pertenecen. Permiten la ejecución concurrente dentro de un proceso ya que múltiples hilos pueden ejecutarse simultáneamente, lo que puede mejorar la eficiencia. Estos, al compartir recursos dentro de un mismo proceso, facilita la comunicación y el intercambio de datos, sin embargo, al igual que en los procesos, hay que tener cuidado en la gestión de estos para evitar problemas de concurrencia.

El término tarea es a veces utilizado de una forma más general, ya sea para referirse a una unidad de trabajo que deba realizarse ya sea correspondiente a un hilo o a un proceso indistintamente. En otros contextos "tarea" se puede utilizar de formma intercambiable con "hilo" para describir la unidad de ejecución dentro del proceso.

# ¿Cómo se maneja el control de prioridad de un proceso en GNU/Linux, detallando que es el NI y el PR y ¿Cómo se modifica este valor para un proceso?¿Cómo se cambia el valor de este proceso para todos los procesos de un usuario?

En sistemas GNU/Linux, el control de prioridad de un proceso se gestiona mediante el Nice Value (NI) y el Priority (PR). El NI, que varía de -20 a 19, determina la prioridad de un proceso, donde un NI vajo indica mayor prioridad. Para modificar la prioridad de un proceso, se puede usar el siguiente comando: 

    renice -c <nuevo_nice_value> -p <PID_del_proceso>
    
Para cambiar el NI para todos los procesos de un usuario en específico se utiliza el comando renice junto con la opción '-u'.

