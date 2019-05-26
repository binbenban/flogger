import os

SECRET_KEY=os.getenv('SECRET_KEY')
DB_USERNAME=os.getenv('DB_USERNAME')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_HOST=os.getenv('DB_HOST')
DATABASE_NAME=os.getenv('DATABASE_NAME')
DB_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:3306/{DATABASE_NAME}"
SQLALCHEMHY=DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
MYSQL_ROOT_PASSWORD=os.getenv('MYSQL_ROOT_PASSWORD')
BLOG_NAME=os.getenv('BLOG_NAME')
BLOG_POST_IMAGES_PATH=os.getenv('BLOG_POST_IMAGES_PATH')
