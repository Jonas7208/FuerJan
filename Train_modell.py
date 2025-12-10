import os
from rembg import remove
from PIL import Image

def remove_background_from_dataset(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):

                input_path = os.path.join(root, file)

                relative_path = os.path.relpath(root, input_folder)
                output_dir = os.path.join(output_folder, relative_path)
                os.makedirs(output_dir, exist_ok=True)

                output_path = os.path.join(output_dir, file.rsplit(".", 1)[0] + ".png")

                print(f"Bearbeite: {input_path}")

                with Image.open(input_path) as img:
                    result = remove(img)
                    result.save(output_path)

    print("✔ Fertig! Alle Bilder inklusive Unterordner wurden verarbeitet.")
remove_background_from_dataset(input_folder="/Users/jonasgasparini/PycharmProjects/garbage-classification-model/dataset",
                               output_folder="/Users/jonasgasparini/Desktop/WithoutBG")