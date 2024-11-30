from models.OpenCv import OpenCv
from models.Person import Person

person_detect = Person()
opencv = OpenCv(person_detect)

opencv.open_window_thread() # open thread the webcam
opencv.capture_movements() # capture the movements with video
opencv.export_movie_generated() # export the video
