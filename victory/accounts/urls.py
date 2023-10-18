from django.urls import path,include
from accounts.views import CreateCustomUser,ProfileView,ProfileUpdateView,ProfileDeleteView


urlpatterns = [
   path('',include('django.contrib.auth.urls')),
   path('profile/', ProfileView.as_view(), name='profile'),
   path('register',CreateCustomUser.as_view(), name='accounts.create'),
   path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
   path('profile/delete/', ProfileDeleteView.as_view(), name='profile_delete'),

]