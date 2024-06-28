from requests import Response


class Checker:

    @staticmethod
    def check_status_code(response, expected_status_code):
        assert response.status_code == expected_status_code
        print(f'Успешно! Статус код: {response.status_code}')

    @staticmethod
    def check_fields_list(response: Response, expected_fields_list):
        assert list(response.json()) == expected_fields_list
        print(f'Все поля присутствуют')

    @staticmethod
    def check_field_value(response: Response, field_name, expected_value):
        json_dict = response.json()
        assert json_dict.get(field_name) == expected_value
        print(f'Поле {field_name} - верно')

    @staticmethod
    def check_phrase_in_field_value(response: Response, field_name, expected_phrase):
        json_dict = response.json()
        assert expected_phrase in json_dict.get(field_name)
        print(f'Фраза в поле {field_name} - присутствует')

    @staticmethod
    def check_data_type(response: Response, expected_data_type):
        json_dict = response.json()
        assert type(json_dict) == expected_data_type
        print(f'Тип данных верный')

    @staticmethod
    def check_not_empty(response: Response):
        json_dict = response.json()
        assert len(json_dict) > 0
        print(f'Коллекция не пуста')
