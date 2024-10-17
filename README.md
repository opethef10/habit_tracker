# Habit Tracker Markdown Generator

This Python script generates a markdown table to track daily habit completions, either in a **weekly** or **monthly** format, based on the dates provided in a YAML file. You can mark completed habits using an emoji or character of your choice.

## Features

- **Weekly View**: Generates a table where each row represents a week, and each column corresponds to a day of the week, starting from Monday.
- **Monthly View**: Generates a table with months as columns and days as rows, allowing you to visualize habit tracking over the entire year.
- **Custom Emojis/Markers**: Mark completed habits with any emoji or character you like (default is ✅).
- **Flexible Year Selection**: Filter the habit dates by specifying a year. If not provided, the current year is used by default.
- **Supports YAML Input**: The script reads habit completion dates from a YAML file in the format `YYYY-MM-DD`.

## Installation

1. Ensure you have Python 3.9 or later installed.
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Create a YAML file containing a list of dates where you completed a habit. **Dates should be in ISO format (`YYYY-MM-DD`), without quotes or special formatting**. Each date should be in a separate line. You can check the `example.yaml` file for reference.
    ```yaml
    - 2024-01-03
    - 2024-01-10
    - 2024-02-15
    - 2024-03-20
    ```

2. Run the script with your YAML file and desired options:

    ### Monthly View (Default)
    ```bash
    python3 habits.py habits.yaml
    ```
    This generates a monthly habit table for the current year

    ### Weekly View
    ```bash
    python3 habits.py habits.yaml --weekly
    ```
    This generates a weekly habit table for 2024, using the ⭐ emoji to mark completed habits.

## Command-Line Options

| Option                | Description                                                              |
|-----------------------|--------------------------------------------------------------------------|
| `yaml_file`           | Path to the YAML file containing habit completion dates.                 |
| `-y`, `--year`        | Year to filter the habit dates (default: current year).                  |
| `-e`, `--emoji`       | Emoji or character to represent completed habits (default: ✅).          |
| `-w`, `--weekly`      | Use the weekly habit tracking template instead of the monthly template.  |
| `-o`, `--output`      | Path to save the generated markdown file (default is to print to stdout).|

## Examples

#### Generate Monthly Habit Markdown for 2022 and Save to File
```bash
python3 habits.py habits.yaml -y 2022 -o monthly_habits.md
```
This will generate a markdown table for the year 2022 in monthly view and save it to `monthly_habits.md`.

#### Generate Weekly Habit Markdown with Custom Emoji
```bash
python3 habits.py habits.yaml -w -y 2024 -e 🔥 -o weekly_habits.md
```
This will generate a markdown table for weekly tracking in 2024, using 🔥 as the marker for completed habits and save it to `weekly_habits.md`.

#### Custom Year with Weekly Format and Default Emoji
```bash
python3 habits.py habits.yaml -w -y 2023 -o my_habits.md
```
Generates a weekly habit table for the year 2023 and saves it to `my_habits.md`.

## Output

The script generates markdown tables like these:

### Monthly View Example:
```markdown
| 2024 | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 01  |     |     |     |     |     |     |     |     |     |     |     |     |
| 02  |     |     |     |     |     |     |     |     |     |     |     |     |
| 03  | ✅  |     |     |     |     |     |     |     |     |     |     |     |
...
```

### Weekly View Example:
```markdown
| 2024 | 月   | 火   | 水   | 木   | 金   | 土   | 日   |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 01/01 |     |     | ✅  |     |     |     |     |
| 08/01 |     |     |     |     |     |     |     |
...
```
