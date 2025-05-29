
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Dashboard config
st.set_page_config(page_title="Sovereign MacroVol Dashboard", layout="wide")

# Theme colors
BACKGROUND_COLOR = "#000000"
GOLD_COLOR = "#FFD700"
NAVY_COLOR = "#001F3F"
TEXT_COLOR = "#FFD700"

# Custom style
st.markdown("""
    <style>
        .stApp {
            background-color: #000000;
            color: #FFD700;
        }
        .block-container {
            padding-top: 2rem;
        }
        h1, h4 {
            font-family: 'Georgia', serif;
            text-align: center;
        }
        p {
            font-family: 'Arial', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='color:#FFD700;'>Sovereign MacroVol Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color:#FFD700;'>Global Trading Intelligence for Nasdaq & S&P Futures</h4>", unsafe_allow_html=True)

# Chart plotting function
def plot_asset(symbol, title):
    data = yf.download(symbol, period="1mo", interval="1d")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data["Close"], mode='lines', line=dict(color="#FFD700")))
    fig.update_layout(
        title=title,
        template="plotly_dark",
        plot_bgcolor="#000000",
        paper_bgcolor="#000000",
        font=dict(color="#FFD700", family="Arial"),
        margin=dict(t=40, b=20, l=20, r=20),
        hovermode="x unified"
    )
    return fig

# Layout
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(plot_asset("^VIX", "Volatility Index (VIX)"), use_container_width=True)
    st.plotly_chart(plot_asset("^VXN", "Nasdaq Volatility Index (VXN)"), use_container_width=True)

with col2:
    st.plotly_chart(plot_asset("DX-Y.NYB", "US Dollar Index (DXY)"), use_container_width=True)
    st.plotly_chart(plot_asset("ES=F", "S&P 500 Futures (ES)"), use_container_width=True)

# Quote section
st.markdown("""
<div style='border: 1px solid #FFD700; padding: 20px; border-radius: 10px; margin-bottom: 30px;'>
<h3 style='color:#FFD700;'>Sovereign Signal of the Day</h3>
<p style='color:#FFD700; font-size:18px;'>True wealth is not measured by accumulation, but by alignment - with purpose, with principle, with the pulse of divine timing.</p>
</div>
""", unsafe_allow_html=True)

# Coming soon section
st.markdown("""
<div style='border: 1px solid #001F3F; padding: 15px; border-radius: 10px;'>
<p style='color:#001F3F; font-size:16px;'>More features coming soon: Gamma Exposure, Dealer Flow, Macro Calendar, and AI Volatility Forecasts.</p>
</div>
""", unsafe_allow_html=True)
