import requests


class Test_new_location():
    """Работа с новой локацией"""

    def __init__(self):
        pass

    def test_create_new_location(self):
        """Создание новой локации"""

        base_url = "https://rahulshettyacademy.com"  # базовый урл
        post_resource = "/maps/api/place/add/json"  # ресурс метода пост
        key = "?key=qaclick123"  # параметр для всех запросов

        post_url = base_url+post_resource+key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        print(result_post.text)
        print("Статус код:" + str(result_post.status_code))
        assert 200 == result_post.status_code

        if result_post.status_code == 200:
            print("Успешно! Создана новая локация")
        else:
            print("Провал!Запрос ошибочный")

#         проверяем, что поле статус содержит в себе значение ОК
        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Статус код ответа:" + check_info_post)
        assert check_info_post == "OK"
        print("Статус код ответа верен!")
        place_id = check_post.get("place_id")
        print("Place_id : " + place_id)

        """Проверка создания новой локации"""
        # place_id = "555"
        get_resource = "/maps/api/place/get/json"  # ресурс метода гет
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)


        print(result_get.text)
        check_get_info = result_get.status_code
        assert check_get_info == 200

        """Изменение созданной локации"""

        put_resource = "/maps/api/place/update/json"  # ресурс метода пут
        put_url = base_url + put_resource + key
        print(put_url)

        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_for_update_new_location)
        print("Ответ" + str(result_put.text))
        print(result_put.status_code)
        assert result_get.status_code == 200
        if result_put.status_code == 200:
            print("Успешно!! Изменение новой локации!")
        else:
            print("Провал!! Запрос ошибочный!")

        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print(check_put_info)
        assert check_put_info == "Address successfully updated"







new_place = Test_new_location()
new_place.test_create_new_location()