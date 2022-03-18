from rest_framework.routers import DefaultRouter

from django.urls import path, include
# from . import views
from watchlist_app.api.views import (ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS,
                                     Watch_Detail, Watch_List,
                                     SPlatformDetail, SPlatformList)


router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path("list/", Watch_List.as_view(), name="movie-list"),
    path("<int:pk>", Watch_Detail.as_view(), name="movie_details"),

    path("", include(router.urls)),

    # path("stream/", SPlatformList.as_view(), name="stream-list"),
    # path("stream/<int:pk>", SPlatformDetail.as_view(), name="stream-detail"),

    # --------Concrete class --------------
    path("stream/<int:pk>/review-create",
         ReviewCreate.as_view(), name="review-create"),
    path("stream/<int:pk>/review", ReviewList.as_view(), name="review-list"),
    path("stream/review/<int:pk>", ReviewDetail.as_view(), name="review-detail"),

    # ----------Mixins & generic api cladss ------------
    # path("stream/<int:pk>/review", ReviewList.as_view(), name="stream-detail"),
    # path("stream/review/<int:pk>", ReviewDetail.as_view(), name="stream-detail"),

    # ------------APIview & generics------------
    # path('review', ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),

    # --------function based vews urls------------
    #  path("list/", views.movie_list, name="movie-list"),
    #  path("<int:pk>", views.movie_details, name="movie_details),


]
