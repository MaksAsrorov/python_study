import requests

class Test_new_joke():
    """Создание новой шутки"""

    # def test_create_new_joke(self):
    #     """"Создание случайной шутки"""
    #     url = "https://api.chucknorris.io/jokes/random"
    #     print(url)
    #     result = requests.get(url)
    #     print("Статус код:" + str(result.status_code))
    #     assert 200 == result.status_code
    #     if result.status_code == 200:
    #         print("Успешно! Мы получили новую шутку!")
    #     else:
    #         print("Провал!Запрос ошибочный")
    #     result.encoding = 'utf-8'
    #     print(result.text)
    #     check = result.json()
    #     # check_info = check.get("categories")
    #     # print(check_info)
    #     # assert  check_info == []
    #     # print("Категория верна")
    #     check_info_value = check.get("value")
    #     print(check_info_value)
    #     name = "Chuck"
    #     assert name in check_info_value

    def test_create_new_random_category_joke (self):
        """"Создание случайной шутки на определенную тему"""
        category = "sport"
        url = f'https://api.chucknorris.io/jokes/random?category={category}'
        print(url)
        result = requests.get(url)
        print("Статус код:" + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успешно! Мы получили новую шутку!")
        else:
            print("Провал!Запрос ошибочный")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        assert  check_info == ["sport"]
        # print("Категория верна")
        # check_info_value = check.get("value")
        # print(check_info_value)
        # name = "Chuck"
        # assert name in check_info_value

sport_joke = Test_new_joke()
sport_joke.test_create_new_random_category_joke()