import streamlit as st
import streamlit.components.v1 as components

st.title('Homepage')

def custom_part(name:str):
    return components.html(
        f'''
        <div id="header" class="text-center">
        <h1>Welcome to {name}'s practice website</h1>
        </div>
        '''
    )

custom_part('colin')

custom_part('abc')
