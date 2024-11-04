import os
from googleapiclient.discovery import build
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_video_comments(video_id, youtube):
    """Get comments for a specific video"""
    comments = []
    try:
        # Get comments in batches using pagination
        next_page_token = None
        while True:
            comments_response = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                textFormat='plainText',
                maxResults=100,
                pageToken=next_page_token
            ).execute()
            
            for item in comments_response.get('items', []):
                comment = {
                    'ID': video_id,
                    'comment_text': item['snippet']['topLevelComment']['snippet']['textDisplay'],
                    'author': item['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                    'like_count': item['snippet']['topLevelComment']['snippet']['likeCount'],
                    'published_at': item['snippet']['topLevelComment']['snippet']['publishedAt']
                }
                comments.append(comment)
            
            # Check if there are more comments
            next_page_token = comments_response.get('nextPageToken')
            if not next_page_token:
                break
            
    except Exception as e:
        print(f"Error getting comments for video {video_id}: {str(e)}")
    
    return comments

def main():
    """Main function to scrape comments from video IDs in a CSV file and merge with existing data"""
    # Get API key from environment variable
    api_key = os.getenv('YOUTUBE_API_KEY')
    
    if not api_key:
        print("Error: YouTube API key not found in .env file")
        return
    
    # Initialize YouTube API client
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # Load video IDs from the first CSV file
    video_ids_df = pd.read_csv('ducky bhai publish dates old to 2022.csv')  # Adjust the path as needed
    video_ids = video_ids_df['ID'].tolist()  # Assuming the column name is 'ID'
    
    # Ask user for sorting preference
    print("Choose how to sort comments:")
    print("1. Top 50 liked comments")
    print("2. Top 50 recent comments")
    choice = input("Enter your choice (1 or 2): ")

    all_comments = []  # To store comments for all videos
    
    for video_id in video_ids:
        print(f"\nCollecting comments for video ID: {video_id}")
        comments = get_video_comments(video_id, youtube)
        
        # Sort comments based on user choice
        if choice == '1':
            # Sort by like count (descending)
            sorted_comments = sorted(comments, key=lambda x: (x['like_count'], x['published_at']), reverse=True)
        elif choice == '2':
            # Sort by published date (descending)
            sorted_comments = sorted(comments, key=lambda x: x['published_at'], reverse=True)
        else:
            print("Invalid choice. Defaulting to top 50 liked comments.")
            sorted_comments = sorted(comments, key=lambda x: (x['like_count'], x['published_at']), reverse=True)

        # Get the top 50 comments based on the chosen sorting method
        top_comments = sorted_comments[:50]
        all_comments.extend(top_comments)  # Add comments to the list
    
    if all_comments:
        # Create DataFrame for comments
        comments_df = pd.DataFrame(all_comments)
        comments_df.rename(columns={'video_id': 'ID'}, inplace=True)
        
        # Save comments to the second CSV file
        comments_output_file = 'video_comments.csv'
        comments_df.to_csv(comments_output_file, index=False, encoding='utf-8')
        print(f"\nData saved to {comments_output_file}")
        print(f"Total comments collected: {len(all_comments)}")
        
        # Merge with the original data
         
        existing_data_df = pd.read_csv('ducky bhai publish dates old to 2022.csv')  # Load the original data
        merged_df = pd.merge(existing_data_df, comments_df, on='ID', how='outer')  # Merge based on ID
        merged_output_file = 'merged_data.csv'
        merged_df.to_csv(merged_output_file, index=False, encoding='utf-8')
        print(f"Merged data saved to {merged_output_file}")
        
    else:
        print("No comments were collected. The videos might have comments disabled or no comments yet.")

if __name__ == "__main__":
    print("YouTube Video Comments Scraper")
    print("=" * 30)
    main()