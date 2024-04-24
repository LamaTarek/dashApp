import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import pickle
import numpy as np
import sklearn

with open('D:/CSE_student_performances/pages/model.pkl', 'rb') as file:
    lr_model = pickle.load(file)

dash.register_page(__name__, path='/model')

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
                    html.H2('ll', id='rate', style={'textAlign': 'center'})
                ])
            )
        ], style={"height": "100vh", })
    ])]))
# Callback to handle prediction
@callback(
    Output(component_id='rate', component_property='children'),
    Input(component_id='submit', component_property='n_clicks'),
    State(component_id='gender', component_property='value'),
    State(component_id='wfh', component_property='value'),
    State(component_id='level', component_property='value'),
    State(component_id='hours', component_property='value'),
    State(component_id='score', component_property='value'),
)
def predict(n_clicks, gender, wft, level, hours, score):
    if n_clicks is None or n_clicks == 0:
        return dash.no_update
    gender_mapper = {
        'Female': 0,
        'Male': 1
    }

    wft_mapper = {
        'No': 0,
        'Yes': 1
    }

    obs = np.array(
        [int(gender_mapper[gender]), int(wft_mapper[wft]), int(level), int(hours), float(score)]).reshape(1, -1)
    rate = float(lr_model.predict(obs)[0])



    return rate