# stock_trading_bot

#python을 이용한 자동주식매매 프로그램.


====구현 예정====

#필수,주요 기술
- 테스트 코드 작성
- 클린코드 도서 기반 작성
- REST API
- api 명세에 따른 url작성
- MTV패턴 적용
- aws, docker


#주요 기능
- 기사 크롤링
- 엘라스틱 본문검색
- 챗봇을 통한 주식 알고리즘
- 알림푸시(sms, 메일, API)

#공통 모듈 구조
- urls.py: 앱의 URL 패턴 선언
- forms.py: 입력 폼 선언
- behaviors.py: 모델 믹스인 위치에 대한 옵션
- constants.py: 앱에 쓰이는 상수 선언
- decorators.py: 데코레이터
- db/: 여러 프로젝트에서 용되는 커스텀 모델이나 컴포넌트
- fields.py: 폼 필드
- factories.py: 테스트 데이터 팩토리 파일
- helpers.py: 뷰와 모델 파일을 가볍게 하기 위해 유틸리티 함수 선언
- managers.py: models.py가 너무 커질 경우 커스텀 모델 매니저가 위치
- signals.py: 커스텀 시그널
- viewmixins.py: 뷰 모듈과 패키지를 더 가볍게하기 위해 뷰 믹스인을 이 모듈로 이전
*Two Scoops of Django 책 참조
