import streamlit as st
from app.query_engine import DataQueryEngine
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Data Query Bot", page_icon="🤖", layout="wide")
st.title("🤖 Data Query Bot")
st.caption("Ask your database anything in plain English.")

if "history" not in st.session_state:
    st.session_state.history = []

engine = DataQueryEngine(db_path="data/orders.db")

with st.sidebar:
    st.header("Example questions")
    for ex in [
        "Top 5 cities by orders this month?",
        "Average delivery time in Bangalore?",
        "Restaurants with >10% cancellation rate?",
        "Daily GMV for last 7 days?",
    ]:
        if st.button(ex, use_container_width=True):
            st.session_state.query = ex

query = st.text_input("Your question", value=st.session_state.get("query",""),
    placeholder="e.g. Top restaurants by revenue last week?")

if st.button("Ask", type="primary") and query:
    with st.spinner("Thinking..."):
        result = engine.run(query)
    st.session_state.history.append({"q": query, "r": result})

for item in reversed(st.session_state.history):
    with st.expander(f"Q: {item['q']}", expanded=True):
        st.code(item["r"].get("sql",""), language="sql")
        if item["r"].get("data") is not None:
            st.dataframe(item["r"]["data"])
        st.markdown(f"**Explanation:** {item['r'].get('explanation','')}")
