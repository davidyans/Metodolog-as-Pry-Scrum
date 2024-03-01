# ESCUELA POLITÉCNICA NACIONAL

---

**Integrantes:**

- Simbaña Ivan
- Suntasig Ariel
- Terán José
- Torres Jeremy
- Verdezoto José
- Yanez David

---

# Historias De Usuario

|***N°: 1***|**Título:** Interfaz de Usuario|
|-|-|
|**Historia de usuario:**|**Como** jugador de "3 en raya", **quiero** una interfaz de usuario intuitiva y atractiva, **para** tener una experiencia de juego agradable y fácil de entender|
|**Criterio de aceptación 1:**|**Dado** que el jugador inicia la aplicación, **cuando** se muestra la pantalla de inicio, **entonces** debe haber campos para ingresar los nombres de Player 1 y Player 2.|
|**Criterio de aceptación 2:**|**Dado** que el jugador está en la pantalla de juego, **cuando** se muestra el tablero, **entonces** los elementos de la interfaz deben ser claros y fácilmente distinguibles.|
|**Estimación**|12 horas|
|**Prioridad**|Alta|
|||


|***N°***|**Tarea**|
|-|-|
|1|Diseñar la pantalla de inicio con campos para los nombres de los jugadores.|
|2|Diseñar la pantalla de juego con un tablero interactivo y los nombres de los jugadores.|
|3|Crear indicadores visuales para el turno actual y el resultado del juego.|
|4|Implementar estilos CSS para hacer la interfaz atractiva y fácil de entender.|
|||


|***N°: 2***|**Título:** Funcionalidad|
|-|-|
|**Historia de usuario:**|**Como** jugador de "3 en raya", **quiero** poder jugar contra otro jugador alternando turnos, **para** disfrutar de una partida.|
|**Criterio de aceptación 1:**|**Dado** que es el turno de un jugador, **cuando** coloca una ficha en el tablero, **entonces** debe poder realizar su jugada sin problemas y pasar el turno al otro jugador|
|**Criterio de aceptación 2:**|**Dado** que se completa una línea de fichas del mismo jugador en el tablero, **cuando** se verifica el resultado del juego, **entonces** se debe mostrar el resultado (ganador o empate) de manera clara en la interfaz|
|**Criterio de aceptación 3:**|**Dado** que el juego ha terminado, **cuando** un jugador elige reiniciar el juego, **entonces** e debe restablecer el tablero y permitir que los jugadores comiencen una nueva partida.|
|**Estimación**|12 horas|
|**Prioridad**|Alta|
|||

|***N°***|**Tarea**|
|-|-|
|1|Implementar la lógica de alternancia de turnos entre los jugadores.|
|2|Desarrollar la lógica para verificar el resultado del juego (ganador o empate).|
|3|Crear un botón para reiniciar el juego.|
|4|Agregar una opción para salir del juego y volver a la pantalla de inicio.|
|||

|***N°: 3***|**Título:** Dockerización|
|-|-|
|**Historia de usuario:**|**Como** jugador de "3 en raya", **quiero** dockerizar la aplicación, **para** facilitar su despliegue y gestión en diferentes entornos.|
|**Criterio de aceptación 1:**|**Dado** que se ejecuta el comando para construir el contenedor, **cuando** el contenedor se crea correctamente, **entonces** la aplicación debe estar dockerizada y funcionar sin errores dentro del contenedor.|
|**Criterio de aceptación 2:**|**Dado** que el contenedor está en ejecución, **cuando** se accede a la aplicación a través del navegador web, **entonces**  la aplicación debe funcionar correctamente sin ningún error relacionado con la configuración del contenedor.|
|**Estimación**|12 horas|
|**Prioridad**|Alta|
|||

|***N°***|**Tarea**|
|-|-|
|1|La aplicación debe ser dockerizada y funcionar correctamente en un contenedor.|
|2|Se deben proporcionar instrucciones claras para construir y ejecutar el contenedor.|
|3|El contenedor debe contener todas las dependencias necesarias para ejecutar la aplicación sin problemas.|
|||