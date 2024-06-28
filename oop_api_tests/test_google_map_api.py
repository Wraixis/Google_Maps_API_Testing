from utils.checker import Checker
from utils.google_maps_api import GoogleMapsAPI


class TestGoogleAPI_Test:
    @staticmethod
    def test_full_cycle_google_maps():
        dictionary = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Petty Friend",
            "phone_number": "(+996) 777 98 11 89",
            "address": "103, Toktogula street",
            "types": [
                "pets’ shop",
                "shop"
            ],
            "website": "http://google.com",
            "language": "English-EN"
        }
        print('\nМЕТОД POST')
        response = GoogleMapsAPI.create_new_location(dictionary)
        json_body_dict = response.json()
        place_id = json_body_dict.get('place_id')
        Checker.check_status_code(response, 200)
        Checker.check_fields_list(response, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checker.check_field_value(response, 'status', 'OK')
        print('\nСОЗДАНИЕ ЛОКАЦИИ ===========> УСПЕХ')

        print('\nМЕТОД GET')
        response = GoogleMapsAPI.get_location(place_id)
        Checker.check_status_code(response, 200)
        Checker.check_fields_list(response,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        Checker.check_field_value(response, 'address', '103, Toktogula street')
        print('\nПОЛУЧЕНИЕ ЛОКАЦИИ ===========> УСПЕХ')

        dictionary = {
            "place_id": place_id,
            "address": "100, Isanova street",
            "key": "qaclick123"
        }

        address = dictionary.get('address')

        print('\nМЕТОД PUT')
        response = GoogleMapsAPI.update_location_address(place_id, dictionary)
        Checker.check_status_code(response, 200)
        Checker.check_field_value(response, 'msg', 'Address successfully updated')
        print('\nОБНОВЛЕНИЕ ЛОКАЦИИ ===========> УСПЕХ')

        print('\nМЕТОД PUT - GET')
        response = GoogleMapsAPI.get_location(place_id)
        Checker.check_status_code(response, 200)
        Checker.check_field_value(response, 'address', address)
        print('\nПОЛУЧЕНИЕ ИЗМЕНЕННОЙ ЛОКАЦИИ ===========> УСПЕХ')

        print('\nМЕТОД DELETE')
        dictionary = {
            "place_id": place_id
        }
        response = GoogleMapsAPI.delete_location(place_id, dictionary)
        Checker.check_status_code(response, 200)
        Checker.check_field_value(response, 'status', 'OK')
        print('\nУДАЛЕНИЕ ЛОКАЦИИ ===========> УСПЕХ')

        print(f'\nМЕТОД DELETE - GET')
        response = GoogleMapsAPI.get_location(place_id)
        msg_value = response.json()['msg']
        Checker.check_status_code(response, 404)
        Checker.check_field_value(response, 'msg', msg_value)
        print('\nПОЛУЧЕНИЕ УДАЛЕННОЙ ЛОКАЦИИ ===========> УСПЕХ')