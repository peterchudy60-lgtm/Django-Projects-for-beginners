from django.shortcuts import render

# Create your views here.
from multiprocessing import context
from urllib import request

from django import template
from django.views.generic import ListView
from .models import Post
from .forms import StatusForm
from django.http import HttpResponse
from django.template import loader
import django.shortcuts


class HomePageView(ListView):
    model = Post
    template_name = "home.html"
#    xx = model(title = 'xxx', choices_title = {1: 'a', 2: 'b', 3: 'c'}, cover = 'images/tosomja.jpg')
#    xx.save()
#    xx = model(title = 'zzz', choices_title = {1: 'd', 2: 'e', 3: 'f'}, cover = 'images/Pexeso_rub.png')
#    xx.save()

def HomePageView1(request):
    otazky = Post.objects.all().values()
    template = loader.get_template('home1.html')
    context = {'sadatotazok': otazky}
    return HttpResponse(template.render(context, request))

def RadioView(request):
    if request.method == "GET":
        # Process the selected choice as needed
        otazky = Post.objects.all().values()
        template = loader.get_template('radio.html')
        context = {'sadatotazok': otazky}
        return HttpResponse(template.render(context, request))

def status_view(request):
    request.session['current_question'] = request.session.get('current_question', 1)  # Initialize current question
    if request.method == "POST":
        current_question = request.session.get('current_question', 1)  # Initialize current question
        form = StatusForm(request.POST, current_question=current_question)
        if form.is_valid():
            selected_value = form.cleaned_data
            template = loader.get_template('status_form1.html')
            template2 = loader.get_template('status_form2.html')
            request.session['current_question'] = current_question + 1
            print(f"Selected statusPOST:" , selected_value, current_question, Post.objects.count())  # You can process the selected value as needed
            if request.session['current_question'] <= Post.objects.count():
#                request.session['current_question'] = 1  # Reset to the first question if it exceeds the total number of questions
#               return django.shortcuts.render(request, "status_form1.html", {"selected_value": selected_value})  # Redirect to a success page or another view
                return HttpResponse(template.render({"selected_value": selected_value}, request))
            else:
                request.session['current_question'] = 1
                return HttpResponse(template2.render({"selected_value": selected_value}, request))
    else:
        current_question = request.session.get('current_question', 1)  # Initialize current question
        form = StatusForm(current_question=current_question)
        print(f"Selected statusGET:", current_question, form)  # You can process the selected value as needed
        template = loader.get_template('status_form.html')
#        return django.shortcuts.render(request, "status_form.html", {"form": form})
        return HttpResponse(template.render({"form": form,"xxx": current_question}, request))
    