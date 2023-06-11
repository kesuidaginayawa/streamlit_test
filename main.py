# ターミナルで実行すると起動する　streamlit run main.py

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit入門')


'Start!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)
'Done!!!!!'




st.write('DataFrame')

df1 = pd.DataFrame({
    'a':[1, 2, 3, 4],
    'b':[10, 20, 30, 40]
})

# st.dataframe(df.style.highlight_max(axis=0), width=300, height=200) #動的な表

st.table(df1.style.highlight_max(axis=0)) #静的な表



df2 = pd.DataFrame(
    np.random.rand(30,3),
    columns=['a','b','c']
)

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)




"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""


df3 = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70] ,
    columns=['lat', 'lon']
)
st.map(df3)



st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('3206_color.png')
    st.image(img, caption='Hey', use_column_width=True)

option = st.sidebar.selectbox(
    '好きな数字は？',
    list(range(1,11))
)
'あなたの好きな数字は', option, 'です'


text = st.sidebar.text_input('趣味は？')
'あなたの趣味は', text, 'です'


con = st.sidebar.slider('調子は?', 0, 100, 50)
'コンディション: ', con

left_col, right_col = st.columns(2)
button = left_col.button('右カラムに文字を表示')
if button:
    right_col.write('ここは右カラム')

exp = st.expander('問題１')
exp.write('答え')
exp = st.expander('問題２')
exp.write('答え')
exp = st.expander('問題３')
exp.write('答え')

