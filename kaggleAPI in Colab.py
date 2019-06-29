# Kaggle API install
# !pip install kaggle

# Kaggle API Authentication information
from google.colab import files
files.upload()

# Kaggle API json file
ls -lha kaggle.json

# Make directory and copy to kaggle folder

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# Import Kaggle Authentication information

!export KAGGLE_USERNAME='your_user_name'
!export KAGGLE_KEY='your_authentication_key'