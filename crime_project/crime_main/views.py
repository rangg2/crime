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
        if search_query == "112":
            # 검색 결과 페이지로 이동합니다.
            return HttpResponseRedirect(reverse('search_results'))
        elif search_query == "검색 1-2":
            # 검색 결과 페이지로 이동합니다.
            return HttpResponseRedirect(reverse('search_results2'))    
    
        else:
            return render(request, '404.html')
        
def search_results(request):
    return render(request, 'result.html')

def search_results2(request):
    return render(request, 'result2.html')