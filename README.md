# Nylas Accounts Extractor

This Python script, developed by `wallacecs007`, interfaces with the Nylas API to extract account information, specifically targeting Microsoft accounts with password authentication, excluding personal account domains like Outlook, Hotmail, and MSN. The extracted data is then stored in a CSV file for further analysis or use.

## Features

- **API Integration**: Connects to the Nylas API to fetch account data.
- **Microsoft Account Filtering**: Filters out Microsoft accounts with 'password' authentication type.
- **Domain Exclusion**: Excludes personal Microsoft account domains.
- **CSV Export**: Outputs relevant account data to a CSV file.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your system.
- The `requests` library installed. You can install it using `pip install requests`.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/nylas-samples/nylas-accounts-extractor.git
cd nylas-accounts-extractor
