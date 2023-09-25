import os

folder_path = r"C:\Users\bakke\Downloads\Python"
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]
image_files.sort()

for index, image_file in enumerate(image_files):
    extension = os.path.splitext(image_file)[1]
    new_name = f"Everett_{index + 1}{extension}"
    
    old_path = os.path.join(folder_path, image_file)
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)
    print(f"Renamed {image_file} to {new_name}")

print("Image renaming completed.")