from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myproject import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base,name='base'),
    path('home', views.home,name='home'),
    path('bookview/', views.bookview,name='bookview'),
    path('bookcreate/', views.bookcreate,name='bookcreate'),
    path('deletepage/<int:id>', views.deletepage,name='deletepage'),
    path('book/<str:id>', views.book,name='book'),
    path('editpage/<str:id>', views.editpage,name='editpage'),
    path('update/', views.update,name='update'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
