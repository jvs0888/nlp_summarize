import nltk
from loguru import logger
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
# from summarizer import Summarizer
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


# MODEL 1
# @logger.catch
# def summarize_text(input_text: str, min_length: int, max_length: int) -> str:
#     tokenizer = AutoTokenizer.from_pretrained('google/mt5-large', legacy=False)
#     model = AutoModelForSeq2SeqLM.from_pretrained('t5-large-ua-news')
#
#     summarizer = pipeline('summarization', model=model, tokenizer=tokenizer, framework='pt')
#     output_text = summarizer(input_text, min_length=min_length, max_length=max_length)
#     return output_text[0]['summary_text']


# MODEL 2
# @logger.catch
# def summarize_text(input_text: str, min_length: int, max_length: int) -> str:
#     summarizer = Summarizer()
#     summary = summarizer(input_text, min_length=min_length, max_length=max_length)
#     return summary

nltk.download('punkt')


# MODEL 3
@logger.catch
def summarize_text(input_text: str, sentences_count: int) -> str:
    parser = PlaintextParser.from_string(input_text, Tokenizer('ukrainian'))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count=sentences_count)
    return '. '.join([str(sentence) for sentence in summary])
