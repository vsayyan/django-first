from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_GET


# Create your views here.
@require_GET
def home(request):
    return HttpResponse("Hello, Django!")

def hello(request,name):
    return HttpResponse(f"Hello, {name}!")

def api_status(request):
    return JsonResponse({"status": "ok", "framework": "django"})
