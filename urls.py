"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Anvi's Animated World</title>
        <style>
            /* 1. Background Animation: Rang badalta hua parda */
            body {
                margin: 0; padding: 0;
                font-family: 'Segoe UI', sans-serif;
                height: 100vh;
                display: flex; justify-content: center; align-items: center;
                background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
                background-size: 400% 400%;
                animation: gradientBG 15s ease infinite;
                overflow: hidden;
            }

            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            /* 2. Floating Card: Jo hawa mein hilega */
            .card {
                background: white;
                padding: 40px;
                border-radius: 30px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                animation: float 4s ease-in-out infinite;
                width: 300px;
            }

            @keyframes float {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-20px); }
                100% { transform: translateY(0px); }
            }

            .icon {
                font-size: 50px;
                display: inline-block;
                animation: spin 5s linear infinite;
            }

            @keyframes spin {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }

            h1 { color: #333; margin: 15px 0; }
            
            .btn {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background: #e73c7e;
                color: white;
                text-decoration: none;
                border-radius: 25px;
                font-weight: bold;
                transition: 0.3s;
            }

            .btn:hover {
                transform: scale(1.1);
                box-shadow: 0 5px 15px rgba(231, 60, 126, 0.4);
            }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="icon">✨</div>
            <h1>Anvi ✨</h1>
            <p>Django Animation Magic!</p>
            <a href="/admin" class="btn">Admin Panel</a>
        </div>
    </body>
    </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]