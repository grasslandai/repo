import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Avoid loading data every time, just load 1 time on the first visit of webpage
@st.cache
def load_data():
    #df = pd.read_csv(".\data\heart.csv")
    df = pd.read_csv("./data/heart.csv") # support deployment environment, need to use linux path notation
    return df

def show_explorer_page():    
    st.title("Explore heart disease datasets")

    ######## Display data distribution
    st.write (""" #### Data distribution with heart disease""")
    data = df["target"].value_counts()
    display_data = pd.DataFrame({
        "With heart disease": [data[1]],
        "Without heart disease": [data[0]]
    })

    # CSS to inject contained in a string
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.table(display_data)
    ###########################################################


    st.write(
        """
    #### Age distribution with heart disease
    """
    )
    data = df.groupby(["age"])["target"].count().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### gender distribution with heart disease
    """
    )
    data = df.groupby(["sex"])["target"].count().sort_values(ascending=True)
    # create pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=("Female","Male"), autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)


df = load_data()