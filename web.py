import streamlit as st
from game_logic import coin_toss

st.set_page_config(page_title='Coin Toss Game')

st.title('Toss the Coin')
st.caption('Made by SS')

st.write('Pick a side and test your luck!')

choice = st.radio('Choose a side:', ['heads', 'tails'])

if st.button("Toss the coin!"):
    result = coin_toss()
    st.subheader(f"The coin landed on: **{result}**")

    if choice == result:
        st.success('YOU WON')
    else:
        st.error('Whoops, Good Luck Next Time')
