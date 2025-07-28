## Commands to be followed


```
mkdir <project_folder_name>
```

```
cd <project_folder_name>
```


## Install uv

```
pip install uv
```


## Vritual Environment creation

```
uv venv <env-name>
```

### Activate Environment

#### Windows git bash
```
source .venv/Scripts/activate
```

#### Linux Terminal
```
source .venv/bin/activate
```

### Install Requirements
```
uv pip install -r requirements.txt
```

### Minimum Requirements for this project
1. LLM Model ##groq, openai, gemini, claude, huggingface, ollama

2. Embedding model ## openai, hf, gemini 

3. vectordatabases ##inmemory ##ondisk ##cloudbased 