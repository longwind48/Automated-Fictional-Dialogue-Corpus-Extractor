from bs4 import BeautifulSoup
import requests
import nltk


def get_soup(http_link):
    """get web page content"""
    page = requests.get(http_link)
    encoding = page.encoding if 'charset' in page.headers.get('content-type', '').lower() else None
    soup = BeautifulSoup(page.content, features="html.parser", from_encoding=encoding)
    # print(soup.prettify())
    return soup


def get_p_tag_text(soup):
    p_texts = [i.get_text() for i in soup.findAll('p')]
    return p_texts


def preprocess(text):
    text = text.replace('\r\n', ' ')
    text = text.strip()
    return text


def tokenize(paragraph_list):
    tokenized_sents = []
    for i in paragraph_list:
        tokenized_sents.extend(nltk.sent_tokenize(i))
    return tokenized_sents


def get_fiction_sentences(http_link):
    soup = get_soup(http_link)
    p_texts = get_p_tag_text(soup)
    p_texts = [preprocess(i) for i in p_texts]
    p_texts = [i for i in p_texts if i]
    sentences = tokenize(p_texts)
    return sentences


if __name__ == "__main__":
    sentences = get_fiction_sentences("https://www.gutenberg.org/files/42671/42671-h/42671-h.htm")
    print(sentences[0:20])
