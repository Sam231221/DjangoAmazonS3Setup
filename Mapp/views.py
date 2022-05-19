from django.http import HttpResponse
from django.shortcuts import redirect, render
from Mapp.forms import UploadForm
from django.views.generic.edit import FormView, View

from .models import Post


class Upload(View):
    def get(self, request):
        upload = UploadForm()
        return render(request,'index.html',{'posts':Post.objects.all(), 'upform':upload})

    def post(self, request):
        form =UploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/') 
        else:
            return HttpResponse('error')    
