from performance_reviews.models import PerformanceReview
from rest_framework import serializers


class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = "__all__"
