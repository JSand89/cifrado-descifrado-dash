import dash_bootstrap_components as dbc
from dash import html, dcc

def get_decrypt_view():
    """
    Vista de descifrado con campo de entrada.
    """
    return dbc.Container([
        html.H2("Descifrado de número", className="my-4"),

        dbc.Input(id="input-encrypted", type="text", placeholder="Ingrese número cifrado"),
        dbc.Button("Descifrar", id="decrypt-btn", color="secondary", className="mt-2"),
        html.Div(id="decrypted-output", className="mt-3"),

        dbc.Button("Volver al inicio", href="/", className="mt-4", color="link")
    ])
