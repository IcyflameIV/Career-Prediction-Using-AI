from django.urls import path
from . import views

urlpatterns = [
    path('',views.predictor, name = 'predictor'),
    path('result',views.formInfo, name = 'result'),
    path('result',views.formInfo, name = 'pred1'),
    path('result',views.formInfo, name = 'pred2'),
    path('result',views.formInfo, name = 'pred3'),
    path('result',views.formInfo, name = 'pred4'),
    path('result',views.formInfo, name = 'pred5'),
    path('result',views.formInfo, name = 'pred6'),
    path('result',views.formInfo, name = 'pred7'),
    path('result',views.formInfo, name = 'pred8'),
    path('result',views.formInfo, name = 'pred9'),
    path('result',views.formInfo, name = 'pred10')
    ]