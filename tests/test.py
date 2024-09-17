from OpenCv_Test import OpenCv
from Person_Test import Person

person_detect = Person()
test = OpenCv(person_detect)

test.open_window_thread()
test.capture_movements()
test.dispose_capture()
test.export_movie_generated()