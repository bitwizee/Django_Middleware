# 🚀 Django Middleware: What & How?

## 🔹 What is Middleware in Django?  
Middleware in Django is a **framework component** that processes requests **before** they reach the view and responses **before** they are sent to the client. It acts as a bridge between Django’s request/response cycle, allowing developers to modify, filter, or process requests and responses.  

---

## 🎥 Watch the Video Tutorial  
Click the link [watch it on YouTube](https://www.youtube.com/watch?v=wtQzV0phuHg&t=931s).  

---

## 🔥 How Middleware Works?  
1️⃣ **Request Processing:** Middleware can modify or inspect incoming requests **before** they reach the view.  
2️⃣ **Response Processing:** Middleware can modify or inspect responses **before** they are sent to the client.  
3️⃣ **Multiple Middleware:** Django allows stacking multiple middleware components, each performing a specific task.  

---

## 🛠 Example: Custom Logging Middleware  
```python
from django.utils.timezone import now
from .models import UserActivityLog

class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Logging user activity
        ip = request.META.get('REMOTE_ADDR', '')
        user = request.user if request.user.is_authenticated else None

        UserActivityLog.objects.create(
            user=user,
            ip_address=ip,
            path=request.path,
            timestamp=now()
        )

        return response
