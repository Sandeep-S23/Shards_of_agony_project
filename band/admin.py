from django.contrib import admin
from . models import Song, Contact, Booking

admin.site.site_header = "Shrads Of Agony"
admin.site.site_title = "Shrads Of Agony Admin";

class ShradsOfAgonyAdmin(admin.ModelAdmin):
	readonly_fields = ('released_date',)
	list_display = ('title', 'released_date',)

admin.site.register(Song, ShradsOfAgonyAdmin)

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone',)	

admin.site.register(Contact, ContactAdmin)

class BookingAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone', 'schedule', 'book_date',)	

admin.site.register(Booking, BookingAdmin)