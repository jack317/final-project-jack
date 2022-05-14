from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from final_project import views
from final_project.views import index


router = routers.DefaultRouter()
router.register('Paragraph', views.ParagraphView)
router.register('Saved', views.SavedView)

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
