#进行users子应用视图路由
from django.urls import path
from users.views import RegisterView

urlpatterns = [
    #1.路由参数，2.视图函数名
    path('register/', RegisterView.as_view(), name='register'),
]
