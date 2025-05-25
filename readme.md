Create virtual env
```bash
python -m venv .venv
```

Activate venv
```bash
.\.venv\Scripts\Activate.ps1
```

Install libraries
```bash
pip install -r requirements.txt
```

Train model
```bash
python model/train_model.py
```

Run the app
```bash
python app.py
```


docker build -t salary-predictor .
docker run -p 5000:5000 salary-predictor


# On data-dev branch
git checkout -b data-dev
# Modify raw_data.csv, track with DVC
dvc add data/raw_data.csv
git add data/raw_data.csv.dvc
git commit -m "Update raw data"

# Push changes
git push origin data-dev


# Docker Build & Run:
# docker build -t salary-predictor .
# docker run -p 5000:5000 salary-predictor

# Docker Compose:
# docker-compose up --build

# Kubernetes:
# kubectl apply -f kubernetes/deployment.yaml

# DockerHub Push (after login):
# docker tag salary-predictor your-dockerhub-username/salary-predictor:latest
# docker push your-dockerhub-username/salary-predictor:latest

# Grafana Access:
# Visit http://localhost:3000 with credentials admin/admin
# Add Prometheus as data source and import dashboard for Flask exporter


======================
git add data/raw/data_v1.csv
git commit -m "Add version 1 of raw dataset"

# Later
git add data/processed/cleaned_v1.csv
git commit -m "Processed version 1 of dataset"


git tag -a data-v1 -m "Version 1 of dataset"
git push origin data-v1
