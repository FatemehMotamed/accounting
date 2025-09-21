
from django.urls import path
from . import views
urlpatterns = [
    path('', views.PaymentList.as_view() , name="home"),
    # path('payments/<str:full_name>', views.student_payment , name="student_payment"),
    # path('payments/',views.payments ,name="payments"),
]
