#!/bin/bash

# AI News Digest - On-Demand Research Assistant
# Fetches recent AI news and generates a conversational summary

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Configuration file
CONFIG_FILE="$SCRIPT_DIR/.ai-digest.conf"

# Load configuration if it exists
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
fi

# Default values if not in config
HOURS_BACK=${HOURS_BACK:-24}
OUTPUT_FORMAT=${OUTPUT_FORMAT:-console}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --hours)
            HOURS_BACK="$2"
            shift 2
            ;;
        --json)
            OUTPUT_FORMAT="json"
            shift
            ;;
        --help|-h)
            echo "AI News Digest - On-Demand Research Assistant"
            echo ""
            echo "Usage: ./ai-digest.sh [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --hours N      Fetch news from the last N hours (default: 24)"
            echo "  --json         Output in JSON format instead of console"
            echo "  --help, -h     Show this help message"
            echo ""
            echo "Configuration:"
            echo "  Set ANTHROPIC_API_KEY environment variable for AI-powered summaries"
            echo "  Or create $CONFIG_FILE with your settings"
            echo ""
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}Error: Python 3 is not installed${NC}"
    exit 1
fi

# Check if required packages are installed
echo -e "${BLUE}Checking dependencies...${NC}"
python3 -c "import feedparser, anthropic" 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}Installing required Python packages...${NC}"
    pip install feedparser anthropic requests --quiet
fi

# Check for API key
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo -e "${YELLOW}Note: ANTHROPIC_API_KEY not set. Will generate basic summary.${NC}"
    echo -e "${YELLOW}For AI-powered summaries, set your API key:${NC}"
    echo -e "${YELLOW}  export ANTHROPIC_API_KEY='your-key-here'${NC}"
    echo ""
fi

# Run the Python script
echo -e "${GREEN}Fetching your AI news digest...${NC}"
echo ""

python3 "$SCRIPT_DIR/ai_news_fetcher.py" --hours "$HOURS_BACK" --output "$OUTPUT_FORMAT"

exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✓ Digest generated successfully!${NC}"
else
    echo ""
    echo -e "${YELLOW}✗ There was an error generating the digest${NC}"
    exit $exit_code
fi
