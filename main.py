import streamlit as st
from src.calculators.clicks import calc_clicks_mrad
from src.calculators.mrad import calculate_mrad_approx
from src.converters.millimeter import Millimeters

st.title("Quickscope")

dist_to_target = st.slider("distance to target m", min_value=1, max_value=1000)
offset = st.slider(
    "point of impact offset from point of hold mm", min_value=1, max_value=100
)

mrad_per_click = st.slider("mrad per click", min_value=0.1, max_value=1.0, step=0.1)

st.write(f"distance to target m: {dist_to_target}")
st.write(f"point of impact offset from point of hold mm: {offset}")
st.write(f"mrad per click: {mrad_per_click}")

range_mm = Millimeters.from_meters(dist_to_target)
subtension_mm = Millimeters.from_millimeters(offset)
mrad_adjustment = calculate_mrad_approx(range_mm, subtension_mm)
clicks_adjustment = calc_clicks_mrad(mrad_adjustment, mrad_per_click)

st.markdown("""---""")

st.write(f"mrad adjustment : {mrad_adjustment}")
st.write(f"clicks : {clicks_adjustment}")
