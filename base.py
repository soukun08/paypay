import requests,os,json,uuid
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept' : 'application/json, text/plain, */*',
    'Content-Type' : 'application/json'
    }

def check_price(code,guild_id):
    client_uuid=str(uuid.uuid4())
    #リンクの情報を取得
    getp2pinfo={
    "Accept":"application/json, text/plain, */*",
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
    }
    #https://pay.paypay.ne.jp/bUjj9yOp
    aaaaaa=requests.get(f"https://www.paypay.ne.jp/app/v2/p2p-api/getP2PLinkInfo?verificationCode={code}&client_uuid={client_uuid}",headers=getp2pinfo)
    dataf=aaaaaa.json()
    return(dataf["payload"]["pendingP2PInfo"]["amount"])
    #SUCCESS
    #Cannot
    #あり,なし