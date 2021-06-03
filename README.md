# Diseño de Compiladores

<h2>
    C Cuak Cuak Compiler
</h2>

<ul>
    <li>
        A01281459 Federico Alcerreca Treviño
    </li>
    <li>
        A01176573 Jaime Montemayor Molina
    </li>
</ul>
<p>
    El proyecto consta de diseñar y programar un compiador que compile nuestra propia especificación de un lenguaje patito basado en c++.
    Asi como la maquina virtual que lo corra junto con la documentación pertinente.
    El contenido esperado incluye:
    <ul>
        <li>
            Análisis de Léxico y Sintaxis
        </li>
        <li>
            Semántica Básica de Variables: Directorio de Procedimientos y Tabla de Variables
        </li>
        <li>
            Semántica Básica de Expresiones: Tabla de Consideraciones semánticas (Cubo Semántico)
            Generación de Código de Expresiones Aritméticas y estatutos secuenciales: Asignación, Lectura, etc.
        </li>
        <li>
            Generación de Código de Estatutos Condicionales: Decisiones/Ciclos
        </li>
        <li>
            Generación de Código de Funciones
        </li>
        <li>
            Mapa de Memoria de Ejecución para la Máquina Virtual
            Máquina Virtual: Ejecución de Expresiones Aritméticas y Estatutos Secuenciales
        </li>
        <li>
            Generacion de Código de Arreglos/Tipos estructurados
            Máquina Virtual: Ejecución de Estatutos Condicionales
        </li>
        <li>
            Documentación
            Generación de Código y Máquina Virtual para aplicación particular
        </li>
    </ul>
<p>
<h4>
    El reporte de cambios por entrega se verá documentado por este mismo medio.
</h4>

<h3>
    Entrega 1
</h3>
<p>
    Se hizo el lexer funcional sin errores, y la gramatica para el parser aun presenta errores, pero ya tenemos los diagramas para basarnos como se muestra en los archivos adjuntos.
</p>

<h3>
    Entrega 2
</h3>
<p>
    Se realiza la correción completa de la gramática junto con los documentos de pruebas de sintáxis y se realizan los cambios necesarios tanto en el lexer como en el documento de diagramas de sintaxis. 
    Actualmente no se pudo escribir a código lo que se esperaba para el avance pero estamos evaluando el esquema en el que se crearán las tablas de funciones y de variables. Esperamos seguir trabajando el día de mañana para pasarlo a código y crear los diagramas correspondientes.
</p>
<h3>
    Entrega 3
</h3>
<p>
    Se realiza una primera version de las estructuras para el directorio de funciones y la tabla de variables, junto con el diseño de las estructuras especificas para clases (directorio de clases y tabla de objetos) además de que se implementa el cubosemantico. Se corrige levemente gramatica (listaidDeclare y param) tanto en código como en los diagramas de documentación. Se genera la documentación de los puntos neuralgicos para entrega 2. Quedamos faltante con la implementación de estos mismos además de los cuadruplos.
</p>
<h3>
    Entrega 4
</h3>
<p>
    No se realizaron muchos cambios, debido a que estamos trabados con el directorio de funciones y tablas de variables, se cambio el archivo de estructuras y se implementaron metodos de inserción y chequeos semanticos de duplicados de id, para llamar en los puntos neuralgicos, pero aun no se implementan sus llamadas en dichos puntos, queda pendiente seguir los diagramas de puntos neuralgicos para la modificacion de la gramática.
</p>
<h3>
    Entrega 5
</h3>
<p>
    Sin cambios
</p>
<h3>
    Entrega 6
</h3>
<p>
    Cambio a Estructuras, Se genera un archivo de modificacion de tablas para ayudar con el manejo de funciones para directorio de funciones y tablas de variables. Se empiezan a hacer los puntos neuralgicos pertinentes a directorio de funciones y tabla de variables y queda "funcional" menos el aspecto de que no logramos manejar los dicionarios de manera dinamica nisiquiera con la funcion copy, cuando modificamos el original cambia la referencia a todo y cuando queremos limpiar la tabla de variables para reciclar, se borran todas. La estructura ya esta funcionando comprobado, nuevo test "test-tablaVariables-declarVar
</p>
<h3>
    Entrega 7
</h3>
<p>
    Directotio de Funciones y Tabla de Variables en implementación final definitiva, se termina Semantica Basica de Expresiones, ya se tenía el cubo pero no estaba implementado en puntos neuralgicos. Se termina generacion de cuadruplos pasa expresiones, estautos secuenciales de todo menos llamada de funciones, se termina generacion de cuadruplos pasa ciclos. Todo con sus tests de funcionalidad y semantica
</p>
<h3>
    Entrega 8
</h3>
<p>
    Terminamos la generación de cuadruplos para código de funciones e implementacion de parche guadalupano. Junto con su set de tests para funcionalidad y semántica.
</p>
<h3>
    Entrega FINAL
</h3>
<p>
    Terminada la generacion de cuadruplos de arreglos, se crea el escritor del obj para código intermedio, terminamos el lector del codigo intermedio del lado de la maquina virtual y logramos sacar adelante el manejo de memoria y todas las acciones de ejecución fuera del scope de orientada a objetos. Clases, metodos, atributos de clase y objetos no estan soportados en nuestra version fonal del compilador.
    Se hicieron pruebas para todos los operadores aritmeticos, condiciones, ciclos, input/output, llamada de funciones y manejo de arreglos. Todo parece estar funcionando.

