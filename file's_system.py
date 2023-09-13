from pathlib import Path

my_dir = Path("d:\\testfolder")
print(my_dir.is_dir())      # is_dir перевіряє чи це тека (якщо так виводить True, якщо ні - False)
print(my_dir.is_file())     # is_file перевіряє чи це файл 
print(my_dir.exists())       # exists перевіряє чи існує цей об'єкт в системі

for i in my_dir.glob("**/*"):
    print(i.is_dir(), i.name)
