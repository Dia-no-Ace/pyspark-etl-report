import requests
import json

def get_data_from_api(entity: str, up_limit: int, file_name: str):
    data = []
    for i in range(1,up_limit):
      url = f"https://dev.to/api/{entity}?page={i}&per_page=1000"
      try:
        response = requests.get(url)
        response.raise_for_status()
        data.extend(response.json())
      except requests.exceptions.Timeout as e:
            print(f"Request timed out: {e}")
      except requests.exceptions.ConnectionError as e:
            print(f"Connection error: {e}")
      except requests.exceptions.HTTPError as e:
          print(f"HTTP error: {e}")
      except requests.exceptions.RequestException as e:
            print(f"Other error: {e}")
    print(len(data))

    with open(file_name, 'w+') as file:
      for el in data:
        json.dump(el, file)
        file.write('\n')

get_data_from_api('articles', 16, 'articles.json')
get_data_from_api('videos', 16, 'videos.json')


