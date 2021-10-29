# PROYECTO_MEMORY
 
# Funcionalidades agregadas

1. Contar y desplegar el número de taps: En este commit se implementó un contador directamente en la función ya definida tap(), el cual tiene un incremento de 1 cada vez que la función es llamada, y su valor es impreso en la terminal del IDE para el usuario. Así, aprovechando el uso de la terminal, también se añade una impresión de “all done” cuando las 64 casillas han sido reveladas, lo cual, a su vez, marca el fin del juego, si bien la ejecución no finaliza, ya que, de seguir haciendo clics, estos siguen siendo contabilizados.

2. Detectar cuando todos los cuadros se han destapado: Dado que esta funcionalidad involucra el uso de la ventana en la que se muestra el juego, este commit consistió en la adición de un ciclo en la función draw(); un ciclo que se ejecuta cada vez que la función es llamada, evaluando si las 64 casillas o tarjetas del juego ya han sido reveladas, lo cual, de ser afirmativo, implica la impresión de un mensaje para el usuario, pero esta vez no en la terminal del IDE.

3. Centrar el dígito en el cuadro: De forma similar a la funcionalidad anterior, este commit consistió en la modificación de los parámetros de la función write() dentro de la función draw() para los elementos del arreglo utilizado en la creación de las parejas que caracterizan a un juego de memoria, de tal manera que dichos elementos, ya sean números enteros, caracteres o cadenas de texto, se muestren al centro de cada casilla o tarjeta.

4. En lugar de números dentro de la tarjeta hay letras y símbolos: En este commit se creó un nuevo arreglo para contener las letras mayúsculas del alfabeto, así como 6 símbolos más para dar paso a los identificadores (más diferenciables) de las 32 parejas necesarias para la jugabilidad característica de este tipo de juegos, lo cual requirió de algunos métodos de la librería “string”, por lo que esta última fue importada.

5. Cambiar la imagen de fondo: Finalmente, en este commit se redefinió la variable correspondiente a la imagen utilizada en el juego. No obstante, fue necesario encontrar una imagen que se adecuara correctamente a la ventana de ejecución ya establecida por el código fuente.
