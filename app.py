# app.py

import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from layout.main_view import get_main_view
from layout.encrypt_view import get_encrypt_view
from layout.decrypt_view import get_decrypt_view
from callbacks import register_callbacks

# Cargar tema Bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.layout = dbc.Container([
    dcc.Location(id='url'),
    html.Div(id='page-content')
], fluid=True)

register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)
