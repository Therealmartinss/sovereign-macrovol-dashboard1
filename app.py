import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Page settings
st.set_page_config(page_title="Sovereign MacroVol Dashboard", layout="wide")

# Define colors
BACKGROUND_COLOR = "#000000"  # Black
GOLD_COLOR = "#FFD700"
NAVY_COLOR = "#001F3F"
TEXT_COLOR = "#FFD700"

# Custom CSS styling
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
        }}
        .block-container {{
            padding-top: 2rem;
        }}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown(f"<h1 style='color:{GOLD_COLOR};'>🧭 Sovereign MacroVol Dashboard</h1>", unsafe_allow_html=True)
st.markdown(f"<h4 style='color:{TEXT_COLOR};'>Real-Time Intelligence for Nasdaq & S&P Futures</h4>", unsafe_allow_html=True)

# Function to fetch and plot data
def plot_asset(symbol, title):
    data = yf.download(symbol, period="1mo", interval="1d")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data["Close"], mode='lines', line=dict(color=GOLD_COLOR)))
    fig.update_layout(title=title, template="plotly_dark", plot_bgcolor=BACKGROUND_COLOR, paper_bgcolor=BACKGROUND_COLOR,
                      font=dict(color=TEXT_COLOR))
    return fig

# Display charts
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(plot_asset("^VIX", "Volatility Index (VIX)"), use_container_width=True)
    st.plotly_chart(plot_asset("^VXN", "Nasdaq Volatility Index (VXN)"), use_container_width=True)

with col2:
    st.plotly_chart(plot_asset("DX-Y.NYB", "US Dollar Index (DXY)"), use_container_width=True)
    st.plotly_chart(plot_asset("ES=F", "S&P 500 Futures (ES)"), use_container_width=True)

# Sovereign quote section
st.markdown("---")
st.markdown(f"<h3 style='color:{GOLD_COLOR};'>🕊 Sovereign Signal of the Day</h3>", unsafe_allow_html=True)
st.markdown(f"<p style='color:{TEXT_COLOR}; font-size:18px;'>“True wealth is not measured by accumulation, but by alignment — with purpose, with principle, with the pulse of divine timing.”</p>", unsafe_allow_html=True)

# Coming soon section
st.markdown("---")
st.markdown(f"<p style='color:{NAVY_COLOR}; font-size:16px;'>More features coming soon: Gamma Exposure, Dealer Flow, Macro Calendar, and AI Volatility Forecasts.</p>", unsafe_allow_html=True)
