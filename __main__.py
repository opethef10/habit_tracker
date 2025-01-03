#! /usr/bin/env python3
import argparse
import calendar
from datetime import date, timedelta
from pathlib import Path

import yaml

DEFAULT_EMOJI = '✅'


def load_dates_from_yaml(file_path: Path) -> list[date]:
    """Load list of dates from the YAML file"""

    with file_path.open() as file:
        dates = yaml.safe_load(file)
    return dates


def generate_monthly_habit_markdown(dates: list[date], year: int, emoji: str) -> str:
    """Generate markdown for monthly template"""

    # Initialize the template for the table
    table = f'| {year} | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |\n'
    table += '|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n'

    rows = []

    # Create a row for each possible day
    for day in range(1, 32):
        row = [f"| {day}  "]
        for month in range(12):
            row.append('   ')  # Pre-fill empty cells for each month
        rows.append(row)

    # Place emoji in the appropriate cell based on the dates
    for date_obj in dates:
        if date_obj.year == year:
            day = date_obj.day
            month = date_obj.month
            rows[day-1][month] = f" {emoji} "  # Fill emoji in corresponding month

    # Build the markdown table string
    for row in rows:
        table += '|'.join(row) + '|\n'

    # Add the total row
    total_row = ""
    total_of_totals = 0
    for month in range(12):
        # Count emojis for the month
        total = sum(1 for row in rows if row[month + 1].strip() == emoji)
        total_row += f"| **{total}** "
        total_of_totals += total

    total_row += "|"
    table += f"| **Σ: {total_of_totals}**" + total_row + '\n'

    return table


def generate_weekly_habit_markdown(dates: list[date], year: int, emoji: str) -> str:
    """Generate markdown for weekly template"""

    # Initialize the weekly template header
    if args.japanese:
        table = f'| {year} | 月   | 火   | 水   | 木   | 金   | 土   | 日   |\n'
    else:
        table = f'| {year} | Mon | Tue | Wed | Thu | Fri | Sat | Sun |\n'
    table += '|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n'

    # Get the first date of the year and adjust to first Monday
    first_date = date(year, 1, 1)
    first_date_weekday = first_date.weekday()
    current_date = first_date - timedelta(days=first_date_weekday)
    offset = int(first_date_weekday != calendar.MONDAY)

    rows = []

    # Iterate week by week until the end of the year
    while current_date.year <= year:
        row = [f"{current_date:%d/%m} "]
        for _ in range(7):
            row.append('   ')  # Fill the row with empty cell for each day of the week
        rows.append(row)
        current_date += timedelta(days=7)  # Move to the next Monday

    # Fill in emoji for dates that match
    for date_obj in dates:
        if date_obj.year == year:
            iso_year, iso_week, iso_weekday = date_obj.isocalendar()  # Get the ISO week number
            if iso_year < date_obj.year:  # Adjust for previous year edge case
                rows[0][iso_weekday] = f" {emoji} "
            else:
                rows[iso_week - 1 + offset][iso_weekday] = f" {emoji} "

    # Build the final table
    for row in rows:
        table += '| ' + '|'.join(row) + '|\n'

    return table


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments for the script."""

    parser = argparse.ArgumentParser(description='Generate habit markdown from YAML date list.')
    parser.add_argument(
        'yaml_file', type=str,
        help='Path to the YAML file containing habit completion dates.'
    )
    parser.add_argument(
        '-y', '--year', type=int, default=date.today().year,
        help='Year to filter the habit dates for (default is current year).'
    )
    parser.add_argument(
        '-e', '--emoji', type=str, default=DEFAULT_EMOJI,
        help='Emoji or character to represent completed habits (default is ✅).'
    )
    parser.add_argument(
        '-w', '--weekly', action='store_true',
        help='Use the weekly habit tracking template.'
    )
    parser.add_argument(
        '-j', '--japanese', action='store_true',
        help='Use Japanese kanji for the days of the week'
    )
    parser.add_argument(
        '-o', '--output', type=str,
        help='Path to save the markdown file (if not specified, output will be printed to stdout).'
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    # Load the dates from the provided YAML file
    input_path = Path(args.yaml_file)
    dates = load_dates_from_yaml(input_path)

    # Generate the markdown based on the template type (weekly or monthly)
    if args.weekly:
        markdown_output = generate_weekly_habit_markdown(dates, args.year, args.emoji)
    else:
        markdown_output = generate_monthly_habit_markdown(dates, args.year, args.emoji)

    if args.output:
        # Save the markdown output to the given path
        output_path = Path(args.output)
        with output_path.open('w') as file:
            file.write(markdown_output)
    else:
        # Output the markdown to the console
        print(markdown_output)
