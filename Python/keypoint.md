# Keypoint

---

"생각보다 인간의 기억력은 나쁘다"

💡 기억해야할 파이썬의 핵심 개념들을 정리합니다.

## escape character 이스케이프 문자 : (\)

### 문자열 내부에 따옴표 넣기

```python
>>> print('"안녕하세요"라고 말했습니다.')
>>> print("\"안녕하세요\"라고 말했습니다.") #이스케이프 문자 사용
"안녕하세요"라고 말했습니다.
```

### 탭 사용 : (\t)

### 줄바꿈 사용 : (\n)

### 역슬래시 (\) 출력

```python
>>> print("\\ \\ \\ \\")
\ \ \ \
```

## 형 변환

```python
int(data) #int 형 변환 (float, bool 변환 가능)
float(data) #float 형 변환 (int, bool 변환 가능)
str(data) #str 형 변환 (int, float, bool, chr, 변환 가능)
chr(data) #chr 형 변환 (int, bool 변환 가능)
bool(data) #bool 형 변환 (int, float, str, chr 변환 가능)
```

- bool 형 변환의 경우 int, float에서 변환할 때는 데이터가 0인지 아닌지에 따라, chr와 str에서 변환할 때는 값이 비어 있는지 아닌지에 따라 True, False를 반환함.
