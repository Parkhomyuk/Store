from django.contrib import admin
from .models import  CategoryPlaceTable, CategoryTable, Characteristic, CharacteristicType, ParentCharacteristic, ParentCharacteristicType, PriceProduct, Product, Brand


@admin.register(CategoryTable)
class CategoryTableAdmin(admin.ModelAdmin):
    list_display = ("name", "final_level")
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["subcategory"].queryset = CategoryTable.objects.filter(final_level=True)
        return form


# admin.site.register(Product)
admin.site.register(Brand)
 
admin.site.register(ParentCharacteristicType)
admin.site.register(CharacteristicType)
admin.site.register(ParentCharacteristic)
admin.site.register(Characteristic) 
admin.site.register(CategoryPlaceTable)
admin.site.register(PriceProduct)