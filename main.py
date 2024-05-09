import subprocess

# 定义.exe文件的路径
exe_path = R"C:\Users\admin\Documents\zengchunming\GenerateThumnailsTool\ShellThumbsDemo.exe"

# 定义要传递给.exe文件的参数列表
args = [R"C:\Users\admin\Documents\zengchunming\GenerateThumnailsTool\test\Boy01_diffuse.jpg", 
        "kkkk.png", 
        "512"]

# 调用.exe文件并传递参数
subprocess.call([exe_path] + args)
print(111)
