"""aplikacja_koncowa_v4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from api import router

from webadminpanel.views import LoginUserView, LogoutUserView, AddUserView, LoggedInView, UsersView, MediaView, \
    AddMediaView, EditMediaView, DeleteMediaView, GroupView, AddGroupView, EditGroupView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', LoginUserView.as_view(), name="index"),
    url(r'^logout$', LogoutUserView.as_view(), name="logout"),
    url(r'^login$', LoginUserView.as_view(), name="login"),
    url(r'^add-user$', AddUserView.as_view(), name="add-user"),
    url(r'^logged-in$', LoggedInView, name="logged-in"),
    url(r'^users$', UsersView.as_view(), name="users"),

    url(r'^media$', MediaView.as_view(), name="media"),
    url(r'^add-media$', AddMediaView.as_view(), name="add-media"),
    re_path(r'^edit-media/(?P<media_id>(\d)+)$', EditMediaView.as_view(), name="edit-media"),
    re_path(r'^delete-media/(?P<media_id>(\d)+)$', DeleteMediaView.as_view(), name="delete-media"),

    url(r'^group$', GroupView.as_view(), name="group"),
    url(r'^add-group$', AddGroupView.as_view(), name="add-group"),
    re_path(r'^edit-group/(?P<group_id>(\d)+)$', EditGroupView.as_view(), name="edit-group"),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/users/', include(router.urls)),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

