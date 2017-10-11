# korbit
Korbit Api Wrapper

## Configuration for oauth
### config.ini

```ini
[OAUTH]
CLIENT_ID={API Key}
CLIENT_SECRET={API Secret Key}
EMAIL={account email address}
PASSWORD={account password}
```

## Examples
### configparser
```
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

client_id = config['OAUTH']['CLIENT_ID']
client_secret = config['OAUTH']['CLIENT_SECRET']
email = config['OAUTH']['EMAIL']
password = config['OAUTH']['PASSWORD']
```

### korbit api - account
```python
from korbit.korbit import Korbit

k = Korbit()

token = k.GetAccessToken(client_id, client_secret, email, password)
access_token = token['access_token']
user = k.GetUserInfo(access_token)
```

### korbit api - public action
```python
from korbit.korbit import Korbit

k = Korbit()

k.GetPrice()
k.GetDetail()
k.GetOrderbook()
k.GetTransactions()
k.GetConstants()
```

### korbit api - private action
```python
from korbit.korbit import Korbit
from korbit.enums import Currency

k = Korbit()

payload = Korbit.OrderBuyLimitTypeParameterBuilder(Currency.ETH, 344400, 0.01, k.nonce)
r = k.OrderBuy(access_token, payload)
```

