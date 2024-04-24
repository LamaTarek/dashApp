import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Read data from the CSV file
df = pd.read_csv('D:/CSE_student_performances/train.csv')
avg = df['Burn Rate'].median()
df["Burnout"] = df["Burn Rate"] > avg
male_count = df.Gender[(df.Gender == 'Male') & (df['Burn Rate'] > avg)].count()
female_count = df.Gender[(df.Gender == 'Female') & (df['Burn Rate'] > avg)].count()
counts = df.groupby(by=["Designation", "Burnout"]).size().reset_index(name="count")

fig1 = px.bar(counts, x="Designation", y="count", color='Burnout', color_discrete_map={
    'Female': 'rgb(0,0,128)',
    'Male': 'rgb(235,207,52)'
})
fig1.update_traces(hovertemplate='Seniority Level: %{x}<br>Count: %{y}')
fig1.update_layout(title="Effect of Seniority Level on Burnout Status", xaxis=dict(
        title="Seniority Level"
    ), yaxis=dict(
        title="Number Of Employees"
    ))
#fig1.update_xaxes(labelalias=dict(true="Burnout", false="Non-burnout"))

dash.register_page(__name__, path='/dashboard')

layout = html.Div(dbc.Container([
    html.H1('Dashboard'),
    dbc.Row([
        # First graph
        dbc.Col([
            dcc.Graph(
                id='graph1',
                figure=fig1
            )
        ], width=6),  # Take up half of the width

        # Second graph
        dbc.Col([
            dcc.Graph(
                id='graph2',
                figure=fig1
            )
        ], width=6)  # Take up half of the width
    ])
]), style={"height": "100vh", }, )
