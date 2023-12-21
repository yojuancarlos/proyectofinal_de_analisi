# proyectofinal_de_analisi
 INTRODUCCIÓN
Despliegue y Documentación del Usuario:
Guía de Instalación: 
Instrucciones detalladas para instalar y configurar el software. En este documento claramente se debe presentar la información que permita al usuario instalar el aplicativo  en una máquina y ejecutarlo correctamente. Se deben tener en cuenta aspectos como las versiones del software instalado, librerías, módulos externos o cualquier herramienta  o recurso tecnológico utilizado en el proceso.
Instalaciones:
Las siguientes instalaciones son necesarias para ejecutar este proyecto:
Entorno virtual (preferible): Utilizar python -m venv .env para configurar un entorno virtual en tu sistema.


luego procede a activarlo con:
Bash: source .env/Scripts/activate
powershell: .\.env\Scripts\activate
Linux: source venv/bin/activate

si presenta problemas a la hora de crearlo o activalo pruebe el comando
Set-ExecutionPolicy -Scope Process 
-ExecutionPolicy Bypass 
utiliza python pip install -r reqs.txt para instalar todos los requisitos para del proyecto.

Para ejecutar la aplicación después de la configuración del proyecto se ejecuta uvicorn main:app --reload en tu terminal.

Front
Para la instalación inicial use el comando npm i

Para la ejecución del proyecto Angular usar ng s.

Back
Para instalar el entorno virtual seguir los siguientes pasos:
Generar el entorno de ejecución con python -m venv .env
Activar el entorno de ejecución, en powershell se realiza mediante cerrar y abrir la terminal
Manual de usuario: Documentación que guía a los usuarios sobre cómo utilizar el software. Este manual puede presentar pantallazos de lo que se muestra al usuario y así explicar  todos los componentes  funcionales (menús, opciones, seguimiento con un ejemplo es aconsejable).

Frontend: Ejecutar npm i para instalar las dependencias de Angular.
Backend: Crear y activar un entorno virtual con python venv .env.
 Ejecución del Proyecto
Frontend: Utilizar ng s para iniciar el servidor de desarrollo de Angular.
Backend: Ejecutar el backend con el entorno virtual activado.
 Uso del Sistema
Iniciar sesión: Introducir credenciales y hacer clic en el botón de inicio de sesión.
Visualizar productos: Navegar a la sección de productos para ver la información detallada.
Documentación
 Especificación de Requisitos del Software (SRS): Describe los requisitos funcionales y no funcionales del sistema.

Propósito
   Este software tiene como objetivo principal la manipulación y análisis de datos utilizando la biblioteca Pandas, Numpy, Scipy, (back: FastAPI) (front: Angular) de Python. Se requiere la instalación y configuración de un entorno virtual para asegurar la ejecución correcta del proyecto.
 Alcance
    El sistema descrito en este documento permitirá a los usuarios realizar operaciones de manipulación y análisis de datos mediante el uso de Pandas. Se espera que los usuarios configuren un entorno virtual y satisfagan las dependencias necesarias antes de ejecutar el software.
Requisitos Funcionales
RF001 - Configuración del Entorno Virtual
El sistema debe permitir la creación de un entorno virtual utilizando python venv.
El sistema debe proporcionar instrucciones para activar el entorno virtual en sistemas Bash y Linux.

RF002 - Instalación de Pandas
 El sistema debe permitir la instalación de la biblioteca Pandas en el entorno virtual.
Se debe proporcionar una opción para instalar Pandas directamente usando pip install pandas.
Se debe proporcionar una opción para instalar todos los requisitos del proyecto a través de pip install -r requirements.txt.
RF003 - Ejecución de la Aplicación
El sistema debe permitir la ejecución de la aplicación principal mediante el comando python app/main.py en la terminal.
RF004 - Manipulación de Datos con Pandas
El sistema debe incluir funcionalidades para cargar, procesar y analizar datos utilizando Pandas.
Se debe permitir la lectura de datos desde fuentes externas, como archivos CSV o bases de datos.
Requisitos No Funcionales
RNF001 - Rendimiento
   La aplicación debe ser capaz de manejar grandes conjuntos de datos de manera eficiente.
RNF002 - Usabilidad
     La interfaz de usuario de la aplicación debe ser intuitiva y fácil de usar.

RNF003 - Mantenibilidad
     El código fuente debe seguir las mejores prácticas de codificación y ser fácilmente mantenible.
Carga de Datos
El sistema deberá ser capaz de cargar conjuntos de datos desde archivos externos en formatos compatibles con Pandas, como CSV, Excel, o HDF5.
Filtrado de Datos
Los usuarios podrán aplicar filtros a los conjuntos de datos cargados para seleccionar subconjuntos específicos de datos según criterios definidos.
Transformación de Datos
Se debe permitir a los usuarios realizar transformaciones en los datos cargados, como la agregación, la modificación de tipos de datos y la creación de nuevas columnas.

Diseño del Algoritmo: 

Arquitectura general:


Componentes del Sistema
Frontend (Angular)
UI/UX: Interfaz de usuario desarrollada con Angular, que proporciona la experiencia visual para los usuarios.
Lógica: Contiene la lógica de presentación y controla la interacción del usuario con la aplicación.
Comunicación: Se comunica con el backend mediante servicios RESTful para intercambiar datos.
Visualización: se permite al usuario observar los resultados finales de las dos matrices.
Backend (Python)
API: Define y gestiona las rutas y endpoints para la comunicación con el frontend.
Servicios: Contiene la lógica de negocio, procesamiento de datos y gestión de solicitudes del frontend.
Entorno Virtual: Configurado utilizando python venv para aislar las dependencias del proyecto.



diagramas de clases:








diagramas de secuencia:



Análisis de Datos
 Estadísticas Descriptivas
El sistema deberá proporcionar funciones para calcular estadísticas descriptivas básicas sobre los datos, como media, mediana, desviación estándar, etc.

Agrupación y Resumen
   Se deberá permitir a los usuarios agrupar datos según columnas específicas y resumirlos mediante funciones agregadas (suma, promedio, máximo, mínimo, etc.).

 Exportación de Resultados
El sistema deberá ser capaz de exportar los resultados del análisis a diferentes formatos de archivo, como CSV, Excel u otros formatos compatibles.


Entorno Virtual
Los usuarios deberán configurar un entorno virtual utilizando el comando python venv .env antes de ejecutar el sistema.

Activación del Entorno Virtual
El entorno virtual deberá ser activado utilizando el siguiente comando, según el sistema operativo:
Bash: source .env/Scripts/activate
Linux: source venv/bin/activate
 Dependencias
 Instalación de Pandas
 Los usuarios podrán instalar la biblioteca Pandas en su entorno virtual mediante el comando python pip install pandas. Alternativamente, podrán instalar todas las dependencias del proyecto utilizando python pip install -r requirements.txt.

Se deberá proporcionar documentación detallada que describa la estructura del proyecto, las funciones disponibles y ejemplos de uso.

 Compatibilidad
    El sistema deberá ser compatible con las versiones específicas de Python y Pandas indicadas en la documentación.
 Este documento establece los requisitos necesarios para el desarrollo y ejecución del software. Cualquier cambio en estos requisitos deberá ser documentado y gestionado adecuadamente.
Diseño del Algoritmo: Detalla la arquitectura y el diseño del sistema, incluyendo diagramas de clases, diagramas de secuencia, y otros documentos relevantes. En esta sección deben explicar detalladamente la lógica detrás de la solución algorítmica propuesta. Aquí hay algunas secciones clave para abordar la estrategia algorítmica:
Descripción General del Algoritmo:
El objetivo principal del problema es evaluar cómo la descomposición de un sistema complejo en subsistemas afecta la información total del sistema. Esto se hace comparando la distribución de probabilidades del sistema completo con la de sus subsistemas combinados.  para ello usamos el enfoque top-down que  comienza con el sistema en su estado más complejo y lo descompone progresivamente en componentes más simples para análisis.
Estrategia Algorítmica
Análisis del Sistema Completo:
Primero se hace un cálculo inical para ello se  calcula la distribución de probabilidades del sistema completo. Esto implica el uso de matrices de transición de probabilidades para modelar cómo el sistema evoluciona de un estado a otro y guarda esta distribución para comparaciones futuras.
Descomposición en Subsistemas:
Se divide el sistema en dos o más subsistemas. Esta división puede basarse en diferentes criterios, como la separación funcional o estructural dentro del sistema.
Se calcula las distribuciones de probabilidades para cada subsistema. Este paso puede requerir marginalización, donde se ignoran ciertas variables para enfocarse en un subconjunto específico del sistema.
Recombinación de Subsistemas:
Utilizamos el producto tensor para recombinar las distribuciones de los subsistemas. Esto te da una nueva distribución que representa cómo los subsistemas interactúan entre sí luego Guardamos esta distribución para comparaciones futuras.
Comparación de Distribuciones:
luego utilizamos la EMD para comparar la distribución de probabilidades del sistema original con la distribución recombinada. La EMD mide cuánto "cuesta" transformar una distribución en otra, lo que en este caso, representa la cantidad de información perdida o alterada debido a la descomposición.
Cuanto mayor es la distancia, mayor es la diferencia entre el sistema original y su versión descompuesta, indicando una mayor pérdida de información.
Idea Detrás del Algoritmo
El algoritmo se basa en la idea de que un sistema complejo puede ser entendido y analizado de manera más efectiva al descomponerlo en partes más manejables. Al comparar cómo estas partes interactúan y se relacionan con el sistema completo, se puede obtener una comprensión más profunda de la estructura y la dinámica del sistema. La EMD proporciona una métrica cuantitativa para evaluar cuánto cambia la información del sistema debido a esta descomposición, permitiendo una evaluación objetiva de diferentes estrategias de descomposición.
o   Análisis de Complejidad:
Incluir un análisis de la complejidad temporal y espacial del algoritmo.
Usar las notaciones asintóticas para diferentes comportamientos del algoritmo, si de eso se tratase.
Análisis de la Complejidad Temporal:
Inicialización (método __init__):

Aquí no se realizan operaciones significativas. Es tiempo constante.
Complejidad Temporal: O(1)
Método run:
Marginalización: El método margin_row y las operaciones subsiguientes dependen del tamaño de la matriz, pero probablemente sean lineales.
Obtener dígitos y construir cadenas (concat_digits) también es lineal.
Obtener la TPM original implica acceder al DataFrame, que es tiempo constante.
Obtener particiones (método obtener_particiones) implica bucles anidados, pero el número de iteraciones es finito y no está directamente relacionado con el tamaño de la entrada.
El cálculo de EMD implica bucles anidados y operaciones de matriz, y su tiempo de ejecución depende del tamaño de los subsistemas.
En general, la complejidad temporal probablemente esté dominada por el cálculo de EMD dentro del bucle.
Complejidad Temporal: O(N^2 * M), donde N es el tamaño de los subsistemas y M es el tamaño de la matriz.
Método hallar_emd:
El método implica bucles anidados y operaciones de matriz, dependiendo del tamaño de los subsistemas.
El cálculo de EMD usando wasserstein_distance también depende del tamaño de las matrices de entrada.
Complejidad Temporal: O(N^2 * M), donde N es el tamaño de los subsistemas y M es el tamaño de la matriz.
Método obtener_particiones:
El método implica bucles anidados, pero el número de iteraciones es finito y no está directamente relacionado con el tamaño de la entrada.
Complejidad Temporal: O(P * Q), donde P y Q son los tamaños de future_states y current_states.
Método calculo_distribucion:

El método implica operaciones de matriz, marginalización y selección.
Complejidad Temporal: O(N * M), donde N es el tamaño de la matriz y M es el tamaño de los subsistemas.
Análisis de la Complejidad Espacial:
Estructuras de Datos:
El diccionario _tabla_resultados almacena resultados de EMD, pero su tamaño está limitado por el número de estados futuros y actuales únicos.
Otras variables son principalmente referencias a matrices y listas.
Complejidad Espacial: O(N), donde N es el número de estados futuros y actuales únicos.
Matrices:
Las matrices se representan mediante arrays de NumPy, y la complejidad espacial depende del tamaño de la matriz.
Complejidad Espacial: O(M), donde M es el tamaño de la matriz.
En general, la complejidad espacial del algoritmo está dominada por las matrices y el diccionario utilizado para almacenar los resultados de EMD. La complejidad temporal está dominada por las operaciones de matriz y los cálculos de EMD dentro de los bucles. Ten en cuenta que este análisis asume que las operaciones de matriz y los cálculos de EMD son los contribuyentes más significativos a la complejidad total.
o   Justificación de la Estrategia:
Ventajas
Permite un análisis profundo y detallado de cada subsistema. Al descomponer el sistema, se puede entender mejor cómo cada parte contribuye al comportamiento general.
Al dividir el sistema en partes más pequeñas, el problema se vuelve más manejable. Es más fácil trabajar con y analizar subsistemas más pequeños que con un sistema grande y complejo.
Proporciona una forma cuantitativa de medir la pérdida de información cuando el sistema se divide. La utilización de la EMD es un método robusto para comparar distribuciones de probabilidad.

Desventajas
El enfoque puede ser computacionalmente intensivo, especialmente en sistemas con muchos estados o cuando se utiliza la EMD para comparar distribuciones. Esto puede limitar la aplicabilidad del método a sistemas más pequeños o requerir un poder computacional significativo para sistemas más grandes.
Al descomponer un sistema, a menudo se asume que los subsistemas son independientes o que su interacción puede ser modelada de manera simple.
La recombinación de subsistemas para evaluar la distribución total puede ser compleja, especialmente si las interacciones entre los subsistemas son no-triviales.

Alternativas No Elegidas
Otras estrategias podrían haber incluido un enfoque bottom-up o métodos de simulación directa Sin embargo, estos métodos también tienen sus propias limitaciones, como la incapacidad de proporcionar análisis detallados de sistemas grandes (bottom-up) o la dependencia de extensas simulaciones que pueden no capturar todas las dinámicas del sistema (simulación directa).La estrategia elegida ofrece un equilibrio entre la capacidad de análisis detallado y la viabilidad computacional, aunque con el costo de una mayor complejidad y posibles suposiciones simplificadoras.
o   Diagramas y Pseudocódigo:

pseudocódigo 
Función calcularDistribuciónSistemaCompleto(sistema):
distribución = calcularDistribuciónProbabilidades(sistema)
devolver distribución
Función descomponerSistema(sistema):
subsistemas = dividirSistemaEnSubsistemas(sistema)
devolver subsistemas
Función calcularDistribucionesSubsistemas(subsistemas):
distribucionesSubsistemas = []
para cada subsistema en subsistemas:
distribución = calcularDistribuciónProbabilidades(subsistema)
agregar distribución a distribucionesSubsistemas
devolver distribucionesSubsistemas
Función recombinarDistribuciones(distribucionesSubsistemas):
distribuciónRecombinada = productoTensor(distribucionesSubsistemas)
devolver distribuciónRecombinada
Función compararDistribuciones(distribuciónOriginal, distribuciónRecombinada):
distanciaEMD = calcularEMD(distribuciónOriginal, distribuciónRecombinada)
devolver distanciaEMD
Función principal():
sistema = obtenerSistemaCompleto()
distribuciónOriginal = calcularDistribuciónSistemaCompleto(sistema)
 subsistemas = descomponerSistema(sistema)
distribucionesSubsistemas = calcularDistribucionesSubsistemas(subsistemas)
distribuciónRecombinada = recombinarDistribuciones(distribucionesSubsistemas)
 distancia = compararDistribuciones(distribuciónOriginal, distribuciónRecombinada)
imprimir "Distancia EMD entre distribuciones:", distancia
principal()
o   Manejo de Casos Especiales y Límites:
Para sistemas pequeños, el algoritmo es directo y eficiente. En sistemas grandes, se podrían implementar optimizaciones, como algoritmos de cálculo de distribuciones de probabilidad más eficientes, o aproximaciones para la EMD que reduzcan la complejidad computacional. Si los subsistemas resultantes tienen tamaños muy diferentes, el algoritmo maneja cada subsistema de manera individual, asegurando que la desigualdad en el tamaño no afecte la precisión de los cálculos de sus distribuciones de probabilidad.
En casos donde hay fuertes interdependencias, el algoritmo de recombinación (producto tensor) debe ser capaz de capturar estas interacciones complejas para que la distribución recombinada refleje fielmente el sistema original.
Para estados nulos o incompletos (por ejemplo, datos faltantes), el algoritmo podría incorporar métodos para manejar incertidumbres o emplear técnicas de imputación para estimar estos valores.
Eficiencia en Condiciones Extremas
En casos de sistemas muy grandes, el algoritmo podría beneficiarse de la paralelización, distribuyendo el cálculo de distribuciones de subsistemas en múltiples procesadores o nodos.
o   Optimizaciones Implementadas:
Eliminación de impresiones y comentarios innecesarios:
Retira impresiones y comentarios de depuración que no son necesarios en el código final.
Uso eficiente de Numpy:
Evita la creación innecesaria de arrays y utiliza operaciones vectorizadas de Numpy cuando sea posible.
Evitar copias innecesarias:
Asegúrate de que las operaciones en calculo_distribucion no generen copias innecesarias de la matriz.
Almacenamiento de resultados intermedios:
Almacena resultados intermedios directamente en la estructura de datos correspondiente en lugar de variables temporales.

o   Comparaciones con Otros Enfoques:
Enfoque Bottom-Up:
Este enfoque habría comenzado con los componentes individuales del sistema, construyendo gradualmente hacia el sistema completo.
por que se descarto: Un enfoque bottom-up podría ser menos eficiente en sistemas donde las interacciones y la dinámica global son cruciales para entender el comportamiento del sistema. Este método puede perder de vista el "panorama general" al centrarse demasiado en los detalles.
Estrategia Seleccionada: 
Enfoque Top-Down
La estrategia elegida fue un enfoque top-down, que implica analizar primero el sistema completo y luego descomponerlo en subsistemas para su estudio.
Comparación y Fortalezas Contra el Enfoque Bottom-Up:
Fortaleza del Top-Down: Proporciona una mejor comprensión de la dinámica global del sistema desde el principio. Al comenzar con una visión completa, se puede evaluar más eficazmente cómo las descomposiciones afectan el sistema en su conjunto.
Aplicabilidad: El enfoque top-down es particularmente valioso en sistemas donde las propiedades emergentes (que no son evidentes a nivel de los componentes individuales) son importantes.
o   Manejo de Recursos:
Gestión de Memoria
Uso de Estructuras de Datos Efectivas:
El algoritmo utiliza  estructuras de datos de numpy, que son eficientes en términos de memoria, especialmente para operaciones matriciales.El uso de operaciones matriciales eficientes en numpy minimiza el uso excesivo de memoria durante los cálculos. También se utiliza comprensión de  diccionarios y listas, ademas se utilizan tablas para el rápido acceso o lecturas y almacenamiento de datos .
para este proyecto utilizamos la marginalización la cual reduce el tamaño de las matrices con las que se trabaja, lo que puede disminuir significativamente la cantidad de memoria necesaria.

Eficiencia de CPU
Al almacenar resultados en funciones, el algoritmo evita calificaciones innecesarias, lo que ahorra tiempo de CPU. El algoritmo no intenta evaluar todas las descomposiciones posibles del sistema, sino que se enfoca en un conjunto manejable de descomposiciones, lo que reduce el tiempo de cálculo y el uso de CPU.


