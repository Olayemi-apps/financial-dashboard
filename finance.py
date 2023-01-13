import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from datetime import datetime
import pandas as pd
# Plotly Graph Objects has more customization options
import plotly.graph_objects as go


font_awesome = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"

external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Roboto&display=swap', font_awesome
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                meta_tags=[{"name": "viewport", "content": "width=device-width"}])

BB_LOGO = "/assets/bberg_logo.png"
P_SPARX = "assets/favicon-32x32.png"


app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(
                src=BB_LOGO,
                style={'height': '50px'},
                className="logo",
            ),
            html.H6('Digital Financial Statement',
                    style={'color': '#3839DB',
                           'margin-top': '20px'},
                    className='nav_title'),
        ], className="nav_header"),  # Will have to add a Space here with the css to move 'current_time' - to the right
        html.H6(id='current_time',
                style={'color': '#3839DB'},
                className="time_position"),

        # Update the time in the nav dash app
        html.Div([
            dcc.Interval(id='realtime_update',
                         interval=1000,  # updates every second
                         n_intervals=0)
        ]),

        html.A(
            href="https://pandasparx.com/dashboards.html",
            target="_blank",
            children=[
                html.Img(
                    alt="pandasparX - Dashboards",
                    src=P_SPARX,
                    className="pandasparx_logo",
                )
            ]
        ),

    ], className="nav_container"),  # Holds all the elements of the top nav

    # First Row - Title

    html.Div([
        html.Div([
            html.H3('Top Performing Crypto Currencies',
                    style={'color': '#3839DB'})
        ])
    ], id='title'),

    # Second Row - Split sections::

    # Update information on the cards
    html.Div([
        dcc.Interval(id='card_update',
                     interval=5000,  # updates 5  second
                     n_intervals=0)
    ]),

    html.Div([
            # Left Column
            html.Div([
                html.Div([
                    html.H3('Top 10  Performing Crypto Currencies',
                            style={'color': '#3839DB'}),
                ], className='leftColumnTitle'),
                html.Div([
                    # Card 1
                    html.Div([
                        # Card Details
                        html.Div([
                            html.Div(id='text_1'),
                            html.Div(id='text_2')
                        ], className='cardInnerPosition')
                    ], className='dataCard'),
                    # Card 2
                    html.Div([
                        # Card Details
                        html.Div([
                            html.Div(id='text_3'),
                            html.Div(id='text_4')
                        ], className='cardInnerPosition')
                    ], className='dataCard'),
                    # Card 3
                    html.Div([
                        # Card Details
                        html.Div([
                            html.Div(id='text_5'),
                            html.Div(id='text_6')
                        ], className='cardInnerPosition')
                    ], className='dataCard'),
                    # Card 4
                    html.Div([
                        # Card Details
                        html.Div([
                            html.Div(id='text_7'),
                            html.Div(id='text_8')
                        ], className='cardInnerPosition')
                    ], className='dataCard'),

                    # Card 5
                    html.Div([
                        # Card Details
                        html.Div([
                            html.Div(id='text_9'),
                            html.Div(id='text_10')
                        ], className='cardInnerPosition')
                    ], className='dataCard'),
                    # Card 6
                    html.Div([
                        # Card Details
                        html.Div([
                            html.Div(id='text_11'),
                            html.Div(id='text_12')
                        ], className='cardInnerPosition')
                    ], className='dataCard'),
                    # Card 7
                    html.Div([
                        # Card Details
                        html.Div([
                            html.Div(id='text_13'),
                            html.Div(id='text_14')
                        ], className='cardInnerPosition')
                    ], className='dataCard'),
                    # Card 8
                    html.Div([
                        # Card Details
                        html.Div([
                            html.Div(id='text_15'),
                            html.Div(id='text_16')
                        ], className='cardInnerPosition')
                    ], className='dataCard'),
                    # Card 9
                    html.Div([
                        # Card Details
                        html.Div([
                            html.Div(id='text_17'),
                            html.Div(id='text_18')
                        ], className='cardInnerPosition')
                    ], className='dataCard'),
                    # Card 10
                    html.Div([
                        # Card Details
                        html.Div([
                            html.Div(id='text_19'),
                            html.Div(id='text_20')
                        ], className='cardInnerPosition')
                    ], className='dataCard'),

                ], className='card_container')  # AKA flexbox_container

            ], className='left_side six columns'),


            # Right Column
            html.Div([
                html.Div([
                    html.H3('Top Five Performing Crypto Currencies',
                            style={'color': '#3839DB'}),
                ], className='rightColumnTitle'),
                html.Div([
                    html.Div(id='tableRanking',
                         className='table')
                ], className='table_container'),

            ], className='right_side six columns')

    ], className='row flex-display'),

    # 2nd Row

    html.Div([
        # left column
        html.Div([
            html.Div([
                html.H3('Crypto Currency Price Scale - (Ethereum)',
                        style={'color': '#3839DB',
                               'margin-top': '100px'})
            ], className='leftColumnTitle'),

            html.Div([
                html.Div(id='ethereumCoin_update')

            ], className='subheading_graphUpdate'),

            html.Div([
                dcc.Graph(id='timescale_chart',
                          animate=True,
                          config={'displayModeBar': False, 'responsive': True},
                          className='Timescale_style')
            ], className='timeScale'),
            # Chart Title #Made Dynamic within the callback
            html.Div(id='timeScaleHeader')

        ], className='left_side six columns'),

        # right column
        html.Div([
            html.Div([
                html.H3('Crypto Currency Price Analysis - (Bitcoin)',
                        style={'color': '#3839DB',
                               'margin-top': '100px'}
                        ),
            ], className='rightColumnTitle'),

            html.Div([
                html.Div(id='bitCoin_update')

            ], className='subheading_graphUpdate'),

            html.Div([
                dcc.Graph(id='Crypto_Chart',
                          animate=True,
                          config={'displayModeBar': False, 'responsive': True},
                          className='Crypto_style')
            ], className='CryptoChart'),
            # Chart Title #Made Dynamic within the callback
            html.Div(id='cryptoChartHeader')

        ], className='right_side six columns')

    ], className='row flex-display'),

    html.Div([
        html.Footer('Digital Financial Statement',
                className='footer_info')

    ], className='footer'),

], id='mainContainer')


@app.callback(Output('current_time', 'children'),
            [Input('realtime_update', 'n_intervals')])
def time_update(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    return[
        html.Div(dt_string)
    ]

# Digital Card Callback

# Text 1 and 2


@app.callback(Output('text_1', 'children'),
              [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        bc_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\bc_data.csv', names=h_list)
        bc_rank = bc_df['Rank'][0] # 0 without the index being shown in the output
        bc_df['Price_Variation'] = bc_df['Price'].diff()
        # Tail will give the last value of the dataframe
        bc_price_variation = bc_df['Price_Variation'].tail(1).iloc[0]
        bc_price = bc_df['Price'].tail(1).iloc[0]

    if bc_price_variation > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('bc.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Bitcoin',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bc_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(bc_price),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(bc_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    if bc_price_variation < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('bc.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Bitcoin',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bc_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(bc_price),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(bc_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    elif bc_price_variation == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('bc.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Bitcoin',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bc_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(bc_price),
                            style={'color': '#333333',
                                   'font-weight': 'bold',
                                   'fontSize': '13px'},
                            className='coinPrice'),
                    html.H6('${0:,.0f}'.format(bc_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

# 2nd Row
@app.callback(Output('text_2', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        bc_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\bc_data.csv', names=h_list)
        # Tail will give the last value of the dataframe
        bc_change24h = bc_df['Change (24) %'].tail(1).iloc[0]
        bc_market = bc_df['Market Cap.'].tail(1).iloc[0]

    if bc_change24h > 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(bc_change24h),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(bc_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]
    elif bc_change24h < 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(bc_change24h),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(bc_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]

    elif bc_change24h == 0:
        return [
                html.Div([
                        html.H6('{0:,.2f}%'.format(bc_change24h),
                                style={'color': '#333333',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.P('Cap: ' + '${0:,.0f}'.format(bc_market),
                                style={'color': '#5c5c5c',
                                       'fontSize': '8px'},
                                className='cap_priceValue'),
                ], className='nonVariationCap_position'),
        ]

# Text 3  and 4
@app.callback(Output('text_3', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        et_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\et_data.csv', names=h_list)
        et_rank = et_df['Rank'][0] # 0 without the index being shown in the output
        et_df['Price_Variation'] = et_df['Price'].diff()
        # Tail will give the last value of the dataframe
        et_price_variation = et_df['Price_Variation'].tail(1).iloc[0]
        et_price = et_df['Price'].tail(1).iloc[0]

    if et_price_variation > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('et.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Ethereum',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(et_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(et_price),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(et_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    if et_price_variation < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('et.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Ethereum',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(et_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(et_price),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(et_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    elif et_price_variation == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('et.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Ethereum',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(et_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(et_price),
                            style={'color': '#333333',
                                   'font-weight': 'bold',
                                   'fontSize': '13px'},
                            className='coinPrice'),
                    html.H6('${0:,.0f}'.format(et_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

# 2nd Row
@app.callback(Output('text_4', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        et_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\et_data.csv', names=h_list)
        # Tail will give the last value of the dataframe
        et_change24h = et_df['Change (24) %'].tail(1).iloc[0]
        et_market = et_df['Market Cap.'].tail(1).iloc[0]

    if et_change24h > 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(et_change24h),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(et_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]
    elif et_change24h < 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(et_change24h),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(et_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]

    elif et_change24h == 0:
        return [
                html.Div([
                        html.H6('{0:,.2f}%'.format(et_change24h),
                                style={'color': '#333333',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.P('Cap: ' + '${0:,.0f}'.format(et_market),
                                style={'color': '#5c5c5c',
                                       'fontSize': '8px'},
                                className='cap_priceValue'),
                ], className='nonVariationCap_position'),
        ]

# Text 5  and 6
@app.callback(Output('text_5', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        tet_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\tet_data.csv', names=h_list)
        tet_rank = tet_df['Rank'][0] # 0 without the index being shown in the output
        tet_df['Price_Variation'] = tet_df['Price'].diff()
        # Tail will give the last value of the dataframe
        tet_price_variation = tet_df['Price_Variation'].tail(1).iloc[0]
        tet_price = tet_df['Price'].tail(1).iloc[0]

    if tet_price_variation > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('tet.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Tether',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(tet_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(tet_price),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(tet_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    if tet_price_variation < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('tet.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Tether',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(tet_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(tet_price),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(tet_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    elif tet_price_variation == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('tet.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Tether',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(tet_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(tet_price),
                            style={'color': '#333333',
                                   'font-weight': 'bold',
                                   'fontSize': '13px'},
                            className='coinPrice'),
                    html.H6('${0:,.0f}'.format(tet_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

# 2nd Row
@app.callback(Output('text_6', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        tet_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\tet_data.csv', names=h_list)
        # Tail will give the last value of the dataframe
        tet_change24h = tet_df['Change (24) %'].tail(1).iloc[0]
        tet_market = tet_df['Market Cap.'].tail(1).iloc[0]

    if tet_change24h > 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(tet_change24h),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(tet_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]
    elif tet_change24h < 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(tet_change24h),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(tet_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]

    elif tet_change24h == 0:
        return [
                html.Div([
                        html.H6('{0:,.2f}%'.format(tet_change24h),
                                style={'color': '#333333',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.P('Cap: ' + '${0:,.0f}'.format(tet_market),
                                style={'color': '#5c5c5c',
                                       'fontSize': '8px'},
                                className='cap_priceValue'),
                ], className='nonVariationCap_position'),
        ]

# Text 7  and 8
@app.callback(Output('text_7', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        usd_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\usd_data.csv', names=h_list)
        usd_rank = usd_df['Rank'][0] # 0 without the index being shown in the output
        usd_df['Price_Variation'] = usd_df['Price'].diff()
        # Tail will give the last value of the dataframe
        usd_price_variation = usd_df['Price_Variation'].tail(1).iloc[0]
        usd_price = usd_df['Price'].tail(1).iloc[0]

    if usd_price_variation > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('usd.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('USD Coin',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(usd_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(usd_price),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(usd_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    if usd_price_variation < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('usd.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('USD Coin',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(usd_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(usd_price),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(usd_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    elif usd_price_variation == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('usd.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('USD Coin',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(usd_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(usd_price),
                            style={'color': '#333333',
                                   'font-weight': 'bold',
                                   'fontSize': '13px'},
                            className='coinPrice'),
                    html.H6('${0:,.0f}'.format(usd_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

# 2nd Row
@app.callback(Output('text_8', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        usd_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\usd_data.csv', names=h_list)
        # Tail will give the last value of the dataframe
        usd_change24h = usd_df['Change (24) %'].tail(1).iloc[0]
        usd_market = usd_df['Market Cap.'].tail(1).iloc[0]

    if usd_change24h > 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(usd_change24h),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(usd_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]
    elif usd_change24h < 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(usd_change24h),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(usd_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]

    elif usd_change24h == 0:
        return [
                html.Div([
                        html.H6('{0:,.2f}%'.format(usd_change24h),
                                style={'color': '#333333',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.P('Cap: ' + '${0:,.0f}'.format(usd_market),
                                style={'color': '#5c5c5c',
                                       'fontSize': '8px'},
                                className='cap_priceValue'),
                ], className='nonVariationCap_position'),
        ]

# Text 9  and 10
@app.callback(Output('text_9', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        bnb_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\bnb_data.csv', names=h_list)
        bnb_rank = bnb_df['Rank'][0] # 0 without the index being shown in the output
        bnb_df['Price_Variation'] = bnb_df['Price'].diff()
        # Tail will give the last value of the dataframe
        bnb_price_variation = bnb_df['Price_Variation'].tail(1).iloc[0]
        bnb_price = bnb_df['Price'].tail(1).iloc[0]

    if bnb_price_variation > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('bnb.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('BNB',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bnb_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(bnb_price),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(bnb_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    if bnb_price_variation < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('bnb.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('BNB',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bnb_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(bnb_price),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(bnb_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    elif bnb_price_variation == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('bnb.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('BNB',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bnb_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(bnb_price),
                            style={'color': '#333333',
                                   'font-weight': 'bold',
                                   'fontSize': '13px'},
                            className='coinPrice'),
                    html.H6('${0:,.0f}'.format(bnb_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

# 2nd Row


@app.callback(Output('text_10', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        bnb_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\bnb_data.csv', names=h_list)
        # Tail will give the last value of the dataframe
        bnb_change24h = bnb_df['Change (24) %'].tail(1).iloc[0]
        bnb_market = bnb_df['Market Cap.'].tail(1).iloc[0]

    if bnb_change24h > 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(bnb_change24h),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(bnb_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]
    elif bnb_change24h < 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(bnb_change24h),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(bnb_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]

    elif bnb_change24h == 0:
        return [
                html.Div([
                        html.H6('{0:,.2f}%'.format(bnb_change24h),
                                style={'color': '#333333',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.P('Cap: ' + '${0:,.0f}'.format(bnb_market),
                                style={'color': '#5c5c5c',
                                       'fontSize': '8px'},
                                className='cap_priceValue'),
                ], className='nonVariationCap_position'),
        ]

# Text 11  and 12


@app.callback(Output('text_11', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        bin_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\bin_data.csv', names=h_list)
        bin_rank = bin_df['Rank'][0] # 0 without the index being shown in the output
        bin_df['Price_Variation'] = bin_df['Price'].diff()
        # Tail will give the last value of the dataframe
        bin_price_variation = bin_df['Price_Variation'].tail(1).iloc[0]
        bin_price = bin_df['Price'].tail(1).iloc[0]

    if bin_price_variation > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('bin.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Binance USD',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bin_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(bin_price),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(bin_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    if bin_price_variation < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('bin.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Bitcoin',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bin_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(bin_price),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(bin_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    elif bin_price_variation == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('bin.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Binance USD',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bin_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(bin_price),
                            style={'color': '#333333',
                                   'font-weight': 'bold',
                                   'fontSize': '13px'},
                            className='coinPrice'),
                    html.H6('${0:,.0f}'.format(bin_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

# 2nd Row


@app.callback(Output('text_12', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        bin_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\bin_data.csv', names=h_list)
        # Tail will give the last value of the dataframe
        bin_change24h = bin_df['Change (24) %'].tail(1).iloc[0]
        bin_market = bin_df['Market Cap.'].tail(1).iloc[0]

    if bin_change24h > 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(bin_change24h),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(bin_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]
    elif bin_change24h < 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(bin_change24h),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(bin_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]

    elif bin_change24h == 0:
        return [
                html.Div([
                        html.H6('{0:,.2f}%'.format(bin_change24h),
                                style={'color': '#333333',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.P('Cap: ' + '${0:,.0f}'.format(bin_market),
                                style={'color': '#5c5c5c',
                                       'fontSize': '8px'},
                                className='cap_priceValue'),
                ], className='nonVariationCap_position'),
        ]

# Text 13  and 14


@app.callback(Output('text_13', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        xrp_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\xrp_data.csv', names=h_list)
        xrp_rank = xrp_df['Rank'][0] # 0 without the index being shown in the output
        xrp_df['Price_Variation'] = xrp_df['Price'].diff()
        # Tail will give the last value of the dataframe
        xrp_price_variation = xrp_df['Price_Variation'].tail(1).iloc[0]
        xrp_price = xrp_df['Price'].tail(1).iloc[0]

    if xrp_price_variation > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('xrp.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('XRP',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(xrp_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(xrp_price),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(xrp_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    if xrp_price_variation < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('xrp.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('XRP',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(xrp_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(xrp_price),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(xrp_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    elif xrp_price_variation == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('xrp.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('XRP',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(xrp_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(xrp_price),
                            style={'color': '#333333',
                                   'font-weight': 'bold',
                                   'fontSize': '13px'},
                            className='coinPrice'),
                    html.H6('${0:,.0f}'.format(xrp_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

# 2nd Row


@app.callback(Output('text_14', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        xrp_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\xrp_data.csv', names=h_list)
        # Tail will give the last value of the dataframe
        xrp_change24h = xrp_df['Change (24) %'].tail(1).iloc[0]
        xrp_market = xrp_df['Market Cap.'].tail(1).iloc[0]

    if xrp_change24h > 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(xrp_change24h),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(xrp_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]
    elif xrp_change24h < 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(xrp_change24h),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(xrp_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]

    elif xrp_change24h == 0:
        return [
                html.Div([
                        html.H6('{0:,.2f}%'.format(xrp_change24h),
                                style={'color': '#333333',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.P('Cap: ' + '${0:,.0f}'.format(xrp_market),
                                style={'color': '#5c5c5c',
                                       'fontSize': '8px'},
                                className='cap_priceValue'),
                ], className='nonVariationCap_position'),
        ]

# Text 15  and 16


@app.callback(Output('text_15', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        dog_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\dog_data.csv', names=h_list)
        dog_rank = dog_df['Rank'][0] # 0 without the index being shown in the output
        dog_df['Price_Variation'] = dog_df['Price'].diff()
        # Tail will give the last value of the dataframe
        dog_price_variation = dog_df['Price_Variation'].tail(1).iloc[0]
        dog_price = dog_df['Price'].tail(1).iloc[0]

    if dog_price_variation > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('dog.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('DogeCoin',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(dog_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(dog_price),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(dog_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    if dog_price_variation < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('dog.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('DogeCoin',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(dog_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(dog_price),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(dog_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    elif dog_price_variation == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('dog.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('DogeCoin',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(dog_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(dog_price),
                            style={'color': '#333333',
                                   'font-weight': 'bold',
                                   'fontSize': '13px'},
                            className='coinPrice'),
                    html.H6('${0:,.0f}'.format(dog_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

# 2nd Row


@app.callback(Output('text_16', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        dog_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\dog_data.csv', names=h_list)
        # Tail will give the last value of the dataframe
        dog_change24h = dog_df['Change (24) %'].tail(1).iloc[0]
        dog_market = dog_df['Market Cap.'].tail(1).iloc[0]

    if dog_change24h > 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(dog_change24h),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(dog_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]
    elif dog_change24h < 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(dog_change24h),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(dog_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]

    elif dog_change24h == 0:
        return [
                html.Div([
                        html.H6('{0:,.2f}%'.format(dog_change24h),
                                style={'color': '#333333',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.P('Cap: ' + '${0:,.0f}'.format(dog_market),
                                style={'color': '#5c5c5c',
                                       'fontSize': '8px'},
                                className='cap_priceValue'),
                ], className='nonVariationCap_position'),
        ]

# Text 17  and 18


@app.callback(Output('text_17', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        car_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\car_data.csv', names=h_list)
        car_rank = car_df['Rank'][0] # 0 without the index being shown in the output
        car_df['Price_Variation'] = car_df['Price'].diff()
        # Tail will give the last value of the dataframe
        car_price_variation = car_df['Price_Variation'].tail(1).iloc[0]
        car_price = car_df['Price'].tail(1).iloc[0]

    if car_price_variation > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('car.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Cardano',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(car_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(car_price),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(car_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    if car_price_variation < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('car.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Cardano',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(car_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(car_price),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(car_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    elif car_price_variation == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('car.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Cardano',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(car_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(car_price),
                            style={'color': '#333333',
                                   'font-weight': 'bold',
                                   'fontSize': '13px'},
                            className='coinPrice'),
                    html.H6('${0:,.0f}'.format(car_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

# 2nd Row


@app.callback(Output('text_18', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        car_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\car_data.csv', names=h_list)
        # Tail will give the last value of the dataframe
        car_change24h = car_df['Change (24) %'].tail(1).iloc[0]
        car_market = car_df['Market Cap.'].tail(1).iloc[0]

    if car_change24h > 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(car_change24h),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(car_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]
    elif car_change24h < 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(car_change24h),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(car_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]

    elif car_change24h == 0:
        return [
                html.Div([
                        html.H6('{0:,.2f}%'.format(car_change24h),
                                style={'color': '#333333',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.P('Cap: ' + '${0:,.0f}'.format(car_market),
                                style={'color': '#5c5c5c',
                                       'fontSize': '8px'},
                                className='cap_priceValue'),
                ], className='nonVariationCap_position'),
        ]

# Text 19  and 20


@app.callback(Output('text_19', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        poly_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\poly_data.csv', names=h_list)
        poly_rank = poly_df['Rank'][0] # 0 without the index being shown in the output
        poly_df['Price_Variation'] = poly_df['Price'].diff()
        # Tail will give the last value of the dataframe
        poly_price_variation = poly_df['Price_Variation'].tail(1).iloc[0]
        poly_price = poly_df['Price'].tail(1).iloc[0]

    if poly_price_variation > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('poly.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Polygon',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(poly_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(poly_price),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(poly_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    if poly_price_variation < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('poly.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Polygon',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(poly_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(poly_price),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '13px'},
                                className='coinPrice'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '80%'}),
                        ], className='arrowPosition'),
                    ], className='priceCoin_position'),
                    html.H6('${0:,.0f}'.format(poly_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

    elif poly_price_variation == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('poly.png'),
                                 style={'height': '30px'},
                                 className='digital_coin'),
                        html.P('Polygon',
                               style={'color': '#333333',
                                      'fontSize': '13px'},
                               className='d_coinName')
                    ], className='d_coinImage'),
                    html.P('Rank: ' + '{0:,.0f}'.format(poly_rank),  # 0f  represents an int number
                           style={'color': '#333333',
                                  'font-weight': 'bold',
                                  'fontSize': '13px'},
                           className='rankPosition'),
                ], className='coinRank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(poly_price),
                            style={'color': '#333333',
                                   'font-weight': 'bold',
                                   'fontSize': '13px'},
                            className='coinPrice'),
                    html.H6('${0:,.0f}'.format(poly_price),
                            style={'color': '#5c5c5c',
                                   'fontSize': '9px'},
                            className='priceValue'),
                ], className='priceValue_position'),
            ], className='coinPriceColumn'),
        ]

# 2nd Row


@app.callback(Output('text_20', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        poly_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\poly_data.csv', names=h_list)
        # Tail will give the last value of the dataframe
        poly_change24h = poly_df['Change (24) %'].tail(1).iloc[0]
        poly_market = poly_df['Market Cap.'].tail(1).iloc[0]

    if poly_change24h > 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(poly_change24h),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-up',
                                   style={'color': '#00cc00',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(poly_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]
    elif poly_change24h < 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(poly_change24h),
                                style={'color': '#FC0303',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.Div([
                            html.I(className='fa-solid fa-caret-down',
                                   style={'color': '#FC0303',
                                          'fontSize': '60%'}),
                        ], className='arrowPosition_Variation'),
                    ], className='variation_position'),
                    html.P('Cap: ' + '${0:,.0f}'.format(poly_market),
                            style={'color': '#5c5c5c',
                                   'fontSize': '8px'},
                            className='cap_priceValue'),
                ], className='variationCap_position'),
        ]

    elif poly_change24h == 0:
        return [
                html.Div([
                        html.H6('{0:,.2f}%'.format(poly_change24h),
                                style={'color': '#333333',
                                       'font-weight': 'bold',
                                       'fontSize': '10px'},
                                className='coinPrice_Variation'),
                        html.P('Cap: ' + '${0:,.0f}'.format(poly_market),
                                style={'color': '#5c5c5c',
                                       'fontSize': '8px'},
                                className='cap_priceValue'),
                ], className='nonVariationCap_position'),
        ]

# HTML TABLE

@app.callback(Output('tableRanking', 'children'),
            [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        bc_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\bc_data.csv', names=h_list)
        bc_price = bc_df['Price'].tail(1).iloc[0]
        bc_change24h = bc_df['Change (24) %'].tail(1).iloc[0]
        bc_market = bc_df['Market Cap.'].tail(1).iloc[0]

        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        et_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\et_data.csv',
                            names=h_list)
        et_price = et_df['Price'].tail(1).iloc[0]
        et_change24h = et_df['Change (24) %'].tail(1).iloc[0]
        et_market = et_df['Market Cap.'].tail(1).iloc[0]

        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        tet_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\tet_data.csv',
                             names=h_list)
        tet_price = tet_df['Price'].tail(1).iloc[0]
        tet_change24h = tet_df['Change (24) %'].tail(1).iloc[0]
        tet_market = tet_df['Market Cap.'].tail(1).iloc[0]

        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        usd_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\usd_data.csv',
                             names=h_list)
        usd_price = usd_df['Price'].tail(1).iloc[0]
        usd_change24h = usd_df['Change (24) %'].tail(1).iloc[0]
        usd_market = usd_df['Market Cap.'].tail(1).iloc[0]

        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        bnb_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\bnb_data.csv',
                             names=h_list)
        bnb_price = bnb_df['Price'].tail(1).iloc[0]
        bnb_change24h = bnb_df['Change (24) %'].tail(1).iloc[0]
        bnb_market = bnb_df['Market Cap.'].tail(1).iloc[0]

    return [
        html.Table([
            html.Thead([
                html.Tr([
                    html.Th(html.Img(src=app.get_asset_url('rankV2.png'), style={'width': '25px', 'textAlign': 'center'})),
                    html.Th('Currency Name', style={'width': '200px', 'textAlign': 'left'}),
                    html.Th('Price', style={'width': '150px', 'textAlign': 'left'}),
                    html.Th('Change 24', style={'width': '150px', 'textAlign': 'left'}),
                    html.Th('Market Capacity', style={'width': '150px', 'textAlign': 'left'}),
                ], className='tableHeader')
            ]),
            html.Tbody([
                html.Tr([
                    html.Td(html.P('1', style={'textAlign': 'center',
                                               'color': '#333333',
                                               'fontSize': 12,
                                               'margin-top': '10px'})),
                    html.Td([
                        html.Div([
                            html.Img(src=app.get_asset_url('bc.png'),
                                     style={'height': '30px'},
                                     className='coinImage'),
                            html.P('Bitcoin', className='coinTextV2')
                        ], className='coinLogoImage')
                    ]),
                    html.Td(html.H6('${0:,.2f}'.format(bc_price),
                                style={'color': '#333333',
                                       'fontSize': '13px'},)),
                    html.Td(html.H6('{0:,.2f}%'.format(bc_change24h),
                                style={'color': '#333333',
                                       'fontSize': '13px'}, )),
                    html.Td(html.H6('${0:,.2f}'.format(bc_market),
                                    style={'color': '#333333',
                                           'fontSize': '13px'}, )),

                ], className='tableRow'),
                html.Tr([
                    html.Td(html.P('2', style={'textAlign': 'center',
                                               'color': '#fff',
                                               'fontSize': 12,
                                               'margin-top': '10px'})),
                    html.Td([
                        html.Div([
                            html.Img(src=app.get_asset_url('et.png'),
                                     style={'height': '30px'},
                                     className='coinImage'),
                            html.P('Ethereum', className='coinText')
                        ], className='coinLogoImage')
                    ]),
                    html.Td(html.H6('${0:,.2f}'.format(et_price),
                                    style={'color': '#FFF',
                                           'fontSize': '13px'}, )),
                    html.Td(html.H6('{0:,.2f}%'.format(et_change24h),
                                    style={'color': '#FFF',
                                           'fontSize': '13px'}, )),
                    html.Td(html.H6('${0:,.2f}'.format(et_market),
                                    style={'color': '#FFF',
                                           'fontSize': '13px'}, )),

                ], className='tableRow'),
                html.Tr([
                    html.Td(html.P('3', style={'textAlign': 'center',
                                               'color': '#333333',
                                               'fontSize': 12,
                                               'margin-top': '10px'})),
                    html.Td([
                        html.Div([
                            html.Img(src=app.get_asset_url('tet.png'),
                                     style={'height': '30px'},
                                     className='coinImage'),
                            html.P('Tether', className='coinTextV2')
                        ], className='coinLogoImage')
                    ]),
                    html.Td(html.H6('${0:,.2f}'.format(tet_price),
                                    style={'color': '#333333',
                                           'fontSize': '13px'}, )),
                    html.Td(html.H6('{0:,.2f}%'.format(tet_change24h),
                                    style={'color': '#333333',
                                           'fontSize': '13px'}, )),
                    html.Td(html.H6('${0:,.2f}'.format(tet_market),
                                    style={'color': '#333333',
                                           'fontSize': '13px'}, )),

                ], className='tableRow'),
                html.Tr([
                    html.Td(html.P('4', style={'textAlign': 'center',
                                               'color': '#fff',
                                               'fontSize': 12,
                                               'margin-top': '10px'})),
                    html.Td([
                        html.Div([
                            html.Img(src=app.get_asset_url('usd.png'),
                                     style={'height': '30px'},
                                     className='coinImage'),
                            html.P('USD Coin', className='coinText')
                        ], className='coinLogoImage')
                    ]),
                    html.Td(html.H6('${0:,.2f}'.format(usd_price),
                                    style={'color': '#FFF',
                                           'fontSize': '13px'}, )),
                    html.Td(html.H6('{0:,.2f}%'.format(usd_change24h),
                                    style={'color': '#FFF',
                                           'fontSize': '13px'}, )),
                    html.Td(html.H6('${0:,.2f}'.format(usd_market),
                                    style={'color': '#FFF',
                                           'fontSize': '13px'}, )),

                ], className='tableRow'),
                html.Tr([
                    html.Td(html.P('5', style={'textAlign': 'center',
                                               'color': '#333333',
                                               'fontSize': 12,
                                               'margin-top': '10px'})),
                    html.Td([
                        html.Div([
                            html.Img(src=app.get_asset_url('bnb.png'),
                                     style={'height': '30px'},
                                     className='coinImage'),
                            html.P('BNB', className='coinTextV2')
                        ], className='coinLogoImage')
                    ]),
                    html.Td(html.H6('${0:,.2f}'.format(bnb_price),
                                    style={'color': '#333333',
                                           'fontSize': '13px'}, )),
                    html.Td(html.H6('{0:,.2f}%'.format(bnb_change24h),
                                    style={'color': '#333333',
                                           'fontSize': '13px'}, )),
                    html.Td(html.H6('${0:,.2f}'.format(bnb_market),
                                    style={'color': '#333333',
                                           'fontSize': '13px'}, )),

                ], className='tableRow'),
            ])
        ], className='t_style')
    ]


# Animated Timescale - Ethereum  Header

@app.callback(Output('ethereumCoin_update', 'children'),
              [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate

    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        et_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\et_data.csv', names=h_list)
        et_time = et_df['Time'].tail(1).iloc[0]
        et_price = et_df['Price'].tail(1).iloc[0]

    return [
        html.Div([
            html.P('Latest Ethereum Price - ',
                   style={'color': '#333333',
                          'fontSize': '13px',
                          'fontWeight': 'bold'},
                   className='update_subText'),

            html.P('${0:,.2f}'.format(et_price),
                    style={'color': '#00cc00',
                           'font-weight': 'bold',
                           'fontSize': '13px'},
                    className='etPrice'),

            html.P('(' + et_time + ')',
                   style={'color': '#333333',
                          'font-weight': 'bold',
                          'fontSize': '13px'},
                   className='etTime'),

        ], className='SubBcPricePosition'),
    ]




# Animated Timescale Analysis Chart
@app.callback(Output('timescale_chart', 'figure'),
              [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        et_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\et_data.csv', names=h_list)
        time_interval = et_df['Time'].tail(30)
        et_price = et_df['Price'].tail(30)  # Displays last 30 values, are the most recent values

    return {
        # Data is also known as the  the figure section
        'data': [go.Scatter(
            x=time_interval,
            y=et_price,
            fill='tonexty',
            fillcolor='rgba(56, 57, 219, 0.1)',
            marker=dict(color='#3839DB'),
            mode='markers',
            hoverinfo='text',
            hovertext=
            '<b>Time</b>: ' + time_interval.astype(str) + '<br>' +
            '<b>Ethereum Price</b>: ' + [f'${x:,.2f}' for x in et_price] + '<br>'
        )],

        'layout': go.Layout(
            margin=dict(t=25, r=10, l=70),
            hovermode='x unified',
            plot_bgcolor='rgba(217, 221, 222, 0)',
            paper_bgcolor='rgba(217, 221, 222, 0)',
            xaxis=dict(
                range=[min(time_interval), max(time_interval)],
                title='<b>Time</b>',
                color='#333333',
                showspikes=True,
                showline=True,
                showgrid=False,
                linecolor='#3839DB',
                linewidth=1,
                ticks='outside',
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='#3839DB'
                )),
            yaxis=dict(
                range=[min(et_price) -3, max(et_price) + 5],
                color='#333333',
                showspikes=True,
                showline=True,
                showgrid=False,
                linecolor='#3839DB',
                linewidth=1,
                ticks='outside',
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='#3839DB'
                )),
            font=dict(
                family='Arial',
                size=12,
                color='#3839DB')
        ),
    }


# Crypto Chart Callback - Time and Price NEEDED


# Animated Crypto Price Analysis Bitcoin Header:

@app.callback(Output('bitCoin_update', 'children'),
              [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate

    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        bc_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\bc_data.csv', names=h_list)
        bc_time = bc_df['Time'].tail(1).iloc[0]
        bc_price = bc_df['Price'].tail(1).iloc[0]

    return [
        html.Div([
            html.P('Latest Bitcoin Price - ',
                   style={'color': '#333333',
                          'fontSize': '13px',
                          'fontWeight': 'bold'},
                   className='update_subText'),

            html.P('${0:,.2f}'.format(bc_price),
                    style={'color': '#00cc00',
                           'font-weight': 'bold',
                           'fontSize': '13px'},
                    className='bcPrice'),

            html.P('(' + bc_time + ')',
                   style={'color': '#333333',
                          'font-weight': 'bold',
                          'fontSize': '13px'},
                   className='bcTime'),

        ], className='SubBcPricePosition'),
    ]



# Animated Price Analysis Chart
@app.callback(Output('Crypto_Chart', 'figure'),
              [Input('card_update', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        # This objects adds headers to the columns
        h_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24) %', 'Market Cap.']
        bc_df = pd.read_csv(r'C:\Users\Admin\Desktop\Plotly_Dashboards\Dashboard_Finance\data\bc_data.csv', names=h_list)
        time_interval = bc_df['Time'].tail(30)
        bc_price = bc_df['Price'].tail(30)  # Displays last 30 values, are the most recent values

    return {
        # Data is also known as the  the figure section
        'data': [
            go.Scatter(
                x=time_interval,
                y=bc_price,
                fill='tonexty', # Initiates the filled area
                fillcolor='rgba(56, 57, 219, 0.1)',
                line=dict(width=3, color='#3839DB'),
                mode='lines',
                hoverinfo='text',
                hovertext=
                '<b>Time</b>: ' + time_interval.astype(str) + '<br>' +
                '<b>Bitcoin Price</b>: ' + [f'${x:,.2f}' for x in bc_price] + '<br>'
            ),

        ],

        'layout': go.Layout(
            margin=dict(t=25, r=10, l=70),
            hovermode='x unified',
            plot_bgcolor='rgba(217, 221, 222, 0)',
            paper_bgcolor='rgba(217, 221, 222, 0)',
            xaxis=dict(
                       range=[min(time_interval), max(time_interval)],
                       title='<b>Time</b>',
                       color='#333333',
                       showspikes=True,
                       showline=True,
                       showgrid=False,
                       linecolor='#3839DB',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           size=12,
                           color='#3839DB'
                       )),
            yaxis=dict(
                        range=[min(bc_price) -3, max(bc_price) + 5], # Important as it helps to build the shaded area
                        color='#333333',
                        showspikes=True,
                        showline=True,
                        showgrid=False,
                        linecolor='#3839DB',
                        linewidth=1,
                        ticks='outside',
                        tickfont=dict(
                            family='Arial',
                            size=12,
                            color='#3839DB'
                        )),
            font=dict(
                family='Arial',
                size=12,
                color='#3839DB'
            )
        )


    }




if __name__ == "__main__":
    app.run(debug=False)
