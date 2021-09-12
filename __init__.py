import cv2
from camera import Camera


img_camera = Camera().capturar_foto()
cv2.imwrite('capturas/foto.png', img_camera)