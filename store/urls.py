from django.urls import path, include
from rest_framework import routers

from store.views import BrandDetail, BrandList,  CategoryPlaceTableViewSet, CategoryTableViewSet,  CharacteristicTypeTypeViewSet, CharacteristicViewSet, ParentCharacteristicViewSet,   ProductDetails, ProductList

router=routers.SimpleRouter()
 
 
router.register('characteristic_types', CharacteristicTypeTypeViewSet)
router.register('parent_characteristic', ParentCharacteristicViewSet)
router.register('product_characteristics', CharacteristicViewSet)
 
router.register('category_table', CategoryTableViewSet)
router.register('category_place', CategoryPlaceTableViewSet)

urlpatterns=[
    # path('category/', CategoryViewSet.as_view({'get':'list'})),
    # path('category/<int:pk>', CategoryViewSet.as_view({'put':'update'})),
    path('', include(router.urls)),
    
     
    path('brands/', BrandList.as_view()),
    path('brands/<int:pk>', BrandDetail.as_view()),
    path('<int:pk>', ProductDetails.as_view()),
    path('', ProductList.as_view())
    
]