import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Read data from the CSV file
df = pd.read_csv('D:/CSE_student_performances/train.csv')
avg = df['Burn Rate'].median()
df["Burnout"] = df["Burn Rate"] > avg

# fig1
counts = df.groupby(by=["Designation", "Burnout"]).size().reset_index(name="count")
fig1 = px.bar(counts, x="Designation", y="count", color='Burnout', color_discrete_map={
    'true': 'rgb(0,0,128)',
    'false': 'rgb(235,207,52)'
})
fig1.update_traces(hovertemplate='Seniority Level: %{x}<br>Count: %{y}')
fig1.update_layout(xaxis=dict(
    title="Seniority Level"
), yaxis=dict(
    title="Number Of Employees"
))

# fig2
counts = df.groupby(by=["Gender", "Burnout"]).size().reset_index(name="count")
fig2 = px.bar(counts, x='Gender', y='count', color='Burnout', color_discrete_map={
    'true': 'rgb(0,0,128)',
    'false': 'rgb(235,207,52)'
}, barmode="group")
fig2.update_traces(hovertemplate='Gender: %{x}<br>Count: %{y}')
fig2.update_layout(xaxis=dict(
    title="Gender"
), yaxis=dict(
    title="Number Of Employees"
))

# fig3
fig3 = px.scatter(df, x="Mental Fatigue Score", y="Burn Rate")

dash.register_page(__name__, path='/dashboard')

layout = html.Div(dbc.Container([
    html.H1('Dashboard'),
    dbc.Stack([
        dbc.Row([
            # First graph
            dbc.Stack([
                dbc.Col([
                    dbc.Card(
                        dbc.CardBody(
                            [html.H4("Effect of seniority level on Burnout Status", className="card-title"),
                             dcc.Graph(
                                 id='graph1',
                                 figure=fig1
                             )
                             ])
                    )

                ], width=6),

                # Second graph
                dbc.Col([
                    dbc.Card(
                        dbc.CardBody(
                            [html.H4("Gender-wise Distribution of Burnout Rate", className="card-title"),
                             dcc.Graph(
                                 id='graph2',
                                 figure=fig2
                             )
                             ])
                    )

                ], width={"size": 6, "offset": 0}),

            ], direction="horizontal")

        ]),
        dbc.Row(
            [
                dbc.Col([
                    dbc.Card(
                        dbc.CardBody(
                            [html.H4("Effect of Mental Fatigue Score and Burnout Rate"),
                             dcc.Graph(
                                 id='graph3',
                                 figure=fig3
                             )
                             ], ), style={'margin': '0 auto',}
                    )

                ], width={'size': 12, 'offset': 0}),  # Adjust width to fill the entire row
            ]
            , justify='center', align="center")
    ], gap='4')

]), style={"height": "200vh", }, )

