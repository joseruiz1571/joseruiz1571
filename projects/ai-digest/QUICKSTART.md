# Quick Start Guide - AI News Digest

Get your AI news digest in 3 simple steps:

## Step 1: Install Dependencies

```bash
cd projects/ai-digest
pip install feedparser anthropic requests
```

## Step 2: (Optional) Set API Key

For AI-powered summaries, get your free API key from Anthropic:

1. Visit: https://console.anthropic.com/
2. Create an account (free tier available)
3. Generate an API key
4. Set it in your environment:

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Or save it permanently in your shell config (`~/.bashrc` or `~/.zshrc`):

```bash
echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

## Step 3: Run the Digest

```bash
./ai-digest.sh
```

That's it! You'll see:
- A conversational summary of recent AI news
- A featured article worth reading or sharing
- All formatted nicely in your terminal

## Daily Usage

Make it even easier by adding an alias:

```bash
echo 'alias ai-news="~/projects/ai-digest/ai-digest.sh"' >> ~/.bashrc
source ~/.bashrc
```

Now just type `ai-news` from anywhere!

## Without API Key

The tool still works without an API key - it will generate a basic summary by grouping articles by source. The AI-powered version just makes the summaries more conversational and better at identifying the most interesting articles.

## Troubleshooting

### "command not found: ./ai-digest.sh"

Make sure you're in the right directory:
```bash
cd ~/projects/ai-digest
```

### "Permission denied"

Make the script executable:
```bash
chmod +x ai-digest.sh
```

### Can't install Python packages?

Try:
```bash
python3 -m pip install --user feedparser anthropic requests
```

## Next Steps

- Read the full [README.md](README.md) for advanced usage
- Customize news sources in `ai_news_fetcher.py`
- Set up the config file for persistent settings
- Integrate with your workflow (email, Slack, etc.)

---

**Enjoy staying up to date with AI - on your own schedule!**
