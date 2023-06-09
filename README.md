# **Добрый день, это учебный проект NewsPaper от Skillfactory.**


## Модуль D1. Знакомство с Django.
### Что было сделанно:
1. Создан проект Django
2. Добавить в него 3 статические странички.
    /home/
    /about/
    /contacts/
    /admin/
        #login: admins
        #password: admins


## #Модуль D2. Модели.
### Что было сделанно:
1. Созданны 5 моделей
    Модель Author
    Модель Category
    Модель Post
    Модель PostCategory
    Модель Comment

### Сделанно в консоли Django.
1. Созданны два пользователя:
        u1=User.objects.create_user(username='Semen')
        u2=User.objects.create_user(username='Dmitry')
3. Созданны 2 автора:
        Autor.objects.create(autorUser=u1)
        Autor.objects.create(autorUser=u2)
3. Добавленны категории:
        Category.objects.create(name="IT")
        Category.objects.create(name="Politic")
        Category.objects.create(name="Tech")
4. Добавленны статьи и новости:
        Post.objects.create(autor=Autor.objects.get(id=1), categoryTypes="AR", title="Новинки рынка IT", text="В последнее время набираю популярность Iphone 13ProMax")
        Post.objects.create(autor=Autor.objects.get(id=2), categoryTypes="AR", title="Безопасность в Интернете", text="Чтобы обезопасить себя от вирусов в сети Интернет необходимо соблюдать следующие правила:")
        Post.objects.create(autor=Autor.objects.get(id=1), categoryTypes="NW", title="Последние новости политики", text="Сегодня Министр иностранных дел РФ совершил визит")
5. Присвоить им категории:
        Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
        Post.objects.get(id=1).postCategory.add(Category.objects.get(id=3))
        Post.objects.get(id=2).postCategory.add(Category.objects.get(id=1))
        Post.objects.get(id=3).postCategory.add(Category.objects.get(id=2))
6. Создал коментарии к постам:
        Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Autor.objects.get(id=2).autorUser, text="Хорошая статья")
        Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Autor.objects.get(id=1).autorUser, text="Отличная работа")
        Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Autor.objects.get(id=2).autorUser, text="Важная новость")
        Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Autor.objects.get(id=1).autorUser, text="Новость дополняется")
        Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Autor.objects.get(id=1).autorUser, text="Спасибо, стараюсь")
6. Применины функции like() и dislike() к статьям/новостям:
        Post.objects.get(id=1).like()
        Post.objects.get(id=1).like()
        Post.objects.get(id=1).like()
        Post.objects.get(id=2).like()
        Post.objects.get(id=2).like()
        Post.objects.get(id=3).dislike()
        Comment.objects.get(id=1).dislike()
        Comment.objects.get(id=3).dislike()
7. Обновил рейтинги пользователей:
        Autor.objects.get(id=1).update_rating()
        Autor.objects.get(id=2).update_rating()
8. Вывел:
    username
    рейтинг лучшего пользователя
        Autor.objects.order_by('-ratingAutor').values('autorUser', 'ratingAutor')[0]
9. Вывел:
    дату добавления 
    username автора, 
    рейтинг, 
    заголовок
    превью лучшей статьи
        Post.objects.order_by('-rating').values('dateCreation', 'rating', 'title')[0], Post.preview(Post.objects.order_by('-rating')[0])
10. Вывел все комментарии
    дата, 
    пользователь, 
    рейтинг, 
    текст)
        Comment.objects.filter(commentPost=Post.objects.order_by('-rating')[0]).values('dateCreation', 'commentUser', 'rating', 'text')


## Модуль D3. Представления и шаблоны
### Что было сделанно:
1. Создал новую страницу с адресом /news/
2. Вывел все статьи в виде
    заголовка
    даты публикации
    первых 20 символов текста
3. Сделал отдельную страницу для полной информации о статье /news/<id новости>
    Название
    текст
    дата загрузки в формате день.месяц.год.
4. Написал собственный фильтр censor, который заменяет буквы нежелательных слов в заголовках и текстах статей на символ «*»
5. Новые страницы используют шаблон default.html как основу.


## Модуль D4. Фильтры и формы
### Что было сделанно:
1. Постраничный вывод на /news/, на одной странице 10 новостей
2. Добавил страницу /news/search.
    по названию;
    по категории;
    позже указываемой даты.
3. Страницы создания, редактирования и удаления новостей и статей
    /news/create/
    /news/<int:pk>/edit/
    /news/<int:pk>/delete/
    /articles/create/
    /articles/<int:pk>/edit/
    /articles/<int:pk>/delete/


## Модуль D5. Авторизация и регистрация
### Что было сделанно:
1. Добавил форму ркгистрации на сайте с возможностью зарегистрироваться с помощью почты и пароля или через Yandex-аккаунт.
2. Создал группу authors, выдал ей права на создание и изменение новых записей в разделах «Статьи» и «Новости».


## Модуль D6. Работа с почтой и выполнение задач по расписанию
### Что было сделанно:
1. Добавил подписки на рассылки о новых материалах в категориях
    /news/subscriptions/
2. Реализовал отправку списка статей на почту подписчиков категорий на основе той же модели Subscriber


## Модуль D7. Работа с асинхронными задачами через Celery
### Что было сделанно:
1. Установил Redis
2. Установил Celery
3. Произвел необходимые конфигурации Django для соединения всех компонент системы
4. Реализовал рассылку уведомлений подписчикам после создания новости.
5. Реализовал еженедельную рассылку с последними новостями (каждый понедельник в 8:00 утра).