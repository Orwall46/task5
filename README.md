# Тестовое задание

### Задание
См. [google.docs](https://docs.google.com/document/d/1frjtOtChwW7ZZ0pHcUQxMPNyteRW8WLKVSsBxTd5Kns/edit)

### Слово автора. 

Хотел бы поблагодарить за задание. Вы первые, кто предложил написать на 2.7, используя Django 1.11. Крутой опыт! 
Нашел интересную особенность. Я Celery запускал через Redis. Потратил несколько часов на изучение проблемы, которая возникала с редиской
![alt text](https://github.com/[Orwall46]/[reponame]/blob/[branch]/image.jpg?raw=true)
По итогу перешел на rabbitmq, там проблем не наблюдалось.

Долго думал, как можно отследить открытие письма. Глупый вариант - переход по ссылке в письме, менее глупый - интеграция с другой системой. Чуть более интересный - привязать чью-то бибилотеку, и мой - на половину рабочий. В голову пришла идея использовать встроенное изображение. Но, у меня не получилось придумать план, как отловить момент загрузки картинки на стороне клиента. Вроде бы запрос идет, а как мне его поймать не придумал. На каждого пользователя генерируется уникальный код, по которым мы можем отследить прочитал он или нет. 


### Запуск проекта
```
git clone ...
```
Install dependencies, run virtual environment
```
python -m venv .venv
```
```
cd .venv/scripts
```
```
activate
```
```
pip install -r requirements.txt
``` 
Run Django, Rabbit, Celery
```
cd Mail
```
```
python manage.py
```
```
docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```
```
celery -A Mail.celeryapp worker --pool=solo -l info
```

На главной странице реализована обычная отправка сообщений без Celery. Мы тут передаем переменную в шаблон и отправляем клиентам. 
Для отправки отложенных писем - используйте раздел в меню "Отложенная отправка"

Админ панель доступна по адресу http://127.0.0.1/admin/ для добавления новых пользователей и отслеживания прочтения письма.