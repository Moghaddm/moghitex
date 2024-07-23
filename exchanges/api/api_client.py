import requests
import json


# need to complete.
def get_nobitex_data():
    response = requests.get(
        url='https://api.nobitex.ir/market/stats?srcCurrency=btc,usdt,eth,etc,doge,ada,bch,ltc,bnb,eos,xlm,xrp,trx,uni,link,dai,dot,shib,aave,ftm,matic,axs,mana,sand,avax,usdc,gmt,mkr,sol,atom,grt,bat,near,ape,qnt,chz,xmr,egala,busd,algo,hbar,1inch,yfi,flow,snx,enj,crv,fil,wbtc,flr,ldo,dydx,apt,mask,comp,bal,lrc,lpt,ens,sushi,api3,one,glm,pmn,dao,cvc,nmr,storj,snt,ant,zrx,slp,egld,imx,blur,100k_floki,1b_babydoge,1m_nft,1m_btt,t,celr,arb,magic,gmx,band,cvx,ton,ssv,mdt,omg,wld,rdnt,jst,bico,rndr,woo,skl,gal,agix,fet,not,trb,1m_pepe,rsr,ethfi,agld,aevo,om,meme,uma,zro&dstCurrency=rls,usdt', )
    response_dict = json.loads(response.text)
    # nobitex_data = response_dict
    return response_dict


def get_btc_data():
    response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    response_dict = json.loads(response.text)
    btc_data = response_dict['price']
    return btc_data


def get_tabdeal_data():
    response = requests.get('https://api-web.tabdeal.org/r/api/order_book/?market_id=2')
    response_dict = json.loads(response.text)
    tabdeal_data = {
        'buy': response_dict['asks'][0]['price'],
        'sell': response_dict['bids'][0]['price']
    }
    return tabdeal_data


# need to complete
def get_wallex_data():
    response = requests.get('https://api.wallex.ir/v1/all-markets')
    response_dict = json.loads(response.text)
    buy_price = response_dict['result']['symbols']['BTCUDST']['EXCHANGE']['stats']['bidPrice']
    sell_price = response_dict['result']['symbols']['BTCUDST']['EXCHANGE']['stats']['askPrice']
    tabdeal_data = {
        'buy': response_dict['asks'][0]['price'],
        'sell': response_dict['bids'][0]['price']
    }
    return tabdeal_data


def get_huluex_data():
    response = requests.get('https://api.huluex.com/api/market/getCoinsPriceV3?version=3&')
    response_dict = json.loads(response.text)
    # huluex_data = {
    #     'buy': response_dict['data'][]
    # }
    return response_dict
