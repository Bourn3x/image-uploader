from flask import request
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def configure_routes(app):
  def allowed_file(filename):
    split = filename.rsplit(".", 1)
    if "." in filename and split[1].lower() in ALLOWED_EXTENSIONS:
      return split[1].lower()
    return False

  def get_counter():
    # Open as append to create new file if it doesn't exist
    with open("counter.txt", "a+") as counter_file:
      counter_file.seek(0)
      counter = counter_file.read()
      if not counter:
        counter = 1
        counter_file.write(str(counter))
    return counter

  def increment_counter(counter):
    with open("counter.txt", "w") as counter_file:
      counter_file.write(f"{int(counter) + 1}")

  def save_file(app, file, file_extension):
    image_id = get_counter()

    filename = secure_filename(f"{image_id}.{file_extension}")
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    increment_counter(image_id)
    
    return image_id

  @app.route('/')
  def index():
    return 'App Running'

  @app.route("/upload", methods=["POST"])
  def upload_image():
    if 'file' not in request.files:
      return "No file part", 400

    file = request.files['file']

    # If the user does not select a file
    if file.filename == '':
      return "No selected file", 400

    # Check if the file extension is allowed
    file_extension = allowed_file(file.filename)
    if not file_extension:
      return "File is not an image", 400

    if file:
      image_id = save_file(app, file, file_extension)
      return f"{request.base_url}/{image_id}"

    else:
      return "Something went wrong", 400

  @app.route("/images/<int:image_id>", methods=["GET"])
  def get_image(image_id):
    return f'Image {image_id}'
