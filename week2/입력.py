#입력
String = float(input("입력> "))

#출력
print("입력+100:", String+100)

#문자열과 숫자는 더할 수 없으므로 형태를 바꿔줘야 함

#input()함수와 float()함수 조합
input_a = float(input("첫 번째 숫자> "))
input_b = float(input("두 번째 숫자> "))

print("덧셈 결과:", input_a + input_b)
print("뺄셈 결과:", input_a - input_b)
print("곱셈 결과:", input_a * input_b)
print("나눗셈 결과:", input_a / input_b)

#숫자를 문자열로 바꾸기
output_a = str(52)
output_b = str(52.273)

print(type(output_a), output_a)
print(type(output_b), output_b)