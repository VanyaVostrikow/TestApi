[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Test+API)](https://git.io/typing-svg)
# TestApi
#!!!ЕСЛИ ПОСТМАН ВЫДАЕТ ОШИБКУ CSRF-TOKEN - СБРОСЬ КУКИСЫ!!!
Роуты авторизации (auth)
========================
### /logout/ - выход из системы headers {} body{}
### /login/ - вход в систему headers{Authorization liwest 'key'}
### /whoami/ - Хто я? - headers{} body{}
#### /create/ - создание пользователя - headers {} body {'username', 'email', 'password'}
#### /gettoken/ - получить/создать токен - headers {} body {'username'\'email', 'password'}

Для авторизации нужно в хэдер передать:
---------------------------------------
### "Authorization":"liwest {key}"

 В Постмане у меня почему-то криво собирается хэдер, собираю через вкладку авторизации:
---------------------------------------------------------------------------------------
### type(API_KEY)
### KEY(Authorization)
### VALUE(liwest{key})

> Реализовал пользовательский класс фильтрации, без либ - 
> Дабы окончательно реализовать тот процесс, который хотел.

FILTER_METHOD
=============
### ?(filter_field)=(value) - частичное совпадение
### ?(price_less) - цена МЕНЬШЕ чем искомое
### ?(price_more) - цена БОЛЬШЕ чем искомое
### ?(price_equal) - полное совпадение по цене

> Не стал реализовывать больше_или_равно и меньше_или_равно, но если что
> достаточно просто переопределить фильтрацию queryset в filterset.py

SEARCH_METHOD
=============
### ?(search_by) + _name or _price - поиск по точному совпадению цены или имени. поиск только для товара, типа хз, можно искать и через фильтрацию

> насчет обратного слеша, реализовал как в ТЗ - работает и с слешем, и без слеша,
> через 300-статус. Но может эксептить при пользовании с обратным слешем, нормальлно
> не переопределил модель роутера, юзал симплроутер, с переопределенными роутами

*** ЧТО Я БЫ СДЕЛАЛ:
====================

> класс фильтрации прописан хреново, не расширяемо.
> переписал бы на авто получение полей моделей, инициализацию класса не по 
> queryset а по модели. Изначально так и хотел, но затупил, и в итоге реализовал другую
> модель. 
> Декомопозировал бы класс роутера, + переработал бы его с обработчиком исключений
> Переработал бы полностью модель аутентификации и вообще приложение Auth
