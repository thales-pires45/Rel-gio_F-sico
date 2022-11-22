import random
import time
from datetime import timedelta
import requests

id = 1

relogio = timedelta(hours=random.randrange(0,24), minutes=random.randrange(0,59), seconds=random.randrange(0,59))

params = {
    'id': int(id),
    'hora': str(relogio)
}


def main():
    requests.post('http://127.0.0.1:5000/relogio/', json=params)
    while True:
        try:
            print(f"Sua hora atual é {params}\n")
            r = requests.get(f'http://127.0.0.1:5000/relogio/{id}')
            data = r.json()
            params.update(data)
            print(f'Sua Hora atualizada é {params}\n')
            time.sleep(3)
        except:
            p = {
                'id': int(id),
                'hora': str(relogio)
            }
            params.update(p)
            requests.post('http://127.0.0.1:5000/relogio/', json=params)


if __name__ == "__main__":
    main()
