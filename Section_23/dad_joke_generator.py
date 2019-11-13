import requests
import pyfiglet
from random import randint
from termcolor import colored

#  ask for a joke topic

def get_dad_joke(topic):
    url = 'https://icanhazdadjoke.com/search'
    response = requests.get(
        url,
        headers={'Accept': 'application/json'},
        params={'term': f'{topic}'}
    )
    # print(response.json()['results'])
    return response.json()['results']

def tell_dad_joke(topic):
    jokes = get_dad_joke(topic)
    ji = 0
    if not jokes:
        print(f'\nSorry, I don\'t have any jokes about {topic}. Ask about something else:\n')
        return ''
    elif len(jokes) > 1:
        print(f'\nI have lots of jokes about that! Here\'s one:')
        ji = randint(0,len(jokes))
    elif len(jokes) == 1:
        print(f'\nI have a joke about that!') 
    return jokes[ji]['joke']

game_title = colored(pyfiglet.figlet_format('Dad Joke Generator'),'red')
print(game_title)
print('Let me tell you a joke! Give me a topic:')
joke = ''
while not joke:
    topic = input()
    dad_joke = tell_dad_joke(topic)
    if dad_joke:
        joke = dad_joke
print(joke)
print('===================================')
