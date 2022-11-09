# 密碼重試程式 password-retry
# 先在程式碼中 設定好密碼 password = 'a123456'
# 讓使用者【最多輸入3次密碼】
# 密碼錯誤,印出"密碼錯誤! 還有__次機會"
# 密碼正確,印出"登入成功!"

password = 'a123456'
x = 3 #剩餘機會
while x != 0 :
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break
	else:
		x = x - 1
		if x != 0:
			print('密碼錯誤! 還有', x ,'次機會')
		else:
			print('密碼錯誤! 請重設密碼')
			break