# YouTube Comments Scraper

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Goals](#project-goals)
3. [Outline](#outline)
4. [Materials and Methods](#materials-and-methods)
5. [Key Analysis Questions](#key-analysis-questions)
6. [Libraries Used](#libraries-used)
7. [Installation](#installation)
8. [Conclusion](#conclusion)
9. [Author](#author)

## Project Overview
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5.3-green)](https://pandas.pydata.org/)
[![Google API](https://img.shields.io/badge/Google%20API-YouTube%20Data%20API-blue)](https://developers.google.com/youtube/v3)

This project focuses on scraping comments from YouTube videos using the YouTube Data API. By collecting and analyzing comments, we aim to gain insights into viewer engagement and sentiment regarding specific videos.

## Project Goals
1. Collect comments from specified YouTube video IDs.
2. Allow users to sort comments based on likes or recency.
3. Save the collected comments to a CSV file for further analysis.
4. Merge the comments data with existing video metadata for comprehensive insights.

## Outline
1. **Materials and Methods**
2. **Data Loading and Preprocessing**
3. **Comment Collection and Sorting**
4. **Data Saving and Merging**
5. **Key Analysis Questions**



## Materials and Methods
The dataset used in this project consists of comments scraped from YouTube videos. The video IDs are obtained from **VidIQ**, a tool that provides insights and analytics for YouTube content. The script utilizes the YouTube Data API to fetch comments based on these provided video IDs. The analysis involves data cleaning, sorting based on user preferences, and saving the results in a structured format.


## Key Analysis Questions
- What are the most liked comments on specific videos?
- How do recent comments compare to older ones in terms of engagement?
- What insights can be drawn from the comments regarding viewer sentiment?

Additionally, we will conduct visual analyses to enhance the understanding of viewer engagement and sentiment trends.

## Libraries Used
1. **NumPy**: For numerical operations and data manipulation.
2. **Pandas**: For data analysis and manipulation.
3. **Google API Client**: For interacting with the YouTube Data API.
4. **dotenv**: For managing environment variables.

## Installation
To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/YouTube-Comments-Scraper.git
   cd YouTube-Comments-Scraper
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, you can install the libraries individually:
   ```bash
   pip install numpy pandas google-api-python-client python-dotenv
   ```

4. **Set up your YouTube Data API key**:
   - Create a `.env` file in the project directory and add your API key:
   ```
   YOUTUBE_API_KEY=your_api_key_here
   ```

## Conclusion
This project aims to provide valuable insights into viewer engagement on YouTube videos by collecting and analyzing comments. The results can help content creators and marketers understand audience sentiment and improve their strategies.

## Author
* Arshman Khalid [Reach me out on LinkedIn](https://www.linkedin.com/in/arshmankhalid/).