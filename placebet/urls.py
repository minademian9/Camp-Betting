from django.urls import path

from . import views


from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.index, name='index'),

    # ex: /bet/details/
    path('bets/', views.details, name='details'),



    path('placebet/', views.addBet, name='placingbet'),

    path('account/', views.accountView, name='myaccount'),

    path('mybetslist/', views.userbets, name='viewbetslist'),


    path('leadershipboard/', views.leaderboardView, name='leadershiptop'),

    path('allbets/', views.allbets, name='all_bets'),


    # POST urls
    path('addbet/', views.post_new_bet, name='addingbettoDB'),
    path('mybet/', views.post_bet_choice, name='addingChoicetoDB'),
    path('closebet/', views.close_bet, name='addingClosureBettoDB'),


    # Login

    path('login/',LoginView.as_view(),name="login_url"),
    path('logout/',LogoutView.as_view(next_page='/'),name="logout"),

    

 


    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),

    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

]
