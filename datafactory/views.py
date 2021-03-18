from django.shortcuts import render, get_object_or_404
from django.http import *
from urllib.parse import urlencode

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from datafactory.models import ToolAttr, Tool
from django_datafactory.utils import get_host_ip


class IndexView(generic.ListView):
    template_name = 'datafactory/index.html'
    context_object_name = 'latest_tool_list'

    def get_queryset(self):
        return Tool.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')[:9]


class ResultView(generic.DetailView):
    model = Tool
    template_name = 'datafactory/results.html'


def create_data(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    i = 1
    tmp = {}
    while request.POST.get("param" + str(i)) is not None:
        tmp["param" + str(i)] = request.POST.get("param" + str(i))
        i = i + 1
    querystring = urlencode(tmp)
    toolpath = tool.toolpath_set.all()
    print(toolpath[0])
    print(querystring)

    # HOST = get_host_ip()
    # if HOST == '10.0.0.0':
    SERVER_HOST = "120.0.0.0"
    # else:
    #     SERVER_HOST = HOST
    return HttpResponseRedirect("http://%s:8088%s?%s" % (SERVER_HOST,
                                                         toolpath[0], querystring))


def detail(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    print(tool.toolattr_set.all())
    return render(request, 'datafactory/detail.html', {"tool": tool, })


class ResultView(generic.DetailView):
    model = Tool
    template_name = 'datafactory/results.html'
