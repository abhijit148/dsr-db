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
/anaconda3/envs/dsr-db/bin/pip
```

Finally, install the pip requirements. 

```
pip install -r requirements.txt
```

### Starting a jupyter server

Make sure you are using jupyter installed in your `dsr-db` environment

```
/anaconda3/envs/dsr-db/bin/jupyter
```

And start a notebook server:

```
jupyter notebook
```
