import cv2


class Camera:
    def __init__(self) -> None:
        self._usuario = ''
        self._senha   = ''
        self._ip      = '192.168.1.108'
        self._porta   = '80'

    
    def capturar_foto(self):
        url = 'http://'+str(self._usuario)+':'+str(self._senha)+'@'+\
            str(self._ip)+':'+str(self._porta)+\
            '/cgi-bin/snapshot.cgi'

        camera  = cv2.VideoCapture(url)
        status, img_camera = camera.read()
        return img_camera