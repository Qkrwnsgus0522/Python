# 한줄 주석
'''
여러줄
주석
'''

print('hello')
# 띄어쓰기도 문법 !!!!!

# ★ 키워드로 변수명을 설정하시면 안됩니다!!!!!

# 문자열 == 문자+배열 == index 개념이 존재
# [-1] 지원함
# 내장된 기능이 매우 많음
# 1) 문자열 슬라이싱
##a[1:4] # [1]인덱스 포함~[4]인덱스 미포함
##'ana'
##alt+3 눌러서 전체 주석처리
##alt+4 눌러서 전체 주석처리해제

a=[10,11,12] # 리스트
b=[10,11.2,'apple'] # index 개념 존재
##li=[10,20,30,40,50,60,70]
##li[3:6]
##[40, 50, 60]
##li[-2:]
##[60, 70]
##li[:6]
##[10, 20, 30, 40, 50, 60]

c=(10,11,12) # 튜플,tuple
d=(10,11.2,'apple') # 값 변경 불가능
e=tuple(c) # 타입 변환 함수를 활용 가능

f={10,11,12} # 세트,set,집합
# 중복 제거용으로 활용됨
# 순서 존재 xxx

g={'a':'apple','b':'banana','c':'kiwi'} # 딕셔너리,dict
##g['a']
##'apple'
##g['b']
##'banana'

##print('a+b는 '+str(a+b)+'입니다.')
##a+b는 30입니다.
##print('a+b는 %d입니다.' % (a+b)) # 포맷팅 출력
##a+b는 30입니다.

##a=input('정수 입력: ')
##정수 입력: 1234
##a
##'1234'
##type(a)
##<class 'str'>
##a=int(input('정수 입력: '))
##정수 입력: 1234
##a
##1234
##type(a)
##<class 'int'>

a=[10,20,30]
# 20이 있나요?
if 20 not in a :
    print('있음')
else :
    print('없음')







