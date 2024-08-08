# Review Report Generator

## Overview

This script helps you quickly understand customer opinions based on app reviews from the Google Play Store and Apple App Store. It extracts all review information and processes them to generate a review report in PDF format.

## Features

- **Extracts Reviews**: Fetches reviews for specified apps and creates a summary of latest impressions.
- **Generates PDF Reports**: Compiles data into a well-formatted PDF factsheet report.

## Planned Features

- [x] Crawl Play Store reviews
- [ ] Crawl App Store reviews
- [x] Export to PDF
- [x] Summary with ChatGPT in PDF
- [x] Summary of stars, etc. (basic metadata section)
- [ ] Summary of app info (crawled from store info)
- [x] Flask API
- [x] Frontend (SveltKit + Flowbite)

## Usage

### Prerequisites

Ensure you have Python installed along with the required libraries as specifed in [requirements.txt](./requirements.txt).

Install the required libraries using pip:

```bash
pip install -r "requirements.txt"
```

### Running the Script

TBD

The script will generate a PDF file named `Review_Report.pdf` (default, if not specified otherwise) containing the extracted data as fact sheet.

### Frontend

TBD

Enter the app's package name and retrieve the report.
