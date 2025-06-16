import dash
from dash import html, dcc
import pandas as pd

# Sample data for the authors table
authors_data = [
    {
        'author': 'John Michael',
        'email': 'john@creative-tim.com',
        'function': 'Manager',
        'department': 'Organization',
        'status': 'ONLINE',
        'employed': '23/04/18'
    },
    {
        'author': 'Alexa Liras',
        'email': 'alexa@creative-tim.com',
        'function': 'Programator',
        'department': 'Developer',
        'status': 'OFFLINE',
        'employed': '11/01/19'
    },
    {
        'author': 'Laurent Perrier',
        'email': 'laurent@creative-tim.com',
        'function': 'Executive',
        'department': 'Projects',
        'status': 'ONLINE',
        'employed': '19/09/17'
    },
    {
        'author': 'Michael Levi',
        'email': 'michael@creative-tim.com',
        'function': 'Programator',
        'department': 'Developer',
        'status': 'ONLINE',
        'employed': '24/12/08'
    },
    {
        'author': 'Richard Gran',
        'email': 'richard@creative-tim.com',
        'function': 'Manager',
        'department': 'Executive',
        'status': 'OFFLINE',
        'employed': '04/10/21'
    },
    {
        'author': 'Miriam Eric',
        'email': 'miriam@creative-tim.com',
        'function': 'Programator',
        'department': 'Developer',
        'status': 'OFFLINE',
        'employed': '14/09/20'
    }
]

# Initialize the Dash app
app = dash.Dash(__name__)

# Custom CSS for Tailwind-like styling and fixed background
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css" rel="stylesheet">
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            }
            
            .fixed-bg {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                z-index: -1;
            }
            
            .sidebar {
                position: fixed;
                left: 0;
                top: 0;
                bottom: 0;
                width: 280px;
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                z-index: 10;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            }
            
            .main-content {
                margin-left: 280px;
                padding: 2rem;
                z-index: 5;
                position: relative;
                min-height: 100vh;
            }
            
            .card {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                border-radius: 12px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
                z-index: 8;
                position: relative;
            }
            
            .nav-item {
                transition: all 0.3s ease;
                margin: 0.25rem 1rem;
                border-radius: 0.5rem;
            }
            
            .nav-item:hover {
                background: rgba(99, 102, 241, 0.1);
                transform: translateX(5px);
            }
            
            .nav-item.active {
                background: linear-gradient(90deg, #ff6b6b, #ee5a24);
                color: white;
                box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4);
            }
            
            .nav-item.active i {
                color: white;
            }
            
            .status-online {
                background: linear-gradient(90deg, #00d2ff, #3a7bd5);
                color: white;
                font-weight: 600;
                text-transform: uppercase;
                font-size: 0.75rem;
                padding: 4px 12px;
                border-radius: 20px;
                letter-spacing: 0.5px;
            }
            
            .status-offline {
                background: linear-gradient(90deg, #a8a8a8, #8e8e93);
                color: white;
                font-weight: 600;
                text-transform: uppercase;
                font-size: 0.75rem;
                padding: 4px 12px;
                border-radius: 20px;
                letter-spacing: 0.5px;
            }
            
            .avatar {
                width: 40px;
                height: 40px;
                border-radius: 50%;
                background: linear-gradient(135deg, #667eea, #764ba2);
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-weight: bold;
                font-size: 14px;
            }
            
            .table-header {
                color: #8492a6;
                font-weight: 600;
                font-size: 0.75rem;
                text-transform: uppercase;
                letter-spacing: 1px;
                padding: 1rem;
                border-bottom: 1px solid #e2e8f0;
            }
            
            .breadcrumb {
                color: rgba(255, 255, 255, 0.8);
                font-size: 0.875rem;
                margin-bottom: 0.5rem;
            }
            
            .page-title {
                color: white;
                font-size: 1.5rem;
                font-weight: 600;
                margin-bottom: 2rem;
            }
            
            .help-section {
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                border-top: 1px solid #e2e8f0;
                background: rgba(255, 255, 255, 0.95);
            }
            
            .logo-icon {
                width: 2rem;
                height: 2rem;
                background: linear-gradient(135deg, #667eea, #764ba2);
                border-radius: 0.5rem;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-right: 0.75rem;
            }
        </style>
    </head>
    <body>
        <div class="fixed-bg"></div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

def make_avatar(name):
    initials = ''.join([word[0] for word in name.split()[:2]]).upper()
    return html.Div(initials, className="avatar")

def make_status_badge(status):
    if status == 'ONLINE':
        return html.Span(status, className="status-online")
    else:
        return html.Span(status, className="status-offline")

# Layout
app.layout = html.Div([
    # Fixed Background
    html.Div(className="fixed-bg"),
    
    # Sidebar
    html.Div([
        # Logo section
        html.Div([
            html.Div([
                html.Div([
                    html.I(className="ri-dashboard-3-line text-white text-xl")
                ], className="logo-icon"),
                html.Span("Argon Dashboard 2", className="text-xl font-semibold text-gray-800")
            ], className="flex items-center p-6 border-b border-gray-200")
        ]),
        
        # Navigation
        html.Div([
            html.Div([
                html.I(className="ri-dashboard-line text-xl mr-3 text-gray-600"),
                html.Span("Dashboard", className="font-medium")
            ], className="nav-item flex items-center p-4 cursor-pointer text-gray-700"),
            
            html.Div([
                html.I(className="ri-table-line text-xl mr-3"),
                html.Span("Tables", className="font-medium")
            ], className="nav-item active flex items-center p-4 cursor-pointer"),
            
            html.Div([
                html.I(className="ri-bill-line text-xl mr-3 text-gray-600"),
                html.Span("Billing", className="font-medium")
            ], className="nav-item flex items-center p-4 cursor-pointer text-gray-700"),
            
            html.Div([
                html.I(className="ri-vr-box-line text-xl mr-3 text-gray-600"),
                html.Span("Virtual Reality", className="font-medium")
            ], className="nav-item flex items-center p-4 cursor-pointer text-gray-700"),
        ], className="py-4"),
        
        # Help section
        html.Div([
            html.Div([
                html.I(className="ri-folder-2-line text-6xl mb-4 opacity-50 text-gray-400"),
                html.H3("Need help?", className="text-lg font-semibold text-gray-800 mb-2"),
                html.P("Please check our docs", className="text-sm text-gray-600 mb-4"),
                html.Button("Documentation", className="w-full bg-gray-800 text-white py-2 px-4 rounded-lg font-medium mb-2 hover:bg-gray-700 transition-colors"),
                html.Button("Upgrade to pro", className="w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white py-2 px-4 rounded-lg font-medium hover:from-blue-600 hover:to-purple-700 transition-all")
            ], className="text-center p-6")
        ], className="help-section")
        
    ], className="sidebar"),
    
    # Main content
    html.Div([
        # Header
        html.Div([
            html.Div([
                html.Div("Pages / Tables", className="breadcrumb"),
                html.H1("Tables", className="page-title")
            ]),
            
            # Search and Sign In
            html.Div([
                html.Div([
                    dcc.Input(
                        placeholder="Type here...",
                        className="px-4 py-2 rounded-lg border-0 focus:outline-none focus:ring-2 focus:ring-blue-500",
                        style={
                            'background': 'rgba(255, 255, 255, 0.9)',
                            'backdropFilter': 'blur(10px)'
                        }
                    )
                ], className="mr-4"),
                html.Button("Sign In", 
                    className="px-6 py-2 rounded-lg font-medium transition-colors",
                    style={
                        'background': 'rgba(255, 255, 255, 0.9)',
                        'backdropFilter': 'blur(10px)',
                        'color': '#374151'
                    }
                )
            ], className="flex items-center")
        ], className="flex justify-between items-start mb-8"),
        
        # Authors table card
        html.Div([
            html.Div([
                html.H2("Authors table", className="text-xl font-semibold text-gray-800 p-6 pb-0")
            ]),
            
            # Table
            html.Div([
                # Table headers
                html.Div([
                    html.Div("AUTHOR", className="table-header flex-1"),
                    html.Div("FUNCTION", className="table-header flex-1"),
                    html.Div("STATUS", className="table-header w-32"),
                    html.Div("EMPLOYED", className="table-header w-32"),
                    html.Div("", className="table-header w-20")
                ], className="flex"),
                
                # Table rows
                html.Div([
                    html.Div([
                        # Author column
                        html.Div([
                            make_avatar(row['author']),
                            html.Div([
                                html.Div(row['author'], className="font-semibold text-gray-800"),
                                html.Div(row['email'], className="text-sm text-gray-500")
                            ], className="ml-3")
                        ], className="flex items-center flex-1 p-4"),
                        
                        # Function column
                        html.Div([
                            html.Div(row['function'], className="font-semibold text-gray-800"),
                            html.Div(row['department'], className="text-sm text-gray-500")
                        ], className="flex-1 p-4"),
                        
                        # Status column
                        html.Div([
                            make_status_badge(row['status'])
                        ], className="w-32 p-4"),
                        
                        # Employed column
                        html.Div([
                            html.Div(row['employed'], className="text-sm text-gray-600")
                        ], className="w-32 p-4"),
                        
                        # Edit column
                        html.Div([
                            html.Button("Edit", className="text-blue-600 hover:text-blue-800 font-medium text-sm")
                        ], className="w-20 p-4")
                        
                    ], className="flex items-center border-b border-gray-100 hover:bg-gray-50 transition-colors") 
                    for row in authors_data
                ])
            ])
        ], className="card")
        
    ], className="main-content")
])

if __name__ == '__main__':
    app.run(debug=True)