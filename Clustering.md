# Clustering 



## Components of a Clustering Task 



(1) pattern representation 

(2) definition of a pattern proximity measure appropriate to the data domain

(3) **grouping**

(4) data abstraction 

(5) assesment of output





## Clustering Techniques



### 1. Hierarchical Clustering Algorithms

- 샘플 하나하나를 클러스터로 간주하고 유사도가 가장 가까운 샘플들을 클러스터화하는 방법

####  (1) Graph-based

: 각 데이터를 노드로 하고, 노드 간 연결선을 링크로 하여, 링크의 길이를 가지고 길이 측정

* **Simple Linkage method (단일 연결법)**

  : 클러스터 간 거리를 잴 때, 다른 클러스터의 점들 중에서 가장 가까운 두 점 간의 거리를 사용

* **Complete Linkage method (완전 연결법)**

  : 클러스터 간 거리를 잴 때, 가장 멀리 있는 두 점 간의 거리를 사용

* Average Linkage method (평균 연결법)

  : 클러스터 간 거리를 잴 때, 모든 점들 사이의 거리를 평균 내어 사용

#### (2) Prototype-based

: 미리 정해놓은 각 클러스터의 프로토타입에 데이터가 얼마나 가까운가로 클러스터의 형태 결정

* Centroid Linkage method (중심 연결법)

  : 클러스터 간 거리를 잴 때, 각 클러스터의 중심 간의 거리를 사용

* Ward Linkage method (Ward 연결법)

  : 두 클러스터의 유사성을 두 클러스터를 합쳤을 때 오차제곱합의 증가분에 기반해서 측정

   -> 거리 행렬 구할 때 오차제곱합의 증가분을 두 클러스터 간의 거리로 측정

  

<img src="/Users/chasuman/Library/Application Support/typora-user-images/image-20211028224826791.png" alt="image-20211028224826791" style="zoom:120%;" />









## Partitional Algorithms



### 1. k-Means Clustering Algorithm

---

1. 클러스터 개수 k개만큼 랜덤하게 k개의 점 선택

2) 이 점들을 기준으로 가장 가까운 점들을 클러스터화

3) 클러스터에 맞게 중심 update

4)  수렴 기준을 달성할 때까지 반복

---

* 초기값을 어떻게 잡는지에 따라 결과가 크게 차이남. 
* Euclidean distance를 metric으로 사용하기 때문에 효돌 데이터에 사용하기에는 어려울듯





### 2. Graph-Theoretic Clustering

* 가장 잘 알려진 알고리즘은 Minimal Spanning Tree(MST)
* 최소 길이의 edge들로 모든 노드들을 연결하고 그 중 가장 길이가 긴 edge를 끊어내어 클러스터를 형성하는 방식



<img src="/Users/chasuman/Library/Application Support/typora-user-images/image-20211028233229250.png" alt="image-20211028233229250" style="zoom:120%;" />





## SOM Algorithm

* 차원 축소와 클러스터링을 동시에 수행하는 기법

* 고차원의 input space를 저차원의 latent space로 매핑시키는 것이 목적
* 결국 저차원의 map을 학습해서 데이터 분포 형태로 근사시키고자 함
* 2차원의 4 x 5 size의 map은 20개의 map point로 이루어지고, 각 node는 데이터의 차원 수와 동일한 weight parameter 개수를 가짐. 



**Algorithm**

---

1. n 개의 feature를 갖는 데이터셋이 있다고 하자. 
2. 맵을 만드는데, 각각의 노드는 n개의 weight elements로 이루어진 weight vector를 parameter로 가짐.
3. weight vector의 초기값은 0에 가까운 값으로 랜덤하게 설정 
4. 데이터셋에서  observation 한 개 랜덤하게 선택.
5. 이 점에서 각각의 노드로의 Euclidean distance 계산 
6. 최소 거리인 노드 선택 -> 얘가 winning node
7. winning node의 weight를 업데이트해서 더 가깝게 만들고, 
8. Gaussian neighborhood function을 써서 winning node의 neighbor들도 그 점에 가깝게 weight update
9. 1~5 반복하고 weight를 계속해서 업데이트해주면 됨. 

---





![img](http://i.imgur.com/ZsAdHxT.png)





## K-Modes

- 범주형 자료에 적용하는 클러스터링 기법 

- 평균 대신 최빈값을 사용

- K-Means와 알고리즘은 동일하지만 유사도를 구하는 방식이 다름

  

  ![image-20211029115746454](/Users/chasuman/Library/Application Support/typora-user-images/image-20211029115746454.png)







## K-Prototypes 

* K-means 와 K-modes 동시에 활용
* 연속형과 범주형 자료를 동시에 활용할 수 있는 클러스터링 방식 
* 연속형 자료는 유클리디안 거리로, 범주형 자료는 k-modes 의 유사도에 가중치를 곱한 것을 더해줘서 유사도를 구함



![image-20211029120138524](/Users/chasuman/Library/Application Support/typora-user-images/image-20211029120138524.png)



* 가중치 선택은 연속형 자료의 분포에 의해 결정됨
* $l$ 번째 클러스터에서 연속형 자료의 표준편차 $\sigma_{l}$ 에 의해 결정됨. 
* 적절한 $\gamma_{l}$ 을 구하는 방법은 없으나, 초기값으로 $\gamma_{l} = \frac{\sigma^2}{2}$ 을 사용함. 







## 논의해볼 점

* 클러스터링이 잘 된다면 후에 어떤 방식으로 프로필 분석을 할지
* 클러스터링이 잘 안 된다면? (고차원 + Sparse 할 경우 잘 안 될 가능성 높음)
* 추천시스템 등으로 대체 해볼 수도 있을 것 같다 



- 