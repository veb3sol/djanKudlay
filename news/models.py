from django.db import models

# Планируем поля в Новостях
"""
id  -- INT
title -- Varchar
content -- Text
created_at -- DateTime
updated_at -- DateTime
photo -- Image
is_published  -- Boolean
"""

class News(models.Model):
    title = models.CharField(max_length = 150, verbose_name='Заголовок')
    # max_length = 150   -- максимальная длина строки, обьязательный атрибут
    content = models.TextField(blank = True, verbose_name='Контент')
    # blank = True  -- поле не обязательное к заполнению, по умолчанию все поля обьязательны к заполнению
    created_at = models.DateTimeField(auto_now_add = True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Відредактовано')
    # auto_now_add = True  -- запишет только дату создания, при перезаписи данные даты и времени не поменяются
    # auto_now = True  -- перезаписывает дату и время при каждом обновлении
    photo = models.ImageField(upload_to = 'photo/%Y/%m/%d', verbose_name='Фото', blank = True)
    # upload_to = 'photo/%Y/%m/%d'  -- куда сохранять фото при загрузке, Y - год, m - месяц, d - день
    is_published = models.BooleanField(default = True, verbose_name = 'Опубліковано')
    # default = True -- значение по умолчанию
    category = models.ForeignKey('Category', on_delete = models.PROTECT, null = True, verbose_name = 'Категорія')    # связывание с моделью Категории
    # 'Category' - как строка если класс модели Категории указан ниже
    # Category - как название класса если класс модели Категории указано выше
    # on_delete = models.PROTECT  -- не позволяем удалять категории если есть статьи такой категории
    # null = True  значение может быть null, потому что изначально у нас нету никакой категории

    # для того что бы не object представлял обьект а строка - например заголовок
    def __str__(self):
        return self.title

    # как модель будет отображаться в админке
    class Meta:
        verbose_name = 'Новина' # название в единственном числе
        verbose_name_plural = 'Новини'   # название в множественном числе
        ordering = ['-created_at']  # по какому полю сортировать - и на сайт тоже влияет, можно и по 2 полям

class Category(models.Model):
    title = models.CharField(max_length = 150, db_index = True, verbose_name = 'Назва категорії')
    # db_index = True - индексировать для повышения скорости поиска по этому полю

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']

