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
            return HttpResponseRedirect(reverse('search_diff'))
        elif search_query == "광성그룹":
            return HttpResponseRedirect(reverse('search_group'))
        elif search_query == "광성바이오틱스":
            return HttpResponseRedirect(reverse('search_bio'))
        elif search_query == "광종훈":
            return HttpResponseRedirect(reverse('search_jong'))
        elif search_query == "23114002":
            return HttpResponseRedirect(reverse('search_report1'))
        elif search_query == "24105397":
            return HttpResponseRedirect(reverse('search_report2'))
        elif search_query == "24105714":
            return HttpResponseRedirect(reverse('search_report3'))
        elif search_query == "24105822":
            return HttpResponseRedirect(reverse('search_report4'))
        elif search_query == "24115233":
            return HttpResponseRedirect(reverse('search_report5'))
        elif search_query == "24119932":
            return HttpResponseRedirect(reverse('search_report7'))
        elif search_query == "2485591":
            return HttpResponseRedirect(reverse('search_report6'))
        elif search_query == "강중기":
            return HttpResponseRedirect(reverse('search_kang'))
        elif search_query == "정기쁨":
            return HttpResponseRedirect(reverse('search_jung'))
        elif search_query == "김규석":
            return HttpResponseRedirect(reverse('search_kim'))
        elif search_query == "안주영":
            return HttpResponseRedirect(reverse('search_ahn'))
        elif search_query == "유상신":
            return HttpResponseRedirect(reverse('search_yu'))
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
    return render(request, 'list/jo_list.html')
def search_pok(request):
    return render(request, 'list/pok_list.html')
def search_est(request):
    return render(request, 'list/est_list.html')
def search_bang(request):
    return render(request, 'list/bang_list.html')
def search_diff(request):
    return render(request, 'list/diff_list.html')
def search_group(request):
    return render(request, 'list/group_list.html')
def search_bio(request):
    return render(request, 'list/bio_list.html')
def search_jong(request):
    return render(request, 'list/jong_list.html')

def search_report1(request):
    return render(request, 'report/23114002.html')
def search_report2(request):
    return render(request, 'report/24105397.html')
def search_report3(request):
    return render(request, 'report/24105714.html')
def search_report4(request):
    return render(request, 'report/24105822.html')
def search_report5(request):
    return render(request, 'report/24115233.html')
def search_report7(request):
    return render(request, 'report/2419932.html')

def search_report6(request):
    return render(request, 'report/2485591.html')

def search_kang(request):
    return render(request, 'info/kang.html')
def search_kim(request):
    return render(request, 'info/kim.html')
def search_jung(request):
    return render(request, 'info/jung.html')
def search_ahn(request):
    return render(request, 'info/ahn.html')
def search_kwang(request):
    return render(request, 'info/kwang.html')
def search_yu(request):
    return render(request, 'info/yu.html')



