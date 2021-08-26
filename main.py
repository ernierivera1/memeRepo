import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], meta_tags = [{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])
app.layout = dbc.Container([
    dbc.Card(
    [
        dbc.CardImg(src="/assets/doomer_nazi.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Nihilistic Nazi Doomer", className="card-title"),
                html.P(
                    "Nazi LARPER with a Doomer attitude. Super negative, Nihilism is the way. Incel inside even tho has a GF. She doesn't know the real Incel doomer inside him.",
                    className="card-text",
                ),
                #dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],),
    dbc.Card(
        [
            dbc.CardImg(src="/assets/weeb_coomer.png", top=True),
            dbc.CardBody(
                [
                    html.H4("Socialist weeb coomer", className="card-title"),
                    html.P(
                        "Pure socialist, has all his money in stocks and accumulates tons of wealth. Its a weeb, a coomer. Linux elitist very proud of his hentai linux super secure server. Always complains capitalism evil while looking at how much his stocks have grown",
                        className="card-text",
                    ),
                    html.Audio(src='/assets/kiniro-mosaic-ayaya-ayaya_Hdugg5f.mp3', controls=True),
                ]
            ),

        ], ),
    dbc.Card(
        [
            dbc.CardImg(src="/assets/eff.jpg", top=True),
            dbc.CardBody(
                [
                    html.H4("Closeted Nazi Incel", className="card-title"),
                    html.P(
                        "A Nazi, racist Incel that hides all his feelings and just watches society, ocasioanlly comenting something anti women. Copes by gaming and coding all day. Has accepted deep down Jews are here to stay.",
                        className="card-text",
                    ),
                ]
            ),
        ], ),
    dbc.Card(
        [
            dbc.CardImg(src="/assets/Chad.png", top=True),
            dbc.CardBody(
                [
                    html.H4("Gov paid proffesional NEET Chad", className="card-title"),
                    html.P(
                        "Plays games all day, or cooms or just travels. Full time NEET just chilling all day being comfy",
                        className="card-text",
                    ),
                ]
            ),
        ], ),
    dbc.Card(
        [
            dbc.CardImg(src="/assets/gi.jpg", top=True),
            dbc.CardBody(
                [
                    html.H4("I want Zuckerberg to Cuck me", className="card-title"),
                    html.P(
                        "Literally a cuck, sold to facebook. His image has copy rights by FACEBOOK@glowies",
                        className="card-text",
                    ),
                ]
            ),
        ], ),
])

# @app.callback(Ouput =
#               Input('playAyayaButton', 'n_clicks'))
#
# def playAyaya(clicks)
#     html.

if __name__ == '__main__':
    app.run_server(debug=True, host='192.168.0.16', port=8050)