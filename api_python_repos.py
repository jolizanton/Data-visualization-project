import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()

# Process results.
print(response_dict.keys())
print(response_dict)

print(f"Total repositories: {response_dict['total_count']}")

#Explore the info about the repositories
items_repositories_dicts= response_dict['items']
print (f"Repositories returned: {len(items_repositories_dicts)}")

#Examine the first repository
print(f"First repository: {items_repositories_dicts[0]}")
items_repositories_dict_first= items_repositories_dicts[0]
print (f"\nKeys: {len(items_repositories_dict_first)}")
for key in sorted(items_repositories_dict_first.keys()):
    print(key)

#Obtaining selected info about the first repository
print("\nSelected information about first repository:")
print(f"Name: {items_repositories_dict_first['name']}")
print(f"owner: {items_repositories_dict_first['owner']['login']}")
print(f"created_at: {items_repositories_dict_first['created_at']}")
print(f"description: {items_repositories_dict_first['description']}")
print(f"deployments_url: {items_repositories_dict_first['deployments_url']}")
print(f"stars: {items_repositories_dict_first['stargazers_count']}")
print(f"html_url: {items_repositories_dict_first['html_url']}")
print(f"created_at: {items_repositories_dict_first['created_at']}")
print(f"updated_at: {items_repositories_dict_first['updated_at']}")

#Selected info about each repository
print("\nSelected information about each repository:")
for items_repositories_dict in items_repositories_dicts:
    print(f"\nName: {items_repositories_dict['name']}")
    print(f"owner: {items_repositories_dict['owner']['login']}")
    print(f"created_at: {items_repositories_dict['created_at']}")
    print(f"description: {items_repositories_dict['description']}")
    print(f"deployments_url: {items_repositories_dict['deployments_url']}")
    print(f"stars: {items_repositories_dict['stargazers_count']}")
    print(f"html_url: {items_repositories_dict['html_url']}")
    print(f"created_at: {items_repositories_dict['created_at']}")
    print(f"updated_at: {items_repositories_dict['updated_at']}")
