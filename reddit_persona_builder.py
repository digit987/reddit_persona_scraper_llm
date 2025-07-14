import praw
import os
from dotenv import load_dotenv
from tqdm import tqdm
import openai
import re

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET,
                     user_agent=REDDIT_USER_AGENT)

def extract_username(profile_url):
    return profile_url.rstrip("/").split("/")[-1]

def get_user_data(username, limit=100):
    user = reddit.redditor(username)
    posts = []
    comments = []

    for submission in tqdm(user.submissions.new(limit=limit), desc="Scraping posts"):
        posts.append({
            "title": submission.title,
            "selftext": submission.selftext,
            "url": f"https://www.reddit.com{submission.permalink}"
        })

    for comment in tqdm(user.comments.new(limit=limit), desc="Scraping comments"):
        comments.append({
            "body": comment.body,
            "url": f"https://www.reddit.com{comment.permalink}"
        })

    return posts, comments

def build_prompt(posts, comments):
    text_snippets = []

    for p in posts:
        snippet = f"Post Title: {p['title']}\nPost Body: {p['selftext']}\nURL: {p['url']}\n"
        text_snippets.append(snippet)

    for c in comments:
        snippet = f"Comment: {c['body']}\nURL: {c['url']}\n"
        text_snippets.append(snippet)

    # Limit to a manageable token size (approx 3000 tokens)
    full_text = "\n\n".join(text_snippets[:30])
    
    prompt = f"""
Below is a collection of Reddit posts and comments from a user. Analyze their text to create a detailed marketing user persona, like this structure:

---
NAME:
AGE:
OCCUPATION:
STATUS:
LOCATION:
TIER:
ARCHETYPE:
TRAITS:
- (e.g., Practical, Adaptable, Spontaneous)
MOTIVATIONS:
PREFERENCES:
DIETARY NEEDS:
PERSONALITY:
BEHAVIOUR & HABITS:
GOALS & NEEDS:
FEELINGS:
FRUSTRATIONS:
CITE SOURCES FOR EACH INSIGHT.
---

User Text:
{full_text}
"""

    return prompt

def generate_persona(prompt):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{
            "role": "user",
            "content": prompt
        }],
        temperature=0.7,
        max_tokens=2048
    )
    return response.choices[0].message.content

def save_to_file(content, username):
    filename = f"{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Persona saved to {filename}")

def main():
    profile_url = input("Enter Reddit user profile URL: ").strip()
    username = extract_username(profile_url)
    print(f"Fetching data for u/{username}...")

    posts, comments = get_user_data(username)
    if not posts and not comments:
        print("No data found.")
        return

    prompt = build_prompt(posts, comments)
    persona = generate_persona(prompt)
    save_to_file(persona, username)

if __name__ == "__main__":
    main()
