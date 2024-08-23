from readline import redisplay
import ipywidgets
from matplotlib import widgets

from fast_autocomplete import AutoComplete # type: ignore

words = {'book': {}, 'burrito': {}, 'pizza': {}, 'pasta':{}}
autocomplete = AutoComplete(words=words)

def on_change(data):
    #print(data)
    
    text = data['new']
    #print(text)
    
    values = autocomplete.search(text, max_cost=3, size=3)
    #print(values)
    
    # convert nested list to string
    #values = ', '.join(sorted(set(str(item) for sublist in values for item in sublist)))

    values = str(values)
    #print(values)
    
    label.value = values
    
label = widgets.Label()

text = ipywidgets.Text(
    value='',
    placeholder='Type something',
    description='String:',
    disabled=False
)
text.observe(on_change, names='value')

redisplay(text, label)