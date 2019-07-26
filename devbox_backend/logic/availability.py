import os
import subprocess

from logic.model.predict import predict

snacks = [
    "coconut almond butter clif bar",
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
    "maple & brown suggar quaker instant oatmeal",
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


def _copy_image_from_pi():
    copy_image_bash_command = [
        'scp',
        'pi@172.30.166.1:{pi_image_path}'.format(pi_image_path=pi_image_path),
        backend_image_path,
    ]
    subprocess.run(copy_image_bash_command)


def _map_predict_outputs_to_snack(predict_outputs):
    return {
        snack: {
          "availability": int(availability)
        }
        for snack, availability in zip(snacks, predict_outputs)
    }           


def get_latest_availability():
    _copy_image_from_pi()
    predict_output = predict(backend_image_path)
    return _map_predict_outputs_to_snack(predict_output)
