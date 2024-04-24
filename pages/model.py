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
    path='/predict.py'
)


with open('D:\CSE_student_performances\pages\model.pkl', 'rb') as file:
    lr_model = pickle.load(file)

group_colors = {"control": "light blue", "reference": "red"}

# App Layout
def layout():
    layout = dbc.Container(
    children=[
        dbc.Row(
            dbc.Col(),
            dbc.Col(),

        ),

    ]
    )
    return layout



# Callback to generate error message
# Also sets the data to be used
# If there is an error use default data else use uploaded data
@callback(
    Output(component_id='img1', component_property='src'),
    Output(component_id='img2', component_property='src'),
    Output(component_id='rate', component_property='children'),
    State(component_id='gender', component_property='value'),
    State(component_id='wfh', component_property='value'),
    State(component_id='level', component_property='value'),
    State(component_id='hours', component_property='value'),
    State(component_id='score', component_property='value'),
    Input(component_id='submit', component_property='n_clicks')
)
def predict(gender, wft, level, hours, score, clicks):

    if not clicks:
        return dash.no_update, dash.no_update, dash.no_update

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

    if rate > 0.5:
        src1 = 'assets/burn.jpeg'
        src2 = 'assets/energy1.jpg'
    else:
        src1 = 'assets/burn1.jpg'
        src2 = 'assets/energy.jpeg'

    return src1, src2, rate


