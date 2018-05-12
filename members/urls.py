"""Members URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.decorators import login_required
from members import views

urlpatterns = [
    # path('search/', views.search_member, name='search_member'),
    # path('delete/<int:id>/', views.delete_member, name='delete_member'),
    # path('update/<int:id>/', views.update_member, name='update_member'),
    path('feedback/new/',
         login_required(views.SendFeedbackView.as_view()),
         name='send-feedback'
        ),
    path('feedback/thanks/',
         login_required(views.FeedbackThanksView.as_view()),
         name='thanks-feedback'
        ),
    path('new/',
         login_required(views.AddMember.as_view()),
         name='add-member'
        ),
    path('',
         login_required(views.ListMembers.as_view()),
         name='member-list'
        ),
]
