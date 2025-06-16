import dash
from dash import html, dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=["https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css", 'https://cdn.jsdelivr.net/npm/remixicon@4.2.0/fonts/remixicon.css'])

# Sample Data for Charts (replace with your actual data)
# Revenue Trend Data
revenue_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Revenue': [2.0, 2.2, 2.5, 2.3, 2.8, 2.7],
    'Target': [2.1, 2.3, 2.4, 2.5, 2.6, 2.8]
}
df_revenue = pd.DataFrame(revenue_data)

# Sales by Region Data
region_data = {
    'Region': ['North', 'South', 'East', 'West'],
    'Sales': [350, 280, 400, 254]
}
df_region = pd.DataFrame(region_data)

# Top Products Data
product_data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'Revenue': [300000, 250000, 180000, 120000, 90000]
}
df_product = pd.DataFrame(product_data)

# Create Plotly Figures
fig_revenue = go.Figure()
fig_revenue.add_trace(go.Scatter(x=df_revenue['Month'], y=df_revenue['Revenue'], mode='lines+markers', name='Actual Revenue',
                                 line=dict(color='#3B82F6')))
fig_revenue.add_trace(go.Scatter(x=df_revenue['Month'], y=df_revenue['Target'], mode='lines', name='Target Revenue',
                                 line=dict(color='#9CA3AF', dash='dash')))
fig_revenue.update_layout(
    margin=dict(l=20, r=20, t=40, b=20),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font_color='#333',
    xaxis=dict(showgrid=False, title=''),
    yaxis=dict(title='Revenue ($M)', gridcolor='#E5E7EB'),
    legend=dict(x=0.01, y=0.99, bordercolor='#E5E7EB', borderwidth=1),
    hovermode='x unified'
)

fig_region = px.bar(df_region, x='Region', y='Sales', text='Sales',
                    color_discrete_sequence=['#3B82F6'])
fig_region.update_traces(texttemplate='%{text}', textposition='outside')
fig_region.update_layout(
    margin=dict(l=20, r=20, t=40, b=20),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font_color='#333',
    xaxis=dict(title=''),
    yaxis=dict(title='Sales Units', showgrid=True, gridcolor='#E5E7EB'),
)

fig_product = px.pie(df_product, values='Revenue', names='Product',
                     color_discrete_sequence=px.colors.sequential.RdBu)
fig_product.update_traces(textposition='inside', textinfo='percent+label',
                          marker=dict(line=dict(color='#000000', width=1)))
fig_product.update_layout(
    margin=dict(l=20, r=20, t=40, b=20),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font_color='#333',
    showlegend=True,
    legend=dict(x=0.01, y=0.99)
)

# App layout
app.layout = html.Div(
    className="min-h-screen p-6 bg-gray-50",
    children=[
        html.Div(
            className="max-w-7xl mx-auto",
            children=[
                # Header
                html.Div(
                    className="mb-8",
                    children=[
                        html.H1("Sales Dashboard", className="text-3xl font-bold text-gray-900 mb-2"),
                        html.P("Track your sales performance and key metrics", className="text-gray-600"),
                    ],
                ),

                # Overview Cards
                html.Div(
                    className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
                    children=[
                        # Total Revenue Card
                        html.Div(
                            className="bg-white shadow-sm border-0 hover:shadow-md transition-shadow rounded-lg",
                            children=[
                                html.Div(
                                    className="flex flex-row items-center justify-between space-y-0 pb-2 p-6",
                                    children=[
                                        html.H3("Total Revenue", className="text-sm font-medium text-gray-600"),
                                        html.I(className="ri-currency-line text-blue-600 text-lg"), # Remixicon
                                    ],
                                ),
                                html.Div(
                                    className="p-6 pt-0",
                                    children=[
                                        html.Div("$2,847,392", className="text-2xl font-bold text-gray-900 mb-1"),
                                        html.P(
                                            className="text-xs flex items-center text-green-600",
                                            children=[
                                                "+12.5%",
                                                html.Span("from last month", className="text-gray-500 ml-1"),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),

                        # Total Sales Card
                        html.Div(
                            className="bg-white shadow-sm border-0 hover:shadow-md transition-shadow rounded-lg",
                            children=[
                                html.Div(
                                    className="flex flex-row items-center justify-between space-y-0 pb-2 p-6",
                                    children=[
                                        html.H3("Total Sales", className="text-sm font-medium text-gray-600"),
                                        html.I(className="ri-line-chart-line text-blue-600 text-lg"), # Remixicon
                                    ],
                                ),
                                html.Div(
                                    className="p-6 pt-0",
                                    children=[
                                        html.Div("1,284", className="text-2xl font-bold text-gray-900 mb-1"),
                                        html.P(
                                            className="text-xs flex items-center text-green-600",
                                            children=[
                                                "+8.2%",
                                                html.Span("from last month", className="text-gray-500 ml-1"),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),

                        # Active Customers Card
                        html.Div(
                            className="bg-white shadow-sm border-0 hover:shadow-md transition-shadow rounded-lg",
                            children=[
                                html.Div(
                                    className="flex flex-row items-center justify-between space-y-0 pb-2 p-6",
                                    children=[
                                        html.H3("Active Customers", className="text-sm font-medium text-gray-600"),
                                        html.I(className="ri-group-line text-blue-600 text-lg"), # Remixicon
                                    ],
                                ),
                                html.Div(
                                    className="p-6 pt-0",
                                    children=[
                                        html.Div("892", className="text-2xl font-bold text-gray-900 mb-1"),
                                        html.P(
                                            className="text-xs flex items-center text-green-600",
                                            children=[
                                                "+5.7%",
                                                html.Span("from last month", className="text-gray-500 ml-1"),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),

                        # Conversion Rate Card
                        html.Div(
                            className="bg-white shadow-sm border-0 hover:shadow-md transition-shadow rounded-lg",
                            children=[
                                html.Div(
                                    className="flex flex-row items-center justify-between space-y-0 pb-2 p-6",
                                    children=[
                                        html.H3("Conversion Rate", className="text-sm font-medium text-gray-600"),
                                        html.I(className="ri-check-double-line text-blue-600 text-lg"), # Remixicon
                                    ],
                                ),
                                html.Div(
                                    className="p-6 pt-0",
                                    children=[
                                        html.Div("4.8%", className="text-2xl font-bold text-gray-900 mb-1"),
                                        html.P(
                                            className="text-xs flex items-center text-red-600",
                                            children=[
                                                "-0.3%",
                                                html.Span("from last month", className="text-gray-500 ml-1"),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),

                # Charts Grid
                html.Div(
                    className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8",
                    children=[
                        # Revenue Chart
                        html.Div(
                            className="bg-white shadow-sm border-0 rounded-lg",
                            children=[
                                html.Div(
                                    className="p-6",
                                    children=[
                                        html.H3("Revenue Trend", className="text-lg font-semibold text-gray-900"),
                                        html.P("Monthly revenue vs target", className="text-sm text-gray-600"),
                                    ],
                                ),
                                html.Div(
                                    className="p-6 pt-0",
                                    children=[
                                        dcc.Graph(figure=fig_revenue, config={'displayModeBar': False})
                                    ],
                                ),
                            ],
                        ),

                        # Sales by Region
                        html.Div(
                            className="bg-white shadow-sm border-0 rounded-lg",
                            children=[
                                html.Div(
                                    className="p-6",
                                    children=[
                                        html.H3("Sales by Region", className="text-lg font-semibold text-gray-900"),
                                        html.P("Regional performance comparison", className="text-sm text-gray-600"),
                                    ],
                                ),
                                html.Div(
                                    className="p-6 pt-0",
                                    children=[
                                        dcc.Graph(figure=fig_region, config={'displayModeBar': False})
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),

                # Bottom Grid
                html.Div(
                    className="grid grid-cols-1 lg:grid-cols-2 gap-6",
                    children=[
                        # Top Products
                        html.Div(
                            className="bg-white shadow-sm border-0 rounded-lg",
                            children=[
                                html.Div(
                                    className="p-6",
                                    children=[
                                        html.H3("Top Products", className="text-lg font-semibold text-gray-900"),
                                        html.P("Revenue by product category", className="text-sm text-gray-600"),
                                    ],
                                ),
                                html.Div(
                                    className="p-6 pt-0",
                                    children=[
                                        dcc.Graph(figure=fig_product, config={'displayModeBar': False})
                                    ],
                                ),
                            ],
                        ),

                        # Recent Deals
                        html.Div(
                            className="bg-white shadow-sm border-0 rounded-lg",
                            children=[
                                html.Div(
                                    className="p-6",
                                    children=[
                                        html.H3("Recent Deals", className="text-lg font-semibold text-gray-900"),
                                        html.P("Latest sales opportunities", className="text-sm text-gray-600"),
                                    ],
                                ),
                                html.Div(
                                    className="p-6 pt-0",
                                    children=[
                                        html.Div(
                                            className="space-y-4",
                                            children=[
                                                # Deal 1
                                                html.Div(
                                                    className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors",
                                                    children=[
                                                        html.Div(
                                                            className="flex-1",
                                                            children=[
                                                                html.Div(
                                                                    className="flex items-center justify-between mb-1",
                                                                    children=[
                                                                        html.H4("Acme Corporation", className="font-medium text-gray-900"),
                                                                        html.Span("$125,000", className="font-semibold text-gray-900"),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="flex items-center justify-between",
                                                                    children=[
                                                                        html.P("Enterprise Software", className="text-sm text-gray-600"),
                                                                        html.Div(
                                                                            className="flex items-center space-x-2",
                                                                            children=[
                                                                                html.Span("closed", className="px-2 py-1 text-xs rounded bg-green-100 text-green-800"),
                                                                                html.Span("2024-06-12", className="text-xs text-gray-500"),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                # Deal 2
                                                html.Div(
                                                    className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors",
                                                    children=[
                                                        html.Div(
                                                            className="flex-1",
                                                            children=[
                                                                html.Div(
                                                                    className="flex items-center justify-between mb-1",
                                                                    children=[
                                                                        html.H4("TechStart Inc.", className="font-medium text-gray-900"),
                                                                        html.Span("$85,000", className="font-semibold text-gray-900"),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="flex items-center justify-between",
                                                                    children=[
                                                                        html.P("Cloud Services", className="text-sm text-gray-600"),
                                                                        html.Div(
                                                                            className="flex items-center space-x-2",
                                                                            children=[
                                                                                html.Span("negotiation", className="px-2 py-1 text-xs rounded bg-yellow-100 text-yellow-800"),
                                                                                html.Span("2024-06-11", className="text-xs text-gray-500"),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                # Deal 3
                                                html.Div(
                                                    className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors",
                                                    children=[
                                                        html.Div(
                                                            className="flex-1",
                                                            children=[
                                                                html.Div(
                                                                    className="flex items-center justify-between mb-1",
                                                                    children=[
                                                                        html.H4("Global Dynamics", className="font-medium text-gray-900"),
                                                                        html.Span("$195,000", className="font-semibold text-gray-900"),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="flex items-center justify-between",
                                                                    children=[
                                                                        html.P("Consulting", className="text-sm text-gray-600"),
                                                                        html.Div(
                                                                            className="flex items-center space-x-2",
                                                                            children=[
                                                                                html.Span("proposal", className="px-2 py-1 text-xs rounded bg-blue-100 text-blue-800"),
                                                                                html.Span("2024-06-10", className="text-xs text-gray-500"),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                # Deal 4
                                                html.Div(
                                                    className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors",
                                                    children=[
                                                        html.Div(
                                                            className="flex-1",
                                                            children=[
                                                                html.Div(
                                                                    className="flex items-center justify-between mb-1",
                                                                    children=[
                                                                        html.H4("Innovation Labs", className="font-medium text-gray-900"),
                                                                        html.Span("$67,000", className="font-semibold text-gray-900"),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="flex items-center justify-between",
                                                                    children=[
                                                                        html.P("Training", className="text-sm text-gray-600"),
                                                                        html.Div(
                                                                            className="flex items-center space-x-2",
                                                                            children=[
                                                                                html.Span("closed", className="px-2 py-1 text-xs rounded bg-green-100 text-green-800"),
                                                                                html.Span("2024-06-09", className="text-xs text-gray-500"),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                # Deal 5
                                                html.Div(
                                                    className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors",
                                                    children=[
                                                        html.Div(
                                                            className="flex-1",
                                                            children=[
                                                                html.Div(
                                                                    className="flex items-center justify-between mb-1",
                                                                    children=[
                                                                        html.H4("Future Systems", className="font-medium text-gray-900"),
                                                                        html.Span("$148,000", className="font-semibold text-gray-900"),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="flex items-center justify-between",
                                                                    children=[
                                                                        html.P("Enterprise Software", className="text-sm text-gray-600"),
                                                                        html.Div(
                                                                            className="flex items-center space-x-2",
                                                                            children=[
                                                                                html.Span("qualified", className="px-2 py-1 text-xs rounded bg-purple-100 text-purple-800"),
                                                                                html.Span("2024-06-08", className="text-xs text-gray-500"),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)