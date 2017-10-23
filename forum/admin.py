from django.contrib import admin
from .models import Board,Topic

# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
