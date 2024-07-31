import streamlit as st
import pandas as pd

# Title of the app
st.title("CSV/Excel File Viewer")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Handling CSV file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
        csv_string = df.to_csv(index=False)
        st.text_area("CSV Content", csv_string, height=300, disabled=True)

    # Handling Excel file
    elif uploaded_file.name.endswith('.xlsx'):
        xls = pd.ExcelFile(uploaded_file)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
            if not df.empty:
                st.subheader(sheet_name)
                csv_string = df.to_csv(index=False)
                st.text_area(f"CSV Content - {sheet_name}", csv_string, height=300, disabled=True)
