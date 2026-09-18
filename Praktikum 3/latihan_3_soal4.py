import math
import os
import zipimport

# 4a. OverflowError > ArithmeticError > Exception
try:
    angka = math.exp(1000)
except OverflowError as e:
    print(f"Tertangkap OverflowError dengan error {e}")
except ArithmeticError as e:
    print(f"Tertangkap ArithmeticError dengan error {e}")
except Exception as e:
    print(f"Tertangkap Exception dengan error {e}")

# 4b. FileExistsError > OSError > Exception
try:
    os.mkdir("folder_tes")
    os.mkdir("folder_tes")
except FileExistsError as e:
    print(f"Tertangkap FileExistsError dengan error {e}")
except OSError as e:
    print(f"Tertangkap OSError dengan error {e}")
except Exception as e:
    print(f"Tertangkap Exception dengan error {e}")
finally:
    if os.path.exists("folder_tes"):
        os.rmdir("folder_tes")

# 4c. ZipImporterError > ImportError > Exception
ZipImporterError = getattr(zipimport, "ZipImporterError", zipimport.ZipImportError)
try:
    zipimport.zipimporter("tidak_ada.zip")
except ZipImporterError as e:
    print(f"Tertangkap ZipImporterError dengan error {e}")
except ImportError as e:
    print(f"Tertangkap ImportError dengan error {e}")
except Exception as e:
    print(f"Tertangkap Exception dengan error {e}")