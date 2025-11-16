import plotly.express as px
from data_manager import load_data

def plot_pie_chart(year, month):
    df = load_data()
    df = df[(df["date"].dt.year == year) & (df["date"].dt.month == month)]
    if df.empty:
        return px.pie(title="No data")
    fig = px.pie(df, values="amount", names="category", 
                 title=f"Spending Breakdown - {year}-{month:02d}")
    return fig

def plot_trend():
    df = load_data()
    df["month"] = df["date"].dt.to_period("M").astype(str)
    monthly = df.groupby("month")["amount"].sum().reset_index()
    if monthly.empty:
        return px.line(title="No data")
    fig = px.line(monthly, x="month", y="amount", 
                  title="Monthly Spending Trend", markers=True)
    return fig
