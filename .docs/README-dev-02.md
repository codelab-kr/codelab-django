## 08. 비동기 작업

```shell
docker pull rabbitmq
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

http://localhost:15672/
guest / guest


celery -A services.shop.shop worker -l info
http://localhost:15672/
guest / guest



celery -A services.shop.shop flower
http://localhost:5555/
```


## 09. 결제
https://stripe.com/  --> 한국에 실제 서버스하기 부적학함
https://docs.stripe.com/payments/local-markets/korea
https://dashboard.stripe.com/settings/account




포트원
- https://developers.portone.io/docs/ko/v2-payment/v2?v=v2
- https://youtu.be/JsiTJlLitMI?si=nCCrchLudqwUXw2C
- https://velog.io/@kisuk623/%ED%8F%AC%ED%8A%B8%EC%9B%90%EA%B3%BC-%ED%86%A0%EC%8A%A4%ED%8E%98%EC%9D%B4%EB%A8%BC%EC%B8%A0%EB%A1%9C-%EA%B2%B0%EC%A0%9C-FLOW-%EC%82%B4%ED%8E%B4%EB%B3%B4%EA%B8%B0
- https://youtu.be/DhcQFLYV9Q8?si=5fdFKjLi8SAA_ZcU
- https://www.canva.com/design/DAFqFrw4MPs/1Oqjy8cBpKOIwS3z9leQ9w/view#14

master@code-lab.kr


https://github.com/portone-io

https://velog.io/@hyeon5819/23.6.22-TIL-%ED%8F%AC%ED%8A%B8%EC%9B%90%EC%95%84%EC%9E%84%ED%8F%AC%ED%8A%B8-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B2%B0%EC%A0%9C-%EC%97%B0%EB%8F%992-%EC%84%9C%EB%B2%84%EC%97%90%EC%84%9C-API%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0

python scripts/add_service_app.py shop payment



00:16 서비스 가입
00:40 아이디 확인 및 하위상점 추가
00:57 디폴트 PG사 테스트 상점아이디
01:20 전자결제신청(PG서비스가입)
01:40 DB 구조
02:08 벡엔드 로직
03:22 재고확인(Confirm Process)
03:40 결제페이지(Checkout Page) 결제창 호출
04:30 로컬환경에서 포트원서버와 통신하기 위한 설정

ngrok
brew install ngrok/ngrok/ngrok
ngrok config add-authtoken xxxx....
ngrok http --domain=termite-beloved-radically.ngrok-free.app http://127.0.0.1:8000

ALLOWED_HOSTS += ['127.0.0.1', 'termite-beloved-radically.ngrok-free.app']  # type: ignore # noqa: F821
CSRF_TRUSTED_ORIGINS = ['https://termite-beloved-radically.ngrok-free.app']


로컬 서버 재시작
https://termite-beloved-radically.ngrok-free.app/ 접속


04:50 cnfirmUrl, redirectUrls, noticeUrl
05:12 콘솔에서 웹훅주소 전송 테스트
05:30 멀티PG 및 다양한 결제수단 호출 시연
06:06 개발자센터에서의 결제요청 및 응답 파라미터와 PG사별 가이드
06:48 결제시연
07:40  재고확인(Confirm Process) 기능 시연
08:40 웹훅우선순위설정
09:33 결제취소
10:00 정산내역통합조회


포트원이 적합해 보이나
v2에 장고 연결 레퍼런스가 거의 없어서 일단 교재의 스트라이프와 연결하고
성공 확인 후 포트원으로 변경하는 걸로 해본다.


https://dashboard.stripe.com/test/apikeys




----


```shell
make css
make runserver
# docker start
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
celery -A services.shop.shop worker -l info
celery -A services.shop.shop flower
# http://localhost:5555/
# http://127.0.0.1:8000/
```


```shell
brew install stripe/stripe-cli/stripe
stripe login
stripe listen --forward-to 127.0.0.1:8000/payment/webhook/
```


```shell
brew install weasyprint

```