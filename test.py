import sys
ASSETS_FOLDER = ".\\assets"
DATASETS_FOLDER = ASSETS_FOLDER + "\\datasets"
DB_FILE = ASSETS_FOLDER + "\\McFit.db"
IMAGE_FOLDER = ASSETS_FOLDER + "\\images"

def main(imageName):
    logo_file = open(f"{IMAGE_FOLDER}\\McFit-weisserHG.png", "rb")

    try:
        with open(f"{IMAGE_FOLDER}\\{imageName}.jpg", "rb") as image_file:
            print("image")
            blob_data = image_file.read()
    except OSError:
        print("logo")
        blob_data = logo_file.read()

    print(blob_data.count)

#------------------------ MAIN ------------------------#
if __name__ == "__main__":
    main(sys.argv[1])
