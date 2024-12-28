from transformers import AutoTokenizer, AutoModel
import argparse

def main():
    parser = argparse.ArgumentParser(description="Hugging face model downloader")
    parser.add_argument('--model', type=str, help="Hugging face model (ex. sentence-transformers/all-MiniLM-L6-v2)")
    parser.add_argument('--dir', type=str, help="Local download directory (ex. /local_dir)")
    args = parser.parse_args()
    
    print("Fetching...")
    hugging_face_model_name  = args.model
    tokenizer = AutoTokenizer.from_pretrained(hugging_face_model_name)
    model = AutoModel.from_pretrained(hugging_face_model_name)
    
    local_directory = args.dir + "/" + hugging_face_model_name
    print("Saving to " + local_directory + "...")
    tokenizer.save_pretrained(local_directory)
    model.save_pretrained(local_directory)
    print("Saved.")

if __name__ == "__main__":
    main()