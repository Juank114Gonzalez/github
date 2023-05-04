from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path("", login_required(HomeView.as_view()), name="home"),
    path("logout/", signout, name="logout"),
    path(
        "projects/resources/",
        login_required(ResourceListView.as_view()),
        name="resources-list",
    ),
    path(
        "projects/resources/create/",
        login_required(ResourceCreateView.as_view()),
        name="resources-create",
    ),
    path(
        "projects/resources/<int:pk>/update/",
        login_required(ResourceUpdateView.as_view()),
        name="resources-update",
    ),
    path(
        "projects/resources/<int:pk>/delete/",
        login_required(ResourceDeleteView.as_view()),
        name="resources-delete",
    ),
    path(
        "projects/categories/",
        login_required(CategoryListView.as_view()),
        name="categories-list",
    ),
    path(
        "projects/categories/create/",
        login_required(CategoryCreateView.as_view()),
        name="categories-create",
    ),
    path(
        "projects/categories/<int:pk>/update/",
        login_required(CategoryUpdateView.as_view()),
        name="categories-update",
    ),
    path(
        "projects/categories/<int:pk>/delete/",
        login_required(CategoryDeleteView.as_view()),
        name="categories-delete",
    ),
    path(
        "projects/announcements/",
        login_required(AnnouncementListView.as_view()),
        name="announcements-list",
    ),
    path(
        "projects/announcements/create/",
        login_required(AnnouncementListView.as_view()),
        name="announcements-create",
    ),
    path(
        "projects/announcements/<int:pk>/update/",
        login_required(AnnouncementListView.as_view()),
        name="announcements-update",
    ),
    path(
        "projects/announcements/<int:pk>/delete/",
        login_required(AnnouncementListView.as_view()),
        name="announcements-delete",
    ),
    path(
        "projects/project/create/",
        login_required(ProjectCreateView.as_view()),
        name="project-create",
    ),
    path(
        "projects/project/create/<int:project_id>/requirements",
        login_required(Requirements2ProjectView.as_view()),
        name="project-create-requirements",
    ),
    path("", login_required(HomeView.as_view()), name="home"),
    path("logout/", signout, name="logout"),
]
