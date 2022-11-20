import random
import time
from datetime import timedelta
import requests

relogio_servidor = timedelta(hours=random.randrange(0, 23), minutes=0, seconds=random.randrange(0, 59))

id = 1
params = {
    'id': id,
    'hora': str(relogio_servidor)
}


def main():
    requests.post('http://127.0.0.1:5000/relogio/', json=params)
    while True:
        try:

            print(f"Sua hora atual é {params['hora']}\n")

            print('Gostaria de sicronizar a hora?\n')
            requests.put(f'http://127.0.0.1:5000/relogio/{id}', json=params)
            i = int(input('1 pra sim e 2 pra n: '))

            if i == 1:
                r = requests.get(f'http://127.0.0.1:5000/relogio/{id}')
                data = r.json()
                params.update(data)
                print(params)
            time.sleep(3)
        except:
            requests.post('http://127.0.0.1:5000/relogio/', json=params)
            print('servidor')


if __name__ == "__main__":
    main()
