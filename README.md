# MedLLM

MedLLM is a medical chatbot designed to answer questions based on PDFs in the `data` folder. It includes a user-friendly interface built with HTML, CSS, and Flask, and utilizes Pinecone for vector storage along with Groq for API handling.

## Quick Start

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/medLLM.git
cd medLLM
```
### Step 2: Set Up the Conda Environment

```bash
conda create -n medibot python=3.10 -y
conda init
conda activate medibot
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Embedding Model

Embedding Links -> https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

### Step 5: Setup PINECONE VECTOR DB API KEY AND GROQ API KEY

``` bash
GROQ_API_KEY = "xxxxxx"
PINECONE_API_KEY = "xxxxxx"
```

### Step 6: Run the store_index.py

```bash
python store_index.py
```

### Step 7: Running the Application

``` bash
python app.py
```

### Features

PDF Ingestion: Answer queries based on content from PDFs in the data folder.

Embedding & Retrieval: Utilizes the all-MiniLM-L6-v2 embedding model and Pinecone for vector storage.

Interactive UI: Chat interface built with HTML, CSS, and Flask.


