from django.urls import path, include

import users

urlpatterns = [
    path('users/', include('users.urls')),
    path('blog/', include('blog.urls')),
]
