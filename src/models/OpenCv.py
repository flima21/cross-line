import cv2 
import numpy as np
import Person

class OpenCv:
    
    def __init__(self, type_object: object):
        self.hog: cv2.HOGDescriptor = cv2.HOGDescriptor()
        self.cap: cv2.VideoCapture = cv2.VideoCapture(0)
        self.out: cv2.VideoWriter = None
        self.ret: bool = False 
        self.math_like: cv2.typing.MatLike = None # frame

        # size area to capture movements inside out or in
        self.rect_xa, self.rect_ya, self.rect_xb, self.rect_yb = 100,100, 500, 500
        self.thread_initialized = False 

        if isinstance(type_object,Person):
            self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
          
    def open_window_thread(self):
        try:
            if self.hog == None:
                return
            
            elif isinstance(self.hog, cv2.HOGDescriptor) == False:
                return 
            
            else: 
                self.thread_initialized = True
                cv2.startWindowThread()
        except Exception as e:
            print(e)
            print('aqui')

    def capture_movements(self,path_file: str = '../../ouput/', file_name: str = 'movie'):
        try:
            if self.thread_initialized == False:
                return 
            
            if self.cap.isOpened():
                self.out = cv2.VideoWriter(f'{path_file}{file_name}.avi',cv2.VideoWriter_fourcc(*'MJPG'),15.,(640,480))
                
                # while web cam is opening
                while True:
                    self.ret,self.math_like = self.cap.read()

                    if self.ret != True:
                        print('NOT CAPTURED THE FRAME BY FRAME')
                        break
                    
                    print(self.ret)
                    # size to capture with faster way
                    self.math_like = cv2.resize(self.math_like,(640,480))

                    # verify the scale 
                    gray = cv2.cvtColor(self.math_like,cv2.COLOR_RGB2HLS)

                    boxes, weights = self.hog.detectMultiScale(self.math_like, winStride=(8,8))
                    boxes = np.array([[x, y, x + w, y + h] for (x,y,w,h) in boxes])

                    for (xA, yA, xB, yB) in boxes:
                        # display the detected boxes in the colour picture
                        cv2.rectangle(self.math_like, (xA, yA), (xB, yB),(0, 255, 0), 2)

                    cv2.imshow('frame',self.math_like)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    
            self.dispose_capture()
        except Exception as e:
            print('aqui to com erro')
            print(e)

    def delimiter_area_capture(self, edges_size: tuple):
        try:
            for i in edges_size:
                self.rect_xa = i[0]
                self.rect_ya = i[1]
                self.rect_xb = i[2]
                self.rect_yb = i[3]
        except:
            pass

    def export_movie_generated(self) -> bool:
        try:
            if self.out == None:  
                raise Exception("Object not open to video export")
            
            # verify if is istance
            if isinstance(self.out, cv2.VideoWriter) == False:
                raise Exception("Object not VideoWriter")
            
            # create the file in ouput
            self.out.write(self.math_like.astype('uint8'))

        except Exception as e:
            print(e)
            print('aconteceu alguma coisa aqui *****')

    def dispose_capture(self):
        try:
            # close the webcam
            if self.cap:
                if self.cap.isOpened():
                    self.cap.release()
            
            # close the writer in video
            if self.out:
                if self.out.isOpened():
                    self.out.release()

            cv2.destroyAllWindows()
            cv2.waitKey(1)
        except Exception as e:
            print(e)