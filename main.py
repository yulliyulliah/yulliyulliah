import datetime
import os

# ================= ⚙️ 설정 구역 =================
TARGET_DATE = datetime.datetime(2026, 4, 6) # 목표 날짜
TARGET_NAME = "웬디"
START_HOUR = 10
END_HOUR = 19
# ===============================================

def update_readme():
    now = datetime.datetime.now()
    today_str = now.strftime("%-m/%-d")
    
    # 1. 전체 남은 기간 계산
    diff = TARGET_DATE - now
    total_days = diff.days
    total_seconds = diff.seconds
    total_hours = total_seconds // 3600
    total_minutes = (total_seconds % 3600) // 60
    
    # 2. 워킹 데이 (주말 제외) 계산
    working_days = 0
    current = now
    while current.date() < TARGET_DATE.date():
        current += datetime.timedelta(days=1)
        if current.weekday() < 5: # 0~4는 월~금
            working_days += 1

    # [수정됨] 줄바꿈 태그(<br>)와 HTML 태그를 사용해서 예쁘게 정리
    readme_text = f"""
<div align="center" style="border: 1px solid #e1e4e8; border-radius: 10px; padding: 20px;">
    <h3>{TARGET_NAME} 없는 오늘은 {today_str}일 🥹</h3>
    <h2>{TARGET_NAME} 오는 {TARGET_DATE.month}/{TARGET_DATE.day}일까지 {total_days}일 남았어요</h2>
    <br>
    <p align="left">
        ⏰ <b>현재 시간 기준</b>: {total_days}일 {total_hours}시간 {total_minutes}분 남았어요<br>
        💼 <b>워킹데이 기준</b>: {working_days}일 남았어요 (주말 제외)<br>
        ⏳ <b>보고싶어요 얼른와요...</b>
    </p>
</div>
"""
    
    # 채팅창에서 글자가 사라지지 않게 조립하는 방식 (그대로 두세요)
    start_marker = "<" + "!-- TIMER_START --" + ">"
    end_marker = "<" + "!-- TIMER_END --" + ">"
    
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    if start_marker in content and end_marker in content:
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[1]
        new_content = before + start_marker + "\n" + readme_text + "\n" + end_marker + after
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
    else:
        print("Error: 표지판을 찾을 수 없습니다.")

if __name__ == "__main__":
    update_readme()
