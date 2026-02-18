# Ricardo: Anki AI Assistant

**Ricardo** is a sidebar add-on for Anki that acts as your personal AI tutor. It uses OpenAI's GPT models prompted with context and intelligent instructions to answer questions about your current flashcard, explain complex topics, and help you study more effectively—all without leaving Anki.

I made this on a whim because 1. I was bored and 2. I was tired of switching between Anki, UWorld, and ChatGPT or OpenEvidence. Unfortunately, OpenEvidence does not have an accessible API, so I used Sporo models initially, then generalized access to OpenAI models to promote ease-of-use for all students. 

This tool not only helped integrate AI into my studying, but also allowed me to explore more on the user-interface side of AI assistants integrated into medical education. Some things I've experimented with are pretty UIs, keeping apps low-size and low-complexity while also being useful, intelligent prompting, user-centered context integration for AI assistants, stress-testing AI assistants, and thinking beyond usage in the user journey during installation, set-up, and edge cases (basically bugs). 

You can use this tool **for free** even with integration into OpenAI API, as they give free credits. Scroll to the bottom for instructions on how to get free credits for easy integration. 

For a quick demo, watch the demo video at this [Google Drive link](https://drive.google.com/file/d/13qsXiuJhkQzKuLwRj8gjjy4I6HB-lIR4/view?usp=sharing).

## Features

-   **Context-Aware**: Ricardo knows which card you're looking at. It sees the question, answer, and fields, so you can ask "Explain this card" or "Why is the answer X?" directly.
-   **High-Yield & Exam-Oriented**: Ricardo is specifically trained to provide concise, exam-relevant information for the USMLE and other medical exams.
-   **Trusted Sources**: Ricardo includes relevant information from trusted sources such as Bootcamp, Pixorize, Medbullets, Boards and Beyond, Sketchy, or any research articles.
-   **Question Generation**: Ricardo can generate practice questions for you to test your knowledge.
-   **Rich Markdown & Tables**: Responses are rendered with beautiful Markdown formatting, including robust support for tables, bold text, lists, and code blocks.
-   **Anki-Native Look**: Designed to feel like a part of Anki (or a modern chat app like Claude), with a clean, serif-font aesthetic and distinct speech bubbles.
-   **Image Support**: If your card has images, Ricardo can see them too! (Requires a multimodal model like `gpt-4o`).
-   **Streamlined Setup**: Built-in onboarding makes setting up your API key a breeze.

## Installation

### From GitHub (Manual)
1.  **Download** the latest release (`.zip` file) from the GitHub Releases page.
2.  **Unzip** the file. You should see a folder named `ricardo_assistant`.
3.  Open **Anki**.
4.  Go to **Tools** -> **Add-ons** -> **View Files**. This opens your Anki `addons21` folder.
5.  **Drag and Drop** the `ricardo_assistant` folder into the `addons21` folder.
6.  **Restart Anki**.

## Setup

1.  Open Anki and start reviewing a deck or open the Browser.
2.  Open the **Ricardo Sidebar** (usually visible by default, or accessible via `Tools` -> `Ricardo Sidebar` or `Ctrl+Shift+G`).
3.  **API Key Prompt**: If this is your first time, Ricardo will ask for your OpenAI API Key.
    -   Please make an OpenAI account at [platform.openai.com](https://platform.openai.com/account/api-keys). You can get a free API key there. 
    -   Click the link in the dialog to generate a key at [platform.openai.com](https://platform.openai.com/account/api-keys).
    -   Paste the key starting with `sk-...` into the box and click **Save**.
    -   If you get an error, please make sure you are using the correct API key. Usually, your usage is actually pretty low and you should be able to use it for free. 
4.  That's it! Ricardo is ready to help.

## Usage

<figure align="center">
  <img width="864" height="540" alt="Screenshot 2026-02-14 at 04 06 41" src="https://github.com/user-attachments/assets/3bdd995f-f40a-480a-97a2-198b6a357c6b"/><br>
</figure>

-   **Ask a Question**: Type your question in the box at the bottom (e.g., "Mnemonic for this?", "Simplify this explanation").
-   **Context**: Ricardo automatically reads the content of the currently displayed card.
-   **Shortcuts**:
    -   `Enter`: Send message.
    -   `Ctrl+Shift+G`: Toggle Sidebar.

## Configuration

You can easily customize Ricardo:
1.  Go to **Tools** -> **Ricardo Settings**.
2.  **Model**: Defaults to `gpt-5-mini` (fast & cheap). You can also choose `gpt-4o`, `o3-mini`, or type any other model.
    * In my opinion, **`gpt-5-mini`** OR **`gpt-4o`** is the best for this application as it is fast and actually gives only the high-yield things instead of the **overthinking/overspending tokens/AI sycophancy** that GPT5 or 5.2 annoyingly does. 
    *   **Pro Tip**: The dropdown is **editable**! You can type *any* valid OpenAI model name (e.g., `gpt-6` when it comes out) and it will work immediately.
4.  **System Prompt**: Edit Ricardo's personality and instructions.
5.  **Max Images**: Set how many images to send to the AI (default: 2).
6.  **Timeout**: usage limits.


## Requirements

-   Anki 2.1.50+
-   An active OpenAI API Key.
     - A paid account required for API access, but from my experience, your usage is so small that the cost is super low (definitely a full month of usage is much less than the 20$/month ChatGPT subscription), and the extra utility you get is worth it.
-   You can get **complimentary (free) credits** from OpenAI by sharing your outputs/inputs. Go to **"Data Controls"** -> **"Sharing"**, or click the direct link [here](https://platform.openai.com/settings/organization/data-controls/sharing).
     - This gives you up to 2.5 million free tokens for the cheaper models and 250,000 tokens for some of the most recent models (like GPT5.2, 5.3).
     - Don't worry - since you are only asking your questions about USMLE questions, you're not violating HIPAA :) - you'll only be sharing your questions! 

## Future Features
Some features I'm working on in the pipeline:
-   Automatic Anki card generator from concepts that you can highlight from GPT's responses.
-   Integration of UWorld content review.
       -  Auto-identifying UWorld Questions and searching for cards with those QIDs or Topics
       -  Auto-generating or rebuilding filtered decks with incorrect, marked, or all cards in each completed 40-question block.
       -  This might require me to create an agent, so I'll probably use Langchain for this just to make my life easier.
-   USMLE question generator with full formatting and answer choices based on cards and concepts.
-   Fine-tuned SLMs for faster performance (Sporo proprietary).
-   Agentic learning: intelligent card look-up, auto-filtered deck creator for extra practices, scheduled reviews.

I'm mostly modeling these future features off of the Anking deck - let me know if you think there is something I'm missing that could be super useful!

## License

MIT License. Feel free to modify and share!
Made with love by **Chanseo Lee** @ Yale, Sporo Health <3
