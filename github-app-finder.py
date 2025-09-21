import requests

def github_profile(value):
    url = f"https://api.github.com/users/{value}"
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()
        print("======Github Profile======")
        print(f"Username: {result['login']}")
        print(f"Profile link: {result['html_url']}")
        print(f"Bio: {result['bio']}")
        print(f"No. of Repos: {result['public_repos']}")
        print(f"Created Data: {result['created_at']}")
    else:
        print("User not found!")

#taking input from user
value = input("Enter username to find the profile: ")
github_profile(value)