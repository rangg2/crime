from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def main(request):
    return render(request, 'main.html')

# def search(request):
#     search_query = request.GET.get('q')
#     if search_query:
#         # 여기서 URL을 동적으로 생성하거나 하드코딩하여 사용자의 검색어에 따라 다른 URL로 이동합니다.
#         # 여기서는 검색 결과 페이지로 이동하는 예시입니다.
#         redirect_url = reverse('search') + f'?q={search_query}'
#         return HttpResponseRedirect(redirect_url)
#     else:
#         return render(request, 'result.html')
    
# def custom_404(request, exception):
#     return render(request, 'custom_404.html', status=404)

def search(request):
        search_query = request.GET.get('q')
        if search_query == "조화도":
            # 검색 결과 페이지로 이동합니다.
            return HttpResponseRedirect(reverse('search_jo'))
        elif search_query == "연쇄폭행사건":
            return HttpResponseRedirect(reverse('search_pok'))    
        elif search_query == "에스텔라티오" or search_query == "Estellatio":
            return HttpResponseRedirect(reverse('search_est'))
        elif search_query == "방향제":
            return HttpResponseRedirect(reverse('search_bang'))
        elif search_query == "디퓨저":
            return HttpResponseRedirect(reverse('search_bang'))
        # elif search_query == "연쇄폭행사건":
        #     return HttpResponseRedirect(reverse('search_pok'))    
        else:
            return render(request, '404.html')
        
def search_news(request):
    return render(request, 'news.html')

def search_news2(request):
    return render(request, 'news2.html')

def search_news3(request):
    return render(request, 'news3.html')

def search_jo(request):
    return render(request, 'jo_list.html')
def search_pok(request):
    return render(request, 'pok_list.html')
def search_est(request):
    return render(request, 'est_list.html')
def search_bang(request):
    return render(request, 'bang_list.html')
