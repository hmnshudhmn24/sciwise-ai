class SciLLM:
    def __init__(self, model=None, tokenizer=None):
        self.model = model
        self.tokenizer = tokenizer
    def generate(self, prompt, max_new_tokens=128):
        # simple echo-based stand-in for real generation
        return 'Generated answer (demo): ' + prompt[:300]
