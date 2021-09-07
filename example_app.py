import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

import time

from numpy.core.arrayprint import _leading_trailing #Display code

from streamlit_metrics import metric_row #Display Ranking value

from typing import Counter #Fix re-session when using function 

# st.title('My first app')

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

#Line Chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#Plot real world map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


#interactive Checkbox to show/hide data
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

#Select box for opition(Dropdown)
# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

#-----------Layout Web App--------------

#Drop down with pin left side
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option

#Divide Column to display two widget with ratio
left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")


#Help Text hide and can be expand
expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

#Show progress with time for long computation
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(10):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

#Text Input(blank box)
st.text_input('Enter your value', key="name")

st.write("""
    # Biggest
    ## Bigger
    ### Big

    **Header**

    >Column

    . Python    
    . Javascript   
    . SQL   
    . Dart    
""")

#Additional style for adjust text size
st.header('header')
st.subheader('subheader')

#Slider(Long button tap)
number = st.slider('Pick a number', 0, 100)


#Radio button
languages = ['python', 'c', 'rust', 'c++']

st.radio('Pick a language', languages)

#Date picker
date = st.date_input('Pick a date')

#Color Selector
color = st.color_picker('Pick a color')

#File Uploader
file = st.file_uploader('Pick a file')

#Display Json value
st.json({
    "code": 0,
    "data": {
        "sex": "female",
        "age": 18,
        "score": 100
    }
})

#Display Python code for easy copy
code = """
    def func():
        print('Hello streamlit.')
"""
st.code(code, language='python')

#Show Table
df = pd.DataFrame(np.random.randn(50, 5), columns=(
    'col %d' % i for i in range(5)))
st.table(df)

#Ranking show value in column
st.write("YOLOv5 performance")
metric_row(
    {
        "YOLOv5s": 100,
        "YOLOv5m": 200,
        "YOLOv5l": 300,
        "YOLOv5x": 400
    }
)

#Creating counting function with button
st.title('Hello streamlit.')
# counter = 0

# increment = st.button('Increment')
# if increment:
#     counter += 1

# st.write('Count= ', counter)

# if 'counter' not in st.session_state:
#     st.session_state.counter = 0

# increment = st.button('Increment')
# if increment:
#     st.session_state.counter += 1

# st.write('Count= ', st.session_state.counter)

# callbacks
# def increment_counter():
#     st.session_state.counter += 1

# st.title('Callbacks')
# if 'counter' not in st.session_state:
#     st.session_state.counter = 0

# st.button('Increment', on_click=increment_counter)
# st.write('Count= ', st.session_state.counter)


# st.title('Callbacks with args')
# if 'counter' not in st.session_state:
#     st.session_state.counter = 0

# increment_value = st.number_input('Enter a value', value=0, step=1)

# def increment_counter(increment_value):
#     st.session_state.counter += increment_value

# increment = st.button('Increment', on_click=increment_counter,
#                       args=(increment_value, ))

# st.write('Count = ', st.session_state.counter)


st.title('Callbacks with kwargs')
if 'counter' not in st.session_state:
    st.session_state.counter = 0

def increment_counter(increment_value=0):
    st.session_state.counter += increment_value

def decrement_counter(decrement_value=0):
    st.session_state.counter -= decrement_value

st.button('Increment', on_click=increment_counter,
          kwargs=dict(increment_value=5))

st.button('Decrement', on_click=decrement_counter,
          kwargs=dict(decrement_value=1))

st.write('Count = ', st.session_state.counter)