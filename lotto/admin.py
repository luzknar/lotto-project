from django.contrib import admin
from .models import LottoTicket  # 설계도 불러오기

# 관리자 페이지에서 로또 티켓 데이터를 볼 수 있도록 등록
admin.site.register(LottoTicket)