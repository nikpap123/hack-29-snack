
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
    "origginal quaker instant oatmeal",
    "white cheddar cheez-it",
    "original turkey jerky",
    "black pepper beef jerky",
    "sea salt crunchy chickpeas",
    "creamy peanut butter jif power ups",
    "strawberry jif power ups",
]


def _map_predict_outputs_to_snack(predict_outputs):
    return {
        snack: availability
        for snack, availability in zip(snacks, predict_outputs)
    }   
         

def get_latest_availability():
    # TODO: get data from training model.
    predict_output = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    return _map_predict_outputs_to_snack(predict_output)