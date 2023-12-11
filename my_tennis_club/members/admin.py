from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('get_fullname', 'age' , 'phone', 'joined_date')

    def get_fullname(self, obj):
        return f"{obj.firstname} {obj.lastname}"
    get_fullname.short_description = 'Full Name'

    def age(self, obj):
        return obj.age

    def phone(self, obj):
        return obj.phone

    def joined_date(self, obj):
        return obj.joined_date
    age.short_description = 'Age'
    phone.short_description = 'Phone'
    joined_date.short_description = 'Joined Date'
# Register your models here.
admin.site.register(Member, MemberAdmin)

