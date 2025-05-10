import dash_bootstrap_components as dbc
from dash import html, dcc

def get_encrypt_view():
    """
    Vista de cifrado con campo de entrada.
    """
    return dbc.Container([
        html.H2("Cifrado de número", className="my-4"),

        dbc.Input(id="input-number", type="text", placeholder="Ingrese número de 6 dígitos"),
        dbc.Button("Cifrar", id="encrypt-btn", color="primary", className="mt-2"),
        html.Div(id="encrypted-output", className="mt-3"),

        dbc.Button("Volver al inicio", href="/", className="mt-4", color="link")
    ])
