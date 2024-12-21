from os import path

API_PREFIX = '/api/v1';
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
GENERATED_IMAGE_EXTENSION = "jpg"

CURRENT_PATH = path.dirname(__file__)
IMAGE_FOLDER = path.join(CURRENT_PATH, 'static', 'images')
UPLOAD_FOLDER = path.join(IMAGE_FOLDER,'uploaded')
GENERATED_IMAGE_FOLDER = path.join(IMAGE_FOLDER ,'generated')
SINGLE_IMAGE_FOLDER = path.join(UPLOAD_FOLDER, 'single')
GROUP_IMAGE_FOLDER = path.join(UPLOAD_FOLDER, 'group')
COMPANY_LOGO = path.join(IMAGE_FOLDER,'company_logo.png')
