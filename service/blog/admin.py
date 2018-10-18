# from django.apps import apps
from django.contrib import admin

from api_basebone.core.admin import ModelAdmin

from blog.models import Tag, Category, Article

# app_list = ['blog']

# for app_name in app_list:
#     application = apps.get_app_config(app_name)

#     for model in application.get_models():
#         admin.site.register(model)


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name', 'show', 'parent')

    class GMeta(ModelAdmin.GMeta):
        parent_attr_map = (
            ('parent', 'category_set', None),
        )


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ('id', 'title', 'is_public', 'author')

    class GMeta(ModelAdmin.GMeta):
        auth_filter_field = 'author'
