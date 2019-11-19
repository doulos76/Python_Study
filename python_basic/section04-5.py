# Quiz
# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
lengthOfQ1 = len(q1)
print(lengthOfQ1)

print("1. ", len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print('apple;orange;banana;lemon')

print("2. ", """apple;orange;banana;lemon""")

# 3. 화면에 * 기호 100개를 표시하세요.
print('*' * 100)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
thirty = "30"
int(thirty)
print(int(thirty))
print(float(thirty))
print(complex(thirty))
print(str(30))

print(type(int(thirty)))
print(type(float(thirty)))
print(type(complex(thirty)))

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
niceman = "Niceman"
print(niceman[4:7])
niceman_idx = niceman.index("man")
print(niceman[niceman_idx: niceman_idx + 3])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
strawberry = "Strawberry"
print(strawberry[::-1])
print(list(reversed(strawberry)))

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
phoneNumber = "010-7777-9999"
number = phoneNumber.replace('-', '')
print(number)

q7 = "010-7777-9999"
print("7. ", q7[0:3] + q7[4:8] + q7[9:13])

# 정규표현식
import re
print("Q7. ", re.sub('[^0-9]', '', q7))

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
url = "http://daum.net"
removeHttp = url[7:]
print(removeHttp)


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
niceman = "NiceMan"
upperNiceman = niceman.upper()
print(upperNiceman)
lowerNiceman = niceman.lower()
print(lowerNiceman)


# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
string10 = "abcdefghijklmn"
print(string10[2:5])


# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
fruits = ["Banana", "Apple", "Orange"]
fruits.remove("Apple")
print(fruits)

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
tuple12 = (1, 2, 3, 4)
list12 = list(tuple12)
print(list12)
print(type(list12))

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
dic = {"성인": 100000, "청소년": 70000, "아동": 30000}
print(type(dic))
print(dic)

q13_dic = {}
q13_dic['성인'] = 100000
q13_dic['청소년'] = 70000
q13_dic['아동'] = 30000
print(q13_dic)

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
dic["소아"] = 0
print(dic)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print(dic.keys())
print(list(dic.keys()))


# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(dic.values())
print(list(dic.values()))
# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***

