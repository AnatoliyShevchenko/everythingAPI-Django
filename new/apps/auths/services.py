from django.db.models.query import QuerySet

from models import User


def re_zero_count_service():
    users: QuerySet[User] = User.objects.all()
    users.update(count_requests=10)