import os
from pathlib import Path
from flask import current_app
from uuid import uuid4

class ImageHandler:
    
    @staticmethod
    def save_image_on_disk(image):
        if not image: return None
        suffix = Path(image.filename).suffix
        image_name = str(uuid4()) + suffix
        image_path = Path(current_app.root_path) / "static/images" / image_name
        image.save(image_path)
        return image_name
    

    @staticmethod
    def update_image_in_disk(current_image_name, new_image_file):
        if not new_image_file.filename: return current_image_name
        image_name = ImageHandler.save_image_on_disk(new_image_file)
        ImageHandler.delete_image_from_disk(current_image_name)
        return image_name

    
    @staticmethod
    def delete_image_from_disk(image_name):
        if not image_name: return
        if image_name == "no-image.jpg": return
        if image_name == "freedom_logo.jpg": return
        image_path = Path(current_app.root_path) / "static/images" / image_name
        image_path.unlink(missing_ok = True)


    @staticmethod
    def get_image_path(image_name):
        image_path = Path(current_app.root_path) / "static/images" / image_name
        if not image_path.exists(): image_path = Path(current_app.root_path) / "static/images/no-image.jpg"
        return image_path


    @staticmethod
    def image_name_by_path(image_name):
        image_path = Path(current_app.root_path) / "static/images" / image_name
        if not image_path.exists(): image_name = "no-image.jpg"
        return image_name
    

    @staticmethod
    def get_background_logo_path(logo_image_name):
        logo_image_path = Path(current_app.root_path) / "static/logos" / logo_image_name
        if not logo_image_path.exists(): logo_image_path = Path(current_app.root_path) / "static/logos/white_heart.png"
        return logo_image_path


    @staticmethod
    def get_home_image_path(image_name):
        image_path = Path(current_app.root_path) / "static/home_gallery_images" / image_name
        if not image_path.exists(): image_path = Path(current_app.root_path) / "static/background_images/no-image.jpg"
        return image_path

    
    @staticmethod
    def get_home_images_list():
        images_folder_path = Path(current_app.root_path) / "static/home_gallery_images"
        if not images_folder_path.exists(): images_folder_path = Path(current_app.root_path) / "static/background_images/no-image.jpg"
        suffix_options = ['.png', '.jpg', '.jpeg', '.gif']
        home_images_list = [img.name for img in images_folder_path.iterdir() if img.suffix.lower() in suffix_options] 
        return home_images_list


