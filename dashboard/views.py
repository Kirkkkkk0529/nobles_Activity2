from django.shortcuts import render
from django import template

data = [
    {"title": "Users", "count": 150},
    {"title": "Orders", "count": 320},
    {"title": "Revenue", "count": 12450},
]

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html', {"data": data})
