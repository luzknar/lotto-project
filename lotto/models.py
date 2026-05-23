from django.db import models

class LottoTicket(models.Model):
    # 1. 구매 방식을 저장 (자동인지 수동인지 글자로 저장)
    # 'auto' 또는 'manual'이 들어갑니다.
    purchase_type = models.CharField(max_length=10, default='auto')
    
    # 2. 로또 번호 6개를 하나의 글자 주머니로 저장 (예: "5, 12, 23, 33, 39, 44")
    numbers = models.CharField(max_length=100)
    
    # 3. 복권을 구매한 날짜와 시간을 자동으로 기록
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.purchase_type.upper()}] {self.numbers} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"