from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "articles"
router = routers.DefaultRouter()
router.register("", views.ArticleViewSet, basename="article")
# router.register("comment", views.CommentViewSet, basename="comment")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "<int:article_pk>/comment",
        views.CommentViewSet.as_view({"post": "create", "get": "list"}),
    ),
    path(
        "<int:article_pk>/comment/<int:pk>",
        views.CommentViewSet.as_view(
            {"put": "update", "patch": "partial_update", "delete": "destroy"}
        ),
    ),
    path(
        "<int:article_pk>/comment/<int:comment_pk>/recomment",
        views.ReCommentViewSet.as_view({"post": "create", "get": "list"}),
    ),
    path(
        "<int:article_pk>/comment/<int:comment_pk>/recomment/<int:pk>",
        views.ReCommentViewSet.as_view(
            {"put": "update", "patch": "partial_update", "delete": "destroy"}
        ),
    ),
]
