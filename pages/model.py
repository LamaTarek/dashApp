import numpy as np
from dash.dependencies import Input, Output, State
import pickle
from dash import html, register_page  # , callback # If you need callbacks, import it here.
import dash
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

register_page(
    __name__,
    name='Are Your Employees Burning Out?',
    path='/model'
)

with open('D:\CSE_student_performances\pages\model.pkl', 'rb') as file:
    lr_model = pickle.load(file)

def layout():
    layout = html.Div(

        children=[
            # User Controls
            html.Div(

                children=[
                    html.Div(
                        className="bg-white user-control",
                        style={'height': '580px',},
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
                                    html.H6("Is work-from-home Setup Available?"),
                                    dbc.Select(id="wfh",
                                               options=[{"label": "Yes", "value": "Yes"},
                                                        {"label": "No", "value": "No"}, ]
                                               )
                                ],
                            ),
                            html.Div(
                                className="padding-top-bot",
                                children=[
                                    html.H6("Designation"),
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
                                    html.H6("Working hours"),
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
                ],
            ),
            # Prediction Area
            html.Div(
                className="card-left",
                children=[
                    html.Div(
                        style={'height': '580px'},
                        className="bg-white",
                        children=[
                            html.H5("Burning Out Rate Prediction"),
                            html.Img(src='assets/burn1.jpg', id='img1',
                                     style={'width': '40%', 'height': '50%',
                                            'margin-left': '30px', 'margin-top': '30px'}),
                            html.Img(src='assets/energy1.jpg', id='img2',
                                     style={'width': '40%', 'height': '50%',
                                            'margin-left': '100px', 'margin-top': '0px'}),
                            html.H2('', id='rate', style={'textAlign': 'center'})
                        ],
                    )
                ],
            ),
            dcc.Store(id="error", storage_type="memory"),
        ],
    ),

    return layout
