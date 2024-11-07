# content_processor.py
import math

from transformers import pipeline
from transformers import AutoTokenizer

class ContentProcessor:
    def __init__(self, max_length=130, min_length=30, do_sample=False):
        """
        Initializes the ContentProcessor with a summarization pipeline.

        Parameters:
            max_length (int): Maximum length of the summary.
            min_length (int): Minimum length of the summary.
            do_sample (bool): Whether to use sampling; if False, greedy decoding is used.
        """
        self.summarizer = pipeline("summarization")
        self.max_length = max_length
        self.min_length = min_length
        self.do_sample = do_sample
        self.tokenizers = AutoTokenizer.from_pretrained("bert-base-uncased")


    def split_text_into_chunks(self,text, max_tokens=1024):
        # Tokenize the input text
        tokens = self.tokenizers.encode(text)

        # Split the tokens into chunks of max_tokens
        chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]

        # Convert each chunk back to text (if needed for some use cases)
        chunk_texts = [self.tokenizers.decode(chunk, skip_special_tokens=True) for chunk in chunks]

        return chunk_texts
    def summarize(self, text):
        """
        Generates a summary of the given text.

        Parameters:
            text (str): The text to summarize.

        Returns:
            str: The summary of the text.
        """

        # option-1
        # summary = self.summarizer(
        #     text,
        #     max_length=self.max_length,
        #     min_length=self.min_length,
        #     do_sample=self.do_sample,
        #     truncation=True
        # )
        # return summary[0]['summary_text']


        # option 2
        # Split the text into manageable chunks (e.g., 1024 tokens per chunk
        text_chunks = self.split_text_into_chunks(text,1024)
        total_size_chunks = len(text_chunks)
        summaries = []
        max_length  = math.floor(self.max_length / total_size_chunks)
        for chunk in text_chunks:
            # Generate summary for each chunk
            summary = self.summarizer(
                chunk,
                max_length=max_length,
                min_length=self.min_length,
                do_sample=self.do_sample,
                truncation=True
            )
            summaries.append(summary[0]['summary_text'])
            # print(summary[0]['summary_text'])

        # Combine the summaries of all chunks
        return " ".join(summaries)