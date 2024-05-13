
import os
import streamlit as st
import numpy as np
import pandas as pd
import datetime
from PIL import Image

def get_file_list(filepath):
    return ['a', 'b']

st.set_page_config(
    page_title= 'my first',
    page_icon='',
    layout='wide'
)

st.title('hello world')

st.markdown('> Streamlit 支持通过 st.markdown 直接渲染 markdown')

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python", line_numbers=False)

#获取当前文件的目录
filepath = st.sidebar.text_input("请输入当前文件的路径", key="name")
if filepath:

    allList = get_file_list(filepath)
    selectValue = st.sidebar.selectbox(label='在当前目录下选择文件', options=allList)
else:
    st.sidebar.error("请输入文件地址")

if st.sidebar.button('点击'):
    st.write("点了")

cb = st.checkbox('确认', value=False)

if cb:
    st.write('选了确认')

sex = st.radio(label='请输入性别', options=('男','女','保密'), index=1, help='如果不选')
if sex=='男':
    st.write('我选择了男')

options = st.multiselect(label= '请问你喜欢吃什么水果', options=('橘子','香蕉','苹果','葡萄'), help='选择您喜欢吃什么水果')

st.write('您喜欢吃的水果是：', options)

age = st.slider(label='请通过滑块选择年龄', min_value=0, max_value=100, value=4, step=1, help='请输入年龄')
st.write('您输入的年龄是：', age)

num = st.number_input(label='请输入数字', min_value=0, max_value=100, step=1, help='请输入年龄')
st.write('您的年龄是：', num)

text = st.text_area(label='请输入文本', value='请输入...', height=5, max_chars=200, help='最大长度限制为200')
st.write('您输入的多行文字是：', text)

birthday = st.date_input(label='请输入您的出生日期', value = None, min_value=None, max_value=datetime.date.today(),help='请输入出生日期')
st.write('您的生日是：', birthday)


t = st.time_input(label = '请输入一个时间', 
                  value=None, 
                  help='请输入一个时间')
 
st.write('您输入的时间是：', t)

random_data = np.random.rand(100, 10)

data = {
    'latitude': [37.7749, 34.0522, 40.7128, 39.8],
    'longitude': [-122.4194, -118.2437, -74.0060, 116.57732],
    'name': ['San Francisco', 'Los Angeles', 'New York', 'china']
}
 
st.map(data, zoom=4, use_container_width=True)

# df = pd.DataFrame(random_data, columns=[f'Col{i}'  for i in range(1,11)])

# st.dataframe(df)
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df)

# im_url = Image.open('https://image.baidu.com/search/detail?ct=503316480&z=0&tn=baiduimagedetail&ipn=d&word=%E5%A4%B4%E5%83%8F%E5%9C%B0%E5%9D%80%E9%93%BE%E6%8E%A5&step_word=&lid=1855015140144513163&ie=utf-8&in=&cl=2&lm=-1&st=-1&hd=0&latest=0&copyright=0&cs=2653788118,1855704992&os=768447720,2436488102&simid=2653788118,1855704992&pn=1&rn=1&di=7355526631391232001&ln=1617&fr=&fmq=1715589476093_R&ic=0&s=undefined&se=&sme=&tab=0&width=&height=&face=undefined&is=0,0&istype=2&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=1e&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fcbu01.alicdn.com%252Fimg%252Fibank%252F2020%252F691%252F145%252F19285541196_2007620675.jpg%26refer%3Dhttp%253A%252F%252Fcbu01.alicdn.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1718181476%26t%3D3a2a75f002f7a8df33041f7a86b7d716&rpstart=0&rpnum=0&adpicid=0&nojc=undefined')
# st.image(im_url, caption='这是一个网络图片')
#st.video("http://www.w3school.com.cn/i/movie.mp4")




