
## Plotly Sales Dashboard

## 🚀 Live Dashboard

👉 **[View Live Sales Dashboard](https://plotlysalesdashboard-production.up.railway.app/)**

The dashboard is deployed on Railway and is available online.

![](Untitled.png)

## 🚀 Installation & Setup

### 🐍 1. Python Requirement

This project requires:

> **Python 3.10**

Make sure Python 3.10 is installed and available in your environment.

---

### 📦 2. Install Poetry

Open your terminal in the project directory and run:

```bash
pip install poetry
```

Verify the installation:

```bash
poetry --version
```

---

### 🔧 3. Install Project Dependencies

You can install the dependencies using Poetry:

```bash
poetry install
```

This will install the packages defined in `pyproject.toml` and use the existing `poetry.lock` file when available.

### 🔒 Or, Update/Regenerate the Lock File

If you need to regenerate the dependency lock file:

```bash
poetry lock
```

Then install the dependencies:

```bash
poetry install
```

---

### ▶️ 4. Run the Application

After the installation is complete, activate the Poetry environment:

```bash
poetry shell
```

Then run the application:

```bash
python index.py
```

> **💡 Tip:** Using `poetry install` is recommended when a `poetry.lock` file is already included in the project, as it helps ensure everyone uses the same dependency versions.



## Run with Docker

```bash
docker compose up --build
```

Then open **http://127.0.0.1:8050/**

```bash
docker compose down
```

## Railway live URL

The link `https://railway.com/project/...` is the **Railway dashboard**, not the public app.

To get the live site:

1. Open your project: https://railway.com/project/666c4eed-9ad4-4941-ba82-58cbfbe4a8b3?environmentId=aa18f677-c672-4a46-9410-4bf78d57db61
2. Click the deployed **service** (not the project name).
3. Go to **Settings → Networking → Public Networking**.
4. Click **Generate Domain**.

Railway will show a public URL like `https://<service-name>.up.railway.app`.
