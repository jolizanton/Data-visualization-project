from operator import itemgetter
import requests

from plotly.graph_objs import Bar
from plotly import offline

#Make api call ans store the response
url='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(url)
print (f"Status code: {r.status_code}")

#Process info about each submission
submission_ids=r.json()
submission_dicts=[]
for submission_id in submission_ids[:20]:
    #Make a separate api call for each submission
    url=f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r=requests.get(url)
    print(f"id:{submission_id}\t Status:{r.status_code}")
    response_dict=r.json()

    #Build a dictionary for each article:
    submission_dict={
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
        'by': response_dict['by'],
        'id':response_dict['id']
    }
    submission_dicts.append(submission_dict)
submission_dicts=sorted(submission_dicts,key=itemgetter('comments'),reverse=True)

labels,comments_s,repo_links=[],[],[]
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

    # Data_visualization
    for key in submission_dict.keys():
        print(key)
    by = submission_dict['by']
    id = submission_dict['id']
    label = f"{by}<br />{id}"
    labels.append(label)

    comments_s.append(submission_dict['comments'])
    repo_name=submission_dict['title']
    repo_url=submission_dict['hn_link']
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

# Make visualization
data=[{
    'type':'bar',
    'x': repo_links,
    'y':comments_s,
    'hovertext':labels,
    'marker':{
        'color':'rgb(60,100,150)',
        'line':{'width':1.5,'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,
}]
my_layout={
    'title': 'Hacker news discussion',
    'titlefont':{'size':28},
    'xaxis': {'title':'Title',
              'titlefont':{'size':24},
              'tickfont':{'size':14},
              },
    'yaxis': {'title': 'Comments',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14},
              }
}
fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='Hacker news submission.html')