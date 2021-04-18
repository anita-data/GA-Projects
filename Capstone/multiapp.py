import streamlit as st

class MultiApp:
    Usage:
        def home():
            st.title("Home")
        def churn():
            st.title("Churn Prediction")
         def model():
        st.title("Models")
        app = MultiApp()
        app.add_app("Home", home)
        app.add_app("Churn Prediction", churn)
        app.add_app("Models", model)
        app.run()
        
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        app = st.sidebar.radio(
            'Go To',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()