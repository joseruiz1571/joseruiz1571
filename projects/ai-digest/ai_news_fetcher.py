#!/usr/bin/env python3
"""
AI News Fetcher and Digest Generator
Fetches recent AI news from multiple sources and generates a conversational summary
"""

import feedparser
import requests
from datetime import datetime, timedelta
import json
import os
from typing import List, Dict
import anthropic


class AINewsFetcher:
    """Fetches AI news from various RSS feeds and news sources"""

    # Popular AI news RSS feeds
    RSS_FEEDS = {
        "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/",
        "MIT Tech Review AI": "https://www.technologyreview.com/topic/artificial-intelligence/feed",
        "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",
        "The Verge AI": "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
        "Google AI Blog": "https://ai.googleblog.com/feeds/posts/default",
        "OpenAI Blog": "https://openai.com/blog/rss.xml",
        "Anthropic News": "https://www.anthropic.com/news/rss.xml",
    }

    def __init__(self, hours_back=24):
        """
        Initialize the news fetcher.

        Args:
            hours_back: How many hours back to fetch news (default: 24)
        """
        self.hours_back = hours_back
        self.cutoff_time = datetime.now() - timedelta(hours=hours_back)

    def fetch_articles(self) -> List[Dict]:
        """
        Fetch articles from all RSS feeds.

        Returns:
            List of article dictionaries with title, link, summary, source, and date
        """
        all_articles = []

        print(f"Fetching AI news from the last {self.hours_back} hours...\n")

        for source_name, feed_url in self.RSS_FEEDS.items():
            try:
                feed = feedparser.parse(feed_url)
                source_count = 0

                for entry in feed.entries:
                    # Parse publication date
                    pub_date = None
                    if hasattr(entry, 'published_parsed'):
                        pub_date = datetime(*entry.published_parsed[:6])
                    elif hasattr(entry, 'updated_parsed'):
                        pub_date = datetime(*entry.updated_parsed[:6])

                    # Skip if too old (if we have a date)
                    if pub_date and pub_date < self.cutoff_time:
                        continue

                    # Extract article info
                    article = {
                        'title': entry.get('title', 'No title'),
                        'link': entry.get('link', ''),
                        'summary': entry.get('summary', entry.get('description', '')),
                        'source': source_name,
                        'date': pub_date.strftime('%Y-%m-%d %H:%M') if pub_date else 'Unknown date',
                        'raw_date': pub_date
                    }

                    all_articles.append(article)
                    source_count += 1

                    # Limit per source to avoid overwhelming
                    if source_count >= 10:
                        break

                if source_count > 0:
                    print(f"  ✓ {source_name}: {source_count} articles")

            except Exception as e:
                print(f"  ✗ {source_name}: Error - {str(e)}")
                continue

        # Sort by date (most recent first)
        all_articles.sort(key=lambda x: x['raw_date'] if x['raw_date'] else datetime.min, reverse=True)

        print(f"\nTotal articles found: {len(all_articles)}\n")
        return all_articles


class AIDigestGenerator:
    """Generates conversational summaries using Claude API"""

    def __init__(self, api_key=None):
        """
        Initialize the digest generator.

        Args:
            api_key: Anthropic API key (if None, reads from ANTHROPIC_API_KEY env var)
        """
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if self.api_key:
            self.client = anthropic.Anthropic(api_key=self.api_key)
        else:
            self.client = None
            print("Warning: No Anthropic API key found. Will generate basic summary.")

    def generate_digest(self, articles: List[Dict]) -> Dict:
        """
        Generate a conversational digest from articles.

        Args:
            articles: List of article dictionaries

        Returns:
            Dictionary with 'summary' and 'featured_article' keys
        """
        if not articles:
            return {
                'summary': "No recent AI news found.",
                'featured_article': None
            }

        # Prepare articles text
        articles_text = self._format_articles_for_prompt(articles)

        if self.client:
            return self._generate_with_claude(articles_text, articles)
        else:
            return self._generate_basic_summary(articles)

    def _format_articles_for_prompt(self, articles: List[Dict]) -> str:
        """Format articles for the Claude prompt"""
        formatted = []
        for i, article in enumerate(articles[:20], 1):  # Limit to top 20 articles
            formatted.append(f"{i}. [{article['source']}] {article['title']}")
            if article['summary']:
                # Clean and truncate summary
                summary = article['summary'][:200].strip()
                formatted.append(f"   {summary}...")
            formatted.append(f"   Link: {article['link']}")
            formatted.append("")

        return "\n".join(formatted)

    def _generate_with_claude(self, articles_text: str, articles: List[Dict]) -> Dict:
        """Generate digest using Claude API"""

        prompt = f"""You are an AI news digest assistant. Based on the following recent AI news articles, create:

1. A conversational summary (2-3 paragraphs) of the most interesting developments
2. Identify ONE article that's particularly worth reading in full or sharing on social media

Recent AI News Articles:
{articles_text}

Please provide:
1. A friendly, conversational summary highlighting the most significant or interesting developments
2. The number (1-{min(20, len(articles))}) of the article you'd most recommend reading/sharing and why

Format your response as:
SUMMARY:
[Your conversational summary here]

FEATURED ARTICLE:
Article #[number]
Why: [Brief explanation of why this article is worth reading/sharing]
"""

        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = message.content[0].text

            # Parse response
            parts = response_text.split("FEATURED ARTICLE:")
            summary = parts[0].replace("SUMMARY:", "").strip()

            featured_article = None
            if len(parts) > 1:
                featured_text = parts[1].strip()
                # Extract article number
                import re
                match = re.search(r'Article #(\d+)', featured_text)
                if match:
                    article_num = int(match.group(1)) - 1
                    if 0 <= article_num < len(articles):
                        featured_article = articles[article_num].copy()
                        # Extract why text
                        why_match = re.search(r'Why: (.+)', featured_text, re.DOTALL)
                        if why_match:
                            featured_article['recommendation_reason'] = why_match.group(1).strip()

            return {
                'summary': summary,
                'featured_article': featured_article
            }

        except Exception as e:
            print(f"Error generating digest with Claude: {e}")
            return self._generate_basic_summary(articles)

    def _generate_basic_summary(self, articles: List[Dict]) -> Dict:
        """Generate a basic summary without AI"""
        summary_lines = ["Recent AI News Highlights:\n"]

        # Group by source
        by_source = {}
        for article in articles[:10]:
            source = article['source']
            if source not in by_source:
                by_source[source] = []
            by_source[source].append(article)

        for source, source_articles in by_source.items():
            summary_lines.append(f"\n{source}:")
            for article in source_articles[:3]:
                summary_lines.append(f"  • {article['title']}")

        return {
            'summary': "\n".join(summary_lines),
            'featured_article': articles[0] if articles else None
        }


def print_digest(digest: Dict):
    """Print the digest in a nice format"""
    print("=" * 80)
    print("AI NEWS DIGEST")
    print("=" * 80)
    print()
    print(digest['summary'])
    print()

    if digest['featured_article']:
        print("=" * 80)
        print("📌 FEATURED ARTICLE - WORTH READING/SHARING")
        print("=" * 80)
        print()
        article = digest['featured_article']
        print(f"Title: {article['title']}")
        print(f"Source: {article['source']}")
        print(f"Link: {article['link']}")
        print(f"Date: {article['date']}")
        if 'recommendation_reason' in article:
            print(f"\nWhy this article: {article['recommendation_reason']}")
        print()

    print("=" * 80)


def main():
    """Main function to run the AI digest"""
    import argparse

    parser = argparse.ArgumentParser(description='Fetch and summarize recent AI news')
    parser.add_argument('--hours', type=int, default=24,
                       help='How many hours back to fetch news (default: 24)')
    parser.add_argument('--output', type=str, choices=['console', 'json'], default='console',
                       help='Output format (default: console)')

    args = parser.parse_args()

    # Fetch news
    fetcher = AINewsFetcher(hours_back=args.hours)
    articles = fetcher.fetch_articles()

    # Generate digest
    generator = AIDigestGenerator()
    digest = generator.generate_digest(articles)

    # Output
    if args.output == 'json':
        print(json.dumps(digest, indent=2, default=str))
    else:
        print_digest(digest)


if __name__ == "__main__":
    main()
