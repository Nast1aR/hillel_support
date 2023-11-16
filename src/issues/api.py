from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from .constants import Status
from .models import Issue
from .permissions import (IssueParticipant, RoleIsAdmin, RoleIsJunior,
                          RoleIsSenior)


class IssueReadonlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"


class IssueCreateSerializer(serializers.ModelSerializer):
    status = serializers.CharField(required=False)
    junior = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Issue
        fields = ["id", "title", "body", "junior", "status"]

    def validate(self, attrs: dict) -> dict:
        attrs["status"] = Status.OPENED
        return attrs


class IssueApiSet(ModelViewSet):
    queryset = Issue.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return IssueCreateSerializer
        return IssueReadonlySerializer


class IssueApiSet(ModelViewSet):
    queryset = Issue.objects.all()

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [RoleIsSenior | RoleIsJunior | RoleIsAdmin]
        elif self.action == "create":
            permission_classes = [RoleIsJunior]
        elif self.action == "retrieve":
            permission_classes = [IssueParticipant]
        elif self.action == "update":
            permission_classes = [RoleIsSenior | RoleIsAdmin]
        elif self.action == "destroy":
            permission_classes = [RoleIsAdmin]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return IssueCreateSerializer
        return IssueReadonlySerializer


# class MessageCreateAPI(CreateAPIView):
#    serializer_class = MessageSerializer
#   lookup_field = "issue_id"
#  lookup_url_kwarg = "issue_id"
