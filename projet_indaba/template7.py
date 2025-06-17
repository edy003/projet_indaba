import dash
from dash import html, dcc, Input, Output, State, callback

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[
    "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
    "https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css"
])

def create_sidebar():
    """Create the sidebar component"""
    return html.Aside(
        className="flex-shrink-0 hidden w-64 bg-white border-r dark:border-gray-700 dark:bg-gray-800 md:block",
        style={"height": "100vh", "position": "fixed", "left": 0, "top": 0},
        children=[
            html.Div(
                className="flex flex-col h-full",
                children=[
                    # Sidebar Navigation
                    html.Nav(
                        className="flex-1 px-2 py-4 space-y-2 overflow-y-hidden hover:overflow-y-auto",
                        children=[
                            # Dashboards Section
                            html.Div([
                                html.A(
                                    id="dashboards-toggle",
                                    className="flex items-center p-2 text-gray-500 transition-colors rounded-md dark:text-white hover:bg-blue-100 dark:hover:bg-blue-600 bg-blue-100 dark:bg-blue-600 cursor-pointer",
                                    children=[
                                        html.I(className="ri-home-line text-xl mr-2"),
                                        html.Span("Dashboards", className="ml-2 text-sm"),
                                        html.I(
                                            id="dashboards-arrow",
                                            className="ri-arrow-down-s-line ml-auto text-base transition-transform transform rotate-180"
                                        )
                                    ]
                                ),
                                html.Div(
                                    id="dashboards-menu",
                                    className="mt-2 space-y-2 px-7",
                                    children=[
                                        html.A("Default", href="/", className="block p-2 text-sm text-gray-700 dark:text-white transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Project Management (soon)", href="#", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("E-Commerce (soon)", href="#", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                    ]
                                )
                            ]),
                            
                            # Components Section
                            html.Div([
                                html.A(
                                    id="components-toggle",
                                    className="flex items-center p-2 text-gray-500 dark:text-white transition-colors rounded-md hover:bg-blue-100 dark:hover:bg-blue-600 cursor-pointer",
                                    children=[
                                        html.I(className="ri-layout-grid-line text-xl mr-2"),
                                        html.Span("Components", className="ml-2 text-sm"),
                                        html.I(
                                            id="components-arrow",
                                            className="ri-arrow-down-s-line ml-auto text-base transition-transform transform"
                                        )
                                    ]
                                ),
                                html.Div(
                                    id="components-menu",
                                    className="mt-2 space-y-2 px-7",
                                    style={"display": "none"},
                                    children=[
                                        html.A("Alerts (soon)", href="#", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Buttons (soon)", href="#", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Cards (soon)", href="#", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Dropdowns (soon)", href="#", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Forms (soon)", href="#", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Lists (soon)", href="#", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Modals (soon)", href="#", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                    ]
                                )
                            ]),
                            
                            # Pages Section
                            html.Div([
                                html.A(
                                    id="pages-toggle",
                                    className="flex items-center p-2 text-gray-500 dark:text-white transition-colors rounded-md hover:bg-blue-100 dark:hover:bg-blue-600 cursor-pointer",
                                    children=[
                                        html.I(className="ri-file-text-line text-xl mr-2"),
                                        html.Span("Pages", className="ml-2 text-sm"),
                                        html.I(
                                            id="pages-arrow",
                                            className="ri-arrow-down-s-line ml-auto text-base transition-transform transform"
                                        )
                                    ]
                                ),
                                html.Div(
                                    id="pages-menu",
                                    className="mt-2 space-y-2 px-7",
                                    style={"display": "none"},
                                    children=[
                                        html.A("Blank", href="/blank", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("404", href="/404", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("500", href="/500", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Profile (soon)", href="#", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Pricing (soon)", href="#", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Kanban (soon)", href="#", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Feed (soon)", href="#", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                    ]
                                )
                            ]),
                            
                            # Authentication Section
                            html.Div([
                                html.A(
                                    id="auth-toggle",
                                    className="flex items-center p-2 text-gray-500 dark:text-white transition-colors rounded-md hover:bg-blue-100 dark:hover:bg-blue-600 cursor-pointer",
                                    children=[
                                        html.I(className="ri-user-line text-xl mr-2"),
                                        html.Span("Authentication", className="ml-2 text-sm"),
                                        html.I(
                                            id="auth-arrow",
                                            className="ri-arrow-down-s-line ml-auto text-base transition-transform transform"
                                        )
                                    ]
                                ),
                                html.Div(
                                    id="auth-menu",
                                    className="mt-2 space-y-2 px-7",
                                    style={"display": "none"},
                                    children=[
                                        html.A("Register", href="/register", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Login", href="/login", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Forgot Password", href="/forgot-password", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Reset Password", href="/reset-password", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                    ]
                                )
                            ]),
                            
                            # Layouts Section
                            html.Div([
                                html.A(
                                    id="layouts-toggle",
                                    className="flex items-center p-2 text-gray-500 dark:text-white transition-colors rounded-md hover:bg-blue-100 dark:hover:bg-blue-600 cursor-pointer",
                                    children=[
                                        html.I(className="ri-layout-3-line text-xl mr-2"),
                                        html.Span("Layouts", className="ml-2 text-sm"),
                                        html.I(
                                            id="layouts-arrow",
                                            className="ri-arrow-down-s-line ml-auto text-base transition-transform transform"
                                        )
                                    ]
                                ),
                                html.Div(
                                    id="layouts-menu",
                                    className="mt-2 space-y-2 px-7",
                                    style={"display": "none"},
                                    children=[
                                        html.A("Two Columns Sidebar", href="/two-columns", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Mini + One Columns Sidebar", href="/mini-one-columns", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                        html.A("Mini Column Sidebar", href="/mini-column", className="block p-2 text-sm text-gray-400 dark:text-gray-400 transition-colors duration-200 rounded-md hover:text-gray-700 dark:hover:text-white"),
                                    ]
                                )
                            ]),
                        ]
                    ),
                    
                    # Sidebar Footer
                    html.Div(
                        className="flex-shrink-0 px-2 py-4 space-y-2",
                        children=[
                            html.Button(
                                id="customize-btn",
                                className="flex items-center justify-center w-full px-4 py-2 text-sm text-white rounded-md bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-500 focus:ring-offset-1 focus:ring-offset-white dark:focus:ring-offset-gray-800",
                                children=[
                                    html.I(className="ri-settings-3-line text-base mr-2"),
                                    html.Span("Customize")
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )

# Callbacks for menu toggles
@callback(
    [Output("components-menu", "style"),
     Output("components-arrow", "style")],
    Input("components-toggle", "n_clicks"),
    State("components-menu", "style"),
    prevent_initial_call=True
)
def toggle_components_menu(n_clicks, current_style):
    if n_clicks:
        is_hidden = current_style.get("display") == "none"
        if is_hidden:
            return {"display": "block"}, {"transform": "rotate(180deg)"}
        else:
            return {"display": "none"}, {"transform": "rotate(0deg)"}
    return current_style, {"transform": "rotate(0deg)"}

@callback(
    [Output("pages-menu", "style"),
     Output("pages-arrow", "style")],
    Input("pages-toggle", "n_clicks"),
    State("pages-menu", "style"),
    prevent_initial_call=True
)
def toggle_pages_menu(n_clicks, current_style):
    if n_clicks:
        is_hidden = current_style.get("display") == "none"
        if is_hidden:
            return {"display": "block"}, {"transform": "rotate(180deg)"}
        else:
            return {"display": "none"}, {"transform": "rotate(0deg)"}
    return current_style, {"transform": "rotate(0deg)"}

@callback(
    [Output("auth-menu", "style"),
     Output("auth-arrow", "style")],
    Input("auth-toggle", "n_clicks"),
    State("auth-menu", "style"),
    prevent_initial_call=True
)
def toggle_auth_menu(n_clicks, current_style):
    if n_clicks:
        is_hidden = current_style.get("display") == "none"
        if is_hidden:
            return {"display": "block"}, {"transform": "rotate(180deg)"}
        else:
            return {"display": "none"}, {"transform": "rotate(0deg)"}
    return current_style, {"transform": "rotate(0deg)"}

@callback(
    [Output("layouts-menu", "style"),
     Output("layouts-arrow", "style")],
    Input("layouts-toggle", "n_clicks"),
    State("layouts-menu", "style"),
    prevent_initial_call=True
)
def toggle_layouts_menu(n_clicks, current_style):
    if n_clicks:
        is_hidden = current_style.get("display") == "none"
        if is_hidden:
            return {"display": "block"}, {"transform": "rotate(180deg)"}
        else:
            return {"display": "none"}, {"transform": "rotate(0deg)"}
    return current_style, {"transform": "rotate(0deg)"}

@callback(
    Output("customize-btn", "children"),
    Input("customize-btn", "n_clicks"),
    prevent_initial_call=True
)
def customize_button_click(n_clicks):
    if n_clicks:
        return [
            html.I(className="ri-check-line text-base mr-2"),
            html.Span("Customized!")
        ]
    return [
        html.I(className="ri-settings-3-line text-base mr-2"),
        html.Span("Customize")
    ]

# Main layout
app.layout = html.Div([
    create_sidebar(),
    html.Div(
        className="ml-64 p-6 bg-gray-50 dark:bg-gray-900 min-h-screen",
        children=[
            html.H1("Dashboard Content", className="text-2xl font-bold text-gray-900 dark:text-white"),
            html.P("This is the main content area. The sidebar is fixed on the left with Tailwind CSS styling.", 
                   className="mt-4 text-gray-600 dark:text-gray-300"),
            html.Div(
                className="mt-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
                children=[
                    html.Div(
                        className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md",
                        children=[
                            html.H3("Card 1", className="text-lg font-semibold text-gray-900 dark:text-white mb-2"),
                            html.P("Sample content card", className="text-gray-600 dark:text-gray-300")
                        ]
                    ),
                    html.Div(
                        className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md",
                        children=[
                            html.H3("Card 2", className="text-lg font-semibold text-gray-900 dark:text-white mb-2"),
                            html.P("Another content card", className="text-gray-600 dark:text-gray-300")
                        ]
                    ),
                    html.Div(
                        className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md",
                        children=[
                            html.H3("Card 3", className="text-lg font-semibold text-gray-900 dark:text-white mb-2"),
                            html.P("Third content card", className="text-gray-600 dark:text-gray-300")
                        ]
                    )
                ]
            )
        ]
    )
])

if __name__ == "__main__":
    app.run(debug=True)