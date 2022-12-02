from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Course, Theme

def home (request):
    return render(request, "#")

def courseList(request, slug=None):
    category = None
    category = "Category".objects.all()
    courses = "Course".objects.all().order_by('-postdate')
    if slug:
        category = get_object_or_404("Category", slug=slug)
        courses =  courses.filter(category=category)
    return render(request, "#",{
        'category': category,
        'categories': categories,
        'courses': courses
    })

def themeList(request, slug=None)
    course = None
    corses = Course.objects.all()
    themes = Theme.objects.all()
    if slug:
        course = get_object_or_404(Course, slug=slug)
        themes = themes.filter(course=cource)
    return render(request, "#", {
        'course': course,
        'couses': corses,
        'themes': themes,
    })

def themeDetail(request, slug, pk):
    course = get_object_or_404(Course, slug=slug)
    theme = get_object_or_404(Theme, pk=pk)
    themes = Theme.objects.all()
    if slug:
        themes = themes.filter(course=course)
    return render(request, "#", {
        'course': cource,
        'theme': theme,
        'themes': themes,
    })

