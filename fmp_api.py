
# coding: utf-8

# In[19]:


##FMP API
import requests as r
import json

def get_comp_profile(t):
    req = r.get("https://financialmodelingprep.com/api/v3/company/profile/" + t)
    return json.loads(req.text)

def get_income_an(t):
    req = r.get("https://financialmodelingprep.com/api/v3/financials/income-statement/" + t)
    return json.loads(req.text)

def get_income_q(t):
    req = r.get("https://financialmodelingprep.com/api/v3/financials/income-statement/" + t + "?period=quarter")
    return json.loads(req.text)
    
def get_bs_an(t):
    req = r.get("https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/" + t)
    return json.loads(req.text)

def get_bs_q(t):
    req = r.get("https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/" + t + "?period=quarter")
    return json.loads(req.text)

def get_cf_an(t):
    req = r.get("https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/" + t)
    return json.loads(req.text)

def get_cf_q(t):
    req = r.get("https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/" + t + "?period=quarter")
    return json.loads(req.text)

def get_ratios(t):
    req = r.get("https://financialmodelingprep.com/api/v3/financial-ratios/" + t)
    return json.loads(req.text)

def get_ev_an(t):
    req = r.get("https://financialmodelingprep.com/api/v3/enterprise-value/" + t)
    return json.loads(req.text)

def get_ev_q(t):
    req = r.get("https://financialmodelingprep.com/api/v3/enterprise-value/" + t + "?period=quarter")
    return json.loads(req.text)

def get_metrics_an(t):
    req = r.get("https://financialmodelingprep.com/api/v3/company-key-metrics/" + t)
    return json.loads(req.text)

def get_metrics_q(t):
    req = r.get("https://financialmodelingprep.com/api/v3/company-key-metrics/" + t + "?period=quarter")
    return json.loads(req.text)
    
def get_fg_an(t):
    req = r.get("https://financialmodelingprep.com/api/v3/financial-statement-growth/" + t)
    return json.loads(req.text)

def get_fg_q(t):
    req = r.get("https://financialmodelingprep.com/api/v3/financial-statement-growth/" + t + "?period=quarter")
    return json.loads(req.text)
    
def get_rating(t):
    req = r.get("https://financialmodelingprep.com/api/v3/company/rating/" + t)
    return json.loads(req.text)

def DCF(t):
    req = r.get("https://financialmodelingprep.com/api/v3/company/discounted-cash-flow/" + t)
    return json.loads(req.text)

def rt_price(t):
    req = r.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/" + t)
    return json.loads(req.text)

def symb_list():
    req = r.get("https://financialmodelingprep.com/api/v3/company/stock/list")
    return json.loads(req.text)

def batch_price(t):
    tickers = ""
    for x in t:
        tickers += x + ','
    tickers = tickers[0:len(tickers)-1]
    req = r.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/" + tickers)
    return json.loads(req.text)

