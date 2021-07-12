from django.urls import path
from .import views

urlpatterns=[
    path('commentcreate/<int:post_id>', views.commentcreate, name='commentcreate'),
    path('/edit', views.edit, name="edit"),
    path('/postupdate/<int:comment_id>', views.postupdate, name='postupdate'),
    path('/postdelete/<int:comment_id>', views.postdelete, name='postdelete'),
]