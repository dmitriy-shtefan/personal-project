import streamlit as st

EMAIL = 'shtefan.dmitry@gmail.com'
GITHUB_URL = 'https://github.com/dmitriy-shtefan/'


def show_about_page():
    st.title("Dmytro")

    st.subheader("Мої проєкти")

    with st.container(border=True):
        st.subheader("Список контактів")
        st.write(
            "Застосунок для збереження контактів. Користувач може додавати, "
            "видаляти, шукати і фільтрувати контакти."
        )
        st.write("Технології: Python, Streamlit, JSON, pandas")

    st.subheader("Мої Контакти")
    with st.container(border=True):
        st.write(f"Email: {EMAIL}")
        st.write(f"Github: {GITHUB_URL}")


