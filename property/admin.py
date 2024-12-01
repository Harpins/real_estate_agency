from django.contrib import admin
from django.contrib import admin
from .models import Flat, Feedback, Owner


class OwnerInstanceInline(admin.StackedInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)
    
    
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by',)
    inlines = (OwnerInstanceInline,)
    
    
class FeedbackAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat_id',)
    search_fields = ('author',)
    
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ('owner',) 

admin.site.register(Flat, FlatAdmin)
admin.site.register(Feedback, FeedbackAdmin) 
admin.site.register(Owner, OwnerAdmin) 

