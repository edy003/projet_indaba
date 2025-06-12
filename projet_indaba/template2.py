import dash
from dash import html, dcc
import plotly.graph_objects as go

# Initialize the Dash app
# We'll include the Tailwind CSS CDN and Font Awesome CDN as external stylesheets
app = dash.Dash(__name__, external_stylesheets=[
    "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" # Font Awesome 6
])

# --- Data for the dashboard (example) ---
monthly_revenue_data = {
    'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'revenue': [20000, 22000, 25000, 23000, 28000, 30000, 32000, 35000, 33000, 36000, 39000, 48352]
}

# Create a placeholder Plotly graph for Monthly Revenue
revenue_chart_figure = go.Figure(
    data=[
        go.Bar(
            x=monthly_revenue_data['months'],
            y=monthly_revenue_data['revenue'],
            marker_color='#4A90E2', # A blue color similar to the image
            name='Revenue'
        )
    ],
    layout=go.Layout(
        title={
            'text': 'Monthly Revenue',
            'x': 0.05, # Align title to left a bit
            'xanchor': 'left'
        },
        xaxis_title="",
        yaxis_title="",
        paper_bgcolor='rgba(0,0,0,0)', # Transparent background
        plot_bgcolor='rgba(0,0,0,0)', # Transparent background
        margin=dict(l=40, r=20, t=60, b=40), # Adjust margins
        showlegend=False,
        height=280 # Adjust height to fit card
    )
)


# --- Sidebar Component ---
sidebar = html.Div(
    className="w-64 h-screen fixed top-0 left-0 bg-white border-r border-gray-200 flex flex-col shadow-md",
    children=[
        html.Div(
            className="flex items-center p-4 border-b border-gray-200",
            children=[
                html.I(className="fas fa-cube text-purple-600 text-2xl mr-3"), # Example icon
                html.H2("Dashboard", className="text-xl font-semibold text-gray-800"),
            ]
        ),
        html.Nav(
            className="flex-grow flex flex-col p-4 space-y-2",
            children=[
                html.A(
                    href="/",
                    className="flex items-center p-2 rounded-md hover:bg-gray-100 text-gray-700 font-medium bg-gray-100 text-purple-600", # Active state
                    children=[
                        html.I(className="fas fa-home mr-3"),
                        "Overview"
                    ]
                ),
                html.A(
                    href="/analytics",
                    className="flex items-center p-2 rounded-md hover:bg-gray-100 text-gray-700 font-medium",
                    children=[
                        html.I(className="fas fa-chart-line mr-3"),
                        "Analytics"
                    ]
                ),
                html.A(
                    href="/users",
                    className="flex items-center p-2 rounded-md hover:bg-gray-100 text-gray-700 font-medium",
                    children=[
                        html.I(className="fas fa-users mr-3"),
                        "Users"
                    ]
                ),
                html.A(
                    href="/projects",
                    className="flex items-center p-2 rounded-md hover:bg-gray-100 text-gray-700 font-medium",
                    children=[
                        html.I(className="fas fa-folder mr-3"),
                        "Projects"
                    ]
                ),
                html.A(
                    href="/reports",
                    className="flex items-center p-2 rounded-md hover:bg-gray-100 text-gray-700 font-medium",
                    children=[
                        html.I(className="fas fa-file-alt mr-3"),
                        "Reports"
                    ]
                ),
                html.A(
                    href="/settings",
                    className="flex items-center p-2 rounded-md hover:bg-gray-100 text-gray-700 font-medium",
                    children=[
                        html.I(className="fas fa-cog mr-3"),
                        "Settings"
                    ]
                ),
            ]
        ),
        html.Div(
            className="flex items-center p-4 border-t border-gray-200 mt-auto",
            children=[
                html.Img(src="https://via.placeholder.com/40", className="rounded-full w-10 h-10 mr-3"),
                html.Div(
                    children=[
                        html.P("John Doe", className="text-sm font-semibold text-gray-800"),
                        html.P("john@example.com", className="text-xs text-gray-500"),
                    ]
                ),
            ]
        ),
    ]
)

# --- Header Component ---
header = html.Div(
    className="flex items-center justify-between p-6 border-b border-gray-200",
    children=[
        html.Div(
            children=[
                html.H4("Dashboard Overview", className="text-2xl font-semibold text-gray-800"),
                html.P("Welcome back! Here's what's happening today.", className="text-gray-500 text-sm mt-1"),
            ]
        ),
        html.Div(
            className="flex items-center space-x-3",
            children=[
                html.Button(
                    className="p-2 rounded-full hover:bg-gray-100 text-gray-600 focus:outline-none",
                    children=html.I(className="fas fa-sync-alt")
                ),
                html.Button(
                    className="relative p-2 rounded-full hover:bg-gray-100 text-gray-600 focus:outline-none",
                    children=[
                        html.I(className="fas fa-bell"),
                        # Optional: Notification dot
                        html.Span(className="absolute top-1 right-1 h-2 w-2 bg-red-500 rounded-full")
                    ]
                ),
                html.Button(
                    className="p-2 rounded-full hover:bg-gray-100 text-gray-600 focus:outline-none",
                    children=html.I(className="fas fa-user-circle text-2xl")
                ),
            ]
        ),
    ]
)

# --- KPI Card Component (reusable function) ---
def make_kpi_card(title, value, percentage, is_positive=True):
    color_class = "text-green-500" if is_positive else "text-red-500"
    bg_color = "bg-green-100" if is_positive else "bg-red-100"
    icon_class = "fas fa-arrow-up" if is_positive else "fas fa-arrow-down"

    return html.Div(
        className="bg-white p-6 rounded-lg shadow-md flex justify-between items-start relative overflow-hidden",
        children=[
            html.Div(
                children=[
                    html.P(title, className="text-gray-500 text-sm mb-1"),
                    html.H3(value, className="text-2xl font-bold text-gray-800 mb-2"),
                    html.P(
                        className="text-xs flex items-center",
                        children=[
                            html.Span(percentage, className=f"font-semibold {color_class} mr-1"),
                            html.Span(f"{'+' if is_positive else '-'}% from last month", className="text-gray-500"),
                        ]
                    ),
                ]
            ),
            html.Div(
                className="absolute top-3 right-3 text-3xl opacity-20", # Large, faded icon
                children=html.I(className="fas fa-chart-bar text-gray-400") # Generic icon for all
            )
        ]
    )

# --- KPI Cards Row ---
kpi_cards = html.Div(
    className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 p-6 pt-0", # p-6 for overall padding, pt-0 to negate top padding if header has it
    children=[
        make_kpi_card("Total Users", "12,482", "+12.5", True),
        make_kpi_card("Revenue", "$48,352", "+8.2", True),
        make_kpi_card("Active Projects", "24", "-3.1", False),
        make_kpi_card("Conversion Rate", "3.24%", "+0.8", True),
    ]
)

# --- Monthly Revenue Card ---
monthly_revenue_card = html.Div(
    className="bg-white p-6 rounded-lg shadow-md h-full flex flex-col",
    children=[
        html.H5("Monthly Revenue", className="text-lg font-semibold text-gray-800 mb-4"),
        dcc.Graph(
            id='monthly-revenue-chart',
            figure=revenue_chart_figure,
            config={'displayModeBar': False}, # Hide Plotly's default toolbar
            className="flex-grow"
        )
    ]
)

# --- Recent Activity Card ---
def make_activity_item(text, time, status_color="blue"):
    dot_class = {
        "blue": "bg-blue-500",
        "green": "bg-green-500",
        "orange": "bg-orange-500",
        "red": "bg-red-500",
        "purple": "bg-purple-500"
    }.get(status_color, "bg-gray-500") # Default to gray if unknown

    return html.Div(
        className="flex items-center py-2 border-b border-gray-100 last:border-b-0",
        children=[
            html.Span(className=f"w-2 h-2 rounded-full {dot_class} mr-3"),
            html.P(text, className="text-gray-700 text-sm flex-grow mb-0"),
            html.Span(time, className="text-gray-500 text-xs"),
        ]
    )

recent_activity_card = html.Div(
    className="bg-white p-6 rounded-lg shadow-md h-full",
    children=[
        html.H5("Recent Activity", className="text-lg font-semibold text-gray-800 mb-4"),
        html.Div(
            className="space-y-2", # Tailwind for vertical spacing between items
            children=[
                make_activity_item("New user registration", "2 minutes ago", "blue"),
                make_activity_item("Payment received from client", "15 minutes ago", "green"),
                make_activity_item("Server maintenance completed", "1 hour ago", "orange"),
                make_activity_item("Critical error resolved", "3 hours ago", "red"),
                make_activity_item("Database backup completed", "5 hours ago", "purple"),
                make_activity_item("Project deployment successful", "1 day ago", "green"),
            ]
        )
    ]
)

# --- Main Content Layout ---
main_content = html.Div(
    className="flex-1 ml-64", # ml-64 to push content right, matching sidebar width (64 * 4px = 256px, close enough to 280px)
    children=[
        header,
        kpi_cards,
        html.Div(
            className="grid grid-cols-1 lg:grid-cols-3 gap-6 p-6 pt-0", # lg:grid-cols-3 for 2/3 and 1/3 split
            children=[
                html.Div(className="lg:col-span-2", children=monthly_revenue_card), # 2/3 width
                html.Div(className="lg:col-span-1", children=recent_activity_card),  # 1/3 width
            ]
        ),
    ]
)

# --- App Layout ---
app.layout = html.Div(
    className="flex bg-gray-100 min-h-screen", # Overall flex container for sidebar + content
    children=[
        sidebar,
        main_content,
    ]
)

if __name__ == '__main__':
    app.run(debug=True)