from django.http import JsonResponse


def home(request):
    return JsonResponse(
        {
            "message": "Welcome to the Django API",
            "version": "1.0.0",
            "endpoints": {"health": "/health", "items": "/api/items"},
        }
    )


def health(request):
    return JsonResponse({"status": "healthy"})


def items(request):
    data = [
        {"id": 1, "name": "Item One", "description": "First example item"},
        {"id": 2, "name": "Item Two", "description": "Second example item"},
        {"id": 3, "name": "Item Three", "description": "Third example item"},
    ]
    return JsonResponse({"items": data})
