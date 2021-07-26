import numpy as np
import pandas as pd
import matplotlib
# 50개의 난수로 이루어진 데이터 생성
data = np.random.rand(50)

# 판다스 시리즈 타입 데이터로 변환
seri = pd.Series(data)

# 선형 그래프 그리기
seri.plot()

# 그래프 보여주기
matplotlib.pyplot.show()
