# Proyecto-Sistemas-Embebidos

Se realiza una implementación de un sistema embebido utilizando un sensor de aceleración y un modulo convertidor USB a TTL. Se utilizan varios hilos para ejecutar varias tareas al mismo tiempo. Se envían datos al servidor de ThingSpeak.

# ¿Cuál es la diferencia entre una tarea, un proceso y un hilo, (task, process, thread)?

Un proceso es un programa en ejecución que incluye un código ejecutable, los datos asociados a ese código, espacio de memoria y otros recursos. Cada proceso tiene su propio espacio de memoria, lo que significa que los datos de un proceso no son directamente accesibles por otro proceso, sino que se tienen que utilizar otros mecanismos de intercomunicación, aunque esto puede presentar cierta sobrecarga y además hay que tener cuidado para evitar problemas de concurrencia.

