# Text Sentiment Analyzer

Simple sentiment analysis of russian economic texts in DOCX and PDF documents. (Educational project)

## Features

- **Keyword counting** in three categories:
  - **Overconfidence**  
  - **Underconfidence**  
  - **Neutral**  
- **Sentiment index calculation** using the formula:  
  \[(Over − Under) / (Over + Under + Neutral)\]
- **Supported formats**: DOCX, PDF  
- **CSV export** of metrics for each processed document

## Requirements
 
- [`uv` - Python project manager](https://docs.astral.sh/uv/)

## Usage

0. **Install `uv`**:


- On **Windows**
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

- On **Linux/MacOS**
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

1. **Clone the repository**:
    ```bash
    git clone https://github.com/theusick/text-sentiment-analyzer.git
    cd text-sentiment-analyzer
    ```

2. **Create a virtual environment and install dependencies**:
    ```bash
    uv venv
    ```

3. **Activate the virtual environment**:

- On **Windows**
    ```bash
    .venv\bin\activate
    ```

- On **Linux/MacOS**
    ```bash
    source .venv/bin/activate
    ```

4. **Prepare your data**:

- Place the documents to be analyzed into `data/docs/`

- Provide your keyword dictionary in `data/dictionary.xlsx` with columns:
    ```r
    lemma        | overconfidence | underconfidence
    ------------ | -------------- | ---------------
    успешный     | overconfidence | NA
    рискованный  | NA             | underconfidence
    нормальный   | NA             | NA
    ```

5. **Run the analysis**
    ```bash
    uv run main.py
    ```

## License

This project is released under the MIT License.
