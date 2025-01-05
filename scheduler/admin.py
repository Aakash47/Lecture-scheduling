from django.contrib import admin
from . import models as s_model
# Register your models here.

admin.site.register(s_model.Course)
admin.site.register(s_model.Instructor)
admin.site.register(s_model.Lecture)