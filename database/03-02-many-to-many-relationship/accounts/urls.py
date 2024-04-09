from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    # <str:username>
    # 변수를 위와 같이 전달받고 상단에 위치하면 
    # login, logout 같은 문자들이 다 username으로 인식하게 된다.
    # 그래서 아래와 같이 
    path('profile/<username>/', views.profile, name='profile'), 
    path('<int:user_pk>/follow.', views.follow, name='follow')
]
