# Hugging face sentence transformer model downloader
## Downloads specified HF sentence transformer model under a specified directory.

### Set up environment:
```bash
python -m venv hf_model_downloader
source hf_model_downloader/bin/activate
hf_model_downloader % pip install -U sentence-transformers
```

### Usage:
```bash
python main.py --model <hf_model> --dir <local_dir>
```

### Example
```bash
python main.py --model sentence-transformers/all-MiniLM-L6-v2 --dir /local_dir
```
