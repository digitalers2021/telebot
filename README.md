# :robot: Telebot

Este es el ejercicio nª 3 dentro del bootcamp del programa Digitalers

Profesor: Xavier Petit

Instituto: Telecom, Educacion IT


**Fecha de entrega: 30/08/2021**

**Forma de entrega:**

Un formulario en google forms con el link al repositorio forkeado,
nombre del grupo y mail, por cada integrante. Llegada la fecha se pasara el link para la entraga.

**Forma de trabajo:**

Un participante del grupo debe hacer un fork de este repositorio. 
El equipo trabaja sobre el repositorio forkeado.


## :triangular_flag_on_post: Objetivos

- Aprender y practicar la utilizacion de la libreria `requests` de python
- Comenzar a leer codigo de terceros
- Trabajo en equipo
- Aprender a interactuar con servicios de terceros, en este caso las API de Telegram
- Tener un primer acercamiento al armado de proyectos en Python (manejo de dependencias, modulos, imports, git, pip, etc)
- Practicar `refactorizacion`(1).
- Practicar conceptos relacionados a POO.

## :dart: Consignas

Las consignas se diven en dos tipos, la primer parte son consignas que requieren modificar el codigo. La segunda son preguntas para ser respondidas, pueden tener pseudocodigo pero no es necesario modificar el proyecto. 

La 4 es opcional. 

1. La funcion `register_message` en `telebot/telegram.py` cumple dos funciones en una: Registrar un mensaje en la base de datos y mandar un mensaje de bienvenida. 
Evaluar dicha funcion y separar ambas tareas.

2. Actualmente `get_updates` en `telebot/telegram.py` obtiene siempre toda la lista de novedades desde la API de telegram, sin embargo se le puede pasar un offset para traer mensajes desde el ultimo lugar que se leyo. Hacer los cambios necesarios para que traiga los mensajes en base a lo que guardo en la base de datos.

Leer: https://core.telegram.org/bots/api#update, los parametros de `offset` y `limit` en el apartado de `getUpdates`.

3. Que pasa si al chat se envia una imagen en vez de un texto?
Realizar los cambios necesarios para manejar dicha situacion. La imagen se puede guardar en el filesystem o la base de datos, pero es opcional, puede descartarse. 

**Opcional**
4. El bot solamente responde un mensaje de bienvenida. Continuar la interaccion con el bot o bien segun cual sea el mensaje de saludo dar alguna informacion determinada como el precio del dolar, el clima, etc. 

Las siguientes son consignas para responder en [respuestas.txt](respuestas.txt):

1. Que significa el `ON CONFLICT REPLACE` en la tabla `message` y que pasaria si no estuviera?

2. Cuales serian las ventajas y desventajas de pasar `telegram.py` a un paradigma orientado a objectos?

3. Hay algo que pueda generalizarse en `models.py` ?

4. Si solo **ciertos** usuarios pudieran hablar con el bot, que habria que modificar para que eso sea posible?


## :rotating_light: Precaucaciones

`telebot/conf.py` levanta la informacion del token del bot de un archivo `.env`. El repositorio de git tiene un `.gitignore` que impide que el archivo quede registrado en git/github. Tener en cuenta que si pone las credenciales en el codigo o en otros archivos esa informacion puede quedar publica.

## :zap: Recomendaciones 

1. Antes que nada, reproducir el environment. Esto significa tener una copia local del proyecto, probar la creacion de virtualenv, ejecutar el codigo, crear un bot, y asegurarse que todo funciona.
2. Utilizar https://github.com/digitalers2021/git_errors para probar el workflow de trabajo del equipo. Estar segur@s primero con como se va a trabajar en equipo.
3. El proyecto consta de varios archivos. Si se trabaja en paralelo lo recomendable es trabajar en archivos distintos para evitar conflictos al momento de un merge.
4. Cualquier problema es reversible. Si se tiene dudas con alguna operacion a realizarse en github, asegurarse que algun compañer@ tenga una copia saludable del repositorio. Pushear codigo a github. 


(1) Refactoring:

Refactoring es una practica muy comun en el desarrollo de software y un topic bastante discutido en la industria. Tanto que tiene su [propio libro](https://martinfowler.com/books/refactoring.html). En ese libro una de las definiciones es:

"Refactorear es una tecnica para reestructurar el cuerpo del codigo, alterando su estructura interna sin modificar su comportamiento exterior".  Martin Fowler.

Lo que nos importa en la refactorizacion es tener un codigo "mas limpio" preservando las APIs. En este caso nuestras api seran: `get_updates`, `send_message` e `init`. 

Por que si el codigo funciona es necesario refactorizar? Porque ante la necesidad de agregar nueva funcionalidad, si internamente el codigo se encuentra desordenado haciendo dificil razonar sobre él, el costo de agregar nueva funcionalidad va a ser cada vez mas alto. 

Por otro lado preservar las interfaces (APIs) hace a la usabilidad de nuestro codigo, da previsibilidad a quienes tengan que trabajar con el, y nos permite ocultar la complejidad de ciertas operaciones en un interfaz limpia `requests.get("https://www.google.com")` 

**Trabajar en un proyecto de software tiene que ser comodo primero para quienes trabajan en dicho codigo.**


## :memo: References

- [Telegram docs](https://core.telegram.org/bots)
- [Crear un entorno virtual en python](https://www.programaenpython.com/miscelanea/crear-entornos-virtuales-en-python/)
- [Crear entorno virtual, doc oficial](https://docs.python.org/es/3/tutorial/venv.html)
- [SQLite browser](https://sqlitebrowser.org/)
- [Refactoring](https://martinfowler.com/books/refactoring.html)
- [Refactoring book](https://refactoring.com/)
