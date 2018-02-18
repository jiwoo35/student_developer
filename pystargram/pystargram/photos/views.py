from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.
def detail(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    context = dict()
    context['photo'] = photo

    #context = {
    #    'photo':photo
    #}
    return render(request, 'photos/detail.html', {'photo': photo})

def create(request):
    # 로그인 한 유저만 사진 업로드 가능
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)

    if request.method == 'GET':
        form = PhotoForm()
    elif request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user   # user가 로그인 했을때만 사진 저장
            photo.save()
            return redirect('photos:detail', photo_id=photo.pk)

    context = {
        'photo_form': form
    }
    return render(request, 'photos/edit.html', context)

def index(request):
    photos = Photo.objects.all().order_by('-pk') # pk: 낮은 -pk:최신부터
    context = dict()
    context['photos'] = photos

    return render(request, 'photos/list.html', context)

def delete(request):

    # 1. POST 요청으로 온 PK값을 받아서 Photo 모델이 맞는지 찾는다.
    # print(request.GET)  # dict 형태로
    if request.method == "POST":
        photo_id = request.POST['photo_id']
        try:
            photo = Photo.objects.get(pk=photo_id, user=request.user)
        except:
            return redirect('photos:detail', pk=photo_id)
        photo.delete()
    return redirect('photos:list')
    # 2. 틀릴 경우, 다시 해당페이지 / 맞을 경우, Photo를 삭제하고, list 페이지를 보여준다.
    return redirect('photos:list')