# from llama_cpp import Llama
from transformers import AutoTokenizer, T5ForConditionalGeneration
import pyperclip
import json
import time
from utils.notification_utils import notification

class LLM:
    def __init__(self):
        self.model_name = json.load(open('config/settings.json'))["ai_model"]
        self.max_token = json.load(open('config/settings.json'))["max_tokens"]
        self.prompt_template = json.load(open('config/settings.json'))["prompt_template"]
        self.processed_text = ""
        self.prev_coppied_text = ""

    def grammar_service_callback(self, clipboard_text: str):
        print(f"Text proccessing Started!")
        
        start_time = time.time()
        if clipboard_text != self.prev_coppied_text and clipboard_text.strip() != "":
            tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            model = T5ForConditionalGeneration.from_pretrained(self.model_name)
            input_text = self.prompt_template.format(text=clipboard_text)
            input_ids = tokenizer(input_text, return_tensors="pt").input_ids
            outputs = model.generate(input_ids, max_length=self.max_token)
            self.prev_coppied_text = clipboard_text
            self.processed_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print(f"Text got proccessed!")

            end_time = time.time()  # Record end time
            duration = end_time - start_time
            print(f"Function execution time: {duration:.3f} seconds")

            pyperclip.copy(self.processed_text)
            notification.send(block=False)