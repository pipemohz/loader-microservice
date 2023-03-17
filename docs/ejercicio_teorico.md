# Desafío Teórico

## Procesos, hilos y corrutinas
### Un caso en el que usarías procesos para resolver un problema y por qué

La programación de procesos es la actividad del administrador de procesos que maneja la eliminación del proceso en ejecución de la CPU y la selección de otro proceso sobre la base de una estrategia particular. Los procesos son una parte esencial de los sistemas operativos de multiprogramación.
* Caso: Se puede utilizar para hacer codificación y decodificación de información por ejemplo en audio y videos porque son tareas vinculadas a la CPU en la que se ejecutan instrucciones que dependen de la velocidad del hardware.

### Un caso en el que usarías threads para resolver un problema y por qué

Un Thread también conocidos como sub-procesos o hilos es una característica que permite a una apliación realizar varias tareas a la vez (concurrentemente). Un thread es la unidad más pequeña a la cual un procesador puede asignar tiempo. Los hilos  poseen la secuencia más pequeña de instrucciones a ejecutar, estos se crean, ejecutan y mueren dentro de los procesos, siendo capaces de compartir información entre ellos.
* Caso: Utilizará threads para enviar requests HTTP porque son tareas relacionadas con usos externos (entrada/salida), Con los threads y los procesos seremos capaces de implementar la programación concurrente, y, dependiendo de la cantidad de procesadores la programación en paralelo.

### Un caso en el que usarías corrutinas para resolver un problema y por qué

Las corrutinas permiten escribir código asíncrono de forma secuencial, lo que reduce drásticamente la carga cognitiva, se usan porque son mucho más eficientes que los hilos. Varias corrutinas se pueden ejecutar utilizando el mismo hilo. Por tanto, mientras que el número de hilos que se pueden ejecutar en una aplicación es bastante limitado, se pueden lanzar tantas corrutinas como se necesite, el límite es casi infinito.
* Caso: Un servidor web que tiene múltiples conexiones simultáneas, requiere programar la lectura y la escritura de todas ellas. Esto se puede implementar usando corrutinas, porque cada conexión es una corrutina que lee / escribe una pequeña cantidad de datos, luego "cede" el control al programador, que pasa a la siguiente corrutina (que hace lo mismo) a medida que recorremos todos los disponibles relación.

## Optimización de recursos del sistema operativo

### Si tuvieras 1.000.000 de elementos y tuvieras que consultar para cada uno de ellos información en una API HTTP. ¿Cómo lo harías? Explicar.

Generaría una piscina de hilos para lanzar varias requests por hilo de manera concurrente, a medida que cada worker vaya resolviendo una tarea quedará disponible para ejecutar una nueva.

## Análisis de complejidad

### Dados 4 algoritmos A, B, C y D que cumplen la misma funcionalidad, con complejidades O(n²), O(n³), O(2n) y O (n log n), respectivamente, ¿Cuál de los algoritmos favorecerías y cuál descartarías en principio? Explicar por qué

En primera instancia descartaria el algoritmo B ( O(n³) ) y C( O(2n) ) cúbico y exponencial respectivamente porque su complejidad tiende aumentar más rápidamente que los otros algoritmos.
Finalmente, tengo el algoritmo A ( O(n²) ) y D ( O (n log n) ), cuadrático y logarítmico respectivamente, de los cuales escogería el logarítmico ya que su complejidad se mantiene casi linealmente.

### Asume que dispones de dos bases de datos para utilizar en diferentes problemas a resolver. La primera llamada AlfaDB tiene una complejidad de O(1) en consulta y O(n²) en escritura. La segunda llamada BetaDB que tiene una complejidad de O(log n) tanto para consulta, como para escritura. ¿Describe en forma sucinta, qué casos de uso podrías atacar con cada una?

En el escenario AlfaDB se podría resolver un caso de sistema de gestion de creditos, puesto que en la consulta O(1) se limita a entregar una clave única de un crédito asignado y en escritura O(n²) involucra un ciclo de búsqueda de registros de créditos existentes antes de crear uno nuevo.

En el caso de BetaDB se podría resolver un caso de estudios estadísticos ya que en la consulta y escritura O(log n) las operaciones se limitan a condiciones particulares, por ejemplo rango de edades definidos, sexo, etc.
