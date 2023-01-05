from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("chores/", views.chores_index, name="index"),
    path("chores/<int:chore_id>/", views.chores_detail, name="detail"),
    path("chores/create/", views.ChoreCreate.as_view(), name="chores_create"),
    path("chores/<int:pk>/update/", views.ChoreUpdate.as_view(), name="chores_update"),
    path("chores/<int:pk>/delete/", views.ChoreDelete.as_view(), name="chores_delete"),
    path("chores/<int:chore_id>/add_comment/", views.add_comment, name="add_comment"),
    path('chores/<int:chore_id>assoc_supply/<int:supply_id>/', views.assoc_supply, name='assoc_supply'),
    path('chores/<int:chore_id>/unassoc_supply/<int:supply_id>/', views.unassoc_supply, name='unassoc_supply'),
    path("supplies/", views.SupplyList.as_view(), name="supplies_index"),
    path("supplies/<int:pk>/", views.SupplyDetail.as_view(), name="supplies_detail"),
    path("supplies/create/", views.SupplyCreate.as_view(), name="supplies_create"),
    path("supplies/<int:pk>/update/", views.SupplyUpdate.as_view(), name="supplies_update"),
    path("supplies/<int:pk>/delete/", views.SupplyDelete.as_view(), name="supplies_delete"),
    path('accounts/signup/', views.signup, name='signup')
]
