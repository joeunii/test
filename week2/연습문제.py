#1. 이스케이프 문자 중 줄바꿈에 사용되는 것은? = \n
#2. 코드 실행결과 예측하기 print("0123456"[1:3]) = 12
print("0123456"[1:3])

#inch 단위를 입력받아 cm 단위 구하기
inch = int(input("인치를 입력하세요: ")) 
cm = inch * 2.54
print(f"{inch}인치는 {cm}cm 입니다.")

#킬로그램 단위를 입력받아 파운드 단위 구하기
kg = int(input("kg을 입력하세요> "))
pound = kg * 2.20462
print(f"{kg}킬로그램을 파운드로 변환하면 {pound}입니다")

#원의 반지름을 입력받아 원의 둘레와 넓이를 구하기
import math

r = int(input("원의 반지름을 입력하세요> "))
circumference = 2 * math.pi * r
area = math.pi * (r**2)

print(f"반지름이 {r}인 원의 둘레는 {circumference}이고,")
print(f"넓이는 {area}입니다.")