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
    title = models.CharField(max_length = 150)
    # max_length = 150   -- максимальная длина строки, обьязательный атрибут
    content = models.TextField(blank = True)
    # blank = True  -- поле не обязательное к заполнению, по умолчанию все поля обьязательны к заполнению
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # auto_now_add = True  -- запишет только дату создания, при перезаписи данные даты и времени не поменяются
    # auto_now = True  -- перезаписывает дату и время при каждом обновлении
    photo = models.ImageField(upload_to = 'photo/%Y/%m/%d')
    # upload_to = 'photo/%Y/%m/%d'  -- куда сохранять фото при загрузке, Y - год, m - месяц, d - день
    is_published = models.BooleanField(default = True)
    # default = True -- значение по умолчанию



