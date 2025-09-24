#建立一個名為 check_password_strength 的函式,接收一個 password 字串
#規則1. 檢查密碼長度是否大於等於8,如果是,分數+1
#規則2. 檢查密碼是否包含至少一個數字,如果是,分數+1
#規則3. 檢查密碼是否包含至少一個大寫字母,如果是,分數+1
#規則4. 檢查密碼是否包含至少一個小寫字母,如果是,分數+1
#規則5. 檢查密碼是否包含至少一個特殊符號,如果是,分數+1
#最後根據總分回傳強度等級:0-2分回傳"弱",3-4分回傳"中等”,5分回傳"強”
import re
def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    
    if score <= 2:
        return "弱"
    elif score <= 4:
        return "中等"
    else:
        return "強"
#測試範例
print("密碼強度",check_password_strength("password"))
print("密碼強度",check_password_strength("Password1"))
print("密碼強度",check_password_strength("Password1!"))