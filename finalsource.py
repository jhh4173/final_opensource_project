import matplotlib.pyplot as plt
import pandas as pd
culture = pd.read_csv('C:/temp/software2.csv')
print(culture)
list1 = ["1996", "2000", "2004", "2007", "2009", "2011", "2013", "2015", "2017", "2019"] #index로 사용할 년도를 작성한다. 
culture.index = list1 #index를 list1로 변경한다.
print(culture) #우리나라의 문화관람률을 출력한다. 
print(culture["영화"]) #우리나라의 년도별 문화관람률 중 영화관람률을 출력한다.
print(culture["영화"].max()) #우리나라의 영화관람률 중 가장 높은 값을 출력한다.
print(culture["영화"].idxmax()) #우리나라의 영화관람률 중 가장 높은 값을 년도와 함께 출력한다. 
print(culture.iloc[8:10])#우리나라의 문화관람률 중 2017년과 2019년도만 출력한다.
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
        



