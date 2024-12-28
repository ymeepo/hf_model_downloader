from transformers import AutoTokenizer, AutoModel

def main():
    
    hugging_face_model_name = input("What is the Hugging face model you want to download? ")
    
    print("Fetching...")
    tokenizer = AutoTokenizer.from_pretrained(hugging_face_model_name)
    model = AutoModel.from_pretrained(hugging_face_model_name)
    
    local_directory = "/local_models/" + hugging_face_model_name
    print("Saving to " + local_directory + "...")
    tokenizer.save_pretrained(local_directory)
    model.save_pretrained(local_directory)
    print("Saved.")

if __name__ == "__main__":
    main()