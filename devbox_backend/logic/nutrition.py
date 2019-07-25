from csv import DictWriter
from csv import DictReader

nutrition_filename = 'nutrition.csv'
nutrition_file_fieldnames = [
    'brand',
    'kind',
    'name',
    'common_name',
    'calories',
    'fats',
    'carbohydrates',
    'protein',
    'cholesterol',
    'sodium',
    'potassium',
]


def _add_nutrition_to_file(
    nutrition_file,
    brand,
    kind,
    name,
    common_name,
    calories,
    fats,
    carbohydrates,
    protein,
    cholesterol,
    sodium,
    potassium,
):
    with open(nutrition_file, mode='a') as file:
        writer = DictWriter(file, fieldnames=nutrition_file_fieldnames)
        writer.writerow(
            {
                'brand': brand,
                'kind': kind,
                'name': name,
                'common_name': common_name,
                'calories': calories,
                'fats': fats,
                'carbohydrates': carbohydrates,
                'protein': protein,
                'cholesterol': cholesterol,
                'sodium': sodium,
                'potassium': potassium,
            }
        )


def _read_nutrition_from_file(nutrition_file):
    with open(nutrition_file, mode='r') as file:
        reader = DictReader(file, fieldnames=nutrition_file_fieldnames)
        return [dict(row) for row in reader]


def _process_common_name_from_nutrition(nutrition_data):
    nutrition_data = {snack_nutrition['common_name']: snack_nutrition for snack_nutrition in nutrition_data}
    for key, value in nutrition_data.items():
        del value['common_name']
    return nutrition_data


def get_nutrition_data(common_snack_name=None):
    nutrition = _process_common_name_from_nutrition(_read_nutrition_from_file(nutrition_filename))
    if common_snack_name is not None:
        return nutrition.get(common_snack_name, None)

    else:
        return nutrition
