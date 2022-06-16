from django.urls import path
from .views import (
    getRoutes,
    partyListCreate,
    
)

urlpatterns = [
    path('', getRoutes),
    path('party/', partyListCreate),
]
