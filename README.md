# Detección de Manos con OpenCV y MediaPipe

<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>

Este proyecto es un script en Python que utiliza las bibliotecas OpenCV y MediaPipe para detectar manos y sus puntos clave (landmarks) en imágenes estáticas. El script procesa una o más imágenes, identifica las manos presentes y marca los puntos de referencia en las mismas, guardando el resultado como nuevas imágenes anotadas.

## Descripción del Proyecto

El objetivo de este proyecto es demostrar cómo utilizar MediaPipe para la detección y seguimiento de manos en imágenes estáticas. El script carga imágenes, procesa cada una para detectar manos y sus landmarks, y luego dibuja estos puntos y las conexiones entre ellos sobre la imagen original. Finalmente, guarda las imágenes anotadas en el disco.

## Librerías Utilizadas

- **OpenCV (cv2)**: Biblioteca de código abierto enfocada en procesamiento de imágenes y visión por computadora. Se utiliza para cargar, procesar y guardar imágenes.

- **MediaPipe**: Framework desarrollado por Google que proporciona soluciones de aprendizaje automático listas para usar y optimizadas para dispositivos móviles y en tiempo real. En este proyecto, se utiliza el módulo de detección de manos de MediaPipe.

## Funcionamiento del Script

1. **Importación de Librerías**: Se importan las bibliotecas necesarias para el procesamiento de imágenes y la detección de manos.

   ```python
   import cv2
   import mediapipe as mp
   ```

2. **Inicialización de MediaPipe**: Se inicializan las utilidades de dibujo y el modelo de manos de MediaPipe.

   ```python
   mp_drawing = mp.solutions.drawing_utils
   mp_hands = mp.solutions.hands
   ```

3. **Lista de Imágenes a Procesar**: Se define una lista `IMAGE_FILES` que contiene los nombres o rutas de las imágenes a procesar. Por defecto, incluye `'hand.jpg'`, pero puedes agregar más imágenes o cambiarla según tus necesidades.

   ```python
   IMAGE_FILES = ['hand.jpg']
   ```

4. **Configuración del Modelo de Manos**: Se configura el modelo de detección de manos de MediaPipe especificando parámetros como el modo de imagen estática, el número máximo de manos a detectar y el umbral mínimo de confianza.

   ```python
   with mp_hands.Hands(
       static_image_mode=True,
       max_num_hands=2,
       min_detection_confidence=0.5) as hands:
   ```

5. **Procesamiento de Cada Imagen**:

   - **Lectura y Preprocesamiento**: Se lee cada imagen, se voltea horizontalmente (para crear un efecto espejo) y se convierte de BGR a RGB, ya que MediaPipe trabaja con imágenes en formato RGB.

     ```python
     image = cv2.flip(cv2.imread(file), 1)
     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
     ```

   - **Detección de Manos**: Se procesa la imagen con el modelo de MediaPipe para detectar manos y obtener los landmarks.

     ```python
     results = hands.process(image_rgb)
     ```

   - **Verificación de Detección**: Si no se detectan manos en la imagen, el script continúa con la siguiente.

     ```python
     if not results.multi_hand_landmarks:
         continue
     ```

   - **Anotación de la Imagen**: Para cada mano detectada, se obtienen las coordenadas de los landmarks y se dibujan sobre una copia de la imagen original. También se imprime en la consola la mano detectada (izquierda o derecha) y las coordenadas de la punta del dedo índice.

     ```python
     annotated_image = image.copy()
     for hand_landmarks in results.multi_hand_landmarks:
         # Obtener coordenadas y dibujar landmarks
         mp_drawing.draw_landmarks(
             annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
     ```

   - **Guardado de la Imagen Anotada**: La imagen con las anotaciones se guarda en el disco con un nombre único para evitar sobrescribir archivos existentes.

     ```python
     cv2.imwrite('annotated_image_' + str(idx) + '.png', cv2.flip(annotated_image, 1))
     ```

6. **Salida en Consola**: El script imprime en la consola información relevante, como la mano detectada y las coordenadas de la punta del dedo índice, lo que puede ser útil para depuración o análisis adicionales.

## Requerimientos

Para ejecutar este script, necesitas tener instaladas las siguientes dependencias:

- **Python 3.x**
- **OpenCV**: Puedes instalarlo usando `pip install opencv-python`
- **MediaPipe**: Puedes instalarlo usando `pip install mediapipe`

## Instrucciones de Ejecución

1. **Clonar el Repositorio**: Descarga o clona este repositorio en tu máquina local.

2. **Instalar Dependencias**: Asegúrate de instalar las bibliotecas requeridas:

   ```bash
   pip install opencv-python mediapipe
   ```

3. **Preparar las Imágenes**: Coloca las imágenes que deseas procesar en el mismo directorio del script o ajusta las rutas en la lista `IMAGE_FILES` dentro del código.

4. **Ejecutar el Script**: Ejecuta el script desde la línea de comandos:

   ```bash
   python nombre_del_script.py
   ```

   Asegúrate de reemplazar `nombre_del_script.py` con el nombre real del archivo del script.

5. **Ver Resultados**: Las imágenes anotadas se guardarán en el mismo directorio con nombres como `annotated_image_0.png`, `annotated_image_1.png`, etc.

## Notas Adicionales

- **Ampliación a Video en Tiempo Real**: Aunque este script está diseñado para imágenes estáticas, puedes modificarlo para procesar video en tiempo real cambiando el parámetro `static_image_mode` a `False` y adaptando el código para capturar frames desde una cámara o archivo de video.

- **Personalización**: Puedes ajustar los parámetros del modelo, como `max_num_hands` o `min_detection_confidence`, para adaptarlos a tus necesidades específicas.

- **Visualización en Pantalla**: Si deseas visualizar las imágenes anotadas en lugar de solo guardarlas, puedes utilizar `cv2.imshow()` y `cv2.waitKey()` en el script.

## Capturas de pantalla:

<span><img src="https://github.com/VintaBytes/Deteccion-de-Manos-con-OpenCV/blob/main/manos1.png"  width="320px"/></span>

<span><img src="https://github.com/VintaBytes/Deteccion-de-Manos-con-OpenCV/blob/main/manos2.png"  width="320px"/></span>


