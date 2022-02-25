import pandas as pd
from fbprophet import Prophet
import yfinance as yf
import streamlit as st
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
from yahooquery import Screener

st.set_page_config(layout="wide")
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<style>
.btn2 {
    background-color: #6f19fa;
    border-radius: 80px 0px 80px 0px;
    padding:10px 20px 10px;
    color: white;
    text-decoration:none;
  
  }
  .btn2:hover {
    background-color: transparent;
    border:2px solid #6f19fa;
    border-radius: 80px 0px 80px 0px;
    padding:10px 20px 10px;
    color: #6f19fa;
    text-decoration:none;
  }
  .space{
    margin-top:120px;
  }
  .space2{
    margin-top:50px;
  }


  .btn3 {
    background-color: transparent;
    border:2px solid #6f19fa;
    border-radius: 80px 0px 80px 0px;
    padding:10px 20px 10px;
    color: #6f19fa;
    text-decoration:none;
  }
  .btn3:hover {
    background-color: #6f19fa;
    border-radius: 80px 0px 80px 0px;
    padding:10px 20px 10px;
    color: white;
    text-decoration:none;
  
  }

  .card{
      border:0px;
      background: transparent;
  }
  .navbar-toggler-icon{
    color:#6f19fa;
  }

  .navbar-light .navbar-nav .nav-link {
    color: #6f19fa;
}
.navbar-light .navbar-nav .nav-link:hover {
  color: #6f19fa;
  text-decoration: underline;
  text-decoration: underline  2px #6f19fa;
  margin-bottom: 5px;
  text-underline-position: under;
}
.navbar-light .navbar-nav .nav-link.active, .navbar-light .navbar-nav .show>.nav-link {
  color: #6f19fa;
  text-decoration: underline;
  background-color: #6f19fa;
  border-radius: 0px 80px 0px 80px;
  padding:10px 30px 10px;
  color: white;
  text-decoration:none;
}
.navbar-light .navbar-nav .nav-link .active {
  color: #6f19fa;
  text-decoration: underline  2px #6f19fa;
  margin-bottom: 5px;
  text-underline-position: under;
}
.bitcoin{
  background-image: url(aave.png);
  background-size: 200px;
  background-repeat: no-repeat;
  opacity: 70%;
}
.purple{
  background-color: #6f19fa;
}
.btn4 {
  background-color: #6f19fa;
  border:2px solid #ffffff;
  border-radius: 100px;
  padding:10px 20px 10px;
  color: #ffffff;
  text-decoration:none;
  font-weight: 700;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" style="color: #6f19fa">
      <div class="container-fluid" style="color: #6f19fa">
        <img class="navbar-brand" src="https://img.icons8.com/ios/50/000000/bitcoin-exchange--v1.png" width="30px" alt="logo"/>
         <a class="navbar-brand fw-bold" href="#" style="color: #6f19fa">Crypto</a>
        <button fill="black" class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"><i class="fa fa-navicon" style="color: rgb(98, 0, 255); font-size: 28px"></i></span>
        </button>
        <div
          class="collapse navbar-collapse flex-grow-1 text-right"
          id="navbarSupportedContent"
        >
          <!-- <div class="d-flex flex-wrap justify-content-end"> -->
          <ul class="navbar-nav ms-auto flex-nowrap" style="color: #6f19fa">
            <li class="nav-item">
              <a class="nav-link " aria-current="page" href="index.html"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#features">Features</a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link active"
                href="https://share.streamlit.io/nandita-exe/crypto/app.py"
                >Predict Now</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="market.html">Trends</a>
            </li>
            <!-- <li class="nav-item">
              <a class="nav-link">About Us</a>
            </li> -->
            <li class="nav-item">
              <a class="nav-link" href="contact.html">Contact Us</a>
            </li>
          </ul>
        </div>
        <!-- </div> -->
      </div>
    </nav>
""", unsafe_allow_html=True)

today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=730)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2
# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.title("CRYPTOCURRENCY PREDICTION")

# df = pd.read_csv('BTC-USD.csv')
# df = pd.read_csv(data)
s = Screener()
data2 = s.get_screeners('all_cryptocurrencies_us', count=250)

# data is in the quotes key
dicts=data2['all_cryptocurrencies_us']['quotes']
symbols = [d['symbol'] for d in dicts]
# symbols
with st.form(key='my_form'):
  user_input=st.selectbox('Enter coin symbol: ', symbols, key=1)
  # user_input=st.text_input("Enter coin name: ", 'BTC-USD')
  coin_name=user_input.upper()
  # period=int(input('Enter number of days: '))
  period=st.slider(label='Enter number of days:', min_value=0, max_value=365, key=3)

  # period=st.number_input("Enter number of days", 10)
  submit_button = st.form_submit_button(label='Submit')
# if submit:
period=int(period)
data = yf.download(coin_name, 
                        start=start_date, 
                        end=end_date, 
                        progress=False)
data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
  # print(data.head())
df = data[["Date", "Close"]]
df.columns = ["ds", "y"]
  # print(df)
prophet = Prophet()
prophet.fit(df)
future = prophet.make_future_dataframe(periods=period)
  # print(future)

figure1 = go.Figure(data=[go.Candlestick(x=data["Date"],
                                          open=data["Open"], 
                                          high=data["High"],
                                          low=data["Low"], 
                                          close=data["Close"])])
figure1.update_layout(title = coin_name+" Price Analysis", 
                      xaxis_rangeslider_visible=True)
  # figure.show()
forecast = prophet.predict(future)
  # forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(30)
forecast1 = forecast[["ds","trend", "yhat", "yhat_lower", "yhat_upper"]].tail(period)

figure = go.Figure()
figure.add_trace(go.Scatter(x=forecast["ds"],y=forecast["yhat"],name='yhat'))
figure.add_trace(go.Scatter(x=forecast["ds"],y=forecast["yhat_lower"],name='yhat_lower'))
figure.add_trace(go.Scatter(x=forecast["ds"],y=forecast["yhat_upper"],name='yhat_upper'))
  # figure.add_trace(go.Scatter(x=forecast["ds"],y=forecast["trend"]))
figure.update_layout(title = coin_name+" Price Analysis and Prediction", 
                      xaxis_rangeslider_visible=True)

  # figure.show()

  # st.write(df.describe())
# st.write("Data for last 15 days")
# st.dataframe(df.tail(15))
# st.plotly_chart(figure1, use_container_width=True)
st.write("Forecast for next "+str(period)+" days")
# st.dataframe(forecast.tail(period))

st.dataframe(forecast1.tail(period))
st.plotly_chart(figure, use_container_width=True)
