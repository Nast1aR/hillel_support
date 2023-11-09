from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import User, Activation_key
import json
from .models import Issue


class GetAllUsers(View):
    def get(self, request):
        users = User.objects.all().values()
        return JsonResponse(list(users), safe=False)


class CreateUser(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode("utf-8"))
            user = User.objects.create(
                email=data["email"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                role_id=data["role_id"],
            )
            return JsonResponse(
                {
                    "id": user.id,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role_id": user.role_id,
                }
            )
        except Exception as e:
            return JsonResponse({"error": "Invalid data format"}, status=400)


class CreateIssue(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode("utf-8"))
            issue = Issue.objects.create(
                title=data["title"],
                body=data["body"],
                junior_id=data["junior_id"],
                senior_id=data["senior_id"],
                status=data["status"],
            )
            return JsonResponse(
                {
                    "id": issue.id,
                    "title": issue.title,
                    "body": issue.body,
                    "junior_id": issue.junior_id.id,
                    "senior_id": issue.senior_id.id,
                    "status": issue.status,
                }
            )
        except Exception as e:
            return JsonResponse({"error": "Invalid data format"}, status=400)


class GetAllIssues(View):
    def get(self, request):
        issues = Issue.objects.all().values()
        return JsonResponse(list(issues), safe=False)



def activate_user(request):
    if request.method == 'POST':
        activation_key = request.POST.get('key')
        try:
            activation_key = uuid.UUID(activation_key)
            activation_key_obj = get_object_or_404(ActivationKey, key=activation_key)
            user = activation_key_obj.user
            user.is_active = True
            user.save()
            activation_key_obj.delete()
            # Send activation success email
            # You can use a library like Django's EmailMessage to send the email.
            return JsonResponse({'message': 'Your email is successfully activated'})
        except (ValueError, ActivationKey.DoesNotExist):
            return JsonResponse({'error': 'Invalid activation key'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
