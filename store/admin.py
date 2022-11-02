from django.contrib import admin
from .models import  CategoryPlaceTable, CategoryTable, Characteristic, CharacteristicType, FeedBack, FeedBackCascade, FeedBackOpinion, FeedBackOpinionType, FeedBackVote, ParentCharacteristic, ParentCharacteristicType, PriceProduct, PriceProductRepresent, Product, Brand


@admin.register(CategoryTable)
class CategoryTableAdmin(admin.ModelAdmin):
    list_display = ("name", "final_level")
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["subcategory"].queryset = CategoryTable.objects.filter(final_level=True)
        return form

@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    pass
@admin.register(FeedBackVote)
class FeedBackVoteAdmin(admin.ModelAdmin):
    pass
@admin.register(FeedBackCascade)
class FeedBackCascadeAdmin(admin.ModelAdmin):
    pass
@admin.register(FeedBackOpinionType)
class FeedBackOpinionTypeAdmin(admin.ModelAdmin):
    pass
@admin.register(FeedBackOpinion)
class FeedBackOpinionAdmin(admin.ModelAdmin):
    pass
 
# admin.site.register(Product)
admin.site.register(Brand)
 
admin.site.register(ParentCharacteristicType)
admin.site.register(CharacteristicType)
admin.site.register(ParentCharacteristic)
admin.site.register(Characteristic) 
admin.site.register(CategoryPlaceTable)
admin.site.register(PriceProduct)
admin.site.register(PriceProductRepresent)

 