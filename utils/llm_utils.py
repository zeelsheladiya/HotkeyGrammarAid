from llama_cpp import Llama
import pyperclip
import json
import time
from utils.notification_utils import notification

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
        print(f"Text proccessing Started!")
        
        start_time = time.time()
        if clipboard_text != self.prev_coppied_text and clipboard_text.strip() != "":
            prompt = self.prompt_template.format(text=clipboard_text)
            llm_processed_text = self.llm(prompt, max_tokens=self.max_tokens)
            self.prev_coppied_text = clipboard_text
            self.processed_text = llm_processed_text["choices"][0]["text"].strip().strip("'").strip('"')
            print(f"Text got proccessed!")

            end_time = time.time()  # Record end time
            duration = end_time - start_time
            print(f"Function execution time: {duration:.3f} seconds")

            pyperclip.copy(self.processed_text)
            notification.send(block=False)