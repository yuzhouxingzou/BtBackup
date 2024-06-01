import os
import zipfile
from datetime import datetime

print("By yzxz&ChatGPT-4o\n")
def get_username():
    return os.getlogin()

def print_paths(username):
    paths = [
        f"C:\\Users\\{username}\\AppData\\Local\\qBittorrent",
        f"C:\\Users\\{username}\\AppData\\Roaming\\qBittorrent",
        f"C:\\Users\\{username}\\AppData\\Local\\transmission"
    ]
    print("将要打包以下目录：")
    for path in paths:
        print(path)
    return paths

def zip_directories(directories, zip_filename, zip_names):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for directory, zip_name in zip(directories, zip_names):
            if os.path.exists(directory):
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, start=directory)
                        zipf.write(file_path, arcname=os.path.join(zip_name, arcname))
            else:
                print(f"路径未找到: {directory}")
                input("按空格键以退出")

def main():
    username = get_username()
    directories = print_paths(username)
    
    user_input = input("\n是否确定打包(y/n): ").strip().lower()
    if user_input == 'y':
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_filename = f"{username}_BtBackup_{timestamp}.zip"
        zip_names = ["qBittorrent_Local", "qBittorrent_Roaming", "transmission"]
        zip_directories(directories, zip_filename, zip_names)
        print(f"\n已经将这些文件打包为 {zip_filename}")
        input("\n按空格键以退出")
    else:
        print("\n操作已取消")
        input("\n按空格键以退出")

if __name__ == "__main__":
    main()
