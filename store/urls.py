from django.urls import path, include
from rest_framework import routers

from store.views import BrandDetail, BrandList, CategoryDetail, CategoryList, CategoryViewSet, ProductDetails, ProductList, SubcategoryDetail, SubcategoryList, SubcategoryWriteDetail

router=routers.SimpleRouter()
router.register('category', CategoryViewSet)

urlpatterns=[
    # path('category/', CategoryViewSet.as_view({'get':'list'})),
    # path('category/<int:pk>', CategoryViewSet.as_view({'put':'update'})),
    path('', include(router.urls)),
    path('subcategory/', SubcategoryList.as_view()),
    path('subcategory/<int:pk>', SubcategoryDetail.as_view()),
    path('subcategory_add/', SubcategoryWriteDetail.as_view()),
    path('brands/', BrandList.as_view()),
    path('brands/<int:pk>', BrandDetail.as_view()),
    path('<int:pk>', ProductDetails.as_view()),
    path('', ProductList.as_view())
    
]