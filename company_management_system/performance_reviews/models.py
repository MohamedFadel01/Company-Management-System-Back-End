from accounts.models import User
from django.db import models
from employees.models import Employee


class PerformanceReview(models.Model):
    STAGES = (
        ("PENDING", "Pending Review"),
        ("SCHEDULED", "Review Scheduled"),
        ("FEEDBACK", "Feedback Provided"),
        ("APPROVAL", "Under Approval"),
        ("APPROVED", "Review Approved"),
        ("REJECTED", "Review Rejected"),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    stage = models.CharField(max_length=10, choices=STAGES, default="PENDING")
    feedback = models.TextField(null=True, blank=True)
    scheduled_date = models.DateField(null=True, blank=True)
    approved_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.employee.name} - {self.stage}"

    def transition_to(self, new_stage, user=None):
        allowed_transitions = {
            "PENDING": ["SCHEDULED"],
            "SCHEDULED": ["FEEDBACK"],
            "FEEDBACK": ["APPROVAL"],
            "APPROVAL": ["APPROVED", "REJECTED"],
            "REJECTED": ["FEEDBACK"],
        }

        if new_stage in allowed_transitions.get(self.stage, []):
            self.stage = new_stage
            if new_stage == "APPROVED" and user:
                self.approved_by = user
            self.save()
            return True
        return False
