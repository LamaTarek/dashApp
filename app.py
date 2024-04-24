import pandas as pd
import dash
from dash import Dash, dcc, html, callback_context
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

data = pd.read_csv("CSE_student_performances.csv")

app = Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR, dbc.icons.BOOTSTRAP], use_pages=True)

app.title = "Are Your Employees Burning Out?"

app.layout = dbc.Container(
    children=[
        dash.page_container
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
