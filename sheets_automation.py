import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google import genai
import datetime  # Import Python's built-in datetime library to get the current time

# 1. Setup Google Sheets API credentials and scopes
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(r"Y:\Ai Automation\secret_key.json.json", scope)
sheet_client = gspread.authorize(creds)

# 2. Open the spreadsheet by its exact name
try:
    print("📋 Available spreadsheets for this service account:")
    for s in sheet_client.openall():
        print(f"  - '{s.title}'")
    
    # Attempt to open the spreadsheet
    sheet = sheet_client.open("Ai Automation project").sheet1
except gspread.exceptions.SpreadsheetNotFound:
    print("\n❌ Error: Cannot find the spreadsheet named 'Ai Automation project'")
    print("Please make sure the name printed above matches this name exactly!")
    exit()

# Initialize the Gemini API client (Replace with your actual key before running locally)
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

ai_client = genai.Client(api_key=GEMINI_API_KEY)

print("⚡ Reading data and generating summaries automatically...")

# 3. Read rows and summarize the content
for row_index in range(2, 4):  # This will read row 2 and row 3
    # Read the original text from Column A (Column 1)
    original_text = sheet.cell(row_index, 1).value 
    
    if original_text:
        # Send the text to Gemini for summarization
        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Summarize this text in one professional line:\n{original_text}"
        )
        
        summary_result = response.text
        
        # Write the summary result into Column B (Column 2)
        sheet.update_cell(row_index, 2, summary_result)
        
        # Capture the exact current date and time
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Write the timestamp into Column C (Column 3)
        sheet.update_cell(row_index, 3, f"AI Updated at: {current_time}")
        
        print(f"✅ Row {row_index} summarized and timestamped!")

print("🎉 Automation finished! Open your Google Sheet now.")