from botocore.vendored import requests

def lambda_handler(event, context):
    coin = event['coin']
    background = event['background']
    fontcolor = event['fontcolor']
    
    api = "https://api.exchangeratesapi.io/latest?base=BRL&symbols=USD,EUR,GBP"
    
    coin_mapping = {
        "USD": "$ D&oacute;lar | ",
        "EUR": "&euro; Euro | ",
        "GBP": "&pound; Libra | ",
    }
    
    response = requests.get(api, "rates")

    rates_content = response.json()["rates"]

    coin_rating = round(1 / rates_content[coin], 2)
    
    
    if background == "":
        htmlstr = '<html><head><link href="https://fonts.googleapis.com/css?family=Roboto:600" rel="stylesheet"></head><body style="overflow: hidden;font-size: 100vh;scroll=no"><div style="font-family: \'Roboto\', sans-serif; color: #{};font-weight: 600;">{} R$ {:,.2f}</div></body></html>'.format(fontcolor, coin_mapping[coin], coin_rating).replace('.', ',')
    else:
        htmlstr = '<html><head><link href="https://fonts.googleapis.com/css?family=Roboto:600" rel="stylesheet"></head><body style="background-color: #{};overflow: hidden;font-size: 100vh;scroll=no"><div style="font-family: \'Roboto\', sans-serif; color: #{};font-weight: 600;">{} R$ {:,.2f}</div></body></html>'.format(background, fontcolor, coin_mapping[coin], coin_rating).replace('.', ',')
    
    
    return htmlstr