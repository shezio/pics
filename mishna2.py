import calendar
from datetime import datetime as dt, timedelta
import requests
import urllib3

# Disable the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Set the first weekday to Sunday
calendar.setfirstweekday(calendar.SUNDAY)

# Define the masechtot dictionary
masechtot = {
    "ברכות": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
    ],
    "פאה": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה", "פרק ו", "פרק ז", "פרק ח"],
    "דמאי": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה", "פרק ו", "פרק ז"],
    "כלאים": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
    ],
    "שביעית": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
    ],
    "תרומות": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
        "פרק יא",
    ],
    "מעשרות": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה"],
    "מעשר שני": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה"],
    "חלה": ["פרק א", "פרק ב", "פרק ג", "פרק ד"],
    "עורלה": ["פרק א", "פרק ב", "פרק ג"],
    "ביכורים": ["פרק א", "פרק ב", "פרק ג", "פרק ד"],
    "שבת": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
        "פרק יא",
        "פרק יב",
        "פרק יג",
        "פרק יד",
        "פרק טו",
        "פרק טז",
        "פרק יז",
        "פרק יח",
        "פרק יט",
        "פרק כ",
        "פרק כא",
        "פרק כב",
        "פרק כג",
        "פרק כד",
    ],
    "עירובין": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
    ],
    "פסחים": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
    ],
    "שקלים": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה", "פרק ו", "פרק ז", "פרק ח"],
    "יומא": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה", "פרק ו", "פרק ז", "פרק ח"],
    "סוכה": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה"],
    "ביצה": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה"],
    "ראש השנה": ["פרק א", "פרק ב", "פרק ג", "פרק ד"],
    "תענית": ["פרק א", "פרק ב", "פרק ג", "פרק ד"],
    "מגילה": ["פרק א", "פרק ב", "פרק ג", "פרק ד"],
    "מועד קטן": ["פרק א", "פרק ב", "פרק ג"],
    "חגיגה": ["פרק א", "פרק ב", "פרק ג"],
    "יבמות": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
        "פרק יא",
        "פרק יב",
        "פרק יג",
        "פרק יד",
        "פרק טו",
        "פרק טז",
    ],
    "כתובות": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
        "פרק יא",
        "פרק יב",
        "פרק יג",
    ],
    "נדרים": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
        "פרק יא",
    ],
    "נזיר": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
    ],
    "סוטה": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
    ],
    "גיטין": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
    ],
    "קידושין": ["פרק א", "פרק ב", "פרק ג", "פרק ד"],
    "בבא קמא": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
    ],
    "בבא מציעא": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
    ],
    "בבא בתרא": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
    ],
    "סנהדרין": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
        "פרק יא",
    ],
    "מכות": ["פרק א", "פרק ב", "פרק ג"],
    "שבועות": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה", "פרק ו", "פרק ז", "פרק ח"],
    "עדיות": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה", "פרק ו", "פרק ז", "פרק ח"],
    "עבודה זרה": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה"],
    "אבות": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה", "פרק ו"],
    "הוריות": ["פרק א", "פרק ב", "פרק ג"],
    "זבחים": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
        "פרק יא",
        "פרק יב",
        "פרק יג",
        "פרק יד",
    ],
    "מנחות": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
        "פרק יא",
        "פרק יב",
        "פרק יג",
    ],
    "חולין": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
        "פרק יא",
        "פרק יב",
    ],
    "בכורות": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
    ],
    "ערכין": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
    ],
    "תמורה": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה", "פרק ו", "פרק ז"],
    "כריתות": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה", "פרק ו"],
    "מעילה": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה", "פרק ו"],
    "תמיד": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה", "פרק ו", "פרק ז"],
    "מדות": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה"],
    "קינים": ["פרק א", "פרק ב", "פרק ג"],
    "כלים": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
        "פרק יא",
        "פרק יב",
        "פרק יג",
        "פרק יד",
        "פרק טו",
        "פרק טז",
        "פרק יז",
        "פרק יח",
        "פרק יט",
        "פרק כ",
        "פרק כא",
        "פרק כב",
        "פרק כג",
        "פרק כד",
        "פרק כה",
        "פרק כו",
        "פרק כז",
        "פרק כח",
        "פרק כט",
        "פרק ל",
    ],
    "אהלות": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
        "פרק יא",
        "פרק יב",
        "פרק יג",
        "פרק יד",
        "פרק טו",
        "פרק טז",
        "פרק יז",
        "פרק יח",
    ],
    "נגעים": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
        "פרק יא",
        "פרק יב",
        "פרק יג",
        "פרק יד",
    ],
    "פרה": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
        "פרק יא",
        "פרק יב",
    ],
    "טהרות": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
    ],
    "מקואות": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
    ],
    "נידה": [
        "פרק א",
        "פרק ב",
        "פרק ג",
        "פרק ד",
        "פרק ה",
        "פרק ו",
        "פרק ז",
        "פרק ח",
        "פרק ט",
        "פרק י",
    ],
    "מכשירין": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה", "פרק ו"],
    "זבים": ["פרק א", "פרק ב", "פרק ג", "פרק ד", "פרק ה"],
    "טבול יום": ["פרק א", "פרק ב", "פרק ג", "פרק ד"],
    "ידים": ["פרק א", "פרק ב", "פרק ג", "פרק ד"],
    "עוקצין": ["פרק א", "פרק ב", "פרק ג"],
}
# Define the start date and the current masechet and chapter
current_masechet = "סוכה"
current_chapter = "פרק ב"

# Define the Hebrew days of the week
hebrew_days = [
    "יום שני",
    "יום שלישי",
    "יום רביעי",
    "יום חמישי",
    "יום שישי",
    "יום שבת",
    "יום ראשון",
]


# Calculate the total number of chapters until the current masechet and chapter
total_chapters_start = 0
for masechet, chapters in masechtot.items():
    if masechet == current_masechet:
        total_chapters_start += chapters.index(current_chapter) + 1
        break
    total_chapters_start += len(chapters)

# Calculate the start date based on today's date and the total number of chapters
today = dt.now()
start_date = today - timedelta(days=total_chapters_start)

# start_date = dt(2023, 9, 2)
# Calculate the total number of chapters until "עוקצין פרק ג"
total_chapters_end = 0
for masechet, chapters in masechtot.items():
    if masechet == "עוקצין" and "פרק ג" in chapters:
        total_chapters_end += chapters.index("פרק ג") + 1
        break
    total_chapters_end += len(chapters)

# Calculate the end date based on the start date and the total number of chapters
# set end date to two weeks from start date
# end_date = start_date + timedelta(days=14)

# set end date to end of masechetot
end_date = start_date + timedelta(days=total_chapters_end)

# Set the end date to today (or two weeks from today)
# end_date = today  # or today + timedelta(weeks=2)


# Define the function to get the Hebrew date
def get_hebrew_date(date): # pylint: disable=unused-variable redefined-outer-name missing-function-docstring
    response = requests.get( # pylint: redefined-outer-name
        f"https://www.hebcal.com/converter?cfg=json&gy={date.year}&gm={date.month}&gd={date.day}&g2h=1",
        verify=False, timeout=600
    )
    hebrew_date = response.json()["hebrew"]
    return hebrew_date


# Define the function to get the daily mishna
def get_daily_mishna(date):
    days_since_start = (date - start_date).days
    total_chapters = 0
    for masechet, chapters in masechtot.items():
        if days_since_start < total_chapters + len(chapters):
            current_masechet = masechet
            current_chapter = chapters[days_since_start - total_chapters]
            break
        total_chapters += len(chapters)
    return current_masechet, current_chapter


# Generate the calendar
html = """
<html dir='rtl'>
   <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #F5F5F5;
                color: #333;
            }
            h1, h2 {
                color: #333;
            }
            h1 {
                font-size: 36px;
            }
            h2 {
                font-size: 30px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th {
                background-color: #4CAF50;
                color: white;
            }
            td {
                font-size: 16px;
                padding: 8px;
                text-align: center;
                border-bottom: 1px solid #ddd;
            }
            td:nth-child(even) {
                background-color: #f2f2f2;
            }
        </style>
        <script type="text/javascript">
            window.onload = function() {
                var img = document.createElement("img");
                img.src = "https://raw.githubusercontent.com/shezio/pics/main/AMIT2.png";
                img.width = 800;
                // Append the image to the body of the document
                document.getElementById("2024").appendChild(img);
            }
        </script>
    </head>
<body>
<div style="display: flex; gap: 25px; width: 100%; margin-bottom: 15px; justify-content: space-between;">
    <div style="margin-inline-start: 50px; margin-block-start: 100px;">
        <h1>לוח שנה לפרקי משנה</h1>
        <h2>לעילוי נשמת עמית בן נועה בונצל הי"ד מפקד ולוחם שנפל בקרב בעזה</h2>
    </div>
    <div id="2024"></div>
</div>
<table border='1'>
"""

for year in range(start_date.year, end_date.year + 1):
    for month in range(
        start_date.month if year == start_date.year else 1,
        end_date.month + 1 if year == end_date.year else 13,
    ):
        response = requests.get(
            f"https://www.hebcal.com/converter?cfg=json&gy={year}&gm={month}&gd=1&g2h=1",
            verify=False,
        )
        hebrew_date = response.json()["hebrew"]
        split_hebrew_date = hebrew_date.split(" ")
        if len(split_hebrew_date) == 4:
            _, hebrew_month, _, hebrew_year = split_hebrew_date
        else:
            _, hebrew_month, hebrew_year = split_hebrew_date

        hebrew_months = [
            "",  # There is no month 0
            "ינואר",
            "פברואר",
            "מרץ",
            "אפריל",
            "מאי",
            "יוני",
            "יולי",
            "אוגוסט",
            "ספטמבר",
            "אוקטובר",
            "נובמבר",
            "דצמבר",
        ]
        hebrew_month = hebrew_month[3:]  # Remove the first character
        html += f"<tr><th colspan='7'>{hebrew_months[month]} {year}</th></tr>"
        month_calendar = calendar.monthcalendar(year, month)
        for week in month_calendar:
            html += "<tr>"
            for day in week:
                if day != 0:
                    date = dt(year, month, day)
                    print(date)
                    if start_date <= date <= end_date:
                        daily_mishna = get_daily_mishna(date)
                        hebrew_date = get_hebrew_date(date)
                        html += f"<td style='background-color: white; color: blue;'>{date.strftime('%d.%m.%Y')}<br>{hebrew_date}<br>{hebrew_days[date.weekday()]}<br>הפרק היומי הוא {daily_mishna[0]} {daily_mishna[1]}</td>"
                    else:
                        html += "<td></td>"
                else:
                    html += "<td></td>"
            html += "</tr>"
html += "</table></body></html>"


# Write the HTML to a file
with open("mishna_calendar.html", "w", encoding="utf-8") as file:
    file.write(html)
