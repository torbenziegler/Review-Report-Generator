# Review Report Generator

## Overview
This script helps you quickly understand customer opinions based on app reviews from the Google Play Store and Apple App Store. It extracts all review information and processes them to generate a review report in PDF format.

## Features
- **Extracts Reviews**: Fetches reviews from specified app URLs.
- **Generates PDF Reports**: Compiles reviews into a well-formatted PDF report.

## Planned Features
- [x] Crawl App Store reviews
- [ ] Crawl Play Store reviews
- [x] Export to PDF
- [ ] Summary with ChatGPT in PDF
- [ ] Summary of stars, etc. (basic metadata section)
- [ ] Summary of app info (crawled from store info)

## Usage

### Prerequisites
Ensure you have Python installed along with the required libraries:
- `requests`
- `beautifulsoup4`
- `reportlab`

Install the required libraries using pip:
```bash
pip install requests beautifulsoup4 reportlab
```

### Running the Script

1. Open the script and replace the placeholder OPEN_AI_API_KEY with your actual OpenAI API key.
2. Specify the URL of the app's reviews page in the URL variable.
3. Run the script:

```bash
python review_report_generator.py
```

The script will generate a PDF file named `Review_Report.pdf` (default, if not specified otherwise) containing the extracted reviews.
