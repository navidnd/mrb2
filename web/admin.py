from django.contrib import admin
from .models import ExersiseAdd, MovementAdd, UserWeight, Sizes, Fat, Muscle, MainUser

admin.site.register(MainUser)
admin.site.register(ExersiseAdd)
admin.site.register(MovementAdd)
admin.site.register(UserWeight)
admin.site.register(Sizes)
admin.site.register(Fat)
admin.site.register(Muscle)

# Register your models here.
