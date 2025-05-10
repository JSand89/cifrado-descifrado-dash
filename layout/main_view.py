import dash_bootstrap_components as dbc
from dash import html

def get_main_view():
    """
    Vista principal con información del autor y navegación.
    """
    return dbc.Container([
        html.H1("Aplicación de Cifrado de Números", className="text-center my-4"),
        html.P("Autor: Javier Sánchez", className="text-center"),

        dbc.Row([
            dbc.Col(dbc.Button("Ir a Cifrado", href="/encrypt", color="primary", className="w-100"), md=6),
            dbc.Col(dbc.Button("Ir a Descifrado", href="/decrypt", color="secondary", className="w-100"), md=6)
        ], className="mt-4")
    ])
