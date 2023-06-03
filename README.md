# Helen

Helen is a good **english teacher** and can help you **improve your speaking habits.**
Helen provide some features that can help during your speaking time.

![image](https://github.com/tmdgusya/helen/assets/57784077/c21264a1-3dcc-4ec6-9d39-751a34c0311e)

---
Helen is **beta project**. I wish I make the project to be **visualized** using typescript and next.js. That is my goal. So, I'm going to write the code using **Typescript** and **Next.js** and **langchainJs**.

## Features

### Record feature

You **can record your voice** when you are talking with someone. 
The voice file will be located `resources` folder. The voice file will be separated by 3 minutes.

<img width="293" alt="image" src="https://github.com/tmdgusya/helen/assets/57784077/5cf5ef85-7a84-4212-aabc-1ac191be6dae">

**[folder structure]**

The structure of resource folder follow as **below structure**

```
- resources
    - date (yy-mm-dd)
        - audio (voice files)
            - original (your voice file)
                - 23-05-13.wav
            - voice files which was sparated by minutes. (3 minutes)
                - 23-05-13_0.wav
                - 23-05-13_1.wav
        - transcript (transcript file was maded from your voice file)
        - review (To be fixied by chat-gpt)
```

<img width="386" alt="image" src="https://github.com/tmdgusya/helen/assets/57784077/2eac0a31-e1a3-4859-80fa-c327155eda09">

We'll fix the feature that can record system sound. Because, I think we need to separate voice file to each person's sentence and separate the voice to make transcript. I think we'll use the hugging face to separate voice.

### Transcript feature

If you recorded your voice perfectly, you can **make transcript file** from your voice file. If you execute the `main.py` in transcript folder, then It make the transcript file from your voice file.

<img width="646" alt="image" src="https://github.com/tmdgusya/helen/assets/57784077/64bcaa4b-411d-473c-9f71-4855822bd91e">

**[Transcript file]**

### NLP feature

**NLP feature** can separate the sentence to each sentence. The sentence will be put in GPT per each sentence.

<img width="963" alt="image" src="https://github.com/tmdgusya/helen/assets/57784077/661c559f-c199-474a-acfc-02041622e116">

### Correction feature

**Correction feature** can fix the sentence that you spoke when you were talking someone. The correction format must be **bellow format**. You can study from the format.

```
Format

- Original sentence (written by the student):
- Grammatically correct sentence:
- Explanation (in bullet point form):
- Example conversation (briefly):
```

<img width="1307" alt="image" src="https://github.com/tmdgusya/helen/assets/57784077/0fa2aa83-0e4a-4fee-9cbf-0add4f9e3f65">

## How to start

Prerequisites
- **You must have python 3 or later installed**.
- **You must install poetry**
- **Make `.env` file on the root directory of project and write your `api-key`**

<img width="425" alt="image" src="https://github.com/tmdgusya/helen/assets/57784077/f718c274-e42e-49ef-ac6a-ee2177b9b0b8">

**[env file]**

```
OPENAI_API_KEY=
```

1. **clone the repository**

```sh
git clone https://github.com/tmdgusya/helen.git
```

2. **Install dependencies**

```sh
poetry install
```

3. **Record your voice**

```sh
poetry run python src/audio/audio.py
```

4. **Resize your voice file to small**

```sh
poetry run python src/audio/resizer.py
```

5. **Make Transcript from voice file**

```sh
poetry run python src/transcript/whisper.py
```

6. **Fix your sentence**

```sh
poetry run python src/main.py
```

7. **Check the file that written by Open-AI**

## Goal

- I wish I make the program to **visualize** using typescript and next.js
- I wish I separate the transcript to each person's sentence
