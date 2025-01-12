from accounts.permissions import IsAdmin, IsEmployee, IsManager
from performance_reviews.models import PerformanceReview
from performance_reviews.serializers import PerformanceReviewSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class PerformanceReviewViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAdmin | IsManager | IsEmployee]
        elif self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = [IsAdmin | IsManager]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]


class PerformanceReviewTransitionView(APIView):
    permission_classes = [IsManager]

    def post(self, request, pk):
        try:
            review = PerformanceReview.objects.get(pk=pk)
            new_stage = request.data.get("stage")

            if review.transition_to(new_stage, request.user):
                return Response({"status": "stage updated"}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "invalid transition"}, status=status.HTTP_400_BAD_REQUEST
                )
        except PerformanceReview.DoesNotExist:
            return Response(
                {"error": "Performance review not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
