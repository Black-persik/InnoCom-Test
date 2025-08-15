
import requests

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload={
  'scope': 'GIGACHAT_API_PERS'
}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'RqUID': 'b15dc234-3503-40d5-ac09-c25453176832',
  'Authorization': 'Basic N2NlY2E4NjMtYjFhMi00N2MxLTkwYjAtNzc3NjVmOWVkY2U5OjA3OGE1NGEzLTRlMjctNDMzMi05N2VlLWEyMWVkMzk5OTMyNQ=='
}

response_for_token = requests.request("POST", url, headers=headers, data=payload, verify=False)


def get_answer(snippet:str) -> str:
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {response_for_token.json()['access_token']}"
    }

    payload = {
        "model": "GigaChat",
        "messages": [
            {"role": "system",
             "content": "Ты — опытный разработчик, который пишет комментарии к коду. Выводи мне закомментированный код внутри самого кода. Пример, пользователь вводит print(1+ 3). Ответ должен быть примерно таким: print(1+ 3) #эта строчка скалыдвает два числа"},
            {"role": "user", "content": f"{snippet}"}
        ],
        "temperature": 0.7
    }
    resp = requests.post(url, headers=headers, json=payload, verify=False)
    answer = resp.json()['choices'][0]['message']['content']
    return answer

