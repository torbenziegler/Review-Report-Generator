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
- [ ] Flask API
- [ ] Frontend (SveltKit + Flowbite)

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
