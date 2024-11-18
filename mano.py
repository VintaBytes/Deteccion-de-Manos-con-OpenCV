# Importar las bibliotecas necesarias
import cv2  # OpenCV para procesamiento de imágenes y video
import mediapipe as mp  # MediaPipe para detección y seguimiento de manos

# Inicializar las utilidades de dibujo y el modelo de manos de MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Lista de archivos de imagen a procesar
IMAGE_FILES = ['hand.jpg']  # Reemplaza 'hand.jpg' con la ruta de tus imágenes

# Configurar el modelo de detección de manos de MediaPipe
with mp_hands.Hands(
    static_image_mode=True,       # True para imágenes estáticas (False para video en tiempo real)
    max_num_hands=2,              # Número máximo de manos a detectar
    min_detection_confidence=0.5  # Umbral mínimo de confianza para la detección
) as hands:
    # Iterar sobre cada imagen en la lista
    for idx, file in enumerate(IMAGE_FILES):
        # Leer la imagen y voltear horizontalmente (espejo)
        image = cv2.flip(cv2.imread(file), 1)
        # Convertir la imagen de BGR a RGB, ya que MediaPipe trabaja con imágenes RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Procesar la imagen para detectar manos y landmarks
        results = hands.process(image_rgb)
        # Imprimir la mano detectada (izquierda o derecha)
        print('Handedness:', results.multi_handedness)
        # Si no se detectan manos, continuar con la siguiente imagen
        if not results.multi_hand_landmarks:
            continue
        # Obtener las dimensiones de la imagen
        image_height, image_width, _ = image.shape
        # Crear una copia de la imagen para anotaciones
        annotated_image = image.copy()
        # Iterar sobre cada mano detectada
        for hand_landmarks in results.multi_hand_landmarks:
            # Obtener las coordenadas del punto de la punta del dedo índice
            index_finger_tip_x = hand_landmarks.landmark[
                mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width
            index_finger_tip_y = hand_landmarks.landmark[
                mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height
            print(
                f'Coordenadas de la punta del dedo índice: ('
                f'{index_finger_tip_x:.2f}, {index_finger_tip_y:.2f})'
            )
            # Dibujar los landmarks y las conexiones en la imagen anotada
            mp_drawing.draw_landmarks(
                annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        # Guardar la imagen anotada con un nombre único
        cv2.imwrite('annotated_image_' + str(idx) + '.png', cv2.flip(annotated_image, 1))
