# 종합설계 

## 태풍 경로 예측
### 예측 순서
1. 태풍 이미지를 이용하여 한반도에 상륙한 태풍과 아닌 태풍을 분류하여 정확도를 확인
2. 여러가지 메타 데이터를 활용하여 태풍의 이미지와 연결해주고 경로를 예측
3. 완성하여 태풍이 일어나면 경로 예측을 할 수 있게 적용 해볼 예정   

### 언어 사양
* python 3.7
  * numpy, pandas, pyplot 활용
  * Machine Learning 도구는 다음중 하나를 선택한다.
  1. fast.ai pytorch based on pytorch
  2. keras in tensorflow


### 어떤 작업을 해야하는가?
* 작성 예정

### 데이터
* 공공 데이터 포털 | 기상청 태풍예보정보(API) : https://www.data.go.kr/dataset/15000174/openapi.do
* 공공 데이터 포털 | 기상청 태풍예보정보(CSV) : https://www.data.go.kr/dataset/15000174/fileData.do
* 공공 데이터 포털 | 위성자료/이미지자료 : https://www.data.go.kr/dataset/3036149/fileData.do 
  * 천리안 및 외국위성 영상자료
* 공공 데이터 포털 | 기상청 특보정보 : https://www.data.go.kr/dataset/15000415/openapi.do
  * 생활기상정보에 기상특보정보 중 기상특보통보문,기상정보문,기상속보,기상예비특보, 특보코드,특보현황,기상특보목록,기상정보목록,기상속보목록,기상예비특보목록 정보를 조회하는 서비스