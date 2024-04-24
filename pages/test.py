import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Read data from the CSV file
df = pd.read_csv('D:/CSE_student_performances/train.csv')
avg = df['Burn Rate'].median()
male_count = df.Gender[(df.Gender == 'Male') & (df['Burn Rate'] > avg)].count()
female_count = df.Gender[(df.Gender == 'Female') & (df['Burn Rate'] > avg)].count()
fig = px.pie(df, values=[female_count, male_count], names=['Female', 'Male'],
             title='Percentage of Male and Female with Burn Rate Above The Average')

dash.register_page(__name__, path='/t')

layout = html.Div(dbc.Container([
    html.H1('Dashboard'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div(
                        children=[
                            html.Div(
                                # className="padding-top-bot",
                                children=[
                                    html.H6("Gender"),
                                    dbc.Select(id="gender",
                                               options=[{"label": "Female", "value": "Female"},
                                                        {"label": "Male", "value": "Male"}, ]
                                               )
                                ],
                                style={'margin-bottom': '5px'}
                            ),
                            html.Div(
                                className="padding-top-bot",
                                children=[
                                    html.H6("Working From Home Availability"),
                                    dbc.Select(id="wfh",
                                               options=[{"label": "Yes", "value": "Yes"},
                                                        {"label": "No", "value": "No"}, ]
                                               )
                                ],
                            ),
                            html.Div(
                                className="padding-top-bot",
                                children=[
                                    html.H6("Seniority Level"),
                                    dbc.Select(id="level",
                                               options=[{"label": "1", "value": "1"},
                                                        {"label": "2", "value": "2"},
                                                        {"label": "3", "value": "3"},
                                                        {"label": "4", "value": "4"},
                                                        {"label": "5", "value": "5"}, ]
                                               )
                                ],
                            ),
                            html.Div(
                                className="padding-top-bot",
                                children=[
                                    html.H6("Working Hours Per Day"),
                                    dbc.Select(id="hours",
                                               options=[{"label": "1", "value": "1"},
                                                        {"label": "2", "value": "2"},
                                                        {"label": "3", "value": "3"},
                                                        {"label": "4", "value": "4"},
                                                        {"label": "5", "value": "5"},
                                                        {"label": "6", "value": "6"},
                                                        {"label": "7", "value": "7"},
                                                        {"label": "8", "value": "8"},
                                                        {"label": "9", "value": "9"},
                                                        {"label": "10", "value": "10"}, ]
                                               )
                                ],
                            ),
                            html.Div(
                                className="padding-top-bot",
                                children=[
                                    html.H6("Mental Fatigue Score"),
                                    dbc.Input(id="score", type="number", min=0, max=10, step=1,
                                              placeholder='Enter Your Score from 0 to 10'),
                                ],
                                style={'margin-bottom': '10px'},
                            ),
                            html.Div(
                                className="padding-top-bot",
                                children=[
                                    dbc.Button('Predict', id='submit', n_clicks=0, className="d-grid gap-2 ",
                                               size='lg', style={'textAlign': 'center'}),
                                ],
                                style={'textAlign': 'center'},
                            ),

                        ],
                    )
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([

                ])
            )
        ], style={"height": "100vh", })
    ])]))
