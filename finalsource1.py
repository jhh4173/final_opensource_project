import matplotlib.pyplot as plt
import pandas as pd

#=============================================================================
culture = pd.read_csv('C:/temp/software2.csv')
print(culture)
list1 = ["1996", "2000", "2004", "2007", "2009", "2011", "2013", "2015", "2017", "2019"] #index로 사용할 년도를 작성한다. 
culture.index = list1 #index를 list1로 변경한다.


print(culture) #우리나라의 문화관람률을 출력한다. 

print(culture["영화"]) #우리나라의 년도별 문화관람률 중 영화관람률을 출력한다.

print(culture["영화"].max()) #우리나라의 영화관람률 중 가장 높은 값을 출력한다.

print(culture["영화"].idxmax()) #우리나라의 영화관람률 중 가장 높은 값을 년도와 함께 출력한다. 


print("================================================")
#영화와 뮤지컬의 1996년~2019년의 평균관람률을 구하고 출력한다. 그리고 더 높은값이 무엇인지도 비교하는 출력도 한다.
print("영화와 뮤지컬 중 문화관람률 평균이 더 높은 값은?")
movie = culture["영화"].mean()
musical = culture["뮤지컬"].mean()
print("1996년부터 2019년 영화관람률 평균은", movie)
print("1996년부터 2019년 뮤지컬관람률 평균은", musical)
if movie > musical:
    print("영화관람률이 뮤지컬관람률보다 평균이 높다.")
else:
    print("뮤지컬관람률이 영화관람률보다 평균이 높다.")
print("=================================================")


#=============================================================================
#문화관람 종류별 데이터 정의
df = pd.DataFrame({
'year' : ['1996','2000','2004','2007','2009','2011','2013','2015','2017','2019'], 
'movie' : [27.2,26.6,40.2,40.1,44.8,47.9,54.4,58.8,58.8,58.4], #영화
'musical' : [8.6,7.3,9.3,12.3,12.9,14.7,15.3,14.9,15,13.7], #뮤지컬
'dance' : [1.3,0.9,1.1,1.2,1.1,1.5,1.5,1.2,1.3,1], #무용
'concert' : [11.4,9.7,10.2,12.6,12.9,14.8,13.7,13.8,13.8,16.5], #음악회
'museum' : [11.3,8.5,12.7,15,13.8,15.5,16.4,17.8,16.7,15.7], #박물관
'artmuseum':[9.8,6.3,8.9,11.3,10.1,12.1,12.3,12.8,13.5,13] #미술관
})


#모든 문화의 관람률 비교해보기
ax = plt.gca() 
df.plot(kind='line',x='year',y='movie',color='orange', ax=ax)
df.plot(kind='line',x='year',y='musical', color='red', ax=ax)
df.plot(kind='line',x='year',y='dance', color='pink', ax=ax)
df.plot(kind='line',x='year',y='artmuseum', color='black', ax=ax)
df.plot(kind='line',x='year',y='concert', color='purple', ax=ax)
df.plot(kind='line',x='year',y='museum', color='green', ax=ax)
plt.show()


df.plot(kind='scatter',x='year',y='musical',color='red') #년도별 뮤지컬 산포도로 그려보기
plt.show()

df.plot(kind='bar',x='year',y='movie') #년도별 영화관람률 막대그래프로 그려보기 
plt.show()


fig = plt.figure(figsize=(16, 16)) #그래프끼리 합쳐지는 혼동 피하는 코드

#=============================================================================

#남,여,전체 문화관람률 데이터 정의
df1 = pd.DataFrame({
'year' : ['2015','2017','2019'],
'man' : [62,61.6,61.1],
'woman' : [66.9,66.3,66.1],
'all' : [64.5,64.0,63.6]    
})

ax = plt.gca()
df1.plot(kind='line',x='year',y='man',color = 'blue', ax=ax)
df1.plot(kind='line',x='year',y='woman', color='red', ax=ax)
df1.plot(kind='line',x='year',y='all', color='orange', ax=ax)
plt.show()
fig = plt.figure(figsize=(16, 16))


#=============================================================================
#2019년도 20~29세 문화관람률 데이터 정의
ratio = [17.2, 82.8]
labels = ['no watch', 'watch']
plt.title('2019 : age of 20~29')
plt.pie(ratio, labels=labels, autopct='%.1f%%')
plt.show()
fig = plt.figure(figsize=(16, 16))
#=============================================================================
#2019년도 30~39세 문화관람률 데이터 정의
ratio = [20.2, 79.8]
labels = ['no watch', 'watch']
plt.title('2019 : age of 30~39')
plt.pie(ratio, labels=labels, autopct='%.1f%%')
plt.show()
fig = plt.figure(figsize=(16, 16))
#=============================================================================
#2019년도 40~49세 문화관람률 데이터 정의
ratio = [25.6, 74.4]
labels = ['no watch', 'watch']
plt.title('2019 : age of 40~49')
plt.pie(ratio, labels=labels, autopct='%.1f%%')
plt.show()
fig = plt.figure(figsize=(16, 16))
#=============================================================================