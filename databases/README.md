# DSR - Databases

### Creating a Conda Environment for this course

```
conda create -n dsr-db python==3.7
```

Activate the conda environment

```
conda activate dsr-db

# Alternatively you can use 

source activate dsr-db # (this is deprecated)
```


Verify your which `pip` you are using

```
(dsr-db) ➜  dsr git:(master) ✗ which pip
/Users/<your-user>/anaconda3/envs/dsr-db/bin/pip
```

Finally, install the pip requirements. 

```
pip install -r requirements.txt
```
