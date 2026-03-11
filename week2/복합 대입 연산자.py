"""
<<숫자에 적용>>
+= 숫자 덧셈 후 대입
-= 숫자 뺄셈 후 대입
*= 숫자 곱셈 후 대입
/= 숫자 나눗셈 후 대입
%= 숫자 나머지 구한 후 대입
**= 숫자 제곱 후 대입

<<문자열에 적용>>
+= 문자열 연결 후 대입
*= 문자열 반복 후 대입
"""

#숫자 복합 대입 연산자
number = 100
number += 10
number -= 20
number *= 30
number /= 40
print("number:", number)

#문자열 복합 대입 연산자
#사실상 += 만 이용 가능
String = "안녕하세요"
String += "!"
String += "!"
String += "!"
print("String:", String)