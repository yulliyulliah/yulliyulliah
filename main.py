import datetime
import os

# ================= ⚙️ 설정 구역 =================
TARGET_DATE = datetime.datetime(2026, 4, 3)
TARGET_NAME = "보고싶은 웬디"
START_HOUR = 10
END_HOUR = 19
# ===============================================

def update_readme():
    now = datetime.datetime.now()
    today_str = now.strftime("%-m/%-d")
    
    # 1. 날짜 계산
    diff = TARGET_DATE - now
    total_days = diff.days
    total_seconds = diff.seconds
    total_hours = total_seconds // 3600
    total_minutes = (total_seconds % 3600) // 60
    
    # 2. 워킹 데이 계산
    working_days = 0
    current = now
    while current.date() < TARGET_DATE.date():
        current += datetime.timedelta(days=1)
        if current.weekday() < 5:
            working_days += 1

    # 메시지 생성
    readme_text = f"""
<div align="center" style="border: 1px solid #e1e4e8; border-radius: 10px; padding: 20px; text-align: left;">

### {TARGET_NAME} 없는 오늘은 {today_str}일 🥹
## {TARGET_NAME} 오는 {TARGET_DATE.month}/{TARGET_DATE.day}일까지 {total_days}일 남았어요

<br>

- ⏰ **현재 시간 기준**: {total_days}일 {total_hours}시간 {total_minutes}분 남았어요
- 💼 **워킹데이 기준**: {working_days}일 남았어요 (주말 제외)
- ⏳ **보고싶어요 얼른와요...**

</div>
"""
    
    # ================= [여기가 핵심입니다!] =================
    # 범인은 바로 여기였습니다! 따옴표 안에 글자가 꼭 있어야 합니다.
    start_marker = "<" + "!-- TIMER_START --" + ">"
    end_marker = "<" + "!-- TIMER_END --" + ">"
    # =======================================================
    
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    if start_marker in content and end_marker in content:
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[1]
        new_content = before + start_marker + "\n" + readme_text + "\n" + end_marker + after
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
    else:
        print("Error: README.md에서 표지판을 못 찾았습니다.")

if __name__ == "__main__":
    update_readme()
