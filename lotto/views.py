from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import LottoTicket  
import random

# [창구 1] 메인 화면 
def index(request):
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()
    
    # 데이터베이스에 저장된 모든 로또 티켓을 가져와서 화면에 같이 보냄
    # 최신 구매 내역이 맨 위에 오도록 정렬
    tickets = LottoTicket.objects.all().order_by('-created_at')
    
    context = {
        'numbers': lotto_numbers,
        'tickets': tickets  
    }
    return render(request, 'index.html', context)


# [창구 2] 수동 번호 구매 처리 및 저장
def buy(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        num3 = request.POST.get('num3')
        num4 = request.POST.get('num4')
        num5 = request.POST.get('num5')
        num6 = request.POST.get('num6')
        
        user_numbers = [int(num1), int(num2), int(num3), int(num4), int(num5), int(num6)]
        user_numbers.sort()
        
        # 숫자가 담긴 리스트를 "1, 2, 3, 4, 5, 6" 형태의 글자로바꿈
        numbers_str = ", ".join(map(str, user_numbers))
        
        # 데이터베이스 금고에 수동 구매 내역을 한 줄 저장
        LottoTicket.objects.create(
            purchase_type='manual',
            numbers=numbers_str
        )
        
        # 저장이 끝났으면 새로고침된 메인 페이지로 다시 돌려보냄
        return redirect('/')
    
    return redirect('/')