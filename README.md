# MarSav Tasador
## **Implementación del modelo de aprendizaje automático (deployment)**
## **¿Qué es la implementación de modelos?**

La implementación es el método mediante el cual se integra un modelo de aprendizaje automático en un entorno de producción existente para tomar decisiones comerciales prácticas basadas en datos. Es una de las últimas etapas del ciclo de vida del aprendizaje automático y puede ser una de las más engorrosas. A menudo, los sistemas de IT de una organización son incompatibles con los lenguajes tradicionales de creación de modelos, lo que obliga a los científicos de datos y a los programadores a dedicar un tiempo valioso y su capacidad intelectual a reescribirlos.

## **¿Por qué es importante la implementación del modelo?**

Para comenzar a utilizar un modelo para la toma de decisiones prácticas, debe implementarse de manera efectiva en producción. Si no puede obtener información práctica confiable de su modelo, entonces el impacto del modelo es muy limitado.

La implementación de modelos es uno de los procesos más difíciles para obtener valor del aprendizaje automático. Requiere coordinación entre científicos de datos, equipos de IT, desarrolladores de software y profesionales de negocios para garantizar que el modelo funcione de manera confiable en el entorno de producción de la organización. Esto presenta un gran desafío porque a menudo existe una discrepancia entre el lenguaje de programación en el que está escrito un modelo de aprendizaje automático y los lenguajes que su sistema de producción puede entender, y la recodificación del modelo puede extender la línea de tiempo del proyecto por semanas o meses.

Para aprovechar al máximo los modelos de aprendizaje automático, es importante implementarlos sin problemas en producción para que una empresa pueda comenzar a usarlos para tomar decisiones prácticas.


## **Objetivo:**

Nos proponemos adaptar uno de los modelos de predicción de precios de propiedades en Buenos Aires para su futura implementación. Nos basamos en una de las funcionalidades de la web de Properati, en la que es posible obtener una tasación online a partir de un form completado por el usuario sobre la propiedad que desea tasar. 
[Valuador Properati](https://www.properati.com.ar/tools/valuador-propiedades)

## **Pasos a seguir:**
1. Adaptar un modelo xgboost para predecir precios de propiedades en Buenos Aires.
2. Descargar el modelo a un archivo .sav o .model para su futuro uso, usando pickle o xgboost.
3. Crear una web app en python usando Flask, combiando con HTLM, CSS y Jinja2 en la que el usuario pueda ejecutar la consulta a partir de un form.
4. Usando OpenStreetMap y folium obtener las coordenadas lat y lon de la propiedad para: 
   - alimentar el modelo predictivo
   - plotear con folium la ubicación de la propiedad
5. Crear una página con algunos datos y visualizaciones interesantes para subir a la app.
6. Usando pythonanywhere.com y github realizamos el deployment de la app.

## **MarSavTasador:**

En el form inicial se agrupan los datos a completar por el usuario en 4 categorías:
1. Tipo de propiedad: Casa, Departamento, PH.
2. Ubicación: Calle, numeración, barrio y región.
3. Tamaño: Metros cuadrados cubiertos y descubiertos, cantidad de ambientes y cantidad de baños.
4. Amenities.

Con los datos provistos por el usuario se ejecuta la consulta al modelo para la tasación (predicción del precio en el modelo previamente entrenado y descargado). Al ejecutar la tasación se muestra al usuario la dirección provista, el valor de la propiedad (predicción) y la ubicación en un mapa.

## **Comentarios:**

Una de las ventajas de utilizar pythonanywhere es que gracias a las “[batteries included](https://www.pythonanywhere.com/batteries_included/)” gran parte de librerías de python se encuentran en los servidores instaladas para su uso. Por este motivo, con una cuenta free con 512MB es suficiente para realizar la implementación.

## **Files:**
- ‘aux_valuador_prop.ipynb’ contiene la adaptación del modelo xgboost
- ‘app.py’ contiene la aplicación usando flask, requests, folium, xgboost
- ‘0001.model’ contiene el modelo descargado 
- ‘templates’ contiene los archivos .html de la app
- ‘static’ contiene los archivos .css y las imágenes

## **Links**
[Web app deployed](https://marsavtasador.pythonanywhere.com/)
[Notebooks Properati](https://github.com/msavransky/properati)

