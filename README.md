# Django_Stripe

```sh
# Клонируйте репозиторий
git clone https://github.com/smirnovds1990/django_stripe.git
# Перейдите внутрь проекта
cd django_stripe
# Запустите контейнер
docker compose up --build
# Перейдите на http://0.0.0.0:8000/admin/
# Данные для входа: username: user, password: 123qwe123qwe
Создайте экземпляр Item, используя админку
# Перейдите на http://0.0.0.0:8000/item/1
# Нажмите на кнопку "Buy"
# Введите данные в форму
# Тестовые данные карты:
    # номер - 4242 4242 4242 4242
    # любая дата больше текущей
    # любой CVC-код
```
