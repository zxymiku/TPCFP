import zipfile

def extract_zip(zip_file_path, password_list):
    for password in password_list:
        try:
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(pwd=bytes(str(password), 'utf-8'))
            print(f"Password found: {password}")
            return True
        except Exception as e:
            if "Bad password" in str(e):
                continue
            else:
                print(e)
                return False
    print("Password not found")
    return False

# 密码字典，纯数字
passwords = [str(i) for i in range(10000)]

zip_file_path = input("请输入压缩文件名")
extract_zip(zip_file_path, passwords)
