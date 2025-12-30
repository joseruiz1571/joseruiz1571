# AI News Digest - On-Demand Research Assistant

Stay up to date with the latest AI developments with a single command. This tool fetches recent AI news from multiple trusted sources and generates a conversational summary, highlighting articles worth reading or sharing.

Inspired by the "Stay up to date with AI" article, this toolkit automates your AI news consumption into a manageable, curated digest.

## Features

- 📰 **Multi-Source Aggregation**: Fetches from TechCrunch, MIT Tech Review, VentureBeat, Google AI Blog, OpenAI, and more
- 🤖 **AI-Powered Summaries**: Uses Claude to generate conversational summaries (optional)
- ⭐ **Featured Article**: Recommends one article particularly worth reading or sharing
- ⚡ **On-Demand**: Run whenever you want an update, no scheduled tasks needed
- 🎨 **Clean Output**: Formatted for easy reading in your terminal

## Quick Start

### 1. Installation

```bash
cd projects/ai-digest

# Install Python dependencies
pip install -r requirements.txt

# (Optional) Set up your Anthropic API key for AI-powered summaries
export ANTHROPIC_API_KEY='your-api-key-here'
```

### 2. Run the Digest

```bash
# Simple run (last 24 hours)
./ai-digest.sh

# Custom time range
./ai-digest.sh --hours 48

# JSON output
./ai-digest.sh --json
```

## Configuration

### Option 1: Environment Variable

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

### Option 2: Configuration File

```bash
cp .ai-digest.conf.example .ai-digest.conf
# Edit .ai-digest.conf and add your API key
```

Get your Anthropic API key from: https://console.anthropic.com/

## Usage Examples

### Daily Morning Digest

Add to your `.bashrc` or `.zshrc`:

```bash
alias ai-news='~/projects/ai-digest/ai-digest.sh'
```

Then simply run:
```bash
ai-news
```

### Weekly Deep Dive

```bash
./ai-digest.sh --hours 168  # 7 days
```

### Save to File

```bash
./ai-digest.sh > ai-news-$(date +%Y-%m-%d).txt
```

### JSON for Further Processing

```bash
./ai-digest.sh --json > digest.json
```

## Sample Output

```
================================================================================
AI NEWS DIGEST
================================================================================

The AI world has been buzzing this week with several major announcements.
Google DeepMind revealed significant improvements to their Gemini models,
particularly in reasoning capabilities and multimodal understanding. Meanwhile,
OpenAI continues to push boundaries with new GPT-4 applications in healthcare
and scientific research.

On the regulatory front, the EU has finalized new AI governance frameworks,
which could have far-reaching implications for AI development globally.
Several startups have also emerged with innovative approaches to AI safety
and alignment, addressing one of the field's most pressing challenges.

================================================================================
📌 FEATURED ARTICLE - WORTH READING/SHARING
================================================================================

Title: New Breakthrough in AI Reasoning Capabilities
Source: MIT Tech Review AI
Link: https://example.com/article
Date: 2024-12-30 09:15

Why this article: This piece provides deep insights into the latest advances
in AI reasoning systems, with practical implications for how these systems
might be deployed in real-world scenarios. The research methodology is
particularly noteworthy and worth sharing with technical audiences.

================================================================================
```

## News Sources

The digest aggregates from these trusted sources:

- **TechCrunch AI** - Industry news and startup coverage
- **MIT Technology Review AI** - In-depth analysis and research
- **VentureBeat AI** - Business and enterprise AI news
- **The Verge AI** - Consumer tech and AI applications
- **Google AI Blog** - Research breakthroughs and updates
- **OpenAI Blog** - Latest from OpenAI
- **Anthropic News** - Updates from Anthropic

## Options

```
./ai-digest.sh [OPTIONS]

Options:
  --hours N      Fetch news from the last N hours (default: 24)
  --json         Output in JSON format instead of console
  --help, -h     Show help message
```

## Advanced Usage

### Running Without API Key

The tool works without an Anthropic API key, generating a basic summary by grouping articles by source. For the best experience with conversational summaries and smart article recommendations, use an API key.

### Customizing News Sources

Edit `ai_news_fetcher.py` and modify the `RSS_FEEDS` dictionary to add or remove sources:

```python
RSS_FEEDS = {
    "Your Source": "https://example.com/feed",
    # Add more sources here
}
```

### Integration with Other Tools

The JSON output makes it easy to integrate with other tools:

```bash
# Send to Slack
./ai-digest.sh --json | jq -r '.summary' | slack-cli post

# Email yourself
./ai-digest.sh | mail -s "Daily AI Digest" you@example.com

# Save to note-taking app
./ai-digest.sh >> ~/Documents/ai-notes.txt
```

## Troubleshooting

### No articles found

- Check your internet connection
- Some RSS feeds may be temporarily unavailable
- Try increasing `--hours` to fetch older articles

### API errors

- Verify your `ANTHROPIC_API_KEY` is set correctly
- Check you have API credits available
- The tool will fall back to basic summaries if the API fails

### Python package errors

```bash
pip install --upgrade feedparser anthropic requests
```

## Philosophy

This tool embodies the principle from the inspiring article: "Staying informed isn't about knowing everything—it's about creating a simple, consistent learning habit."

Instead of being overwhelmed by constant AI news, you decide when to check in and get a curated, conversational summary of what matters.

## Contributing

Feel free to customize this tool for your needs:
- Add new RSS sources
- Modify the summary format
- Integrate with your workflow tools
- Adjust the AI prompt for different perspectives

## License

Free to use and modify for personal or professional use.

## Inspiration

Based on the article "Stay up to date with AI" which emphasizes creating personal, curated toolkits for staying informed about AI developments without feeling overwhelmed.
