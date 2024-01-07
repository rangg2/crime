from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Board
from .forms import PostForm
from .serializers import BoardSerializer
from rest_framework import viewsets


# def main(request):
#     return render(request, 'main.html')

# def search(request):
#         search_query = request.GET.get('q')
#         if search_query == "조화도":
#             # 검색 결과 페이지로 이동합니다.
#             return HttpResponseRedirect(reverse('search_jo'))
#         elif search_query == "연쇄폭행사건":
#             return HttpResponseRedirect(reverse('search_pok'))    
#         elif search_query == "에스텔라티오" or search_query == "Estellatio":
#             return HttpResponseRedirect(reverse('search_est'))
#         elif search_query == "방향제":
#             return HttpResponseRedirect(reverse('search_bang'))
#         elif search_query == "디퓨저":
#             return HttpResponseRedirect(reverse('search_diff'))
#         elif search_query == "광성그룹":
#             return HttpResponseRedirect(reverse('search_group'))
#         elif search_query == "광성바이오틱스":
#             return HttpResponseRedirect(reverse('search_bio'))
#         elif search_query == "광종훈":
#             return HttpResponseRedirect(reverse('search_jong'))
#         elif search_query == "피해자정보":
#             return HttpResponseRedirect(reverse('search_dead'))
#         elif search_query == "피해자 정보":
#             return HttpResponseRedirect(reverse('search_dead'))
#         # elif search_query == "4002":
#         #     return HttpResponseRedirect(reverse('search_report1'))
#         elif search_query == "5397":
#             return HttpResponseRedirect(reverse('search_report2'))
#         elif search_query == "5714":
#             return HttpResponseRedirect(reverse('search_report3'))
#         elif search_query == "5822":
#             return HttpResponseRedirect(reverse('search_report4'))
#         elif search_query == "5233":
#             return HttpResponseRedirect(reverse('search_report5'))
#         elif search_query == "9932":
#             return HttpResponseRedirect(reverse('search_report7'))
#         elif search_query == "5591":
#             return HttpResponseRedirect(reverse('search_report6'))
#         elif search_query == "강중기":
#             return HttpResponseRedirect(reverse('search_kang'))
#         elif search_query == "정기쁨":
#             return HttpResponseRedirect(reverse('search_jung'))
#         elif search_query == "김규석":
#             return HttpResponseRedirect(reverse('search_kim'))
#         elif search_query == "안주영":
#             return HttpResponseRedirect(reverse('search_ahn'))
#         elif search_query == "유상신":
#             return HttpResponseRedirect(reverse('search_yu'))
#         elif search_query == "김구순":
#             return HttpResponseRedirect(reverse('search_jang'))
#         # elif search_query == "연쇄폭행사건":
#         #     return HttpResponseRedirect(reverse('search_pok'))    
#         else:
#             pass
#         #     return render(request, '404.html')
        
# def search_news(request):
#     return render(request, 'news.html')

# def search_news2(request):
#     return render(request, 'news2.html')

# def search_news3(request):
#     return render(request, 'news3.html')

# def search_jo(request):
#     return render(request, 'list/jo_list.html')
# def search_pok(request):
#     return render(request, 'list/pok_list.html')
# def search_est(request):
#     return render(request, 'list/est_list.html')
# def search_bang(request):
#     return render(request, 'list/bang_list.html')
# def search_diff(request):
#     return render(request, 'list/diff_list.html')
# def search_group(request):
#     return render(request, 'list/group_list.html')
# def search_bio(request):
#     return render(request, 'list/bio_list.html')
# def search_jong(request):
#     return render(request, 'list/jong_list.html')
# def search_dead(request):
#     return render(request, 'list/dead_list.html')

# def search_report1(request):
#     return render(request, 'report/23114002.html')
# def search_report2(request):
#     return render(request, 'report/24105397.html')
# def search_report3(request):
#     return render(request, 'report/24105714.html')
# def search_report4(request):
#     return render(request, 'report/24105822.html')
# def search_report5(request):
#     return render(request, 'report/24115233.html')
# def search_report7(request):
#     return render(request, 'report/24119932.html')

# def search_report6(request):
#     return render(request, 'report/2485591.html')

# def search_kang(request):
#     return render(request, 'info/kang.html')
# def search_kim(request):
#     return render(request, 'info/kim.html')
# def search_jung(request):
#     return render(request, 'info/jung.html')
# def search_ahn(request):
#     return render(request, 'info/ahn.html')
# def search_kwang(request):
#     return render(request, 'info/kwang.html')
# def search_yu(request):
#     return render(request, 'info/yu.html')
# def search_jang(request):
#     return render(request, 'info/jang.html')

# def search_jung_song(request):
#     return render(request, 'dead/jung_song.html')
# def search_ahn_so(request):
#     return render(request, 'dead/ahn_so.html')
# def search_kim_lee(request):
#     return render(request, 'dead/kim_lee.html')
# def search_kang_sung(request):
#     return render(request, 'dead/kang_sung.html')

# def write(request):
#     return render(request, 'write/write.html')

from rest_framework import generics
from .models import Board
from .serializers import BoardSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Board.objects.all()
    return render(request, 'write/list.html', {'posts': posts})

def post_new(request):
    print(0)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(1)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # return redirect('post_detail', pk=post.pk)
            return redirect('post_list')
        else:
            print(form.errors)  # 에러 출력을 확인하기 위한 부분 추가
    else:
        form = PostForm()
    return render(request, 'write/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Board, pk=pk)
    return render(request, 'write/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'write/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Board, pk=pk)
    post.delete()
    return redirect('post_list')


from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

@csrf_exempt
def custom_login(request):
    # 이미 로그인한 경우
    if request.user.is_authenticated:
        return redirect('main')
    
    else:
        form = CustomLoginForm(data=request.POST or None)
        if request.method == "POST":

            # 입력정보가 유효한 경우 각 필드 정보 가져옴
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                # 위 정보로 사용자 인증(authenticate사용하여 superuser로 로그인 가능)
                user = authenticate(request, username=username, password=password)

                # 로그인이 성공한 경우
                if user is not None:
                    login(request, user) # 로그인 처리 및 세션에 사용자 정보 저장
                    return redirect('main')  # 리다이렉션
                else:
                    messages.error(request, "사용자 정보가 없습니다.")
                #     return render(request, 'login/login.html', {'form': form})
        return render(request, 'login/login.html', {'form': form}) #폼을 템플릿으로 전달


# 로그 아웃
@csrf_exempt
def custom_logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == "POST":
        logout(request)
        return redirect("login")

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, "login/login.html")

from django.contrib import messages

@csrf_exempt
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")

        # 빈 값 체크
        if not username or not password or not confirm:
            messages.error(request, "모든 필드를 작성해주세요.")
            return render(request, "login/signup.html")

        # 패스워드 일치 여부 확인
        if password == confirm:
            user = User.objects.create_user(username=username, password=password)
            # 로그인 코드(auth.login)를 사용하려면 적절한 상황에서 활용해야 합니다.
            return redirect("/")
        else:
            messages.error(request, "패스워드가 일치하지 않습니다.")
            return render(request, "login/signup.html", {'username': username})

    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, "login/signup.html")

def sbar(request):
    return render(request, "search/s_bar.html")

from .forms import SearchCrimeForm
from django.db.models import Q

def search_crime(request):
    
    form = SearchCrimeForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        # 검색어가 제공되면 "crime" 모델에서 검색
        if query:
            # 각 필드에 대해 __in 필터를 사용하여 리스트 전체에 대한 OR 조건으로 검색
            results = Board.objects.filter(tag__contains=[query])

    return render(request, 'search/search.html', {'results': results, 'query': query})

def crime_image(request, crime_id):
    board = get_object_or_404(Board, id=crime_id)
    return render(request, 'search/image.html', {'board': board})