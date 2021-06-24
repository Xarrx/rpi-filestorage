from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import ImageData
from .forms import UploadImageForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the storage index.")

class FileUpload(View):
    def get(self, request):
        form = UploadImageForm()
        return render(request, 'main/upload.html', {'form': form})

    def post(self, request):
        form = UploadImageForm(request.POST, request.FILES)
        '''
         Need to handle the thumbnail generation and model creation here.
         Cannot use a ModelForm since the thumbnail is generated.
        '''
        print(request.FILES)
        return HttpResponse(request.FILES)
