
import requests

def question_data():
    param ={
        'amount':'10',
        'type':'boolean'
    }
    data = requests.get('https://opentdb.com/api.php',params=param)
    data.raise_for_status()


    game_questions = data.json()['results']
    return game_questions


