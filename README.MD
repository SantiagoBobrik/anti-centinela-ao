

# Anti centinela Argentum Online

**IMPORTANTE**: Este script es solo para fines educativos y no debe utilizarse con fines ilegales.

Este script fue diseñado para vulnerar el sistema de centinelas en el juego Argentum Online. Utiliza las siguientes librerías:

*   PyAutoGUI: para tomar capturas de pantalla
*   PyTesseract: para convertir imágenes a texto


## Requisitos

Para poder ejecutar este script, es necesario tener instaladas las siguientes dependencias:

*   PyAutoGUI
*   PyTesseract
*   Tesseract-OCR

Es necesario también especificar la ruta al ejecutable de Tesseract-OCR en la línea `pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"`.

## Ejecución

Una vez se han instalado las dependencias necesarias, se puede ejecutar el script para iniciar el proceso de vulneración del sistema de centinelas.

1.  Se tomará una captura de pantalla en una region del juego (modo ventana).
2.  Se mejorará la imagen reduciendo su profundidad de color.
3.  Se convertirá la imagen a texto utilizando PyTesseract.
4.  Se buscará un número en el texto obtenido.
5.  Si se encuentra un número, se escribirá  el comando `/centinela` seguido del numero encontrado.
6.  Este proceso se repetirá cada segundo.

