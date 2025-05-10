# callbacks.py

from dash import Input, Output, State
from layout.main_view import get_main_view
from layout.encrypt_view import get_encrypt_view
from layout.decrypt_view import get_decrypt_view
from crypto_utils import encrypt_number, decrypt_number

def register_callbacks(app):
    """
    Registra los callbacks para navegación y lógica de cifrado/descifrado.
    """

    @app.callback(
        Output("page-content", "children"),
        Input("url", "pathname")
    )
    def display_page(pathname):
        if pathname == "/encrypt":
            return get_encrypt_view()
        elif pathname == "/decrypt":
            return get_decrypt_view()
        return get_main_view()

    @app.callback(
        Output("encrypted-output", "children"),
        Input("encrypt-btn", "n_clicks"),
        State("input-number", "value")
    )
    def handle_encryption(n_clicks, value):
        if n_clicks and value and value.isdigit() and len(value) == 6:
            return f"Número cifrado: {encrypt_number(int(value))}"
        elif n_clicks:
            return "Por favor ingrese un número entero de 6 dígitos."
        return ""

    @app.callback(
        Output("decrypted-output", "children"),
        Input("decrypt-btn", "n_clicks"),
        State("input-encrypted", "value")
    )
    def handle_decryption(n_clicks, value):
        if n_clicks and value and value.isdigit() and len(value) == 6:
            return f"Número original: {decrypt_number(value)}"
        elif n_clicks:
            return "Por favor ingrese un número cifrado válido de 6 dígitos."
        return ""
