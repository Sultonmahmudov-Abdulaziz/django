from django.shortcuts import render,get_list_or_404
from .models import Student,Category
# Create your views here.


def index(request):
    students = Student.objects.all()
    categories = Category.objects.all()

    data = {
        "talabalar": students,
        "categories": categories,
    }

    return render(request, template_name= 'student/index.html', context=data)


def category(request,id):
    categories = Category.objects.all()
    category = get_list_or_404(Category, pk=id)
    students = Student.objects.filter(category=category)

    data = {
       'categories' : categories,
       "talabalar": students,
    }

    return render(request,template_name= 'student/category.html', context=data)