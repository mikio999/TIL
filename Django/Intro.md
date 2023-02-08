> Django의 기본 개념 및 용어 정리한 문서

# What is Django?

---

## Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

- 보안이 우수하고 유지보수가 편리한 웹사이트를 신속하게 개발하는 하도록 도움을 주는 파이썬 웹 프레임워크

## 장점

---

- complete : "Batteries included" 의 철학을 기반으로 개발자들이 개발하고 싶은 거의 모든것을 개발하는데 도움을 줌
- versatile : 다양한 클라이언트측 프레임워크와 협업 가능, 대부분의 형식(HTML, RSS 피드, JSON, XML 등)으로 컨텐츠를 전송
- secure : 보안 문제에 많은 도움을 줌 (ex. hash 함수를 통해 안전하게 비밀번호 저장)
- scalable : 컴포넌트 기반의 아키텍쳐 사용 -> 확장성에 용이
- maintainable : Django 코드는 유지보수에 용이, 재사용성을 높이는 디자인 원칙들과 패턴들을 이용하여 작성됨
- portable : 특정한 플랫폼에 얽매이지 않는 파이썬 기반

## Django 구조

---

- 데이터 기반 웹 사이트 특성상 웹 어플리케이션은 클라이언트로부터 HTTP Request를 기다림.
- Request를 받으면, 웹 어플리케이션은 URL과 POST 나 GET 데이터 기반의 요구사항을 분석함.
- 그에 따른 분석을 기반으로, DB로부터 정보를 읽거나 쓰고, 필요한 다른 작업들 수행.
- 웹 어플리케이션은 웹 브라우저에 동적인 HTML 페이지를 생성하면서 응답(Response)을 반환함.

<h2>모델 뷰 템플릿 아키텍쳐 (Model View Template Architecture)</h2>

- URLs : URL mapper는 요청 URL을 기준으로 HTTP 요청을 적절한 뷰(view)로 보내주기 위해 사용됨. 또한 URL에 나타나는 특정한 문자열이나 숫자의 패턴을 일치시켜 데이터로서 뷰 함수에 전달할 수 있음.
- View: HTTP 요청을 수신하고 응답을 반환하는 요청 처리 함수. View는 Model을 통해 요청에 필요한 데이터에 접근하고, Templates에 응답의 서식 설정을 위임한다.
- Models: 응용프로그램의 데이터 구조를 정의, DB의 기록을 관리(add, modify, delete)하고 DB의 쿼리를 제공하는 파이썬의 객체.
- Templates: 파일 구조나 레이아웃을 정의 (ex. HTML 페이지), View는 Templates를 이용하여 동적으로 HTML page를 만들고 Models에서 가져온 데이터로 채운다. Templates로 모든 파일의 구조를 정의할 수 있으며 반드시 HTML 타입을 필요는 없다.

## Django의 추가 기능

- Forms (양식) : 양식 작성, 유효석 검사 및 처리를 단순화.
- User authentication and permissions : Django에는 보안 강화를 위한 사용자 인증 및 권한 시스템이 포함되어 있음.
- Caching : 컨텐츠를 동적으로 작성하는 것은 많은 연산을 필요로 하기 때문에 속도가 중요하다. Django는 유연한 캐싱을 제공하여 필요한 때를 제외하고 재렌더링을 방지한다.
- Administration site : 사이트 관리자가 사이트의 모든 데이터 모델을 손쉽게 작성, 편집할 수 있는 관리 페이지를 제공받을 수 있음.
- Serializing data (데이터 직렬화): Django를 통해 데이터를 XML 또는 JSON으로 직렬화하고 제공받을 수 있음.

### 참고문헌

- https://www.djangoproject.com/start/overview/
- https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction
