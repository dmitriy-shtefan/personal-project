import streamlit as st


def show_places_page():
    styles = """"<style>
        
    </style>
    """

    html = """
    <article>
        <p>United Kingdom</p>
        <img src="" alt="London image" />
        <h3>London</h3>
        <p>A historic city with famous landmarks, museums, and beautiful parks</p>
        <span>Already visited</span>
    </article>
    """

    st.html(styles + html)
