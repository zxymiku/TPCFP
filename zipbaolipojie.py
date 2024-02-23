import zipfile
import itertools

# 假设你的zip文件名为'your_file.zip'
filename = input("your file name")

# 生成10位数字的所有组合
password_combinations = itertools.product(range(10), repeat=10)

with zipfile.ZipFile(filename, 'r') as zip_ref:
    for combination in password_combinations:
        password_attempt = ''.join(str(digit) for digit in combination)

        try:
            zip_ref.extractall(pwd=bytes(password_attempt, 'utf-8'))
            print(f"Password found: {password_attempt}")
            break  # 密码找到后退出循环
        except (RuntimeError, zipfile.BadZipFile):
            continue  # 密码错误，继续尝试下一个
