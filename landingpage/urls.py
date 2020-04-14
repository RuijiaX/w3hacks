from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views
from hackathon import views as hackathonViews
from app import views as appViews

urlpatterns = [
    url('admin/', admin.site.urls),
    url("^$", views.index, name="index"),
    url("^about/$", views.about, name="about"),
    url("^contact/$", views.contact, name="contact"),
    url("^login/$", views.user_login, name="login"),
    url("^register/$", views.register, name="register"),

    # # Hackathon views
    # url("^(?P<hackathon_id>[^/]+)/$", hackathonViews.index, name="index"),
    # url("^(?P<hackathon_id>[^/]+)/competitors/$", hackathonViews.competitors, name="competitors"),
    # url("^(?P<hackathon_id>[^/]+)/schedule/$", hackathonViews.schedule, name="schedule"),
    # url("^(?P<hackathon_id>[^/]+)/submissions/$", hackathonViews.submissions, name="submissions"),
    # url("^(?P<hackathon_id>[^/]+)/submit/$", hackathonViews.submit, name="submit"),
    # url("^(?P<hackathon_id>[^/]+)/awards/$", hackathonViews.awards, name="awards"),

    # App views
    url("^achievements/$", appViews.achievements, name="achievements"),
    url("^leaderboards/$", appViews.leaderboards, name="leaderboards"),

    # Activities URL routes
    url("^exercises/$", appViews.exercises, name="exercises"),
    url("^exercises/project-exercises/$", appViews.project_exercises, name="project_exercises"),
    url("^exercises/project-exercises/exercise/$", appViews.project_exercise, name="project_exercise"),
    url("^exercises/quiz-exercises/$", appViews.quiz_exercises, name="quiz_exercises"),
    url("^exercises/quiz-exercises/exercise/$", appViews.quiz_exercise, name="quiz_exercise"),
    url("^exercises/quiz-exercises/exercise/take-quiz/$", appViews.take_quiz, name="take_quiz"),
    url("^exercises/mini-exercises/$", appViews.mini_exercises, name="mini_exercises"),
    url("^exercises/mini-exercises/exercise/$", appViews.mini_exercise, name="mini_exercise"),

    # Hackathon views
    url("^hackathon/$", appViews.hackathon, name="hackathon"),
    url("^about-the-hackathon/$", appViews.about_the_hackathon, name="about_the_hackathon"),
    url("^past-hackathons/$", appViews.past_hackathons, name="past_hackathons"),
    url("^future-hackathons/$", appViews.future_hackathons, name="future_hackathons"),

    # Profile views
    url("^profile/(?P<user_id>[^/]+)/$", appViews.profile, name="profile"),
    url("^edit-profile/(?P<user_id>[^/]+)/$", appViews.edit_profile, name="edit_profile"),
    url("^logout/$", appViews.user_logout, name="logout"),

    # API views
    url("create-completed-quiz-exercise/$", appViews.create_completed_quiz_exercise, name="create_completed_quiz_exercise"),
]

urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
