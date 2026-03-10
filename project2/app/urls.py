from django.urls import path



from .views import EmployeeListCreate, EmployeeRetrieveUpdateDestroy, EmployeeList, EmployeeCreate, EmployeeRetrieve

urlpatterns = [
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(), name='employee-retrieve-update-destroy'),
    path('employees/list/', EmployeeList.as_view(), name='employee-list'),
    path('employees/create/', EmployeeCreate.as_view(), name='employee-create'),
    path('employees/<int:pk>/retrieve/', EmployeeRetrieve.as_view(), name='employee-retrieve'),
]
