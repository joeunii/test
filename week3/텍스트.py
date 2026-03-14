a = 'Hello, World.'
b = "안녕하세요."
c = """어서와
파이썬은
처음이지?"""
d = """Welcome to 
Python."""
print(a)
print(b)
print(c)
print(d)
print(type(d))

# + 연산자가 문자열을 결합한다고 해서 - 연산자가 문자열을 분리하는 것은 아님
# 문자열 분리(슬라이싱)는 [:] 연산자를 통해 수행해야 함

s = 'Good Morning'
print(s[0:4])

#in 연산자: 프로그래머가 원하는 부분이 문자열 안에 존재하는지 확인
a = 'Good Morning'
print('Good' in a) #True
print('X' in a) #False

#len(): 순서열 길이를 재는 함수, 문자열에도 사용 가능
a = 'Good Morning'
print(len(a))

#startswith(): 원본문자열이 매개변수로 입력한 문자열로 시작되는지를 판단
a = 'Hello'
print(a.startswith('He')) #True
print(a.startswith('lo')) #False

#endswith(): 원본문자열이 매개변수로 입력한 문자열로 끝나는지를 판단
a = 'Hello'
print(a.endswith('He')) #False
print(a.endswith('lo')) #True

#find(): 원본문자열 안에 매개변수로 입력한 문자열이 존재하는 위치를 앞에서부터 찾고 존재하지 않으면-1을 결과로 내놓음
a = 'Hello'
print(a.find('ll')) #2, 왼쪽(처음)부터 찾기 시작해서 가장 먼저 만나는 'll'의 위치를 알려
print(a.find('k')) #-1

#rfind(): 원본문자열 안에 매개변수로 입력한 문자열이 존재하는 위치를 뒤에서부터 찾고 존재하지 않으면 -1을 결과로 내놓음
a = 'Hello'
print(a.rfind('H')) #오른쪽(끝)부터 거꾸로 찾기 시작해서 가장 먼저 만나는 'H'의 위치를 알려줌

#count()
a = 'Hello'
print(a.count('l'))

#lstrip(): 원본문자열 왼쪽에 있는 공백 제거
#rstrip(): 원본문자열 오른쪽에 있는 공백 제거
#strip(): 문자열 양쪽 공백 제거

"""
isalpha(): 원본 문자열이 숫자와 기호를 제외한 알파벳으로만 이루어져 있는지를 평가
isnumeric(): 원본 문자열이 수로마 이뤄져 있는지를 평가
isalnum(): 원본 문자열이 알파벳과 수로만 이뤄져 있는지를 평가
"""

#문자열 변경
a = 'Hello World'
b = a.replace('World', 'Korea')
print(b)

#원본문자열 나누어 리스트 만들기
a = 'Apple, Orange, Kiwi'
b = a.split(',')
print(b) #['Apple', ' Orange', ' Kiwi']

#모두 대문자로 변경
a = 'lower case'
b = a.upper()
print(b) #LOWER CASE

#모두 소문자로 변경
a = 'UPPER CASE'
b = a.lower()
print(b) #upper case

#형식을 갖춘 문자열: 문자열 안에 중괄호와 다른 데이터가 들어갈 자리를 만들어주고 format()함수를 호출할 때 이 자리에 들어갈 데이터를 순서대로 넣어주면 원하는 형식의 문자열을 만들어낼 수 있음
a = 'My name is {0}. I am {1} years old.'.format('Mario',40)
print(a) #My name is Mario. I am 40 years old.
b = 'My name is {name}. I am {age} years old.'.format(name='Luigi', age=35)
print(b)