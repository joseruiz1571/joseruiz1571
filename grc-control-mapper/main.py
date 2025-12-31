#!/usr/bin/env python3
"""
GRC Framework Control Mapper
A simple tool to map controls across AI governance frameworks

This tool helps you find equivalent controls across:
- NIST AI RMF (AI Risk Management Framework)
- ISO/IEC 42001 (AI Management System)
- EU AI Act

Author: Built with Claude Code
Version: 1.0
"""

import json
import os
import sys
from difflib import SequenceMatcher


class ControlMapper:
    """Main class for loading and searching framework control mappings"""

    def __init__(self, json_file='framework_mappings.json'):
        """
        Initialize the mapper by loading the JSON database

        Args:
            json_file: Path to the JSON file containing control mappings
        """
        self.json_file = json_file
        self.mappings = []
        self.metadata = {}
        self.load_mappings()

    def load_mappings(self):
        """
        Load control mappings from the JSON file
        Handles file not found and JSON parsing errors
        """
        try:
            # Get the directory where this script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(script_dir, self.json_file)

            # Open and parse the JSON file
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.mappings = data.get('control_mappings', [])
                self.metadata = data.get('metadata', {})

            print(f"✓ Loaded {len(self.mappings)} control mappings from {self.json_file}")
            print(f"  Frameworks: {', '.join(self.metadata.get('frameworks_included', []))}\n")

        except FileNotFoundError:
            print(f"ERROR: Could not find {self.json_file}")
            print(f"Make sure the file exists in: {script_dir}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {self.json_file}: {e}")
            sys.exit(1)

    def calculate_similarity(self, text1, text2):
        """
        Calculate similarity between two text strings
        Uses SequenceMatcher for fuzzy matching

        Args:
            text1: First text string
            text2: Second text string

        Returns:
            Float between 0 and 1 (1 being identical)
        """
        return SequenceMatcher(None, text1.lower(), text2.lower()).ratio()

    def search_controls(self, query, threshold=0.2):
        """
        Search for controls matching the query text

        The search algorithm:
        1. Converts query and all text to lowercase for case-insensitive matching
        2. Checks for keyword matches (highest priority)
        3. Calculates similarity scores against descriptions and control text
        4. Returns results sorted by relevance score

        Args:
            query: The search query (control description or keywords)
            threshold: Minimum similarity score (0-1) to include a result

        Returns:
            List of tuples: (mapping, score) sorted by score descending
        """
        results = []
        query_lower = query.lower()

        for mapping in self.mappings:
            # Start with a base score of 0
            score = 0.0

            # Check for exact keyword matches (weighted heavily)
            keywords = mapping.get('keywords', [])
            keyword_matches = sum(1 for keyword in keywords if keyword in query_lower)
            if keyword_matches > 0:
                score += keyword_matches * 0.3  # Each keyword match adds 0.3

            # Check similarity with the mapping description
            desc_similarity = self.calculate_similarity(query, mapping.get('description', ''))
            score += desc_similarity * 0.4  # Description match weighted at 0.4

            # Check similarity with each framework's control text
            for framework in ['nist_ai_rmf', 'iso_42001', 'eu_ai_act']:
                if framework in mapping:
                    control_text = mapping[framework].get('control_text', '')
                    text_similarity = self.calculate_similarity(query, control_text)
                    score += text_similarity * 0.1  # Each framework match weighted at 0.1

            # Only include results above the threshold
            if score >= threshold:
                results.append((mapping, score))

        # Sort by score (highest first)
        results.sort(key=lambda x: x[1], reverse=True)
        return results

    def format_table(self, mappings_with_scores):
        """
        Format search results as a readable table

        Args:
            mappings_with_scores: List of (mapping, score) tuples
        """
        if not mappings_with_scores:
            print("No matching controls found. Try different keywords or a broader search.\n")
            return

        print(f"\n{'='*100}")
        print(f"FOUND {len(mappings_with_scores)} MATCHING CONTROL(S)")
        print(f"{'='*100}\n")

        for i, (mapping, score) in enumerate(mappings_with_scores, 1):
            # Header for each mapping
            print(f"[{i}] {mapping['category'].upper()} (Match Score: {score:.2f})")
            print(f"ID: {mapping['id']}")
            print(f"Description: {mapping['description']}")
            print(f"{'-'*100}")

            # NIST AI RMF
            if 'nist_ai_rmf' in mapping:
                nist = mapping['nist_ai_rmf']
                print(f"\n  🔹 NIST AI RMF")
                print(f"     Control: {nist['control_id']}")
                print(f"     Text: {nist['control_text']}")

            # ISO 42001
            if 'iso_42001' in mapping:
                iso = mapping['iso_42001']
                print(f"\n  🔹 ISO/IEC 42001")
                print(f"     Control: {iso['control_id']}")
                print(f"     Text: {iso['control_text']}")

            # EU AI Act
            if 'eu_ai_act' in mapping:
                eu = mapping['eu_ai_act']
                print(f"\n  🔹 EU AI Act")
                print(f"     Control: {eu['control_id']}")
                print(f"     Text: {eu['control_text']}")

            # Keywords for reference
            print(f"\n  Keywords: {', '.join(mapping.get('keywords', []))}")
            print(f"\n{'='*100}\n")


def print_banner():
    """Print a welcome banner"""
    print("\n" + "="*100)
    print(" "*30 + "GRC FRAMEWORK CONTROL MAPPER")
    print(" "*20 + "Map controls across NIST AI RMF, ISO 42001, and EU AI Act")
    print("="*100 + "\n")


def print_help():
    """Print usage instructions"""
    print("\nHow to use this tool:")
    print("  1. Enter a control description or keywords (e.g., 'risk management', 'bias')")
    print("  2. The tool will search across all frameworks and show matching controls")
    print("  3. Results are scored by relevance (higher = better match)")
    print("\nCommands:")
    print("  'help'  - Show this help message")
    print("  'list'  - List all available control mappings")
    print("  'quit'  - Exit the program")
    print()


def list_all_controls(mapper):
    """Display all available control mappings"""
    print(f"\n{'='*100}")
    print(f"ALL AVAILABLE CONTROL MAPPINGS ({len(mapper.mappings)} total)")
    print(f"{'='*100}\n")

    for i, mapping in enumerate(mapper.mappings, 1):
        print(f"[{i}] {mapping['id']} - {mapping['category']}")
        print(f"    {mapping['description']}")
        print(f"    Keywords: {', '.join(mapping.get('keywords', []))}")
        print()


def main():
    """Main program loop"""
    # Print welcome banner
    print_banner()

    # Initialize the mapper (loads the JSON file)
    mapper = ControlMapper()

    # Print instructions
    print_help()

    # Main interaction loop
    while True:
        try:
            # Get user input
            query = input("Enter control description or keywords (or 'help'/'list'/'quit'): ").strip()

            # Handle empty input
            if not query:
                print("Please enter a search query.\n")
                continue

            # Handle commands
            if query.lower() == 'quit':
                print("\nThank you for using GRC Framework Control Mapper!\n")
                break
            elif query.lower() == 'help':
                print_help()
                continue
            elif query.lower() == 'list':
                list_all_controls(mapper)
                continue

            # Perform the search
            results = mapper.search_controls(query)

            # Display results
            mapper.format_table(results)

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nExiting... Goodbye!\n")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again.\n")


# This is the entry point when running the script
if __name__ == "__main__":
    main()
