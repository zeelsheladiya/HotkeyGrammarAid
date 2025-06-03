# ✨ HotkeyGrammarAid - Lightweight Grammar Correction via Clipboard & Hotkey

HotkeyGrammarAid is a **cross-platform**, **offline-friendly** grammar correction tool that works quietly in the background. It monitors your clipboard for copied text, and—when you press a hotkey—automatically replaces that text with a grammatically improved version, ready to paste.

---

## 🚀 Features

- ✅ **Clipboard Monitoring** – Automatically picks up copied text.
- 🔠 **Grammar Correction** – Applies local or remote grammar correction logic.
- 🎯 **Custom Hotkey Trigger** – Fix text with a single key combo.
- 🧠 **Paste-Ready** – Replaces clipboard content, so your next paste is corrected.
- ⚡ **Lightweight and Fast** – No GUI or bloat.
- 🛠️ **Local Model Compatible** – Designed to support local LLMs (no internet needed).
- 🔒 **Privacy-First** – Your clipboard never leaves your machine.
- 🪟🧑‍💻 **Cross-Platform** – Works on Windows, macOS, and Linux.

---

## 🎯 Use Case

You're writing an email, code comment, or document. You quickly select and copy a sentence like:

> `i am going to office tomorrow maybe we can meeting`

Instead of opening Grammarly or switching windows, just press your configured hotkey (e.g., `Ctrl+Shift+,`), and HotkeyGrammarAid silently corrects the sentence to:

> `I am going to the office tomorrow. Maybe we can meet.`

Now just `Ctrl+V` to paste the corrected version — no browser, no cloud, no lag.

---

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/zeelsheladiya/HotkeyGrammarAid.git
cd HotkeyGrammarAid
```

## 2. Install dependencies
```bash
pip install -r requirements.txt
```

## 3. Configure your shortcut
> Edit config/settings.json:
```json
{
  "shortcut": ["ctrl", "shift", ","]
}
```

## 4. Download your LLM model you want to use 
> It only supports `.gguf` model file fot fast and smoother experiance.

* Download your model and put it in the project folder
* Best place to doenload models https://huggingface.co/models

## 5. Configure your downloaded model
```json
{
    "ai_model": "your model path",
}
```

## ▶️ Running the Tool

```bash
python main.py
```

> make sure you give OS level permission to run and listen events. For EX: (For macos you need Input Monitoring permission in order to listen keyboard input)

## 📁 Project Structure

```bash
HotkeyGrammarAid/
├── main.py                   # Main script - starts listeners
├── utils/
│   ├── clipboard_utils.py    # Clipboard monitoring
│   ├── keyboard_utils.py     # Hotkey listener
│   └── llm_utils.py          # Grammar correction logic (LLM or rule-based)
├── config/
│   └── settings.json         # User-defined hotkey
└── README.md

```


## 🧠 How It Works
1. Clipboard Monitoring: Watches for new copied text.
2. Hotkey Detection: Listens for your chosen key combo.
3. Correction Callback: Calls your grammar function with copied text.
4. Clipboard Update: Replaces the clipboard with corrected text.

## 🌐 Possibilities & Extensions
🤖 Use your own LLM – Swap out the grammar logic to use local models like transformers, llama.cpp, or gemma.

🌍 Add Multilingual Support – Detect and correct other languages.

📦 Bundle as App – Convert into a system tray app with GUI for toggling.

🧪 Clipboard History – Maintain versions of what was fixed.

🖱️ Right-click Context Menu – Integrate into desktop context menus.

🔌 Plugin System – Support formatting, summarization, etc.

## 🛡️ Privacy & Performance

HotkeyGrammarAid does not send your data anywhere. Everything happens on your machine, and you control the logic. It’s ideal for security-conscious users or offline environments.

## ❤️ Contributing

Have an idea? Found a bug? Open a GitHub issue or submit a pull request. Contributions are welcome!