import streamlit as st
from pathlib import Path
from .place import Place

SCRIPT_DIR = Path(__file__).resolve().parent
CSS_FILE_NAME = SCRIPT_DIR / 'styles.css'


PLACES = [
    Place(
        name="Львів",
        country="Україна",
        description=("Місто старовинної архітектури, затишних вулиць"
                     " і ароматної кави."),
        image_url="https://images.unsplash.com/photo-1630827601338-4891ff8d962a?auto=format&fit=crop&w=900&q=80",
        visited=True
    ),
    Place(
        name="Рим",
        country="Італія",
        description=("Хочу побачити Колізей, Римський форум"
                     " і прогулятися історичним центром."),
        image_url="https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=900&q=80",
        visited=False
    )
]


def load_styles():
    styles = ""
    try:
        with open(CSS_FILE_NAME) as f:
            styles = f.read()
    except FileNotFoundError:
        pass

    return styles


def show_places_page():
    css = load_styles()
    styles = f"<style>{css}</style>"

    places_html = ""
    for place in PLACES:
        places_html += place.to_html()

    html = f"""
        <main class="places-page">
            <header class="page-header">
                <h1>Мої улюблені місця</h1>
                <p>Місця, які я вже відвідав або хочу відвідати.</p>
            </header>
            <section class="places-grid">
                {places_html}
            </section>
        </main>
    """

    st.html(styles + html)
