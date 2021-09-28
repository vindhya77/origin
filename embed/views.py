from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Videos
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import VideoForm
# Create your views here.

def upload_video(request):
    
    # if request.method == 'POST': 
        
    #     title = request.POST['title']
    #     video = request.POST['video']

    #     video_url = 'videos/{file_name}'.format(file_name=video)

    #     content = Videos(title=title,video=video_url)
    #     content.save()
    #     return redirect('videos')

    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('videos')
    
    context = {
              'form': form
              }
    
    return render(request,'upload.html', context=context)


def display(request):
    # import pdb;pdb.set_trace()
    videos = Videos.objects.all()
    context ={
        'videos':videos,
    }
    
    return render(request,'videos.html',context)


@csrf_exempt
def embed(request):
	# import pdb;pdb.set_trace()
	video_id = request.POST.get('video_id')
	video_obj = Videos.objects.filter(id=video_id).first()
	if video_obj:
		iframe_html = "http://localhost:8000{url}".format(url=video_obj.video.url)
		return JsonResponse({'ihtml': iframe_html})
	return JsonResponse({'ihtml': 'Url Not Found'})