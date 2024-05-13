import streamlit as st
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


