from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Optional
import json
import os

app = FastAPI()

# نماذج البيانات
class AssessmentResult(BaseModel):
    student_id: int
    score: float

# بيانات المقررات المستخرجة من ملفاتك
db_courses = [
    {"title": "شبكات الحاسب", "code": "CS301", "skills": ["IPv4/IPv6", "Routing", "Security"]},
    {"title": "بحوث العمليات", "code": "CS302", "skills": ["Linear Programming", "Duality", "Optimization"]}
]

# قراءة واجهة المستخدم من ملف HTML (masar-dashboard.html)
# ملاحظة: تأكد أن ملف masar-dashboard.html موجود في المجلد الرئيسي
def get_ui_content():
    try:
        with open("masar-dashboard.html", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "<h1>Error: Dashboard file not found</h1>"

@app.get("/", response_class=HTMLResponse)
async def root():
    content = get_ui_content()
    return content

@app.get("/api/analyze")
async def analyze(id: int, score: float):
    # منطق الذكاء الاصطناعي للتنبؤ بالتعثر
    risk = "High" if score < 60 else "Medium" if score < 75 else "Low"
    recommendation = "يحتاج الطالب لتدخل أكاديمي فوري ومراجعة المتطلبات السابقة." if risk == "High" else "أداء مستقر، ينصح بالاستمرار في المسار الحالي."
    
    return {
        "student_id": id,
        "risk_level": risk,
        "ai_recommendation": recommendation,
        "avg_score": score
    }
