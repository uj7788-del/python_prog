import streamlit as st

# 타이틀 텍스트 출력
st.title('첫번째 웹 어플 만들기 🤙😁🤙🎮🕹️👾')

'''
# 이것이 제목 :smile: :sunglasses:
이것은 그냥 문자열 
### 지금부터는 코드 

```python
import streamlit as st
import pandas

a=3
c=5
print(a+c)
```

## 마크다운에서 yellow(작성법)
1. 번호입력
  1. 하위목록  
- 번호 없는 ~목록1 
- 번호 없는 목록1
- **번호없는** 목록1

이것은 본문입니다.
 
'''
st.divider()

with st.echo():
  # 이 블록의 코드와 결과를 출력
  name = 'yujeong'
  st.write("hello, streamllit!", 'name')

st.caption('이것이 캡션이다.')
'안녕하세요'

# :blue[데이터 테이블]

#### :orange[Pandas 데이터프레임]

import pandas as pd

df = pd.DataFrame(
    {
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [24, 34, 45]
    }
)

df  # 👉 데이터프레임 출력


#### :orange[지표(Metric)]

col1, col2, col3 = st.columns(3)  # 3개의 컬럼 생성

col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.divider()  # 👉 구분선

# :blue[Streamlit 그래프]

import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

#### :orange[st.area_chart()]
st.area_chart(chart_data)

#### :orange[st.line_chart()]
st.line_chart(chart_data)

#### :orange[st.bar_chart()]
st.bar_chart(chart_data)

#### :orange[st.scatter_chart()]
st.scatter_chart(chart_data)

#### :orange[st.map()]
df = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [37.55, 126.92],
    columns=["lat", "lon"],
)

st.map(df)

st.divider()  # 👉 구분선

# :blue[시각화 라이브러리]

#### :orange[Matplotlib: st.pyplot()]

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)  # 👉 차트 출력