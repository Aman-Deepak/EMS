from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('salary',views.salary,name='salary'),
    path('Dshow',views.Dshow,name='Dshow'),
    path('S_show',views.S_show,name='S_show')
]

# {% extends 'body.html' %}
# {% block content %}

# {% for te in tt %}
#     <p>code     :{{te.id}}</p>
#     <p>name     :{{te.name}}</p>
#     <p>position :{{te.position}}</p>
#     <p>DOB      :{{te.DOB}}</p>
#     <p>address  :{{te.address}}</p>
#     <p>basic pay:{{te.basic_pay}}</p>
#     <p>DOJ      :{{te.DOJ}}</p>
# {% endfor %}


# {% endblock %}