from django.contrib import admin

# Taskモデルをインポート
from .models import Thread, Comment

# 管理サイトへのモデルを登録
admin.site.register(Thread)
admin.site.register(Comment)