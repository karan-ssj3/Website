# utils/medium_feed.py
import feedparser
import re
from datetime import datetime


def extract_image_from_summary(summary: str):
    """Extract the first image URL from HTML summary."""
    # Look for img tags in the summary
    img_pattern = r'<img[^>]+src="([^"]+)"[^>]*>'
    match = re.search(img_pattern, summary)
    if match:
        return match.group(1)
    return None


def clean_summary_text(summary: str):
    """Remove HTML tags and clean up the summary text."""
    # Remove HTML tags
    clean_text = re.sub(r'<[^>]+>', '', summary)
    # Remove extra whitespace
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    # Truncate to reasonable length
    if len(clean_text) > 200:
        clean_text = clean_text[:200] + "..."
    return clean_text


def fetch_medium_posts(username: str = "karanbhutani477", max_posts: int = 20):
    """
    Fetch blog posts from Medium RSS feed.
    
    Args:
        username: Medium username
        max_posts: Maximum number of posts to fetch
        
    Returns:
        List of blog post dictionaries
    """
    try:
        # Medium RSS feed URL
        feed_url = f"https://medium.com/feed/@{username}"
        
        # Parse the feed
        feed = feedparser.parse(feed_url)
        
        posts = []
        
        for entry in feed.entries[:max_posts]:
            # Extract image from summary
            image_url = extract_image_from_summary(entry.get("summary", ""))
            
            # Clean up summary text
            clean_summary = clean_summary_text(entry.get("summary", ""))
            
            # Extract post data
            post = {
                "title": entry.get("title", "Untitled"),
                "url": entry.get("link", ""),
                "published": entry.get("published", ""),
                "summary": clean_summary,
                "image": image_url,  # Add image URL
                "tags": [tag.term for tag in entry.get("tags", [])[:5]],  # Max 5 tags
            }
            
            # Format date
            try:
                pub_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %Z")
                post["date"] = pub_date.strftime("%b %d, %Y")
            except:
                post["date"] = "Recent"
            
            # Estimate read time (assuming 200 words per minute)
            word_count = len(clean_summary.split())
            read_time = max(1, word_count // 200)
            post["read_time"] = f"{read_time} min read"
            
            posts.append(post)
        
        return posts
    
    except Exception as e:
        print(f"Error fetching Medium posts: {e}")
        return []


# Fallback posts if fetch fails
FALLBACK_POSTS = [
    {
        "title": "Visit my Medium profile",
        "excerpt": "Check out my latest articles on Medium for insights on AI, data science, and technology.",
        "date": "Recent",
        "read_time": "",
        "url": "https://medium.com/@karanbhutani477",
        "image": None,
        "tags": ["AI", "Data Science"],
    }
]