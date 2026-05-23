from django.shortcuts import render, redirect 
from django.http import HttpResponse
import random

# [창구 1] 메인 화면 (자동 번호 생성)
def index(request):
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()
    context = {
        'numbers': lotto_numbers
    }
    return render(request, 'index.html', context)

# [창구 2] 수동 번호 구매 처리 
def buy(request):
    if request.method == 'POST':
        # 사용자가 입력한 빈칸 6개의 데이터를 name 기준으로 쏙쏙 뽑아옵니다.
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        num3 = request.POST.get('num3')
        num4 = request.POST.get('num4')
        num5 = request.POST.get('num5')
        num6 = request.POST.get('num6')
        
        # 글자로 들어온 숫자들을 계산할 수 있게 정수(int)로 바꿔서 리스트에 넣습니다.
        user_numbers = [int(num1), int(num2), int(num3), int(num4), int(num5), int(num6)]
        user_numbers.sort() # 보기 좋게 오름차순 정렬
        
        # 아직 데이터베이스가 없으니, 우선 브라우저 화면에 잘 받았다고 임시로 띄워줍니다.
        return HttpResponse(f"<h1>수동 복권 구매 완료!</h1><p>선택하신 번호: {user_numbers}</p><a href='/'>돌아가기</a>")
    
    # 만약 이상한 방식으로 들어오면 메인 페이지로 튕겨내기
    return redirect('/')