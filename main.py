import requests
from datetime import datetime as tm

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('pictures/img_1.png', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'Pz898jUwEqLfwGbGNzen92cG'},
)
if response.status_code == requests.codes.ok:
    with open(f"Upload/IMG {tm.now().strftime('%Y-%m-%d %H-%M-%S')}.png", 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)


