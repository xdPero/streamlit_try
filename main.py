import streamlit as sl
import pandas

data={
    'Series_1' : [1,2,3,4,5],
    'Series_2' : [10,30,40,50,70]
}

df = pandas.DataFrame(data)


sl.title("My first Streamlit app")
sl.subheader("Introducing Streamlit")
sl.write("I hope that you enjoyed my Streamlit app")
sl.write(df)
sl.line_chart(df)
sl.area_chart(df)
my_slider = sl.slider("Celsius")
sl.write(my_slider,' in Fahrenheit is: ', my_slider * 9/5 + 32)
