import os
import subprocess
import cv2

from logic.model.predict import predict
from logic.model.person_model import load_rcnn_model 
from logic.model.person_model import detect_person 

snacks = [
    "coconut almond butter cliff bar",
    "strawberry fig bar",
    "lemonzest luna bar",
    "chocolate peanut butter luna bar",
    "peanut butter dark chocolate healthy grains kind bar",
    "oat & honey kind healthy grains kind bar",
    "dutch caramel & vanilla rip van wafels",
    "cookies & cream rip van wafels",
    "organic dried mango",
    "dried blenheim apricots",
    "kirkland organic fruit snacks",
    "cinnamon & spice quaker instant oatmeal",
    "maple & brown sugar quaker instant oatmeal",
    "apple & cinnamon quaker instant oatmeal",
    "original quaker instant oatmeal",
    "white cheddar cheez-it",
    "original turkey jerky",
    "black pepper beef jerky",
    "sea salt crunchy chickpeas",
    "creamy peanut butter jif power ups",
    "strawberry jif power ups",
]

user = os.environ.get('USER')
pi_image_path = '/home/pi/hack-29-snack/devbox_backend/image.jpg'
backend_image_path = '/Users/{user}/hack-29-snack/devbox_backend/image.jpg'.format(user=user)
frontend_image_path = '/Users/{user}/hack-29-snack/website/src/images/image.jpg'.format(user=user)
person_image_path = '/Users/{user}/hack-29-snack/devbox_backend/image.b0cc0fad.jpg'.format(user=user)

person_model = load_rcnn_model(os.path.abspath('logic/model/mask_rcnn_coco.h5'))
person_model.keras_model._make_predict_function()

def person_exists():
    img = cv2.imread(backend_image_path)
    if detect_person(person_model, img):
      return True
    else:
      return False

def _copy_image_from_pi():
    copy_image_bash_command = [
        'scp',
        '-P 19885',
        'pi@0.tcp.ngrok.io:{pi_image_path}'.format(pi_image_path=pi_image_path),
        backend_image_path,
    ]
    subprocess.run(copy_image_bash_command)

def _copy_image_to_frontend():
    copy_image_to_frontend = [
        'cp',
        backend_image_path,
        frontend_image_path
 
    ]
    subprocess.run(copy_image_to_frontend)

def _map_predict_outputs_to_snack(predict_outputs):
    return {
        snack: {
          "availability": int(availability)
        }
        for snack, availability in zip(snacks, predict_outputs)
    }           

def get_latest_availability():
    _copy_image_from_pi()
    if person_exists():
      print ("FOUND SOMEONE")
      return None
    _copy_image_to_frontend()
    predict_output = predict(backend_image_path)
    return _map_predict_outputs_to_snack(predict_output)
