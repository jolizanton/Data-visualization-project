import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
items_repositories_dicts= response_dict['items']

# Data_visualization
#repository_names=[items_repositories_dict['name'] for items_repositories_dict in items_repositories_dicts]
stars=[items_repositories_dict['stargazers_count'] for items_repositories_dict in items_repositories_dicts]

labels,repo_links=[],[]
for items_repositories_dict in items_repositories_dicts:
    owner=items_repositories_dict['owner']['login']
    description=items_repositories_dict['description']
    label=f"{owner}<br />{description}"
    labels.append(label)

    repo_name= items_repositories_dict['name']
    repo_url=items_repositories_dict['html_url']
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

# Make visualization
data=[{
    'type':'bar',
    #'x':repository_names,
    'x': repo_links,

    'y':stars,
    'hovertext':labels,
    'marker':{
        'color':'rgb(60,100,150)',
        'line':{'width':1.5,'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,
}]
my_layout={
    'title': 'Most starred Java project on Github',
    'titlefont':{'size':28},
    'xaxis': {'title':'Repository',
              'titlefont':{'size':24},
              'tickfont':{'size':14},
              },
    'yaxis': {'title': 'stars',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14},
              }
}
fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='java_repos.html')