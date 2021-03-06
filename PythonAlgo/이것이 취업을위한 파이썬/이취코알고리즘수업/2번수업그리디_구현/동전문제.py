
#그리디 1번문제 점원이 500우너 100원 50원 10원 짜리 동전이 무한히 존재 할때 손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 동전의 최소 개수는?
# 단,  거스를 돈은 항상 10의 배수다
# 큰돈부터 거슬러주면 되지 않을까? 라고 생각했다.
n=1260
count =0 
# 큰단위 화페부터 확인하기
array= [500,100,50,10]
for coin in array:
    count += n // coin
    n %= coin
print(count)


# 나는 풀긴 했지만 정당성을 분석해보자
# 가장 큰 화폐부터 거스르는 이유는 뭘까 ?
# 동전중 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올수 없기 떄문 

# N이 1이 될 때까지 다음 두과정 중 하나를 반복한다 단 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.

# 1. N에서 1을 뺍니다.
# 2. N을 K로 나눕니다.
# 예로 N이 17 K가 4일때   1번 과정으로 N은 16이 되고 이후  2번 과정을 두번 하면 N은 1이 된다.
# N 이 1이 될 때까찌 1번 혹은 2번의 과정을 수행해야하는 최소 횟수를 구하는 프로그램을 작성 


# 찾아낸 규칙 1   N이 k로 나누어 떨어지면 그떄부터는 쭉 2번만 시행하는게 좋다.
n=25
k=3
count=0
#
while n!=1:  
    if n%k==0:  # 나누어 떨어지는 수가 되면   
        n=n/k
    else: 
        n=n-1
    count+=1
print(count)
# 위의 과정은 시간 복잡도가 높다
#### 모범담안
n=25
k=3

result=0

## 이렇게하면 log의 시간복잡도를 가짐     기존에 한번비교 한번 반복문 계산에서 한번에 계산으로 바뀜
while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 뺴기
    target = (n//k) * k   
    result += (n - target)      # n-target는 나누어 떨어지기 위해서  - 를 반복해야하는 횟수
    n = target  # 위에서 - 해야하는 만큼 반복 했으니 나누어 떨어지는 수로 바꿈 
    # N 이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k
#마지막으로 남은 수에 대하여 1씩 빼기
result += (n -1)
print(result)
# 직관으로 찾아낸 방법은 나눌수 있을때는 최대한 나눈다
# 정당성 분석
# K가 2이상이기만 하면 K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N을 줄일 수 있다.




# 모험가 길드 
# N명의 모험가가 있다.
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 한다.
# 최대 몇 개의 모험가 그룹을 만들 수 있나?   N명의 호험가에 대한 정보가 주어졌을때 여행을 떠날수 있는 그룹 수의 최대값을 구하는 프로그램을 작성하여라

# 입출
# 첫 쨰줄에 모험가수 N주어짐
# 둘쨰 줄에 공포도 값을 N이하 자연수로 주어짐  공백으로 구분

# 내 풀이 : 핵심은 가장 낮은 공포도 모험가 먼저 보내야 한다.
# print("모험가 길드 문제")
# n=input()
# data=list(map(int,input().split()))
# data.sort()

# result = 0  # 총 그룹의 수 
# count = 0 # 현재 그룹 포함된 모험가 수

# for i in data: # data 값 하나 씩 비교 
#     count += 1 # 
#     if count >= i:  # 카운트보다 data현재 값이 낮으면 
#         result += 1  # 결과 즉 그룹을 하나 추가한다.
#         count=0      #

# print(result)


#################
## 여기부터 구현 부분

# 구현은 머리속으로 생각은 쉽지만 실제 프로그램 구현은 어려운 문제
# 
#

# 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용된다.

# 대표적인 좌표이동 코드 
# 동, 북 , 서 , 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 현재 위치
x,y = 2,2   # (2, 2) 위치

for i in range(4):
    #다음위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx,ny)


# 여행가 이동 문제
# 여행가를 원하는 위치로 옮기는 문제
# 여행가는 N X N 크기 정사각형 가장 왼쪽이 위가 (1,1)이고 가장 오른쪽 아래좌표는 (N,N) 시작좌표는 항상 (1,1)
# 공간 밖이면 무시

# 문제 조건
# 첫째줄에 공간의 크기를 나타내는 N이 주어진다
# 둘쨰 줄에 여행가 A가 이동할 계획서 내용이 주어진다

# 입력예시
# 5
# R R R U D D

# 출력예시
# 3 4 
 
# 현 좌표 1-1,1-1
# x = 1
# y = 1
# n = int(input())  # 공간 크기 N
# orders = input().split() # 명령


# # U D R L  상 하 우 좌
# dx=[-1,1,0,0]
# dy=[0,0,1,-1]
# move_types = ['U','D','R','L']

# # 이동 명령 하나씩 확인
# for order in orders:
#     # 이동후 좌표 구하기
#     for i in range(len(move_types)):
#         if order ==move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     #공간 벗어나면 무시
#     if nx < 1 or ny < 1 or nx > n or ny> n:
#         continue
#     #이동 수행
#     x,y = nx, ny

# print(x,y)    
    
    
    
#시각 문제
# N시까지 3이 하나라도 포함되는 경우의 수 구하기

# 입력
# 5

# 출력
# 11475  (5시까지 3이 포함 된수)
    

# 풀이   이건 완전 탐색 문제다 
# 즉 완전탐색  모든 조건을 다 일일이 확인하는 방법이다
# 하루는 86400초 그냥 새면 된다.

# 입력받기    
# h= int(input())

# count=0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             # 매 시각 시 분 초 중에 '3'이 포함되어 있다면 카운트 증가
#             if '3' in str(i) +str(j) +str(k):
#                 count += 1
                
# print(count)

### 문법 기억하기
# if '3' in str(i):  # i 라는 문자열안에 3이 포함되어 있는지 확인
#    print("3이 있어")
# 'j' not in 'python'  # True 가 나옴

# 왕실의 나이트 문제 
# 

# 못 풀었음 나중에 풀어보기

# # 현재 나이트의 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# #8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     #해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result +=1


# 문자열 재정렬 문제 
# 

# 알파벳 대문자와 숫자로만 구성된 문자열이 입력된다.
# 이를 알파벳은 오름차순으로 출력하고 모든숫자를 더한 값을 맨뒤에 출력

# ex)  K1KA5CB7 -> ABCKK13  

#####################나의 답안
# input_data = input()  #문자열로 일단받음
# sort_data=[]

# num=0
# for i in range(len(input_data)):
#     if ord('A')<=ord(input_data[i])<=ord('Z'):
#         sort_data+=input_data[i]
#     else:
#         num+=int(input_data[i])
# sort_data.sort()
# for i in range(len(sort_data)):
#     print(sort_data[i],end='')
# print(num)
#####################나의 답안 끝

##################모범답안
# data = input()
# result = []
# value = 0

# # 문자를 하나씩 확인하며
# for x in data:
#     # 알파벳인 경우 결과 리스트에 삽입
#     if x.isalpha():  # isalpha() 문자열 구성이 알파벳인지 확인
#         result.append(x)  # 리스트에 값을 하나씩 추가한다 -> append
#         print(result)
#     # 숫자는 따로 더하기
#     else:
#         value += int(x)
        
# # 알파벳을 오름차순으로 정렬
# result.sort()

# # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
# if value != 0:
#     result.append(str(value))
    
# # 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
# print(''.join(result))


#다시 풀어보기 
# 상하좌우문제
# print("상하좌우다시풀기")
# n=int(input())
# order=list(input().split())

# print(order)
# x,y=1,1
# #L, R, U, D
# dx=[0,0,-1,1]
# dy=[-1,1,0,0]

# for i in range(len(order)):
#     if order[i]=='L' and y>1:
#         x=x+dx[0]
#         y=y+dy[0]
#     if order[i]=='R' and y<n:
#         x=x+dx[1]
#         y=y+dy[1]
#         print(x,y)
#     if order[i]=='U' and x>1:
#         x=x+dx[2]
#         y=y+dy[2]
#     if order[i]=='D' and x<n:
#         x=x+dx[3]
#         y=y+dy[3]
# print(x,y)

#

# 숫자3 이 들어간 시간 문제 

# n=int(input())

# result=0
# for i in range(0,n+1):  # 시간
#     for j in range(0,60):  # 분
#         for z in range(0,60):  # 초   
#             if i%10==3 or j%10==3 or j//10==3 or z%10==3 or z//10==3:
#                 result+=1         

# print(result)

# 왕실의 나이트 문제 
# result=0  # 이동가능한 위치
# location=input()
# x = int(location[1]) # a1 에서 1 
# y = ord(location[0])-ord('a')+1 # a 를 넣으면 1

# #나이트가 이동 8가지 정의
# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# # 
# result = 0
# for step in steps:
#     #이동할 다음 위치
#     next_x=x+step[0]
#     next_y=y+step[1]
#     #
#     if next_x>=1 and next_x<=8 and next_y>=1 and next_y<=8:
#         result+=1

# print(result)

# 문자열 재정렬 

















