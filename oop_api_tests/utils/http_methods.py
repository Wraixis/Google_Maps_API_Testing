import requests


class HttpMethods:
    headers = {
        'Authorization': 'Bearer ce5f1ed74f6b5ac788c78825c2b1143a7529b299c9ab49b2f97486db89e29f65'
    }

    @staticmethod
    def get(url):
        response = requests.get(url=url, headers=HttpMethods.headers)
        return response

    @staticmethod
    def post(url, body):
        response = requests.post(url=url, json=body, headers=HttpMethods.headers)
        return response

    @staticmethod
    def put(url, body):
        response = requests.put(url=url, json=body, headers=HttpMethods.headers)
        return response

    @staticmethod
    def patch(url, body):
        response = requests.patch(url=url, json=body, headers=HttpMethods.headers)
        return response

    @staticmethod
    def delete(url, body=None):
        if body:
            response = requests.delete(url=url, json=body, headers=HttpMethods.headers)
        else:
            response = requests.delete(url=url, headers=HttpMethods.headers)
        return response
