from llama_cpp import Llama
import pyperclip
import json

class LLM:
    def __init__(self):
        self.llm = Llama(
            model_path=json.load(open('config/settings.json'))["ai_model"],
            n_ctx=json.load(open('config/settings.json'))["n_ctx"],
            n_threads=json.load(open('config/settings.json'))["n_threads"],
            verbose=json.load(open('config/settings.json'))["verbose"]
        )
        self.max_tokens = json.load(open('config/settings.json'))["max_tokens"]
        self.prompt_template = json.load(open('config/settings.json'))["prompt_template"]
        self.processed_text = ""
        self.prev_coppied_text = ""

    def grammar_service_callback(self, clipboard_text: str):
        if clipboard_text != self.prev_coppied_text and clipboard_text.strip() != "":
            prompt = self.prompt_template.format(text=clipboard_text)
            llm_processed_text = self.llm(prompt, max_tokens=self.max_tokens)
            self.prev_coppied_text = clipboard_text
            self.processed_text = llm_processed_text["choices"][0]["text"].strip().strip("'").strip('"')
            print(f"Text got proccessed!")
            pyperclip.copy(self.processed_text)