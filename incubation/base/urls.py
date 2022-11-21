from django.urls import path
from . import views


urlpatterns = [
    path('booking',views.BookingForm.as_view(),name='booking'),
    path('approvedlist',views.ApprovedList.as_view(),name='approvedlist'),
    path('declinedlist',views.DeclinedList.as_view(),name='declinedlist'),
    path('pendinglist',views.PendingList.as_view(),name='pendinglist'),
    path('approving/<int:id>', views.Approving.as_view(),name='approving'),
    path('declining/<int:id>', views.Declining.as_view(),name='declining'),
    path('slots', views.Slots.as_view(), name='slots'),

]