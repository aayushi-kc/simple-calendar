from flask import Flask
import calendar
from datetime import datetime

app = Flask(__name__)

# Expanded Nepali calendar data (2015-2030)
# Format: {year: {month: (nepali_month_name, days_in_month)}}
NEPALI_CALENDAR = {
    2015: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2016: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2017: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2018: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2019: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2020: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2021: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2022: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2023: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2024: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2025: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2026: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2027: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2028: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2029: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    },
    2030: {
        1: ("पुष", 30),
        2: ("माघ", 29),
        3: ("फाल्गुन", 30),
        4: ("चैत्र", 31),
        5: ("वैशाख", 31),
        6: ("जेठ", 31),
        7: ("आषाढ", 31),
        8: ("श्रावण", 31),
        9: ("भदौ", 31),
        10: ("असोज", 30),
        11: ("कार्तिक", 29),
        12: ("मंसिर", 30)
    }
}

# Nepali month names (for when specific year data is not available)
NEPALI_MONTHS = [
    "बैशाख", "जेठ", "आषाढ", "श्रावण", "भदौ", "असोज", "कार्तिक", "मंसिर", "पुष",
    "माघ", "फाल्गुन", "चैत्र"
]

# Nepali weekday names
NEPALI_WEEKDAYS = [
    "आइतबार", "सोमबार", "मङ्गलबार", "बुधबार", "बिहिबार", "शुक्रबार", "शनिबार"
]


# Simple Gregorian to Nepali date conversion (approximate)
def gregorian_to_nepali(year, month, day):
    try:
        # Base date: 2023-01-01 = 2079-09-17 (approximate)
        base_date = datetime(2023, 1, 1)
        target_date = datetime(year, month, day)

        # Calculate days difference
        days_diff = (target_date - base_date).days

        # Calculate approximate Nepali year
        nepali_year = 2079 + (days_diff // 365)

        # Calculate approximate Nepali month
        nepali_month_num = (9 + (days_diff % 365) // 30) % 12
        if nepali_month_num == 0:
            nepali_month_num = 12

        # Get Nepali month name
        nepali_month_name = NEPALI_MONTHS[(nepali_month_num - 1) % 12]

        return nepali_year, nepali_month_num, nepali_month_name
    except:
        # Fallback to current year approximation
        return 2080 + (year - 2023), month, NEPALI_MONTHS[(month - 1) % 12]


def get_nepali_date_info(year, month, day):
    """Get Nepali date information"""
    try:
        nepali_year, nepali_month, nepali_month_name = gregorian_to_nepali(
            year, month, day)

        # Get Nepali weekday
        weekday = datetime(year, month, day).weekday()
        nepali_weekday = NEPALI_WEEKDAYS[weekday]

        return {
            'year': nepali_year,
            'month': nepali_month,
            'month_name': nepali_month_name,
            'weekday': nepali_weekday,
            'day': day
        }
    except:
        # Return fallback information
        return {
            'year': 2080,
            'month': month,
            'month_name': NEPALI_MONTHS[(month - 1) % 12],
            'weekday': NEPALI_WEEKDAYS[datetime.now().weekday()],
            'day': day
        }


def generate_nepali_calendar(year, month):
    """Generate a simple Nepali calendar display"""
    try:
        # Get Nepali year and month
        nepali_year, nepali_month, nepali_month_name = gregorian_to_nepali(
            year, month, 15)

        # Check if we have data for this year
        if nepali_year in NEPALI_CALENDAR and nepali_month in NEPALI_CALENDAR[
                nepali_year]:
            month_name, days = NEPALI_CALENDAR[nepali_year][nepali_month]
        else:
            # Use generic month data
            month_name = nepali_month_name
            days = 30  # Default days for Nepali month

        # Create calendar header
        header = f"{month_name} {nepali_year}"
        week_header = "आइ सो मं बु बि शु श"

        # Create calendar grid
        cal_lines = [f"{header:^21}", week_header]

        # Get the day of week for the first day of month
        # This is approximate - in real implementation would need accurate data
        first_weekday = 0  # Default to Sunday

        # Start the first line
        current_line = ""

        # Add empty spaces for days before the first day
        for _ in range(first_weekday):
            current_line += "   "

        # Add days
        for day_num in range(1, days + 1):
            if len(current_line) >= 20:  # Start new line
                cal_lines.append(current_line)
                current_line = ""

            current_line += f"{day_num:2} "

        # Add the last line if not empty
        if current_line:
            cal_lines.append(current_line)

        return "\n".join(cal_lines)
    except Exception as e:
        # Return a simple fallback calendar
        nepali_year, nepali_month, nepali_month_name = gregorian_to_nepali(
            year, month, 15)
        return f"{nepali_month_name} {nepali_year}\n\nनेपाली पात्रो\n(अनुमानित)\n\nदिनहरू: ३०"


@app.route('/')
def home():
    # Get current date
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    # Generate Gregorian calendar
    month_name = calendar.month_name[month]
    cal = calendar.month(year, month)

    # Highlight today in the calendar
    today_str = f' {day} ' if day < 10 else f'{day} '
    cal_highlighted = cal.replace(today_str, f'[{day}]')

    # Get Nepali date information
    nepali_date = get_nepali_date_info(year, month, day)

    # Generate Nepali calendar
    nepali_cal = generate_nepali_calendar(year, month)

    # Simple HTML with responsive design
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>📅 Dual Calendar | English & Nepali</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}

            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
                padding: 15px;
            }}

            .calendar-box {{
                background: white;
                padding: 25px 20px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 800px;
                width: 100%;
                margin: 10px;
            }}

            h1 {{
                color: #333;
                margin-bottom: 8px;
                font-size: clamp(1.5rem, 4vw, 2rem);
            }}

            .calendar-container {{
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                justify-content: center;
                margin: 20px 0;
            }}

            .calendar-section {{
                flex: 1;
                min-width: 300px;
                max-width: 400px;
            }}

            .section-title {{
                color: #667eea;
                font-size: clamp(1.2rem, 3vw, 1.5rem);
                font-weight: bold;
                margin: 15px 0;
                padding-bottom: 5px;
                border-bottom: 2px solid #667eea;
            }}

            .nepali-title {{
                color: #ff6b6b;
                border-color: #ff6b6b;
            }}

            .calendar {{
                background: #f8f9fa;
                padding: 15px;
                border-radius: 10px;
                font-family: monospace;
                font-size: clamp(0.9rem, 2.5vw, 1.1rem);
                white-space: pre;
                text-align: center;
                margin: 15px 0;
                border: 2px solid #e9ecef;
                overflow-x: auto;
                min-height: 200px;
                display: flex;
                align-items: center;
                justify-content: center;
            }}

            .nepali-calendar {{
                font-family: 'Arial Unicode MS', 'Noto Sans Devanagari', 'Mangal', sans-serif;
                direction: ltr;
            }}

            .today {{
                background: #ff6b6b;
                color: white;
                padding: 2px 4px;
                border-radius: 3px;
                font-weight: bold;
            }}

            .date-info {{
                display: flex;
                flex-wrap: wrap;
                gap: 15px;
                justify-content: center;
                margin: 20px 0;
            }}

            .info-box {{
                background: #e8f5e9;
                padding: 15px;
                border-radius: 10px;
                font-weight: bold;
                color: #2e7d32;
                font-size: clamp(0.9rem, 2.5vw, 1rem);
                flex: 1;
                min-width: 250px;
            }}

            .nepali-info {{
                background: #fff3e0;
                color: #e65100;
            }}

            .nav-buttons {{
                display: flex;
                justify-content: center;
                gap: 10px;
                margin-top: 20px;
                flex-wrap: wrap;
            }}

            .nav-btn {{
                background: #667eea;
                color: white;
                border: none;
                padding: clamp(10px, 3vw, 12px) clamp(20px, 4vw, 25px);
                border-radius: 8px;
                cursor: pointer;
                font-size: clamp(14px, 3vw, 16px);
                transition: all 0.3s;
                min-width: 120px;
                flex: 1;
                max-width: 150px;
            }}

            .nav-btn:hover, .nav-btn:active {{
                background: #764ba2;
                transform: translateY(-2px);
            }}

            .today-btn {{
                background: #ff6b6b;
            }}

            .today-btn:hover, .today-btn:active {{
                background: #ff5252;
            }}

            .footer {{
                margin-top: 20px;
                color: #666;
                font-size: clamp(0.8rem, 2vw, 0.9rem);
                text-align: center;
            }}

            .language-toggle {{
                margin-bottom: 15px;
            }}

            .toggle-btn {{
                background: #4CAF50;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 5px;
                cursor: pointer;
                font-size: 14px;
                margin: 0 5px;
                transition: all 0.3s;
            }}

            .toggle-btn:hover {{
                background: #45a049;
                transform: translateY(-1px);
            }}

            .note {{
                font-size: 0.8rem;
                color: #666;
                margin-top: 10px;
                font-style: italic;
            }}

            /* Mobile-specific adjustments */
            @media (max-width: 768px) {{
                body {{
                    padding: 10px;
                    align-items: flex-start;
                }}

                .calendar-box {{
                    padding: 20px 15px;
                    margin: 5px;
                }}

                .calendar-section {{
                    min-width: 100%;
                }}

                .calendar {{
                    padding: 10px;
                    font-size: 0.9rem;
                    min-height: 180px;
                }}

                .nav-buttons {{
                    flex-direction: row;
                    gap: 8px;
                }}

                .nav-btn {{
                    min-width: 100px;
                    padding: 10px 15px;
                    font-size: 14px;
                }}

                .info-box {{
                    min-width: 100%;
                }}
            }}

            /* Tablet adjustments */
            @media (min-width: 769px) and (max-width: 1024px) {{
                .calendar-box {{
                    max-width: 700px;
                }}
            }}

            /* Touch device improvements */
            @media (hover: none) {{
                .nav-btn:hover, .toggle-btn:hover {{
                    transform: none;
                }}

                .nav-btn:active, .toggle-btn:active {{
                    transform: scale(0.98);
                }}
            }}
        </style>
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari&display=swap" rel="stylesheet">
    </head>
    <body>
        <div class="calendar-box">
            <h1>📅 Dual Calendar</h1>
            <div class="language-toggle">
                <button class="toggle-btn" onclick="showGregorian()">English</button>
                <button class="toggle-btn" onclick="showNepali()">नेपाली</button>
                <button class="toggle-btn" onclick="showBoth()">Both</button>
            </div>

            <div class="date-info">
                <div class="info-box">
                    📍 English Date:<br>
                    {now.strftime("%A, %B %d, %Y")}<br>
                    <span class="note">(Gregorian Calendar)</span>
                </div>
                <div class="info-box nepali-info">
                    📍 नेपाली मिति:<br>
                    {nepali_date['weekday']}, {nepali_date['month_name']} {nepali_date['day']}, {nepali_date['year']} BS<br>
                    <span class="note">(विक्रम संवत्, अनुमानित)</span>
                </div>
            </div>

            <div class="calendar-container" id="calendarContainer">
                <div class="calendar-section">
                    <div class="section-title">English Calendar</div>
                    <div class="calendar" id="englishCalendar">
                        {cal_highlighted}
                    </div>
                </div>
                <div class="calendar-section">
                    <div class="section-title nepali-title">नेपाली पात्रो</div>
                    <div class="calendar nepali-calendar" id="nepaliCalendar">
                        {nepali_cal}
                    </div>
                </div>
            </div>

            <div class="nav-buttons">
                <button class="nav-btn" onclick="changeMonth(-1)">◀ Previous</button>
                <button class="nav-btn today-btn" onclick="goToday()">Today / आज</button>
                <button class="nav-btn" onclick="changeMonth(1)">Next ▶</button>
            </div>

            <div class="footer">
                prepared by: Aayushi KC | English & Nepali Calendar<br>
                <span class="note">Note: Nepali dates are approximate. For accurate dates, refer to official Nepali calendar.</span>
            </div>
        </div>

        <script>
            let currentMonth = {month};
            let currentYear = {year};

            function changeMonth(direction) {{
                // Update month
                currentMonth += direction;

                // Handle year wrap-around
                if (currentMonth > 12) {{
                    currentMonth = 1;
                    currentYear += 1;
                }} else if (currentMonth < 1) {{
                    currentMonth = 12;
                    currentYear -= 1;
                }}

                // Reload page with new month
                window.location.href = `/${{currentYear}}/${{currentMonth}}`;
            }}

            function goToday() {{
                window.location.href = '/';
            }}

            function showGregorian() {{
                document.getElementById('englishCalendar').style.display = 'flex';
                document.getElementById('nepaliCalendar').style.display = 'none';
                document.querySelectorAll('.calendar-section')[1].style.display = 'none';
            }}

            function showNepali() {{
                document.getElementById('englishCalendar').style.display = 'none';
                document.getElementById('nepaliCalendar').style.display = 'flex';
                document.querySelectorAll('.calendar-section')[0].style.display = 'none';
                document.querySelectorAll('.calendar-section')[1].style.display = 'block';
            }}

            function showBoth() {{
                document.getElementById('englishCalendar').style.display = 'flex';
                document.getElementById('nepaliCalendar').style.display = 'flex';
                document.querySelectorAll('.calendar-section')[0].style.display = 'block';
                document.querySelectorAll('.calendar-section')[1].style.display = 'block';
            }}

            // Add keyboard shortcuts
            document.addEventListener('keydown', (event) => {{
                if (event.key === 'ArrowLeft') {{
                    changeMonth(-1);
                }} else if (event.key === 'ArrowRight') {{
                    changeMonth(1);
                }} else if (event.key === 't' || event.key === 'T') {{
                    goToday();
                }} else if (event.key === '1') {{
                    showGregorian();
                }} else if (event.key === '2') {{
                    showNepali();
                }} else if (event.key === '3') {{
                    showBoth();
                }}
            }});

            // Touch swipe support for mobile
            let touchStartX = 0;
            let touchEndX = 0;

            document.body.addEventListener('touchstart', (e) => {{
                touchStartX = e.changedTouches[0].screenX;
            }}, false);

            document.body.addEventListener('touchend', (e) => {{
                touchEndX = e.changedTouches[0].screenX;
                handleSwipe();
            }}, false);

            function handleSwipe() {{
                const swipeThreshold = 50;
                const diff = touchStartX - touchEndX;

                if (Math.abs(diff) > swipeThreshold) {{
                    if (diff > 0) {{
                        // Swipe left - next month
                        changeMonth(1);
                    }} else {{
                        // Swipe right - previous month
                        changeMonth(-1);
                    }}
                }}
            }}

            // Show both calendars by default
            showBoth();
        </script>
    </body>
    </html>
    '''

    return html


@app.route('/<int:year>/<int:month>')
def specific_month(year, month):
    # Validate month
    if month < 1 or month > 12:
        month = datetime.now().month

    # Get today's date for comparison
    now = datetime.now()
    today_day = now.day if year == now.year and month == now.month else None

    # Generate Gregorian calendar
    month_name = calendar.month_name[month]
    cal = calendar.month(year, month)

    # Highlight today if it's the current month
    if today_day:
        today_str = f' {today_day} ' if today_day < 10 else f'{today_day} '
        cal = cal.replace(today_str, f'[{today_day}]')

    # Get Nepali date information for today or middle of month
    display_day = today_day if today_day else 15
    nepali_date = get_nepali_date_info(year, month, display_day)

    # Generate Nepali calendar
    nepali_cal = generate_nepali_calendar(year, month)

    # HTML
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>📅 Dual Calendar | {month_name} {year}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}

            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
                padding: 15px;
            }}

            .calendar-box {{
                background: white;
                padding: 25px 20px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 800px;
                width: 100%;
                margin: 10px;
            }}

            h1 {{
                color: #333;
                margin-bottom: 8px;
                font-size: clamp(1.5rem, 4vw, 2rem);
            }}

            .calendar-container {{
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                justify-content: center;
                margin: 20px 0;
            }}

            .calendar-section {{
                flex: 1;
                min-width: 300px;
                max-width: 400px;
            }}

            .section-title {{
                color: #667eea;
                font-size: clamp(1.2rem, 3vw, 1.5rem);
                font-weight: bold;
                margin: 15px 0;
                padding-bottom: 5px;
                border-bottom: 2px solid #667eea;
            }}

            .nepali-title {{
                color: #ff6b6b;
                border-color: #ff6b6b;
            }}

            .calendar {{
                background: #f8f9fa;
                padding: 15px;
                border-radius: 10px;
                font-family: monospace;
                font-size: clamp(0.9rem, 2.5vw, 1.1rem);
                white-space: pre;
                text-align: center;
                margin: 15px 0;
                border: 2px solid #e9ecef;
                overflow-x: auto;
                min-height: 200px;
                display: flex;
                align-items: center;
                justify-content: center;
            }}

            .nepali-calendar {{
                font-family: 'Arial Unicode MS', 'Noto Sans Devanagari', 'Mangal', sans-serif;
                direction: ltr;
            }}

            .today {{
                background: #ff6b6b;
                color: white;
                padding: 2px 4px;
                border-radius: 3px;
                font-weight: bold;
            }}

            .date-info {{
                display: flex;
                flex-wrap: wrap;
                gap: 15px;
                justify-content: center;
                margin: 20px 0;
            }}

            .info-box {{
                background: #e8f5e9;
                padding: 15px;
                border-radius: 10px;
                font-weight: bold;
                color: #2e7d32;
                font-size: clamp(0.9rem, 2.5vw, 1rem);
                flex: 1;
                min-width: 250px;
            }}

            .nepali-info {{
                background: #fff3e0;
                color: #e65100;
            }}

            .nav-buttons {{
                display: flex;
                justify-content: center;
                gap: 10px;
                margin-top: 20px;
                flex-wrap: wrap;
            }}

            .nav-btn {{
                background: #667eea;
                color: white;
                border: none;
                padding: clamp(10px, 3vw, 12px) clamp(20px, 4vw, 25px);
                border-radius: 8px;
                cursor: pointer;
                font-size: clamp(14px, 3vw, 16px);
                transition: all 0.3s;
                min-width: 120px;
                flex: 1;
                max-width: 150px;
            }}

            .nav-btn:hover, .nav-btn:active {{
                background: #764ba2;
                transform: translateY(-2px);
            }}

            .today-btn {{
                background: #ff6b6b;
            }}

            .today-btn:hover, .today-btn:active {{
                background: #ff5252;
            }}

            .footer {{
                margin-top: 20px;
                color: #666;
                font-size: clamp(0.8rem, 2vw, 0.9rem);
                text-align: center;
            }}

            .language-toggle {{
                margin-bottom: 15px;
            }}

            .toggle-btn {{
                background: #4CAF50;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 5px;
                cursor: pointer;
                font-size: 14px;
                margin: 0 5px;
                transition: all 0.3s;
            }}

            .toggle-btn:hover {{
                background: #45a049;
                transform: translateY(-1px);
            }}

            .note {{
                font-size: 0.8rem;
                color: #666;
                margin-top: 10px;
                font-style: italic;
            }}

            /* Mobile-specific adjustments */
            @media (max-width: 768px) {{
                body {{
                    padding: 10px;
                    align-items: flex-start;
                }}

                .calendar-box {{
                    padding: 20px 15px;
                    margin: 5px;
                }}

                .calendar-section {{
                    min-width: 100%;
                }}

                .calendar {{
                    padding: 10px;
                    font-size: 0.9rem;
                    min-height: 180px;
                }}

                .nav-buttons {{
                    flex-direction: row;
                    gap: 8px;
                }}

                .nav-btn {{
                    min-width: 100px;
                    padding: 10px 15px;
                    font-size: 14px;
                }}

                .info-box {{
                    min-width: 100%;
                }}
            }}

            /* Tablet adjustments */
            @media (min-width: 769px) and (max-width: 1024px) {{
                .calendar-box {{
                    max-width: 700px;
                }}
            }}

            /* Touch device improvements */
            @media (hover: none) {{
                .nav-btn:hover, .toggle-btn:hover {{
                    transform: none;
                }}

                .nav-btn:active, .toggle-btn:active {{
                    transform: scale(0.98);
                }}
            }}
        </style>
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari&display=swap" rel="stylesheet">
    </head>
    <body>
        <div class="calendar-box">
            <h1>📅 Dual Calendar</h1>
            <div class="language-toggle">
                <button class="toggle-btn" onclick="showGregorian()">English</button>
                <button class="toggle-btn" onclick="showNepali()">नेपाली</button>
                <button class="toggle-btn" onclick="showBoth()">Both</button>
            </div>

            <div class="date-info">
                <div class="info-box">
                    📅 Viewing: {month_name} {year}
                    {'<br>📍 Today is highlighted in red' if today_day else ''}
                    <br><span class="note">(Gregorian Calendar)</span>
                </div>
                <div class="info-box nepali-info">
                    📅 नेपाली: {nepali_date['month_name']} {nepali_date['year']}
                    {'<br>📍 आज रातो रंगमा देखाइएको छ' if today_day else ''}
                    <br><span class="note">(विक्रम संवत्, अनुमानित)</span>
                </div>
            </div>

            <div class="calendar-container" id="calendarContainer">
                <div class="calendar-section">
                    <div class="section-title">English Calendar</div>
                    <div class="calendar" id="englishCalendar">
                        {cal}
                    </div>
                </div>
                <div class="calendar-section">
                    <div class="section-title nepali-title">नेपाली पात्रो</div>
                    <div class="calendar nepali-calendar" id="nepaliCalendar">
                        {nepali_cal}
                    </div>
                </div>
            </div>

            <div class="nav-buttons">
                <button class="nav-btn" onclick="changeMonth(-1)">◀ Previous</button>
                <button class="nav-btn today-btn" onclick="goToday()">Today / आज</button>
                <button class="nav-btn" onclick="changeMonth(1)">Next ▶</button>
            </div>

            <div class="footer">
                Prepared by: Aayushi KC | English & Nepali Calendar<br>
                <span class="note">Note: Nepali dates are approximate. For accurate dates, refer to official Nepali calendar.</span>
            </div>
        </div>

        <script>
            let currentMonth = {month};
            let currentYear = {year};

            function changeMonth(direction) {{
                // Update month
                currentMonth += direction;

                // Handle year wrap-around
                if (currentMonth > 12) {{
                    currentMonth = 1;
                    currentYear += 1;
                }} else if (currentMonth < 1) {{
                    currentMonth = 12;
                    currentYear -= 1;
                }}

                // Reload page with new month
                window.location.href = `/${{currentYear}}/${{currentMonth}}`;
            }}

            function goToday() {{
                window.location.href = '/';
            }}

            function showGregorian() {{
                document.getElementById('englishCalendar').style.display = 'flex';
                document.getElementById('nepaliCalendar').style.display = 'none';
                document.querySelectorAll('.calendar-section')[1].style.display = 'none';
            }}

            function showNepali() {{
                document.getElementById('englishCalendar').style.display = 'none';
                document.getElementById('nepaliCalendar').style.display = 'flex';
                document.querySelectorAll('.calendar-section')[0].style.display = 'none';
                document.querySelectorAll('.calendar-section')[1].style.display = 'block';
            }}

            function showBoth() {{
                document.getElementById('englishCalendar').style.display = 'flex';
                document.getElementById('nepaliCalendar').style.display = 'flex';
                document.querySelectorAll('.calendar-section')[0].style.display = 'block';
                document.querySelectorAll('.calendar-section')[1].style.display = 'block';
            }}

            // Add keyboard shortcuts
            document.addEventListener('keydown', (event) => {{
                if (event.key === 'ArrowLeft') {{
                    changeMonth(-1);
                }} else if (event.key === 'ArrowRight') {{
                    changeMonth(1);
                }} else if (event.key === 't' || event.key === 'T') {{
                    goToday();
                }} else if (event.key === '1') {{
                    showGregorian();
                }} else if (event.key === '2') {{
                    showNepali();
                }} else if (event.key === '3') {{
                    showBoth();
                }}
            }});

            // Touch swipe support for mobile
            let touchStartX = 0;
            let touchEndX = 0;

            document.body.addEventListener('touchstart', (e) => {{
                touchStartX = e.changedTouches[0].screenX;
            }}, false);

            document.body.addEventListener('touchend', (e) => {{
                touchEndX = e.changedTouches[0].screenX;
                handleSwipe();
            }}, false);

            function handleSwipe() {{
                const swipeThreshold = 50;
                const diff = touchStartX - touchEndX;

                if (Math.abs(diff) > swipeThreshold) {{
                    if (diff > 0) {{
                        // Swipe left - next month
                        changeMonth(1);
                    }} else {{
                        // Swipe right - previous month
                        changeMonth(-1);
                    }}
                }}
            }}

            // Show both calendars by default
            showBoth();
        </script>
    </body>
    </html>
    '''

    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
