# this is a demo for the streamlit application
import joblib
import streamlit as st

st.title("This is a demo title")

st.header("Hello streamlit header")

st.subheader('This is how a subtitle looks like')

st.text('Some text to see')

st.success('How success message is displayed')

st.warning('How warning messages are shown')

st.info('How information is displayed')

st.error('How an error message is displayed')

if st.checkbox('select/unselect'):
    st.text("user selected the checkbox")
else:
    st.text('user has not selected the box')

state = st.radio('What is your favourite color?',{'Red',"Orange","Teal"})

if state == 'Teal':
    st.success('That is a perfect color')
else:
    st.warning('Have some taste')

occupation = st.selectbox('What do you do?',['Ml engineer','Data scientist','Data engineeer'])
st.text(f'Your occupation is {occupation}')

if st.button('Submit'):
    st.info("You submited your work")

st.sidebar.header("Demo work")
st.sidebar.text('Learning Mlops')


