import requests
import pyfiglet
from random import randint
from termcolor import colored

def get_dad_joke(topic):
    url = 'https://icanhazdadjoke.com/search'
    response = requests.get(
        url,
        headers={'Accept': 'application/json'},
        params={'term': f'{topic}'}
    )
    return response.json()

def tell_dad_joke(topic):
    jokes = get_dad_joke(topic)
    ji = 0
    num_jokes = jokes['total_jokes']
    if num_jokes > 1:
        print(f'\nI have {num_jokes} of jokes about that! Here\'s one:')
        ji = randint(0,len(jokes))
    elif num_jokes == 1:
        print(f'\nI have a joke about that!') 
    else:
        print(f'\nSorry, I don\'t have any jokes about {topic}. Ask about something else:\n')
        return ''
    return jokes['results'][ji]['joke']

header = pyfiglet.figlet_format('Dad Joke Generator')
header = colored(header,'red')
print(header)
print('Let me tell you a joke! Give me a topic:')
joke = ''
while not joke:
    topic = input()
    dad_joke = tell_dad_joke(topic)
    if dad_joke:
        joke = dad_joke
print(joke)
print('===================================')
