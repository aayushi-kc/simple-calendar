from flask import Flask
import calendar
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Get current date
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    # Generate calendar
    month_name = calendar.month_name[month]
    cal = calendar.month(year, month)

    # Highlight today in the calendar
    today_str = f' {day} ' if day < 10 else f'{day} '
    cal_highlighted = cal.replace(today_str, f'[{day}]')

    # Simple HTML
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>📅 Simple Calendar | Replit</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
                padding: 20px;
            }}
            .calendar-box {{
                background: white;
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 500px;
                width: 100%;
            }}
            h1 {{
                color: #333;
                margin-bottom: 10px;
            }}
            .month-year {{
                color: #667eea;
                font-size: 1.5em;
                font-weight: bold;
                margin: 20px 0;
            }}
            .calendar {{
                background: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                font-family: monospace;
                font-size: 1.2em;
                white-space: pre;
                text-align: center;
                margin: 20px 0;
                border: 2px solid #e9ecef;
            }}
            .today {{
                background: #ff6b6b;
                color: white;
                padding: 2px 5px;
                border-radius: 3px;
                font-weight: bold;
            }}
            .today-info {{
                background: #e8f5e9;
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
                font-weight: bold;
                color: #2e7d32;
            }}
            .nav-buttons {{
                display: flex;
                justify-content: center;
                gap: 15px;
                margin-top: 25px;
            }}
            .nav-btn {{
                background: #667eea;
                color: white;
                border: none;
                padding: 12px 25px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
                transition: all 0.3s;
            }}
            .nav-btn:hover {{
                background: #764ba2;
                transform: translateY(-2px);
            }}
            .replit-footer {{
                margin-top: 25px;
                color: #666;
                font-size: 0.9em;
            }}
        </style>
    </head>
    <body>
        <div class="calendar-box">
            <h1>📅 Simple Calendar</h1>

            <div class="month-year">
                {month_name} {year}
            </div>

            <div class="calendar">
                {cal_highlighted}
            </div>

            <div class="today-info">
                📍 Today: {now.strftime("%A, %B %d, %Y")}
            </div>

            <div class="nav-buttons">
                <button class="nav-btn" onclick="changeMonth(-1)">◀ Previous</button>
                <button class="nav-btn" onclick="changeMonth(1)">Next ▶</button>
            </div>

            <div class="replit-footer">
                Made with Flask on Replit
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

            // Add keyboard shortcuts
            document.addEventListener('keydown', (event) => {{
                if (event.key === 'ArrowLeft') {{
                    changeMonth(-1);
                }} else if (event.key === 'ArrowRight') {{
                    changeMonth(1);
                }} else if (event.key === 't' || event.key === 'T') {{
                    // Go to today
                    window.location.href = '/';
                }}
            }});
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

    # Generate calendar
    month_name = calendar.month_name[month]
    cal = calendar.month(year, month)

    # Highlight today if it's the current month
    if today_day:
        today_str = f' {today_day} ' if today_day < 10 else f'{today_day} '
        cal = cal.replace(today_str, f'[{today_day}]')

    # HTML
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>📅 Calendar | {month_name} {year}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
                padding: 20px;
            }}
            .calendar-box {{
                background: white;
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 500px;
                width: 100%;
            }}
            h1 {{
                color: #333;
                margin-bottom: 10px;
            }}
            .month-year {{
                color: #667eea;
                font-size: 1.5em;
                font-weight: bold;
                margin: 20px 0;
            }}
            .calendar {{
                background: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                font-family: monospace;
                font-size: 1.2em;
                white-space: pre;
                text-align: center;
                margin: 20px 0;
                border: 2px solid #e9ecef;
            }}
            .today {{
                background: #ff6b6b;
                color: white;
                padding: 2px 5px;
                border-radius: 3px;
                font-weight: bold;
            }}
            .today-info {{
                background: #e8f5e9;
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
                font-weight: bold;
                color: #2e7d32;
            }}
            .nav-buttons {{
                display: flex;
                justify-content: center;
                gap: 15px;
                margin-top: 25px;
            }}
            .nav-btn {{
                background: #667eea;
                color: white;
                border: none;
                padding: 12px 25px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
                transition: all 0.3s;
            }}
            .nav-btn:hover {{
                background: #764ba2;
                transform: translateY(-2px);
            }}
            .today-btn {{
                background: #ff6b6b;
            }}
            .today-btn:hover {{
                background: #ff5252;
            }}
            .replit-footer {{
                margin-top: 25px;
                color: #666;
                font-size: 0.9em;
            }}
        </style>
    </head>
    <body>
        <div class="calendar-box">
            <h1>📅 Simple Calendar</h1>

            <div class="month-year">
                {month_name} {year}
            </div>

            <div class="calendar">
                {cal}
            </div>

            <div class="today-info">
                📅 Viewing: {month_name} {year}
                {'<br>📍 Today is highlighted in red' if today_day else ''}
            </div>

            <div class="nav-buttons">
                <button class="nav-btn" onclick="changeMonth(-1)">◀ Previous</button>
                <button class="nav-btn today-btn" onclick="goToday()">Today</button>
                <button class="nav-btn" onclick="changeMonth(1)">Next ▶</button>
            </div>

            <div class="replit-footer">
                Made with Flask on Replit
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

            // Add keyboard shortcuts
            document.addEventListener('keydown', (event) => {{
                if (event.key === 'ArrowLeft') {{
                    changeMonth(-1);
                }} else if (event.key === 'ArrowRight') {{
                    changeMonth(1);
                }} else if (event.key === 't' || event.key === 'T') {{
                    goToday();
                }} else if (event.key === 'Enter') {{
                    // Today button on Enter
                    goToday();
                }}
            }});
        </script>
    </body>
    </html>
    '''

    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)