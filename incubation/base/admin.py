from django.contrib import admin


from .models import  Application, Account, SlotBooking
# Register your models here.


admin.site.register(Account)
admin.site.register(Application)
admin.site.register(SlotBooking)
