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
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Anvi Magic Heart</title>
        <style>
            body { margin: 0; height: 100vh; display: flex; justify-content: center; align-items: center; background-color: #fff0f3; overflow: hidden; font-family: sans-serif; }
            .heart { position: relative; width: 100px; height: 90px; background-color: #ff4d6d; cursor: pointer; animation: beat 1s infinite; box-shadow: 0 0 20px rgba(255,77,109,0.3); }
            .heart:before, .heart:after { content: ""; position: absolute; top: 0; width: 100px; height: 150px; border-radius: 100px 100px 0 0; background-color: #ff4d6d; }
            .heart:before { left: 100px; transform: rotate(-45deg); transform-origin: 0 100%; }
            .heart:after { left: 0; transform: rotate(45deg); transform-origin: 100% 100%; }
            @keyframes beat { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.1); } }
            #butterfly { display: none; font-size: 100px; animation: fly 2s infinite ease-in-out; cursor: pointer; }
            @keyframes fly { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-40px) rotate(10deg); } }
            h1 { color: #ff4d6d; margin-top: 60px; font-size: 2.5rem; text-align: center; }
        </style>
    </head>
    <body>
        <div style="text-align: center;">
            <div id="heart" class="heart" onclick="transformMagic()"></div>
            <div id="butterfly">🦋</div>
            <h1 id="msg">ANVI ✨<br><small style="font-size: 1rem;">(Touch the Heart for Magic)</small></h1>
        </div>
        <script>
            function transformMagic() {
                document.getElementById('heart').style.display = "none";
                document.getElementById('butterfly').style.display = "block";
                document.getElementById('msg').innerHTML = "Butterfly Magic! 🦋<br>You did it, Anvi!";
                document.body.style.backgroundColor = "#e0f7fa";
            }
        </script>
    </body>
    </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]