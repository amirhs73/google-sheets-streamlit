import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Define a function to load data from Google Sheets
def load_data():
    # Configure Google Sheets API with Streamlit secrets
    creds = Credentials.from_service_account_info({
        "type": st.secrets["service_account"],
        "project_id": st.secrets["sales-collateral"],
        "private_key_id": st.secrets["56a4619299d651d5ad749909ffa0951c54e210c9"],
        "private_key": st.secrets["-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCgvC0Fcp9KHflQ\nEdel8QPR/hm0rzo6Z/Y0OCzd4wyXWPIeCim0xOB6dKH4PYVy3Wuyj3r8mALNVhAt\nQ14wV/JIhXgll8qv+tzh/zoNl1Uu8wwfP4nP9qo0dYqjnRf4NRwF4e5bTHtp5ZJH\nVm2/QkRxNhEq19hb+cFAlvi3gPa8RHtsn3dnA13ou0sHClJMiooV3NOgyYROqyHt\nD3Vs09VzPt3MC8Od2oeOp4xTYYVlbGk8GNg2AC0tYdmf/xWNaMy+wnOAxATTP5j7\n13yYnK+MvrRiMWATk/M1RJpau6BCVsIVB2E25hCSGX2kQ5AiB3QuU8SalE7rxTwX\n+h5+QO69AgMBAAECggEAB2MenpV6BKoD/04SnynIhyoqfEdhYbXNdvDt/vSka4BH\nAGJvMEOsHXSmzQXm0DSk8nvtpxZFarJ949aoyYgBNpwLvY6QXi4lYK2eOWmvHI1H\nDViaONiZUffk+0gJBftK4mpTzhZhxagrZOPv/05IXvuhJlrtMqzz2MgXfjeLH3Pj\noYznGQojudE/6w9/rv7WqATvwbLvsIqQm2qcXXqdRnEpPq/hzpNCmvme8gaDKwZF\nAcK8uwIg5tf2nRdZ1/13aICKaRsjtyK18J2sVDj4vyATSSQVy9F4VetGLGrR1Pv4\ncpVaLE6/e95oJ8Jn8SAh97IPYiXnkrL+htMNjdrxgQKBgQDP1hIaR0RXvQ5jLLYl\nm6xmTXerLXTTUfpH+JSTEY4z/JDE+Zo/apTszZAQD9kpIUD4uc0E07IDaOO2SoS2\n4CoqdmL3l4ITT8W42yy1b972IThNYLZo3/+4x+dGnqZuRCbDlRJrIs1mmQxQh8Q7\n+VnI2HpGzKr3WgpfPl4eDPhnRQKBgQDF+9GksX1YG50ej+yW4/1G5arfIdkpuNgw\n0d6D1hbR/XFEsQe+IHuPWFxWN4J6u7fYicwfusue+cuHMks0PG6fDj3rSFGDKzd9\nQKhRXgGi+TldCw2VoycVbAmvjcMSDVVE/0tADTf1kITYRhiuobPdqoAoHQQNvmNi\npR6E9HiFGQKBgQCa9IIesY/U0pHNg2Jye7R3ub5FE+kMPQybaExtsiMRw3a0RVyp\nd299dm24a/h+39ovF2gx9xu7yxIrsTdtmYgWjJmQ+5bxiwJhppeY1sWnQHFXz4lw\ne8GPJQvb7SEtCQbVv2kyE4qMugMib3bxOCGmyy+vZZz6OlmNVVSalxUE+QKBgQCX\nXthDvjxicAJqCopON5Q/b3t8TEnYH26TrPIfBEHAXbELXvrXf8hYqas3dAt7wSho\nE7sQi2YBb2UQQgDDuGyviVkIGevQiOtNBXFrfJ9ttnUIUVoajXplY4voQE/j7nPC\nZBppp3Gge9VF8hoO8q0tjp2bjcu6olUkZ7B04OGAiQKBgBGqb7B0bV/1rDjBqEt6\n7N+3WtgpUTpCajNEtUt46Naz4EB48n2SctyOuFC+s/AbejzHUlz+fjCmU2Gj77FA\n9/XwvDmYHTvshFA1GisXDxAIQwfCBaK4SXWmux3okHMPVbpPjGzqbtcaVF4X5e+E\nuIJ9mrlXEcQD6WDzRVsagWPj\n-----END PRIVATE KEY-----\n"],
        "client_email": st.secrets["ubiweb@sales-collateral.iam.gserviceaccount.com"],
        "client_id": st.secrets["100395982034621045137"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": st.secrets["https://oauth2.googleapis.com/token"],
        "auth_provider_x509_cert_url": st.secrets["https://www.googleapis.com/oauth2/v1/certs"],
        "client_x509_cert_url": st.secrets["https://www.googleapis.com/robot/v1/metadata/x509/ubiweb%40sales-collateral.iam.gserviceaccount.com"]
    })
    client = gspread.authorize(creds)
    sheet = client.open("PPC Sales Collateral").sheet1  # Replace with your sheet name
    return pd.DataFrame(sheet.get_all_records())


# Load data and perform analysis
st.title("Google Sheets Data Analysis App")
data = load_data()
st.write("Data from Google Sheets:")
st.write(data)

# Perform analysis or add interactive elements here
st.write("Summary Statistics:")
st.write(data.describe())
