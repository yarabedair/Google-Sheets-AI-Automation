from google import genai

# 1. Provide your secret Gemini API Key inside the quotation marks
API_KEY = "AQ.Ab8RN6IUD5ghzgL2k5VPRjKpvBAEIwqssVpScExxVia27qS-QA"

# 2. Initialize the Gemini API client
client = genai.Client(api_key=API_KEY)

# 3. The text that we want Gemini to summarize
text_to_summarize = """
الذكاء الاصطناعي وتطبيقات الأتمتة أصبحت من أهم ركائز سوق العمل الحر حالياً. 
حيث تتيح للشركات توفير الوقت والجهد من خلال بناء وكلاء أذكياء يقومون بالمهام المتكررة 
مثل قراءة جداول البيانات وتلخيص التقارير الطبية وإرسال رسائل البريد الإلكتروني تلقائياً، 
مما يرفع من كفاءة العمل ويوفر مئات الساعات على الموظفين.
"""

# 4. Send the text to the fast and efficient Gemini 2.5 Flash model
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=f"Summarize this text in one professional line:\n{text_to_summarize}"
)

# 5. Print the final summary result in the Terminal
print("--- Gemini AI Summary ---")
print(response.text)