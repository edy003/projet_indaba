import dash
from dash import dcc, html, Input, Output, callback, State
import plotly.graph_objects as go
import plotly.express as px

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[
    "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
    "https://cdn.jsdelivr.net/npm/remixicon@4.0.0/fonts/remixicon.css"
])

# Store for sidebar state
app.server.secret_key = 'your-secret-key'

# Sample data for the monthly sales chart
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_data = [150, 380, 200, 300, 180, 220, 320, 100, 250, 380, 300, 120]

def create_monthly_sales_chart():
    fig = go.Figure(data=[
        go.Bar(
            x=months,
            y=sales_data,
            marker_color='#6366f1',
            marker_line_color='rgba(0,0,0,0)',
            hovertemplate='<b>%{x}</b><br>Sales: %{y}<extra></extra>'
        )
    ])
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#6b7280'),
        xaxis=dict(
            showgrid=False,
            showline=False,
            zeroline=False
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)',
            showline=False,
            zeroline=False
        ),
        margin=dict(l=20, r=20, t=20, b=20),
        height=300
    )
    
    return fig

def create_progress_chart():
    fig = go.Figure(data=[
        go.Pie(
            values=[75.55, 24.45],
            hole=0.7,
            marker_colors=['#6366f1', '#e5e7eb'],
            showlegend=False,
            hoverinfo='skip',
            textinfo='none'
        )
    ])
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=200,
        width=200
    )
    
    return fig

# Define the layout
app.layout = html.Div([
    # Store for sidebar state
    dcc.Store(id='sidebar-state', data={'collapsed': False}),
    
    # Main container
    html.Div([
        # Sidebar
        html.Div([
            # Logo
            html.Div([
                html.Div([
                    html.I(className="ri-admin-line text-white text-2xl flex-shrink-0"),
                    html.Span("TailAdmin", className="text-white font-bold text-xl ml-2", id="logo-text")
                ], className="flex items-center p-4 bg-indigo-600 rounded-lg mb-6")
            ]),
            
            # Menu section
            html.Div([
                html.P("MENU", className="text-gray-400 text-xs font-semibold mb-4 px-4", id="menu-label"),
                
                # Dashboard
                html.Div([
                    html.I(className="ri-dashboard-line text-xl flex-shrink-0"),
                    html.Span("Dashboard", className="ml-3", id="dashboard-text"),
                    html.I(className="ri-arrow-down-s-line ml-auto", id="dashboard-arrow")
                ], className="flex items-center px-4 py-3 text-indigo-600 bg-indigo-50 rounded-lg mx-4 mb-2 cursor-pointer", title="Dashboard"),
                
                # Calendar
                html.Div([
                    html.I(className="ri-calendar-line text-xl flex-shrink-0"),
                    html.Span("Calendar", className="ml-3", id="calendar-text")
                ], className="flex items-center px-4 py-3 text-gray-600 hover:bg-gray-100 rounded-lg mx-4 mb-2 cursor-pointer", title="Calendar"),
                
                # User Profile
                html.Div([
                    html.I(className="ri-user-line text-xl flex-shrink-0"),
                    html.Span("User Profile", className="ml-3", id="profile-text")
                ], className="flex items-center px-4 py-3 text-gray-600 hover:bg-gray-100 rounded-lg mx-4 mb-2 cursor-pointer", title="User Profile"),
                
                # Task
                html.Div([
                    html.I(className="ri-task-line text-xl flex-shrink-0"),
                    html.Span("Task", className="ml-3", id="task-text"),
                    html.I(className="ri-arrow-down-s-line ml-auto", id="task-arrow")
                ], className="flex items-center px-4 py-3 text-gray-600 hover:bg-gray-100 rounded-lg mx-4 mb-2 cursor-pointer", title="Task"),
                
                # Forms
                html.Div([
                    html.I(className="ri-file-text-line text-xl flex-shrink-0"),
                    html.Span("Forms", className="ml-3", id="forms-text"),
                    html.I(className="ri-arrow-down-s-line ml-auto", id="forms-arrow")
                ], className="flex items-center px-4 py-3 text-gray-600 hover:bg-gray-100 rounded-lg mx-4 mb-2 cursor-pointer", title="Forms"),
                
                # Tables
                html.Div([
                    html.I(className="ri-table-line text-xl flex-shrink-0"),
                    html.Span("Tables", className="ml-3", id="tables-text"),
                    html.I(className="ri-arrow-down-s-line ml-auto", id="tables-arrow")
                ], className="flex items-center px-4 py-3 text-gray-600 hover:bg-gray-100 rounded-lg mx-4 mb-2 cursor-pointer", title="Tables"),
                
                # Pages
                html.Div([
                    html.I(className="ri-pages-line text-xl flex-shrink-0"),
                    html.Span("Pages", className="ml-3", id="pages-text"),
                    html.I(className="ri-arrow-down-s-line ml-auto", id="pages-arrow")
                ], className="flex items-center px-4 py-3 text-gray-600 hover:bg-gray-100 rounded-lg mx-4 mb-6 cursor-pointer", title="Pages"),
                
                # Support section
                html.P("SUPPORT", className="text-gray-400 text-xs font-semibold mb-4 px-4", id="support-label"),
                
                # Chat
                html.Div([
                    html.I(className="ri-chat-3-line text-xl flex-shrink-0"),
                    html.Span("Chat", className="ml-3", id="chat-text")
                ], className="flex items-center px-4 py-3 text-gray-600 hover:bg-gray-100 rounded-lg mx-4 mb-2 cursor-pointer", title="Chat"),
            ])
        ], className="w-72 bg-white shadow-lg h-screen fixed left-0 top-0 p-4 transition-all duration-300 ease-in-out z-20", id="sidebar"),
        
        # Main content
        html.Div([
            # Header
            html.Div([
                html.Div([
                    html.I(className="ri-menu-line text-2xl text-gray-600 cursor-pointer", id="toggle-sidebar"),
                    
                    # Search bar
                    html.Div([
                        html.I(className="ri-search-line absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400"),
                        dcc.Input(
                            placeholder="Search or type command...",
                            className="pl-10 pr-10 py-2 w-96 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
                        ),
                        html.Kbd("⌘K", className="absolute right-4 top-1/2 transform -translate-y-1/2 text-xs bg-gray-100 px-2 py-1 rounded")
                    ], className="relative mx-8"),
                    
                    # Right side icons
                    html.Div([
                        html.I(className="ri-moon-line text-2xl text-gray-600 cursor-pointer mr-4"),
                        html.Div([
                            html.I(className="ri-notification-3-line text-2xl text-gray-600 cursor-pointer"),
                            html.Span(className="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full w-4 h-4 flex items-center justify-center")
                        ], className="relative mr-4"),
                        
                        # Profile
                        html.Div([
                            html.Img(src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' viewBox='0 0 40 40'%3E%3Crect width='40' height='40' rx='20' fill='%236366f1'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' fill='white' font-family='Arial' font-size='16'%3EM%3C/text%3E%3C/svg%3E", 
                                   className="w-10 h-10 rounded-full"),
                            html.Span("Musharaf", className="ml-2 font-medium text-gray-700"),
                            html.I(className="ri-arrow-down-s-line ml-2 text-gray-400")
                        ], className="flex items-center cursor-pointer")
                    ], className="flex items-center")
                ], className="flex items-center justify-between")
            ], className="bg-white shadow-sm p-4 mb-6"),
            
            # Dashboard content
            html.Div([
                # Top row - Stats cards
                html.Div([
                    # Customers card
                    html.Div([
                        html.Div([
                            html.I(className="ri-user-3-line text-3xl text-indigo-600"),
                        ], className="mb-4"),
                        html.P("Customers", className="text-gray-600 text-sm mb-2"),
                        html.Div([
                            html.H3("3,782", className="text-3xl font-bold text-gray-900"),
                            html.Div([
                                html.I(className="ri-arrow-up-line text-green-500 mr-1"),
                                html.Span("11.01%", className="text-green-500 font-medium")
                            ], className="flex items-center ml-4")
                        ], className="flex items-end")
                    ], className="bg-white p-6 rounded-lg shadow-sm"),
                    
                    # Orders card
                    html.Div([
                        html.Div([
                            html.I(className="ri-shopping-bag-line text-3xl text-indigo-600"),
                        ], className="mb-4"),
                        html.P("Orders", className="text-gray-600 text-sm mb-2"),
                        html.Div([
                            html.H3("5,359", className="text-3xl font-bold text-gray-900"),
                            html.Div([
                                html.I(className="ri-arrow-down-line text-red-500 mr-1"),
                                html.Span("9.05%", className="text-red-500 font-medium")
                            ], className="flex items-center ml-4")
                        ], className="flex items-end")
                    ], className="bg-white p-6 rounded-lg shadow-sm"),
                    
                    # Monthly Target card
                    html.Div([
                        html.Div([
                            html.H3("Monthly Target", className="text-lg font-semibold text-gray-900 mb-2"),
                            html.P("Target you've set for each month", className="text-gray-600 text-sm mb-6"),
                            
                            # Progress circle
                            html.Div([
                                dcc.Graph(
                                    figure=create_progress_chart(),
                                    config={'displayModeBar': False},
                                    className="w-48 h-48 mx-auto"
                                ),
                                html.Div([
                                    html.H2("75.55%", className="text-3xl font-bold text-gray-900"),
                                    html.P("+10%", className="text-green-500 font-medium")
                                ], className="absolute inset-0 flex flex-col items-center justify-center")
                            ], className="relative mb-6"),
                            
                            html.P("You earn $3287 today, it's higher than last month.", className="text-gray-600 text-center mb-2"),
                            html.P("Keep up your good work!", className="text-gray-600 text-center mb-6"),
                            
                            # Bottom stats
                            html.Div([
                                html.Div([
                                    html.P("Target", className="text-gray-500 text-sm"),
                                    html.Div([
                                        html.Span("$20K", className="font-bold text-gray-900"),
                                        html.I(className="ri-arrow-down-line text-red-500 ml-1")
                                    ], className="flex items-center")
                                ], className="text-center"),
                                
                                html.Div([
                                    html.P("Revenue", className="text-gray-500 text-sm"),
                                    html.Div([
                                        html.Span("$20K", className="font-bold text-gray-900"),
                                        html.I(className="ri-arrow-up-line text-green-500 ml-1")
                                    ], className="flex items-center")
                                ], className="text-center"),
                                
                                html.Div([
                                    html.P("Today", className="text-gray-500 text-sm"),
                                    html.Div([
                                        html.Span("$20K", className="font-bold text-gray-900"),
                                        html.I(className="ri-arrow-up-line text-green-500 ml-1")
                                    ], className="flex items-center")
                                ], className="text-center")
                            ], className="grid grid-cols-3 gap-4")
                        ])
                    ], className="bg-white p-6 rounded-lg shadow-sm col-span-2")
                ], className="grid grid-cols-4 gap-6 mb-6"),
                
                # Bottom row - Monthly Sales chart
                html.Div([
                    html.Div([
                        html.Div([
                            html.H3("Monthly Sales", className="text-lg font-semibold text-gray-900"),
                            html.I(className="ri-more-2-line text-gray-400 cursor-pointer")
                        ], className="flex items-center justify-between mb-6"),
                        
                        dcc.Graph(
                            figure=create_monthly_sales_chart(),
                            config={'displayModeBar': False}
                        )
                    ], className="bg-white p-6 rounded-lg shadow-sm")
                ], className="grid grid-cols-1")
            ], className="p-6")
        ], className="ml-72 bg-gray-50 min-h-screen transition-all duration-300 ease-in-out", id="main-content")
    ])
], className="bg-gray-50")

# Callback for sidebar toggle
@callback(
    [Output('sidebar', 'className'),
     Output('main-content', 'className'),
     Output('logo-text', 'style'),
     Output('menu-label', 'style'),
     Output('support-label', 'style'),
     Output('dashboard-text', 'style'),
     Output('dashboard-arrow', 'style'),
     Output('calendar-text', 'style'),
     Output('profile-text', 'style'),
     Output('task-text', 'style'),
     Output('task-arrow', 'style'),
     Output('forms-text', 'style'),
     Output('forms-arrow', 'style'),
     Output('tables-text', 'style'),
     Output('tables-arrow', 'style'),
     Output('pages-text', 'style'),
     Output('pages-arrow', 'style'),
     Output('chat-text', 'style'),
     Output('sidebar-state', 'data')],
    [Input('toggle-sidebar', 'n_clicks')],
    [State('sidebar-state', 'data')]
)
def toggle_sidebar(n_clicks, state):
    if n_clicks is None:
        n_clicks = 0
    
    # Toggle collapsed state
    collapsed = not state.get('collapsed', False) if n_clicks > 0 else state.get('collapsed', False)
    
    if collapsed:
        # Collapsed state - show only icons
        sidebar_class = "w-20 bg-white shadow-lg h-screen fixed left-0 top-0 p-4 transition-all duration-300 ease-in-out z-20"
        main_content_class = "ml-20 bg-gray-50 min-h-screen transition-all duration-300 ease-in-out"
        hidden_style = {'display': 'none'}
    else:
        # Expanded state - show full sidebar
        sidebar_class = "w-72 bg-white shadow-lg h-screen fixed left-0 top-0 p-4 transition-all duration-300 ease-in-out z-20"
        main_content_class = "ml-72 bg-gray-50 min-h-screen transition-all duration-300 ease-in-out"
        hidden_style = {'display': 'block'}
    
    return (
        sidebar_class,
        main_content_class,
        hidden_style,  # logo-text
        hidden_style,  # menu-label
        hidden_style,  # support-label
        hidden_style,  # dashboard-text
        hidden_style,  # dashboard-arrow
        hidden_style,  # calendar-text
        hidden_style,  # profile-text
        hidden_style,  # task-text
        hidden_style,  # task-arrow
        hidden_style,  # forms-text
        hidden_style,  # forms-arrow
        hidden_style,  # tables-text
        hidden_style,  # tables-arrow
        hidden_style,  # pages-text
        hidden_style,  # pages-arrow
        hidden_style,  # chat-text
        {'collapsed': collapsed}
    )

if __name__ == '__main__':
    app.run(debug=True)