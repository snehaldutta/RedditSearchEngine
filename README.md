# RedditSearchEngine
Here's a detailed README for a GitHub repository featuring a Reddit Crawler built with `praw`, `pandas`, and `streamlit`:

---

# Reddit Crawler

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PRAW](https://img.shields.io/badge/PRAW-7.5.0-brightgreen)
![Pandas](https://img.shields.io/badge/Pandas-1.3.3-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.4.0-red)

## Overview

This project is a Reddit Crawler built using Python, which leverages the `praw` library to interact with the Reddit API, `pandas` for data manipulation, and `streamlit` to create a simple, interactive frontend. The crawler allows users to search for posts within specific subreddits, sort them by score, and display the results in an easy-to-read format.

## Features

- **Search Reddit Posts**: Retrieve posts from any subreddit using a keyword-based search.
- **Sort by Score**: The fetched posts are automatically sorted by their score, so you can easily find the most popular content.
- **User-friendly Interface**: A simple web interface built with Streamlit allows for easy interaction with the crawler.
- **Customizable**: Users can specify the number of posts to retrieve and the subreddit to search within.

## Demo

![Demo](demo.gif) *(Include a GIF showing a demo of your crawler in action)*

## Installation

### Prerequisites

Ensure you have Python 3.8+ installed on your machine.

### Clone the Repository

```bash
git clone https://github.com/yourusername/reddit-crawler.git
cd reddit-crawler
```

### Install Dependencies

Use `pip` to install the required Python libraries:

```bash
pip install -r requirements.txt
```

Alternatively, you can install them individually:

```bash
pip install praw pandas streamlit
```

### Setup Reddit API Credentials

To interact with Reddit's API, you need to set up a Reddit app to get your credentials:

1. Go to [Reddit's app preferences](https://www.reddit.com/prefs/apps).
2. Click on "Create App" or "Create Another App".
3. Fill in the required fields:
   - **name**: Choose a name for your app.
   - **App type**: Choose "script".
   - **description**: Optional.
   - **about url**: Optional.
   - **redirect uri**: `http://localhost:8080` (or any URL, it won't be used in a script).
   - **permissions**: Leave as is.
4. Click "Create app".
5. Note down your `client_id`, `client_secret`, and `user_agent`.

### Configure the Crawler

Create a `config.py` file in the root directory with your Reddit API credentials:

```python
# config.py

REDDIT_CLIENT_ID = 'your_client_id'
REDDIT_CLIENT_SECRET = 'your_client_secret'
REDDIT_USER_AGENT = 'your_user_agent'
```

### Run the Crawler

Launch the Streamlit app:

```bash
streamlit run app.py
```

This will start a local server. Open the URL provided in the terminal (typically `http://localhost:8501`) to access the app.

## Usage

1. **Enter Subreddit Name**: Specify the subreddit you want to search within.
2. **Enter Search Query**: Provide a keyword or phrase to search for.
3. **Set Post Limit**: Use the slider to define how many posts to retrieve (between 1 and 50).
4. **Search**: Click the "Search" button to fetch and display the results.

## Project Structure

```bash
reddit-crawler/
│
├── app.py                # Main application file for Streamlit
├── config.py             # Configuration file for Reddit API credentials
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add YourFeature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out:

- **GitHub**: [yourusername](https://github.com/snehaldutta)
- **Email**: snehaldutta1230@gmail.com

---

This README provides a clear and structured overview of your Reddit Crawler project, making it easy for others to understand and contribute.
