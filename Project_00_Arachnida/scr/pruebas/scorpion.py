import exifread

image_paths = ["ruta/a/la/imagen1.jpg", "ruta/a/la/imagen2.jpg", "ruta/a/la/imagen3.jpg"]
for image_path in image_paths:
    with open(image_path, "rb") as image_file:
        tags = exifread.process_file(image_file)
        print(f"Metadatos de {image_path}:")
        for tag in tags.keys():
            if tag not in ("JPEGThumbnail", "TIFFThumbnail", "Filename", "EXIF MakerNote"):
                print(f"{tag}: {tags[tag]}")
