import requests
import json
class Test_new_joke():
    def __init__(self):
        pass

    def test_get_all_categories(self):
        """"Получение всех доступных категорий шуток"""
        url = f"https://api.chucknorris.io/jokes/categories"
        result = requests.get(url)
        print("Статус код:" + str(result.status_code))
        # проверяем, что сервер отдал статус код 200. Выводим комментарий на экран, если не 200
        assert 200 == result.status_code, f"Ошибка: ожидаемый статус код 200, получен {result.status_code}"
        result.encoding = 'utf-8'
        # с помощью библиотеки json преобразовываем ответ от сервера в список с категориями
        categories_list = json.loads(result.text)
        # возвращаем категории из метода
        return categories_list

    def test_create_new_random_category_joke(self, categories_list):
        """"Получение по 1-ой шутке в каждой из переданных категорий"""
        category = input()

        if category in categories_list:
            url = f'https://api.chucknorris.io/jokes/random?category={category}'
            result = requests.get(url)
            print("Статус код:" + str(result.status_code))

            # добавили проверку, что каждый раз нам будет возвращаться 200
            assert 200 == result.status_code, f"Ошибка: ожидаемый статус код 200, получен {result.status_code}"

            # ответ от сервера преобразуем в json и выводим на экран только текст шутки
            check = result.json()
            check_info = check.get("value")

            # проверяем что нам действительно вернулись шутки в поле value и нет пропусков
            assert check_info != "", "Не прислали шутку!"

            print(check_info)
        else:
            print("Указанной категории нет в списке доступных!")


new_joke = Test_new_joke()
categories_list = new_joke.test_get_all_categories()
new_joke.test_create_new_random_category_joke(categories_list)
