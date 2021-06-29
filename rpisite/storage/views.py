from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import ImageData, ThumbnailData
from .forms import UploadImageForm

from PIL import Image

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the storage index.")

class FileUpload(View):
    
    def get(self, request):
        form = UploadImageForm()
        return render(request, 'main/upload.html', {'form': form})
        
    def post(self, request):
        
        # create the form
        form = UploadImageForm(request.POST, request.FILES)
        
        # check if the form is valid
        if form.is_valid():
            
            # bind the uploaded image to a model instance
            new_image = ImageData(image = request.FILES['image'])
            
            # save the instance 
            new_image.save()
            
            '''
            # Attempt to handle thumbnail creation
            thumb_image = Image.open(request.FILES['image'])
            size = (128, 128)
            thumb_image.thumbnail(size, Image.ANTIALIAS)
            '''
            
            # save a new thumbnail
            new_thumbnail = ThumbnailData(thumbnail = request.FILES['image'], image = new_image)
            new_thumbnail.save()
            
        else:
            
            print("Form Validation Failed")
        '''
         Need to handle the thumbnail generation and model creation here.
         Cannot use a ModelForm since the thumbnail is generated.
        '''
        
        form = UploadImageForm()
        return render(request, 'main/upload.html', {'form': form})

