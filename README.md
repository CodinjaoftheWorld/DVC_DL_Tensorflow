# DVC - DL - TF - AIOPS - Demo

## Commands - 

### Create a new environment
```bash
conda create --prefix ./env python=3.7 -y
```

### Activate new environment
```bash
conda activate ./env
```

### initialize DVC
```bash
git init
dvc init
```
### Create empty files
```bash
mkdir -p src/utils config
touch dvc.yaml setup.py README.md src/__init__.py src/utils.py params.yaml config/config.yaml src/utils/all_utils.py .gitignore 
```



