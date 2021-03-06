from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from . import views as views

urlpatterns = [
    url("admin/", admin.site.urls),
    url("^$", views.index, name="index"),
    url("^sign-up/$", views.sign_up, name="sign_up"),
    url("^login/$", views.user_login, name="login"),
    url("^logout/$", views.user_logout, name="logout"),

    # Portal routes
    url("^dashboard/$", views.dashboard, name="dashboard"),
    url("^leaderboards/$", views.leaderboards, name="leaderboards"),

    # Activities URL routes
    url("^exercises/$", views.exercises, name="exercises"),
    url("^exercises/project-exercises/$", views.project_exercises, name="project_exercises"),
    url("^exercises/project-exercises/exercise/$", views.project_exercise, name="project_exercise"),

    url("^exercises/quiz-exercises/$", views.quiz_exercises, name="quiz_exercises"),
    url("^exercises/quiz-exercises/exercise/$", views.quiz_exercise, name="quiz_exercise"),
    url("^exercises/quiz-exercises/exercise/take-quiz/$", views.take_quiz, name="take_quiz"),
    url("^exercises/quiz-exercises/exercise/quiz-results/$", views.quiz_results, name="quiz_results"),

    # Profile views
    url("^@(?P<username>[^/]+)/$", views.profile, name="profile"),
    url("^@(?P<username>[^/]+)/edit/$", views.edit_profile, name="edit_profile"),
    url("^@(?P<username>[^/]+)/submit-project/$", views.submit_project, name="submit_project"),
    url("^@(?P<username>[^/]+)/edit-project/$", views.edit_project, name="edit_project"),

    # API views
    url("create-completed-quiz-exercise/$", views.create_completed_quiz_exercise, name="create_completed_quiz_exercise"),

    url('^', include('django.contrib.auth.urls')),
]

urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
