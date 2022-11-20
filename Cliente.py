import random
import time
from datetime import timedelta
import requests

id = 4
relogio_servidor = timedelta(hours=0, minutes=0, seconds=random.randrange(0, 59))

params = {
    'id': int(id),
    'hora': str(relogio_servidor)
}


def main():
    requests.post('http://127.0.0.1:5000/relogio/', json=params)
    while True:
        try:
            # requests.put(f'http://127.0.0.1:5000/relogio/{id}')
            print(f"Sua hora atual é {params['hora']}\n")
            r = requests.get(f'http://127.0.0.1:5000/relogio/{id}')
            data = r.json()
            params.update(data)
            print(params)
            time.sleep(3)
        except:
            requests.post('http://127.0.0.1:5000/relogio/', json=params)


if __name__ == "__main__":
    main()
