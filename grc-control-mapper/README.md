# GRC Framework Control Mapper

A simple command-line tool for mapping AI governance controls across multiple frameworks.

## What It Does

This tool helps you find equivalent or related controls across three major AI governance frameworks:

- **NIST AI RMF** (AI Risk Management Framework)
- **ISO/IEC 42001:2023** (AI Management System)
- **EU AI Act**

Simply input a control requirement or keywords, and the tool will search through a database of mapped controls and show you related controls across all three frameworks.

## Project Structure

```
grc-control-mapper/
├── README.md                   # This file
├── main.py                     # Main Python script
└── framework_mappings.json     # Control mappings database
```

## Requirements

- **Python 3.6 or higher**
- No external dependencies! Uses only Python built-in libraries

## How to Run

### Option 1: Quick Start

1. Open a terminal and navigate to the project directory:
   ```bash
   cd grc-control-mapper
   ```

2. Run the script:
   ```bash
   python3 main.py
   ```

### Option 2: Make it executable (Linux/Mac)

1. Make the script executable:
   ```bash
   chmod +x main.py
   ```

2. Run it directly:
   ```bash
   ./main.py
   ```

## How to Use

Once the program starts, you'll see a welcome screen. Here's what you can do:

### Search for Controls

Type in keywords or a control description:

```
Enter control description or keywords: risk management
```

The tool will search and display matching controls with:
- Match score (higher = more relevant)
- Control category
- Description
- Equivalent controls from all three frameworks
- Related keywords

### Available Commands

- **Search**: Just type your query (e.g., "bias", "data quality")
- **`help`**: Display usage instructions
- **`list`**: Show all available control mappings
- **`quit`**: Exit the program

### Example Searches

Try these example searches to get started:

1. **"risk management"** - Find controls related to AI risk frameworks
2. **"bias"** - Find controls about bias and fairness
3. **"data quality"** - Find data governance controls
4. **"human oversight"** - Find controls about human supervision
5. **"documentation"** - Find transparency and documentation requirements

## Sample Output

```
====================================================================================================
FOUND 1 MATCHING CONTROL(S)
====================================================================================================

[1] BIAS & FAIRNESS (Match Score: 0.85)
ID: MAP-004
Description: Identify, measure, and mitigate bias and ensure fairness
----------------------------------------------------------------------------------------------------

  🔹 NIST AI RMF
     Control: MEASURE 2.1
     Text: AI systems are evaluated for harmful bias and discrimination

  🔹 ISO/IEC 42001
     Control: ISO 42001:6.2.3
     Text: Objectives for fairness and bias mitigation in AI systems

  🔹 EU AI Act
     Control: Article 10(2)(f)
     Text: Training data examined for possible biases and mitigation measures

  Keywords: bias, fairness, discrimination, equity, harmful, mitigation

====================================================================================================
```

## Understanding the Database

The `framework_mappings.json` file contains all control mappings. Each mapping includes:

- **id**: Unique identifier (e.g., "MAP-001")
- **category**: Control category (e.g., "Risk Management")
- **description**: Brief description of what the control addresses
- **nist_ai_rmf**: NIST AI RMF control details
- **iso_42001**: ISO 42001 control details
- **eu_ai_act**: EU AI Act control details
- **keywords**: Search keywords for finding this mapping

### Current Mappings

The tool includes 6 pre-configured control mappings covering:

1. **Risk Management** - Establishing AI risk frameworks
2. **Data Governance** - Data quality and integrity
3. **Transparency & Documentation** - System documentation requirements
4. **Bias & Fairness** - Identifying and mitigating bias
5. **Human Oversight** - Human supervision requirements
6. **Model Validation & Testing** - Testing and validation controls

## How to Add More Controls

To add your own control mappings:

1. Open `framework_mappings.json` in a text editor
2. Add a new entry to the `control_mappings` array following this template:

```json
{
  "id": "MAP-007",
  "category": "Your Category",
  "description": "Brief description",
  "nist_ai_rmf": {
    "control_id": "NIST Control ID",
    "control_text": "Control description",
    "framework": "NIST AI RMF"
  },
  "iso_42001": {
    "control_id": "ISO Control ID",
    "control_text": "Control description",
    "framework": "ISO/IEC 42001"
  },
  "eu_ai_act": {
    "control_id": "Article X",
    "control_text": "Control description",
    "framework": "EU AI Act"
  },
  "keywords": ["keyword1", "keyword2", "keyword3"]
}
```

3. Save the file and restart the program

**Tip**: Make sure your JSON is valid! Use a JSON validator if needed.

## Troubleshooting

### "Could not find framework_mappings.json"
- Make sure you're running the script from the `grc-control-mapper` directory
- Check that `framework_mappings.json` exists in the same folder as `main.py`

### "Invalid JSON" error
- Your JSON file may have syntax errors
- Check for missing commas, brackets, or quotes
- Use a JSON validator tool to identify the issue

### No matching controls found
- Try broader keywords (e.g., "risk" instead of "risk assessment procedures")
- Use the `list` command to see all available mappings
- Check the keywords in the JSON file for search terms

## Learning Objectives

This project demonstrates:

- **Reading and parsing JSON** files in Python
- **Object-oriented programming** with Python classes
- **Text search and matching** using fuzzy algorithms
- **Command-line interface** design
- **Error handling** and user input validation
- **Code organization** and documentation

## License

Free to use and modify for educational and professional purposes.

## Author

Built as a learning project with Claude Code for AI governance work.

---

**Questions or suggestions?** Edit the code, add features, and make it your own!
