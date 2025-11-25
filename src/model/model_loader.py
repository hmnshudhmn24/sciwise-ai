from transformers import AutoTokenizer, AutoModelForCausalLM
def load_model(model_name='sshleifer/tiny-gpt2'):
    # lightweight default model for offline demo
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer
