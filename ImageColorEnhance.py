import os
from PIL import Image, ImageEnhance

def is_image_corrupted(image_path):
    try:
        with Image.open(image_path) as _:
            return False
    except Exception:
        return True

def enhance_image_quality(input_folder, output_folder, color_factor=1.5, sharpness_factor=1.5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    processed_count = 0

    for filename in os.listdir(input_folder): 
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            if is_image_corrupted(input_path):
                print(f"Skipped '{filename}' due to corruption")
                continue

            try:
                with Image.open(input_path) as image:
                    if image.mode != 'RGB':
                        image = image.convert('RGB')

                    color_enhancer = ImageEnhance.Color(image)
                    image = color_enhancer.enhance(color_factor)

                    sharpness_enhancer = ImageEnhance.Sharpness(image)
                    image = sharpness_enhancer.enhance(sharpness_factor)

                    image.save(output_path)
                    image.close()

                processed_count += 1
                print(f"Processed '{filename}'")
            except Exception as e:
                print(f"An error occurred processing '{filename}': {e}")

    return processed_count

input_folder = "C:\\Users\\DELL\\Desktop\\imagesFile"
output_folder = "C:\\Users\\DELL\\Desktop\\QualityImprovedImages"

try:
    processed_images = enhance_image_quality(input_folder, output_folder)
    print(f"Image quality enhancement for {processed_images} images complete.")
except Exception as e:
    print("An error occurred:", e)