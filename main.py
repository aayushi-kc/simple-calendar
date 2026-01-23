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

    # Simple HTML with responsive design
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>📅 Simple Calendar | Replit</title>
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
                max-width: 500px;
                width: 100%;
                margin: 10px;
            }}

            h1 {{
                color: #333;
                margin-bottom: 8px;
                font-size: clamp(1.5rem, 4vw, 2rem);
            }}

            .month-year {{
                color: #667eea;
                font-size: clamp(1.2rem, 3vw, 1.5rem);
                font-weight: bold;
                margin: 15px 0;
            }}

            .calendar {{
                background: #f8f9fa;
                padding: 15px;
                border-radius: 10px;
                font-family: monospace;
                font-size: clamp(0.9rem, 2.5vw, 1.2rem);
                white-space: pre;
                text-align: center;
                margin: 15px 0;
                border: 2px solid #e9ecef;
                overflow-x: auto;
            }}

            .today {{
                background: #ff6b6b;
                color: white;
                padding: 2px 4px;
                border-radius: 3px;
                font-weight: bold;
            }}

            .today-info {{
                background: #e8f5e9;
                padding: 12px;
                border-radius: 10px;
                margin: 15px 0;
                font-weight: bold;
                color: #2e7d32;
                font-size: clamp(0.9rem, 2.5vw, 1rem);
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

            .replit-footer {{
                margin-top: 20px;
                color: #666;
                font-size: clamp(0.8rem, 2vw, 0.9rem);
            }}

            /* Mobile-specific adjustments */
            @media (max-width: 480px) {{
                body {{
                    padding: 10px;
                    align-items: flex-start;
                    min-height: 100vh;
                    height: auto;
                }}

                .calendar-box {{
                    padding: 20px 15px;
                    margin: 5px;
                    border-radius: 15px;
                }}

                .calendar {{
                    padding: 10px;
                    font-size: 0.9rem;
                    overflow-x: auto;
                    -webkit-overflow-scrolling: touch;
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
            }}

            /* Tablet adjustments */
            @media (min-width: 481px) and (max-width: 768px) {{
                .calendar-box {{
                    max-width: 450px;
                    padding: 25px;
                }}

                .calendar {{
                    font-size: 1rem;
                }}
            }}

            /* Large screen adjustments */
            @media (min-width: 1200px) {{
                .calendar-box {{
                    max-width: 550px;
                    padding: 30px;
                }}
            }}

            /* Touch device improvements */
            @media (hover: none) {{
                .nav-btn:hover {{
                    transform: none;
                }}

                .nav-btn:active {{
                    transform: scale(0.98);
                }}
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
                max-width: 500px;
                width: 100%;
                margin: 10px;
            }}

            h1 {{
                color: #333;
                margin-bottom: 8px;
                font-size: clamp(1.5rem, 4vw, 2rem);
            }}

            .month-year {{
                color: #667eea;
                font-size: clamp(1.2rem, 3vw, 1.5rem);
                font-weight: bold;
                margin: 15px 0;
            }}

            .calendar {{
                background: #f8f9fa;
                padding: 15px;
                border-radius: 10px;
                font-family: monospace;
                font-size: clamp(0.9rem, 2.5vw, 1.2rem);
                white-space: pre;
                text-align: center;
                margin: 15px 0;
                border: 2px solid #e9ecef;
                overflow-x: auto;
            }}

            .today {{
                background: #ff6b6b;
                color: white;
                padding: 2px 4px;
                border-radius: 3px;
                font-weight: bold;
            }}

            .today-info {{
                background: #e8f5e9;
                padding: 12px;
                border-radius: 10px;
                margin: 15px 0;
                font-weight: bold;
                color: #2e7d32;
                font-size: clamp(0.9rem, 2.5vw, 1rem);
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
                min-width: 100px;
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

            .replit-footer {{
                margin-top: 20px;
                color: #666;
                font-size: clamp(0.8rem, 2vw, 0.9rem);
            }}

            /* Mobile-specific adjustments */
            @media (max-width: 480px) {{
                body {{
                    padding: 10px;
                    align-items: flex-start;
                    min-height: 100vh;
                    height: auto;
                }}

                .calendar-box {{
                    padding: 20px 15px;
                    margin: 5px;
                    border-radius: 15px;
                }}

                .calendar {{
                    padding: 10px;
                    font-size: 0.9rem;
                    overflow-x: auto;
                    -webkit-overflow-scrolling: touch;
                }}

                .nav-buttons {{
                    flex-direction: row;
                    gap: 8px;
                }}

                .nav-btn {{
                    min-width: 80px;
                    padding: 10px 12px;
                    font-size: 14px;
                }}

                .today-btn {{
                    order: -1; /* Move Today button to top on mobile */
                    flex-basis: 100%;
                    max-width: 200px;
                    margin-bottom: 5px;
                }}
            }}

            /* Tablet adjustments */
            @media (min-width: 481px) and (max-width: 768px) {{
                .calendar-box {{
                    max-width: 450px;
                    padding: 25px;
                }}

                .calendar {{
                    font-size: 1rem;
                }}
            }}

            /* Large screen adjustments */
            @media (min-width: 1200px) {{
                .calendar-box {{
                    max-width: 550px;
                    padding: 30px;
                }}
            }}

            /* Touch device improvements */
            @media (hover: none) {{
                .nav-btn:hover {{
                    transform: none;
                }}

                .nav-btn:active {{
                    transform: scale(0.98);
                }}
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
              prepared by:Aayushi KC
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
        </script>
    </body>
    </html>
    '''

    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)