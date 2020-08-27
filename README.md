# Previsión de precios de alquiler en Barcelona para 2020 - 2021

Este es un proyecto de autoaprendizaje mediante el cuál pretendo realizar una previsión de precios de alquiler en Barcelona, un tema de gran interés ya que la 
vivienda es uno de los principales problemas en las grandes ciudades de España, sobretodo para la juventud. 

Aunque primero intenté aplicar la metodología ARIMA, tras varios intentos tuve que descartarla ya que los parámetros del modelo eran muy elevados haciendo imposible
la obtención de predictores estadísticamente eficientes. Por ello finalmente opté por el modelo Prophet de Facebook, que está bien documentado y tiene una guía de 
inicio que permite arrancar un proyecto con relativa facilidad: https://facebook.github.io/prophet/

Los tres archivos del proyecto son:
* code_prophet_v0.py el código del proyecto en Python.
* PrevisionAlquileres.ipynb el notebook en el que se documenta todo el proceso de análisis y simulación del modelo.
* datos_bcn.csv los datos utilizados.

Los datos se han conseguidos de:
* Web de Idealista: https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/alquiler/
* Web de Ayuntamiento de Barcelona: https://www.bcn.cat/estadistica/castella/index.htm

Espero poder ampliar el proyecto durante los próximos días. 
