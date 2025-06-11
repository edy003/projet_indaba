import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
# import dash_daq as daq # For the toggle switch

# Initialize the Dash app
app = dash.Dash(__name__,
                external_scripts=[
                    "https://cdn.tailwindcss.com/3.4.16",
                    "https://cdnjs.cloudflare.com/ajax/libs/echarts/5.5.0/echarts.min.js" # Although ECharts would need custom integration for full Dash interactivity, we include it here for completeness
                ],
                external_stylesheets=[
                    "https://fonts.googleapis.com",
                    "https://fonts.gstatic.com",
                    "https://cdnjs.cloudflare.com/ajax/libs/remixicon/4.6.0/remixicon.min.css"
                ])

# Inline Tailwind CSS configuration and custom styles
# app.index_string = '''
# <!DOCTYPE html>
# <html lang="fr">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Tableau de Bord</title>
#     <script>
#         tailwind.config={
#             theme:{
#                 extend:{
#                     colors:{
#                         primary:'#4f46e5',
#                         secondary:'#8b5cf6'
#                     },
#                     borderRadius:{
#                         'none':'0px',
#                         'sm':'4px',
#                         DEFAULT:'8px',
#                         'md':'12px',
#                         'lg':'16px',
#                         'xl':'20px',
#                         '2xl':'24px',
#                         '3xl':'32px',
#                         'full':'9999px',
#                         'button':'8px'
#                     }
#                 }
#             }
#         }
#     </script>
#     {%css%}
#     <style>
#         :where([class^="ri-"])::before { content: ""; } /* Override default content to prevent issues with Dash rendering */

#         .sidebar-toggle:checked ~ .sidebar {
#             transform: translateX(0);
#         }
#         .sidebar-toggle:not(:checked) ~ .sidebar {
#             transform: translateX(-100%);
#         }
#         @media (min-width: 1024px) {
#             .sidebar-toggle:not(:checked) ~ .sidebar {
#                 transform: translateX(0);
#             }
#             .sidebar-toggle:not(:checked) ~ .content {
#                 margin-left: 16rem;
#             }
#         }
#         input[type="range"] {
#             -webkit-appearance: none;
#             width: 100%;
#             height: 6px;
#             background: #e5e7eb;
#             border-radius: 5px;
#             outline: none;
#         }
#         input[type="range"]::-webkit-slider-thumb {
#             -webkit-appearance: none;
#             width: 18px;
#             height: 18px;
#             background: #4f46e5;
#             border-radius: 50%;
#             cursor: pointer;
#         }
#         .custom-checkbox {
#             position: relative;
#             display: inline-block;
#             width: 20px;
#             height: 20px;
#             background-color: #fff;
#             border: 2px solid #d1d5db;
#             border-radius: 4px;
#             cursor: pointer;
#         }
#         .custom-checkbox.checked {
#             background-color: #4f46e5;
#             border-color: #4f46e5;
#         }
#         .custom-checkbox.checked::after {
#             content: "";
#             position: absolute;
#             top: 2px;
#             left: 6px;
#             width: 6px;
#             height: 10px;
#             border: solid white;
#             border-width: 0 2px 2px 0;
#             transform: rotate(45deg);
#         }
#         .switch {
#             position: relative;
#             display: inline-block;
#             width: 44px;
#             height: 24px;
#         }
#         .switch-input {
#             opacity: 0;
#             width: 0;
#             height: 0;
#         }
#         .switch-slider {
#             position: absolute;
#             cursor: pointer;
#             top: 0;
#             left: 0;
#             right: 0;
#             bottom: 0;
#             background-color: #e5e7eb;
#             transition: .4s;
#             border-radius: 34px;
#         }
#         .switch-slider:before {
#             position: absolute;
#             content: "";
#             height: 18px;
#             width: 18px;
#             left: 3px;
#             bottom: 3px;
#             background-color: white;
#             transition: .4s;
#             border-radius: 50%;
#         }
#         .switch-input:checked + .switch-slider {
#             background-color: #4f46e5;
#         }
#         .switch-input:checked + .switch-slider:before {
#             transform: translateX(20px);
#         }
#     </style>
#     {%metas%}
#     {%favicon%}
# </head>
# <body class="bg-gray-50 min-h-screen">
#     <input type="checkbox" id="sidebar-toggle" class="sidebar-toggle hidden">
#     {%app_entry%}
#     <footer>
#         {%config%}
#         {%scripts%}
#         {%renderer%}
#     </footer>
# </body>
# </html>
# '''

app.layout = html.Div(className="bg-gray-50 min-h-screen", children=[
    html.Header(className="bg-white shadow-sm fixed top-0 left-0 right-0 z-10", children=[
        html.Div(className="flex items-center justify-between px-4 py-3", children=[
            html.Div(className="flex items-center", children=[
                html.Label(html.Div(className="w-6 h-6 flex items-center justify-center text-gray-600", children=html.I(className="ri-menu-line ri-lg")),
                           htmlFor="sidebar-toggle", className="lg:hidden cursor-pointer mr-3"),
                html.Div("logo", className="font-['Pacifico'] text-2xl text-primary")
            ]),
            html.Nav(className="hidden md:flex items-center space-x-6", children=[
                html.A("Tableau de bord", href="#", className="text-primary font-medium"),
                html.A("Rapports", href="#", className="text-gray-600 hover:text-primary"),
                html.A("Projets", href="#", className="text-gray-600 hover:text-primary"),
                html.A("Équipe", href="#", className="text-gray-600 hover:text-primary")
            ]),
            html.Div(className="flex items-center space-x-4", children=[
                html.Button(className="w-8 h-8 flex items-center justify-center text-gray-600 hover:bg-gray-100 rounded-full relative", children=[
                    html.I(className="ri-notification-3-line ri-lg"),
                    html.Span(className="absolute top-0 right-0 w-2 h-2 bg-red-500 rounded-full")
                ]),
                html.Div(className="flex items-center", children=[
                    html.Div(className="w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center", children=html.Span("JP", className="text-sm font-medium")),
                    html.Div(className="ml-2 hidden md:block", children=[
                        html.P("Jean Petit", className="text-sm font-medium text-gray-700"),
                        html.P("Administrateur", className="text-xs text-gray-500")
                    ])
                ])
            ])
        ])
    ]),
    html.Aside(className="sidebar fixed left-0 top-0 bottom-0 w-64 bg-white shadow-md pt-16 transition-transform duration-300 ease-in-out z-0 transform -translate-x-full lg:translate-x-0", children=[
        html.Div(className="p-4", children=[
            html.Div(className="mb-6", children=[
                html.H3("Filtres", className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3"),
                html.Div(className="mb-4", children=[
                    html.Label("Période", className="block text-sm font-medium text-gray-700 mb-1"),
                    html.Div(className="relative", children=[
                        dcc.Dropdown(
                            id='period-dropdown',
                            options=[
                                {'label': 'Aujourd\'hui', 'value': 'today'},
                                {'label': 'Cette semaine', 'value': 'this_week'},
                                {'label': 'Ce mois', 'value': 'this_month'},
                                {'label': 'Ce trimestre', 'value': 'this_quarter'},
                                {'label': 'Cette année', 'value': 'this_year'},
                                {'label': 'Personnalisé', 'value': 'custom'}
                            ],
                            value='this_month',
                            clearable=False,
                            className="w-full border-gray-300 rounded bg-white py-2 pl-3 pr-8 text-sm focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary",
                            style={'border': '1px solid #d1d5db', 'padding': '0px', 'min-height': 'auto'} # Adjust style to match original
                        ),
                        html.Div(className="absolute inset-y-0 right-0 flex items-center px-2 pointer-events-none", children=html.I(className="ri-arrow-down-s-line"))
                    ])
                ]),
                html.Div(className="mb-4", children=[
                    html.Label("Département", className="block text-sm font-medium text-gray-700 mb-1"),
                    html.Div(className="space-y-2", children=[
                        html.Div(className="flex items-center", children=[
                            html.Div(id='checkbox-marketing', className="custom-checkbox checked", **{'data-value': 'marketing'}),
                            html.Span("Marketing", className="ml-2 text-sm text-gray-700")
                        ]),
                        html.Div(className="flex items-center", children=[
                            html.Div(id='checkbox-ventes', className="custom-checkbox", **{'data-value': 'ventes'}),
                            html.Span("Ventes", className="ml-2 text-sm text-gray-700")
                        ]),
                        html.Div(className="flex items-center", children=[
                            html.Div(id='checkbox-finance', className="custom-checkbox checked", **{'data-value': 'finance'}),
                            html.Span("Finance", className="ml-2 text-sm text-gray-700")
                        ]),
                        html.Div(className="flex items-center", children=[
                            html.Div(id='checkbox-rh', className="custom-checkbox", **{'data-value': 'rh'}),
                            html.Span("Ressources Humaines", className="ml-2 text-sm text-gray-700")
                        ])
                    ])
                ]),
                html.Div(className="mb-4", children=[
                    html.Label("Région", className="block text-sm font-medium text-gray-700 mb-1"),
                    html.Div(className="relative", children=[
                        dcc.Dropdown(
                            id='region-dropdown',
                            options=[
                                {'label': 'Toutes les régions', 'value': 'all'},
                                {'label': 'Europe', 'value': 'europe'},
                                {'label': 'Amérique du Nord', 'value': 'north_america'},
                                {'label': 'Asie-Pacifique', 'value': 'asia_pacific'},
                                {'label': 'Amérique Latine', 'value': 'latin_america'},
                                {'label': 'Afrique', 'value': 'africa'}
                            ],
                            value='europe',
                            clearable=False,
                            className="w-full border-gray-300 rounded bg-white py-2 pl-3 pr-8 text-sm focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary",
                            style={'border': '1px solid #d1d5db', 'padding': '0px', 'min-height': 'auto'} # Adjust style to match original
                        ),
                        html.Div(className="absolute inset-y-0 right-0 flex items-center px-2 pointer-events-none", children=html.I(className="ri-arrow-down-s-line"))
                    ])
                ]),
                html.Div(className="mb-4", children=[
                    html.Label("Seuil de performance", className="block text-sm font-medium text-gray-700 mb-1"),
                    dcc.Slider(
                        id='performance-slider',
                        min=0,
                        max=100,
                        step=1,
                        value=75,
                        marks={i: str(i) + '%' for i in [0, 50, 100]},
                        className="performance-slider w-full"
                    ),
                    html.Div(className="flex justify-between text-xs text-gray-500 mt-1", children=[
                        html.Span("0%"),
                        html.Span("50%"),
                        html.Span("100%")
                    ])
                ]),
                html.Div(className="mb-4", children=[
                    html.Label(className="flex items-center justify-between text-sm font-medium text-gray-700 mb-1", children=[
                        html.Span("Données en temps réel"),
                        # # daq.ToggleSwitch(
                        #     id='realtime-data-switch',
                        #     value=True,
                        #     size=24,
                        #     className="switch"
                        # )
                    ])
                ]),
                html.Button("Réinitialiser les filtres", id='reset-filters-button', className="w-full bg-gray-100 text-gray-700 py-2 px-4 rounded-button text-sm font-medium hover:bg-gray-200 transition-colors whitespace-nowrap")
            ]),
            html.Div(children=[
                html.H3("Rapports enregistrés", className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3"),
                html.Ul(className="space-y-2", children=[
                    html.Li(html.A(href="#", className="flex items-center text-sm text-gray-700 hover:text-primary", children=[
                        html.Div(className="w-5 h-5 flex items-center justify-center mr-2", children=html.I(className="ri-file-chart-line")),
                        html.Span("Performance mensuelle")
                    ])),
                    html.Li(html.A(href="#", className="flex items-center text-sm text-gray-700 hover:text-primary", children=[
                        html.Div(className="w-5 h-5 flex items-center justify-center mr-2", children=html.I(className="ri-file-chart-line")),
                        html.Span("Analyse des ventes Q2")
                    ])),
                    html.Li(html.A(href="#", className="flex items-center text-sm text-gray-700 hover:text-primary", children=[
                        html.Div(className="w-5 h-5 flex items-center justify-center mr-2", children=html.I(className="ri-file-chart-line")),
                        html.Span("Prévisions 2025")
                    ]))
                ])
            ])
        ])
    ]),
    html.Main(className="content pt-16 lg:ml-64 min-h-screen transition-all duration-300", children=[
        html.Div(className="p-4 md:p-6", children=[
            html.Div(className="mb-6", children=[
                html.H1("Tableau de bord", className="text-2xl font-bold text-gray-900"),
                html.P("Dernière mise à jour: 11 juin 2025, 10:45", className="text-sm text-gray-500")
            ]),
            html.Div(className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6", children=[
                html.Div(className="bg-white rounded shadow p-4", children=[
                    html.Div(className="flex items-center justify-between mb-2", children=[
                        html.H3("Chiffre d'affaires", className="text-sm font-medium text-gray-500"),
                        html.Div(className="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center text-primary", children=html.I(className="ri-money-euro-circle-line ri-lg"))
                    ]),
                    html.P("1,458,213 €", className="text-2xl font-bold text-gray-900"),
                    html.Div(className="flex items-center mt-2", children=[
                        html.Div(className="flex items-center text-green-600 text-sm", children=[
                            html.I(className="ri-arrow-up-line"),
                            html.Span("12.5%", className="ml-1")
                        ]),
                        html.Span("vs mois précédent", className="text-xs text-gray-500 ml-2")
                    ])
                ]),
                html.Div(className="bg-white rounded shadow p-4", children=[
                    html.Div(className="flex items-center justify-between mb-2", children=[
                        html.H3("Nouveaux clients", className="text-sm font-medium text-gray-500"),
                        html.Div(className="w-8 h-8 rounded-full bg-green-100 flex items-center justify-center text-green-600", children=html.I(className="ri-user-add-line ri-lg"))
                    ]),
                    html.P("842", className="text-2xl font-bold text-gray-900"),
                    html.Div(className="flex items-center mt-2", children=[
                        html.Div(className="flex items-center text-green-600 text-sm", children=[
                            html.I(className="ri-arrow-up-line"),
                            html.Span("8.3%", className="ml-1")
                        ]),
                        html.Span("vs mois précédent", className="text-xs text-gray-500 ml-2")
                    ])
                ]),
                html.Div(className="bg-white rounded shadow p-4", children=[
                    html.Div(className="flex items-center justify-between mb-2", children=[
                        html.H3("Taux de conversion", className="text-sm font-medium text-gray-500"),
                        html.Div(className="w-8 h-8 rounded-full bg-purple-100 flex items-center justify-center text-purple-600", children=html.I(className="ri-percent-line ri-lg"))
                    ]),
                    html.P("24.8%", className="text-2xl font-bold text-gray-900"),
                    html.Div(className="flex items-center mt-2", children=[
                        html.Div(className="flex items-center text-red-600 text-sm", children=[
                            html.I(className="ri-arrow-down-line"),
                            html.Span("2.1%", className="ml-1")
                        ]),
                        html.Span("vs mois précédent", className="text-xs text-gray-500 ml-2")
                    ])
                ]),
                html.Div(className="bg-white rounded shadow p-4", children=[
                    html.Div(className="flex items-center justify-between mb-2", children=[
                        html.H3("Panier moyen", className="text-sm font-medium text-gray-500"),
                        html.Div(className="w-8 h-8 rounded-full bg-orange-100 flex items-center justify-center text-orange-600", children=html.I(className="ri-shopping-cart-line ri-lg"))
                    ]),
                    html.P("187 €", className="text-2xl font-bold text-gray-900"),
                    html.Div(className="flex items-center mt-2", children=[
                        html.Div(className="flex items-center text-green-600 text-sm", children=[
                            html.I(className="ri-arrow-up-line"),
                            html.Span("5.7%", className="ml-1")
                        ]),
                        html.Span("vs mois précédent", className="text-xs text-gray-500 ml-2")
                    ])
                ])
            ]),
            html.Div(className="mb-6", children=[
                html.Div(className="bg-white rounded shadow p-4", children=[
                    html.Div(className="flex items-center justify-between mb-4", children=[
                        html.H2("Évolution des ventes", className="text-lg font-semibold text-gray-900"),
                        html.Div(className="flex space-x-2", children=[
                            html.Button("Exporter", className="bg-gray-100 text-gray-700 py-1 px-3 rounded-button text-sm font-medium hover:bg-gray-200 transition-colors whitespace-nowrap"),
                            html.Div(className="relative", children=[
                                html.Button(className="bg-gray-100 text-gray-700 py-1 px-3 rounded-button text-sm font-medium hover:bg-gray-200 transition-colors whitespace-nowrap flex items-center", children=[
                                    html.Span("Mensuel"),
                                    html.I(className="ri-arrow-down-s-line ml-1")
                                ])
                            ])
                        ])
                    ]),
                    dcc.Graph(
                        id='sales-chart',
                        style={'width': '100%', 'height': '320px'}
                    )
                ])
            ]),
            html.Div(className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6", children=[
                html.Div(className="bg-white rounded shadow p-4", children=[
                    html.Div(className="flex items-center justify-between mb-4", children=[
                        html.H2("Répartition par produit", className="text-lg font-semibold text-gray-900"),
                        html.Div(className="relative", children=[
                            html.Button(className="bg-gray-100 text-gray-700 py-1 px-3 rounded-button text-sm font-medium hover:bg-gray-200 transition-colors whitespace-nowrap flex items-center", children=[
                                html.Span("Top 5"),
                                html.I(className="ri-arrow-down-s-line ml-1")
                            ])
                        ])
                    ]),
                    dcc.Graph(
                        id='product-chart',
                        style={'width': '100%', 'height': '256px'}
                    )
                ]),
                html.Div(className="bg-white rounded shadow p-4", children=[
                    html.Div(className="flex items-center justify-between mb-4", children=[
                        html.H2("Répartition géographique", className="text-lg font-semibold text-gray-900"),
                        html.Div(className="relative", children=[
                            html.Button(className="bg-gray-100 text-gray-700 py-1 px-3 rounded-button text-sm font-medium hover:bg-gray-200 transition-colors whitespace-nowrap flex items-center", children=[
                                html.Span("Europe"),
                                html.I(className="ri-arrow-down-s-line ml-1")
                            ])
                        ])
                    ]),
                    dcc.Graph(
                        id='geo-chart',
                        style={'width': '100%', 'height': '256px'}
                    )
                ])
            ]),
            html.Div(className="grid grid-cols-1 lg:grid-cols-3 gap-6", children=[
                html.Div(className="bg-white rounded shadow p-4 lg:col-span-2", children=[
                    html.Div(className="flex items-center justify-between mb-4", children=[
                        html.H2("Dernières transactions", className="text-lg font-semibold text-gray-900"),
                        html.Button("Voir tout", className="text-primary text-sm font-medium hover:underline")
                    ]),
                    html.Div(className="overflow-x-auto", children=[
                        html.Table(className="min-w-full divide-y divide-gray-200", children=[
                            html.Thead(children=[
                                html.Tr(children=[
                                    html.Th("Client", scope="col", className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"),
                                    html.Th("Produit", scope="col", className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"),
                                    html.Th("Date", scope="col", className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"),
                                    html.Th("Montant", scope="col", className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"),
                                    html.Th("Statut", scope="col", className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider")
                                ])
                            ]),
                            html.Tbody(className="bg-white divide-y divide-gray-200", children=[
                                html.Tr(children=[
                                    html.Td(className="px-4 py-3 whitespace-nowrap", children=[
                                        html.Div(className="flex items-center", children=[
                                            html.Div(className="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-600", children=html.Span("ML", className="text-sm font-medium")),
                                            html.Div(className="ml-3", children=[
                                                html.P("Marie Lefevre", className="text-sm font-medium text-gray-900"),
                                                html.P("marie.l@example.com", className="text-xs text-gray-500")
                                            ])
                                        ])
                                    ]),
                                    html.Td("Premium Suite", className="px-4 py-3 whitespace-nowrap text-sm text-gray-700"),
                                    html.Td("11 juin 2025", className="px-4 py-3 whitespace-nowrap text-sm text-gray-700"),
                                    html.Td("2,450 €", className="px-4 py-3 whitespace-nowrap text-sm text-gray-700"),
                                    html.Td(className="px-4 py-3 whitespace-nowrap", children=html.Span("Complété", className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800"))
                                ]),
                                html.Tr(children=[
                                    html.Td(className="px-4 py-3 whitespace-nowrap", children=[
                                        html.Div(className="flex items-center", children=[
                                            html.Div(className="w-8 h-8 rounded-full bg-green-100 flex items-center justify-center text-green-600", children=html.Span("TD", className="text-sm font-medium")),
                                            html.Div(className="ml-3", children=[
                                                html.P("Thomas Dubois", className="text-sm font-medium text-gray-900"),
                                                html.P("thomas.d@example.com", className="text-xs text-gray-500")
                                            ])
                                        ])
                                    ]),
                                    html.Td("Standard Plan", className="px-4 py-3 whitespace-nowrap text-sm text-gray-700"),
                                    html.Td("10 juin 2025", className="px-4 py-3 whitespace-nowrap text-sm text-gray-700"),
                                    html.Td("950 €", className="px-4 py-3 whitespace-nowrap text-sm text-gray-700"),
                                    html.Td(className="px-4 py-3 whitespace-nowrap", children=html.Span("Complété", className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800"))
                                ]),
                                html.Tr(children=[
                                    html.Td(className="px-4 py-3 whitespace-nowrap", children=[
                                        html.Div(className="flex items-center", children=[
                                            html.Div(className="w-8 h-8 rounded-full bg-purple-100 flex items-center justify-center text-purple-600", children=html.Span("SB", className="text-sm font-medium")),
                                            html.Div(className="ml-3", children=[
                                                html.P("Sophie Bernard", className="text-sm font-medium text-gray-900"),
                                                html.P("sophie.b@example.com", className="text-xs text-gray-500")
                                            ])
                                        ])
                                    ]),
                                    html.Td("Basic Plan", className="px-4 py-3 whitespace-nowrap text-sm text-gray-700"),
                                    html.Td("9 juin 2025", className="px-4 py-3 whitespace-nowrap text-sm text-gray-700"),
                                    html.Td("450 €", className="px-4 py-3 whitespace-nowrap text-sm text-gray-700"),
                                    html.Td(className="px-4 py-3 whitespace-nowrap", children=html.Span("En attente", className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800"))
                                ]),
                                html.Tr(children=[
                                    html.Td(className="px-4 py-3 whitespace-nowrap", children=[
                                        html.Div(className="flex items-center", children=[
                                            html.Div(className="w-8 h-8 rounded-full bg-red-100 flex items-center justify-center text-red-600", children=html.Span("RM", className="text-sm font-medium")),
                                            html.Div(className="ml-3", children=[
                                                html.P("Robert Martin", className="text-sm font-medium text-gray-900"),
                                                html.P("robert.m@example.com", className="text-xs text-gray-500")
                                            ])
                                        ])
                                    ]),
                                    html.Td("Premium Suite", className="px-4 py-3 whitespace-nowrap text-sm text-gray-700"),
                                    html.Td("8 juin 2025", className="px-4 py-3 whitespace-nowrap text-sm text-gray-700"),
                                    html.Td("2,450 €", className="px-4 py-3 whitespace-nowrap text-sm text-gray-700"),
                                    html.Td(className="px-4 py-3 whitespace-nowrap", children=html.Span("Annulé", className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800"))
                                ])
                            ])
                        ])
                    ])
                ]),
                html.Div(className="bg-white rounded shadow p-4", children=[
                    html.Div(className="flex items-center justify-between mb-4", children=[
                        html.H2("Activités récentes", className="text-lg font-semibold text-gray-900"),
                        html.Button("Voir tout", className="text-primary text-sm font-medium hover:underline")
                    ]),
                    html.Div(className="space-y-4", children=[
                        html.Div(className="flex", children=[
                            html.Div(className="flex-shrink-0 w-10", children=html.Div(className="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-600", children=html.I(className="ri-user-line"))),
                            html.Div(children=[
                                html.P(children=[
                                    html.Span("Marie Lefevre", className="font-medium text-gray-900"),
                                    " a complété son achat de Premium Suite"
                                ], className="text-sm text-gray-700"),
                                html.P("Il y a 15 minutes", className="text-xs text-gray-500 mt-1")
                            ])
                        ]),
                        html.Div(className="flex", children=[
                            html.Div(className="flex-shrink-0 w-10", children=html.Div(className="w-8 h-8 rounded-full bg-green-100 flex items-center justify-center text-green-600", children=html.I(className="ri-file-list-line"))),
                            html.Div(children=[
                                html.P(children=[
                                    "Nouveau rapport ",
                                    html.Span("Analyse Q2", className="font-medium text-gray-900"),
                                    " généré"
                                ], className="text-sm text-gray-700"),
                                html.P("Il y a 45 minutes", className="text-xs text-gray-500 mt-1")
                            ])
                        ]),
                        html.Div(className="flex", children=[
                            html.Div(className="flex-shrink-0 w-10", children=html.Div(className="w-8 h-8 rounded-full bg-yellow-100 flex items-center justify-center text-yellow-600", children=html.I(className="ri-alert-line"))),
                            html.Div(children=[
                                html.P(children=[
                                    html.Span("Alerte de stock", className="font-medium text-gray-900"),
                                    " pour le produit Premium Suite"
                                ], className="text-sm text-gray-700"),
                                html.P("Il y a 2 heures", className="text-xs text-gray-500 mt-1")
                            ])
                        ]),
                        html.Div(className="flex", children=[
                            html.Div(className="flex-shrink-0 w-10", children=html.Div(className="w-8 h-8 rounded-full bg-purple-100 flex items-center justify-center text-purple-600", children=html.I(className="ri-mail-line"))),
                            html.Div(children=[
                                html.P(children=[
                                    html.Span("Campagne email", className="font-medium text-gray-900"),
                                    " \"Offre d'été\" envoyée à 5,240 clients"
                                ], className="text-sm text-gray-700"),
                                html.P("Il y a 3 heures", className="text-xs text-gray-500 mt-1")
                            ])
                        ]),
                        html.Div(className="flex", children=[
                            html.Div(className="flex-shrink-0 w-10", children=html.Div(className="w-8 h-8 rounded-full bg-red-100 flex items-center justify-center text-red-600", children=html.I(className="ri-alert-line"))),
                            html.Div(children=[
                                html.P(children=[
                                    html.Span("Problème de paiement", className="font-medium text-gray-900"),
                                    " pour la transaction #12345"
                                ], className="text-sm text-gray-700"),
                                html.P("Il y a 4 heures", className="text-xs text-gray-500 mt-1")
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])
])

# Callbacks for interactivity (examples)

# Callback for custom checkboxes (Département filter)
@app.callback(
    [Output('checkbox-marketing', 'className'),
     Output('checkbox-ventes', 'className'),
     Output('checkbox-finance', 'className'),
     Output('checkbox-rh', 'className')],
    [Input('checkbox-marketing', 'n_clicks'),
     Input('checkbox-ventes', 'n_clicks'),
     Input('checkbox-finance', 'n_clicks'),
     Input('checkbox-rh', 'n_clicks')],
    [State('checkbox-marketing', 'className'),
     State('checkbox-ventes', 'className'),
     State('checkbox-finance', 'className'),
     State('checkbox-rh', 'className')]
)
def toggle_checkboxes(n_clicks_m, n_clicks_v, n_clicks_f, n_clicks_rh,
                       class_m, class_v, class_f, class_rh):
    ctx = dash.callback_context
    if not ctx.triggered:
        # Initial load, keep existing classes
        return class_m, class_v, class_f, class_rh
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        new_class_m = class_m
        new_class_v = class_v
        new_class_f = class_f
        new_class_rh = class_rh

        if button_id == 'checkbox-marketing':
            new_class_m = "custom-checkbox" if "checked" in class_m else "custom-checkbox checked"
        elif button_id == 'checkbox-ventes':
            new_class_v = "custom-checkbox" if "checked" in class_v else "custom-checkbox checked"
        elif button_id == 'checkbox-finance':
            new_class_f = "custom-checkbox" if "checked" in class_f else "custom-checkbox checked"
        elif button_id == 'checkbox-rh':
            new_class_rh = "custom-checkbox" if "checked" in class_rh else "custom-checkbox checked"
        
        return new_class_m, new_class_v, new_class_f, new_class_rh

# Callback for sales chart (example data)
@app.callback(
    Output('sales-chart', 'figure'),
    [Input('period-dropdown', 'value')] # Example: chart updates with period selection
)
def update_sales_chart(selected_period):
    # In a real application, you'd fetch/process data based on selected_period
    if selected_period == 'this_month':
        sales_data = [120, 130, 150, 140, 160, 170, 180, 190, 200, 210, 220, 230]
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    else:
        sales_data = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
        months = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11', 'Week 12']

    figure = {
        'data': [
            {
                'x': months,
                'y': sales_data,
                'type': 'line',
                'mode': 'lines+markers',
                'marker': {'color': '#4f46e5'},
                'name': 'Sales'
            }
        ],
        'layout': {
            'title': 'Sales Evolution',
            'xaxis': {'title': 'Period'},
            'yaxis': {'title': 'Revenue (€)'},
            'margin': {'l': 40, 'r': 0, 't': 40, 'b': 30},
            'hovermode': 'closest',
            'plot_bgcolor': 'white',
            'paper_bgcolor': 'white'
        }
    }
    return figure

# Callback for product chart (example data)
@app.callback(
    Output('product-chart', 'figure'),
    [Input('period-dropdown', 'value')] # Example: chart updates with period selection
)
def update_product_chart(selected_period):
    # In a real application, you'd fetch/process data based on selected_period
    product_data = [
        {'label': 'Premium Suite', 'value': 40},
        {'label': 'Standard Plan', 'value': 30},
        {'label': 'Basic Plan', 'value': 15},
        {'label': 'Enterprise Solution', 'value': 10},
        {'label': 'Other', 'value': 5},
    ]

    figure = {
        'data': [
            {
                'labels': [d['label'] for d in product_data],
                'values': [d['value'] for d in product_data],
                'type': 'pie',
                'hoverinfo': 'label+percent',
                'textinfo': 'none',
                'marker': {'colors': ['#4f46e5', '#8b5cf6', '#a78bfa', '#c4b5fd', '#ddd6fe']}
            }
        ],
        'layout': {
            'title': 'Product Distribution',
            'margin': {'l': 0, 'r': 0, 't': 40, 'b': 0},
            'plot_bgcolor': 'white',
            'paper_bgcolor': 'white'
        }
    }
    return figure

# Callback for geo chart (example data)
@app.callback(
    Output('geo-chart', 'figure'),
    [Input('region-dropdown', 'value')] # Example: chart updates with region selection
)
def update_geo_chart(selected_region):
    # In a real application, you'd fetch/process data based on selected_region
    if selected_region == 'europe':
        geo_data = [
            {'label': 'France', 'value': 30},
            {'label': 'Germany', 'value': 25},
            {'label': 'UK', 'value': 20},
            {'label': 'Spain', 'value': 15},
            {'label': 'Italy', 'value': 10},
        ]
    else:
        geo_data = [
            {'label': 'USA', 'value': 50},
            {'label': 'Canada', 'value': 20},
            {'label': 'Mexico', 'value': 10},
            {'label': 'Brazil', 'value': 10},
            {'label': 'Argentina', 'value': 10},
        ]
    figure = {
        'data': [
            {
                'labels': [d['label'] for d in geo_data],
                'values': [d['value'] for d in geo_data],
                'type': 'pie',
                'hoverinfo': 'label+percent',
                'textinfo': 'none',
                'marker': {'colors': ['#4f46e5', '#8b5cf6', '#a78bfa', '#c4b5fd', '#ddd6fe']}
            }
        ],
        'layout': {
            'title': 'Geographical Distribution',
            'margin': {'l': 0, 'r': 0, 't': 40, 'b': 0},
            'plot_bgcolor': 'white',
            'paper_bgcolor': 'white'
        }
    }
    return figure

# Callback to reset filters
@app.callback(
    [Output('period-dropdown', 'value'),
     Output('checkbox-marketing', 'className'),
     Output('checkbox-ventes', 'className'),
     Output('checkbox-finance', 'className'),
     Output('checkbox-rh', 'className'),
     Output('region-dropdown', 'value'),
     Output('performance-slider', 'value'),
     Output('realtime-data-switch', 'value')],
    [Input('reset-filters-button', 'n_clicks')]
)
def reset_filters(n_clicks):
    if n_clicks:
        return 'this_month', \
               "custom-checkbox checked", \
               "custom-checkbox", \
               "custom-checkbox checked", \
               "custom-checkbox", \
               'europe', \
               75, \
               True
    return dash.no_update # Prevents update on initial load

if __name__ == '__main__':
    app.run(debug=True)