# 자바스크립트의 역사

---

- 1995년 넷스케이프의 Brendan Eich는 웹사이트에 쉽게 접근하고 사용할 수 있는 자바스크립트를 10일만에 설계
- 2015년부터 자바스크립트 운영위원회인 TC39는 자바스크립트의 기반이 되는 언어 사양인 ECMA스크립트의 새로운 버전을 매년 출시.
- 이로 인해 자바스크립트는 브라우저, 임베디드 애플리케이션 그리고 서버 런타임을 포함한 다양한 환경에서 새로운 버전과 이전 버전과의 호환성을 수십년 동안 유지

# 자바스크립트의 장점

---

- 한 언어로 유연하게 여러가지 프로그래밍 기법 구사 가능
- 별도의 설치 없이 텍스트 에디터, IDE 에서 사용 가능
- 결과를 인터넷 브라우저 화면 (chrome)에서 볼 수 있음
- 다양한 라이브러리, 프레임워크 등의 확장된 기능성

# 자바스크립트의 함정

---

## 자유도

- 자바스크립트는 코드를 구성하는 방법에 제한이 없음 (자유)
- 하지만 파일이 늘어날수록 자유가 점점 훼손됨.
- 자바스크립트와 같은 동적 타입 언어는 충돌 가능성을 확인하지 않고 코드를 실행함
- 코드를 안전하게 실행하기가 어려움

## JSDoc 표준

- 자바스크립트 언어 사양에는 함수의 매개변수, 함수 반환, 변수 또는 다른 구성 요소의 의미를 설명하는 표준이 없음.
- JSDoc : 자바스크립트 소스 코드에 주석을 달기 위해 사용하는 마크업 단어
- JSDoc 표준 : 표준으로 형식화된 함수와 변수 코드 바로 위에 문서 주석을 작성하는 방식
- JSDoc의 문제점
  - JSDoc 설명 자체가 코드의 오류를 잡아낼 수 없음
  - JSDoc 설명이 이전에는 정확했더라도 코드 리펙토링 중에 생긴 변경사항과 현재와 관련없는 주석을 모두 찾기가 어려움
  - 복잡한 객체의 타입과 관계를 정의하려면 다수의 독립형 주석이 필요함.

## 부족한 개발자 도구

- 타입을 식별하는 내장된 방법 제공 x
- 코드가 JSDoc 주석에서 쉽게 분리됨
  -> 코드베이스에 대한 대규모 변경을 자동화하거나 통찰력을 얻기 어려움
