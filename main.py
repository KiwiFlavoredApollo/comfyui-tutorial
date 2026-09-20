from dotenv import load_dotenv
from catvton import CatVTONGenerator

load_dotenv(verbose=True)

if __name__ == "__main__":
    CatVTONGenerator().run()