from django.urls import path
from performance_reviews.views import PerformanceReviewTransitionView

urlpatterns = [
    path(
        "performance-reviews/<int:pk>/transition/",
        PerformanceReviewTransitionView.as_view(),
        name="review-transition",
    ),
]
