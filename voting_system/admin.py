
from django.contrib import admin
from .models import Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'get_created_at')

    def get_created_at(self, obj):
        return obj.created_at
    get_created_at.admin_order_field = 'created_at'  # Makes it sortable
    get_created_at.short_description = 'Created At'  # Sets the column name


admin.site.register(Rating, RatingAdmin)

