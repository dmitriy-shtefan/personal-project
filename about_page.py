import streamlit as st

EMAIL = 'shtefan.dmitry@gmail.com'
GITHUB_URL = 'https://github.com/dmitriy-shtefan/'
AVATAR_URL = 'https://github.com/dmitriy-shtefan.png?size=250'


def show_about_page():
    title_col, avatar_col = st.columns([3, 1])

    with title_col:
        st.title("Dmytro")

    with avatar_col:
        st.html(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src="{AVATAR_URL}" 
                     style="width: 170px; height: 170px; object-fit: cover;
                            border-radius: 50%; border: 3px solid #4b7bec;
                            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);">
            </div>
            """
        )

    st.subheader("Мої проєкти")

    with st.container(border=True):
        st.subheader("Список контактів")
        st.write(
            "Застосунок для збереження контактів. Користувач може додавати, "
            "видаляти, шукати і фільтрувати контакти."
        )
        st.write("Технології: Python, Streamlit, JSON, pandas.")

    with st.container(border=True):
        st.subheader("Мої улюблені місця")
        st.write(
            "Застосунок для перегляду добірки пам'ятних і цікавих локацій. "
            "Допомагає зберегти спогади про подорожі і планувати майбутні пригоди."
        )
        st.write("Технології: Python, Streamlit, HTML, CSS.")

    st.subheader("Мої Контакти")
    with st.container(border=True):
        st.write(f"Email: {EMAIL}")
        st.write(f"Github: {GITHUB_URL}")


