# Reddit User Persona Builder

This script fetches posts and comments from a Reddit user's profile, analyzes the data to generate a detailed **User Persona**, and outputs the persona as a text file. It uses **PRAW** for Reddit API interactions and **OpenAI GPT-4** for text analysis.

---

## Features

* Scrapes Reddit user's posts and comments.
* Analyzes data to generate a marketing persona based on text patterns.
* Cites sources for each extracted characteristic.
* Outputs the user persona into a text file.

---

## Requirements

1. **Python 3.10+**
2. **PIP** – Python package installer (comes with Python)

---

## Setup Instructions

### 1. **Clone the Repository**

If you haven’t already, clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/reddit-persona-builder.git
cd reddit-persona-builder
```

### 2. **Install Dependencies**

Create a `requirements.txt` file and install the required libraries by running the following:

```bash
pip install -r requirements.txt
```

Alternatively, manually install dependencies:

```bash
pip install praw openai python-dotenv tqdm
```

### 3. **Set Up Reddit API Access**

1. Visit [Reddit App Preferences](https://www.reddit.com/prefs/apps).

2. Create a new **script-type** app.

3. Fill out the fields:

   * **Name**: `Reddit Persona Builder`
   * **App type**: **script**
   * **Redirect URI**: `http://localhost:8080` (required, but not used in the script)
   * Leave the **description** and **about URL** fields blank.

4. Copy the **Client ID** and **Client Secret**.

   * **Client ID**: Found under the app name.
   * **Client Secret**: Found under the app's details.

5. Store these credentials in an `.env` file.

---

### 6. **Create `.env` File**

Create a `.env` file in the root directory of the project, and add the following:

```env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=script:persona:v1.0 (by u/your_reddit_username)
OPENAI_API_KEY=your_openai_api_key
```

* **REDDIT\_CLIENT\_ID**: Your Reddit app's client ID.
* **REDDIT\_CLIENT\_SECRET**: Your Reddit app's client secret.
* **REDDIT\_USER\_AGENT**: A custom user agent (e.g., `script:persona:v1.0 (by u/your_reddit_username)`).
* **OPENAI\_API\_KEY**: Your OpenAI GPT-4 API key (from [OpenAI API](https://platform.openai.com/)).

### 7. **Install OpenAI API Key (Optional)**

If you're using OpenAI for GPT-4, create an account and get an API key from [OpenAI](https://platform.openai.com/). Insert it in the `.env` file.

---

## Running the Script

1. **Run the Script**:

```bash
python reddit_persona_builder.py
```

### 2. **Provide User Profile URL**

The script will prompt you to enter a Reddit user's profile URL. For example:

```
https://www.reddit.com/user/kojied/
```

The script will scrape the posts and comments from the specified profile and generate a user persona.

---

## Example Output

After running the script, you will receive a `.txt` file containing the user persona. The file is named based on the Reddit username (e.g., `kojied_persona.txt`). It contains:

* **Demographics** (Age, Occupation, Location, etc.)
* **Behavioral Patterns** (Habits, Goals, Motivations)
* **Frustrations, Needs & Preferences**
* **Citations** for each extracted characteristic

---

## Example User Persona:

```text
---
NAME: Lucas Mellor
AGE: 31
OCCUPATION: Content Manager
STATUS: Single
LOCATION: London, UK
TIER: Early Adopters
ARCHETYPE: The Creator

TRAITS:
- Practical
- Adaptable
- Spontaneous
- Active

MOTIVATIONS:
- Convenience
- Wellness
- Speed

PREFERENCES:
- Comfort
- Healthy Takeaways

PERSONALITY:
- Introvert
- Intuitive
- Perceiving

BEHAVIOR & HABITS:
Lucas prefers ordering healthy takeaways and has been adjusting his lifestyle since the lockdown.

CITE SOURCES:
- Post: [link]
- Comment: [link]
```

---

## Troubleshooting

1. **Error: API Key Missing**
   Ensure you have added your **OpenAI API Key** in the `.env` file.

2. **Error: Reddit Authentication Fails**
   Double-check your **Reddit Client ID** and **Client Secret** in the `.env` file.

---
