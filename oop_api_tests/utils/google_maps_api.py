from utils.http_methods import HttpMethods


class GoogleMapsAPI:
    base_url = 'https://rahulshettyacademy.com'
    key = '?key=qaclick123'

    @staticmethod
    def create_new_location(body):
        url = 'https://rahulshettyacademy.com/maps/api/place/add/json?key=qaclick123'
        print(f'\nURL: {url}')
        response = HttpMethods.post(url=url, body=body)
        print(f'Тело ответа:\n{response.text}')
        return response

    @staticmethod
    def get_location(place_id):
        url = f'{GoogleMapsAPI.base_url}/maps/api/place/get/json{GoogleMapsAPI.key}&place_id={place_id}'
        print(f'\nURL: {url}')
        response = HttpMethods.get(url=url)
        print(f'Тело ответа:\n{response.text}')
        return response

    @staticmethod
    def update_location_address(place_id, body):
        url = f'https://rahulshettyacademy.com/maps/api/place/update/json?key=qaclick123&place_id={place_id}'
        print(f'\nURL: {url}')
        response = HttpMethods.put(url, body)
        print(f'Тело ответа:\n{response.text}')
        return response

    @staticmethod
    def delete_location(place_id, body):
        url = f'https://rahulshettyacademy.com/maps/api/place/delete/json?key=qaclick123&place_id={place_id}'
        print(f'\n{url}')
        response = HttpMethods.delete(url=url, body=body)
        print(f'Тело ответа:\n{response.text}')
        return response
