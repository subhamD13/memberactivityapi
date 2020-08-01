from django.contrib import admin
from .models import User, Timezone, Activity

admin.site.register(Timezone)
admin.site.register(Activity)
admin.site.register(User)