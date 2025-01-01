## accept the GitHub username as an argument
## fetch the user’s recent activity using the GitHub API
## display it in the terminal.

import argparse
import requests
import sys


def fetchActivty(username):
    url = f"https://api.github.com/users/{username}/events"
    try: 
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 404:
            print(f"{username} not found")
        else:
            print(f"Error: Unable to fetch data (status code {res.status_code}).")
    except requests.RequestException as e:
        print(f"error: {e}")
    
    return []


def display_activity(events):
    if not events:
        print("No recent activity found.")
        return
    
    print("\nRecent Activity:")
    for event in events[:5]:  
        event_type = event.get("type", "Unknown Event")
        repo_name = event["repo"]["name"] if "repo" in event else "Unknown Repo"
        created_at = event.get("created_at", "Unknown Time")
        print(f"- {event_type} in {repo_name} at {created_at}")

def main():
    parser = argparse.ArgumentParser(description="Fetch recent GitHub activity for a user.")
    parser.add_argument("--username", type=str, help="GitHub username to fetch activity for")
    
    username = input("enter username: ")
    

    print(f"Fetching recent activity for '{username}'...\n")
    events = fetchActivty(username)
    display_activity(events)

if __name__ == "__main__":
    main()


