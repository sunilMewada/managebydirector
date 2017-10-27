# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import employees, project, projectEmployee

'''class IndexView (generic.ListView):
    model3 = employees
    model1 = project
    model2 = projectEmployee
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return employees.objects;'''

'''def index(request):
    latest_employee_list = employees.objects.order_by ('employee_id')[0:100]
    output = ', '.join ([e.first_name for e in latest_employee_list])
    return HttpResponse (output)'''


def index(request):
    return render(request, 'polls/index.html')


def employee(request):
    latest_employee_list = employees.objects.order_by ('first_name')[:100]
    context = {'latest_employee_list': latest_employee_list}
    return render(request, 'polls/employee.html', context)


def projects(request):
    query = request.GET.get("q")
    if query:
        latest_project_list = project.objects.filter(project_name__icontains=query).order_by ('project_name')[:3]

    else:
        latest_project_list = project.objects.order_by ('project_name')[:100]
    context = {'latest_project_list': latest_project_list}
    return render (request, 'polls/project.html', context,{'filter ': filter})


def projectDetail(request):
    latest_projectDetail_list = projectEmployee.objects.order_by ('project_manager')[:100]
    context = {'latest_projectDetail_list': latest_projectDetail_list}
    return render (request, 'polls/projectDetail.html', context)
