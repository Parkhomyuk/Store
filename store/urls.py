from django.urls import path

from store.views import BrandDetail, BrandList, CategoryDetail, CategoryList, ProductDetails, ProductList, SubcategoryDetail, SubcategoryList

urlpatterns=[
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view()),
    path('subcategory/', SubcategoryList.as_view()),
    path('subcategory/<int:pk>', SubcategoryDetail.as_view()),
    path('brands/', BrandList.as_view()),
    path('brands/<int:pk>', BrandDetail.as_view()),
    path('<int:pk>', ProductDetails.as_view()),
    path('', ProductList.as_view())
    
]