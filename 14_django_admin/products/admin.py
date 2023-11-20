from django.contrib import admin
from django.utils import timezone
from django.utils.safestring import mark_safe

from .models import Products, Review

# Register your models here.




admin.site.site_title = "Cosmios Title"
admin.site.site_header = "Cosmios Admin Portal"
admin.site.index_title = "Welcome to Cosmios Admin Portal"


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    classes = ('collapse',)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date', "update_date", 'is_in_stock','added_days_ago', 'how_many_review',"bring_img_to_list")
    list_editable = ('is_in_stock',)
    list_display_links = ('create_date',)
    list_filter = ('is_in_stock', 'create_date')
    ordering = ('-name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 25
    date_hierarchy = 'update_date'
    # fields = (('name', 'slug'), 'is_in_stock', 'description')

    inlines = [ReviewInline]

    readonly_fields = ("bring_image",)

    fieldsets = (
        (None, {
            "fields": (
                ('name', 'slug'), 'is_in_stock'
            )
        }),
        ('Optioals Settings', {
            "classes": ('collapse',),
            "fields": ('description',"image","bring_image"),
            "description": "You can use this sevtion for optionals settings"
        })
    )

    actions = ('is_in_stock',)

    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} ürün stoğa eklendi")

    # is_in_stock.short_description("İşaretlenen ürünleri stoğa ekle")


    def added_days_ago(self, product):
        fark = timezone.now() - product.create_date
        return fark.days
    
    def how_many_review(self, obj):
        count = obj.riviews.count()
        return count
    
    def bring_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src={obj.image.url} width=400 height=400></img>")
        return mark_safe(f"<h3>{obj.name} has not image </h3>")
    
    def bring_img_to_list(self, obj):
        if obj.image:
            return mark_safe(f"<img src={obj.image.url} width=50 height=50></img>")
        return mark_safe("******")

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'create_date', 'is_released')
    list_per_page = 50
    row_id_fields = ('product',)

admin.site.register(Products, ProductsAdmin)
admin.site.register(Review, ReviewAdmin)