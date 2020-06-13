import re
import string

def clean(data):
    data['clean_text'] = data['text'].apply(lambda x: removeURL(x))
    data['clean_text'] = data['clean_text'].apply(lambda x: removeEmoji(x))
    data['clean_text'] = data['clean_text'].apply(lambda x: removeHtml(x))
    data['clean_text'] = data['clean_text'].apply(lambda x: removePunct(x))
    return data

def removeURL(text):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'', text)

def removeEmoji(text):
    emoji_pattern = re.compile(
        '['
        u'\U0001F600-\U0001F64F'  # emoticons
        u'\U0001F300-\U0001F5FF'  # symbols & pictographs
        u'\U0001F680-\U0001F6FF'  # transport & map symbols
        u'\U0001F1E0-\U0001F1FF'  # flags (iOS)
        u'\U00002702-\U000027B0'
        u'\U000024C2-\U0001F251'
        ']+',
        flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def removeHtml(text):
    html = re.compile(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    return re.sub(html, '', text)

def removePunct(text):
    table = str.maketrans('', '', string.punctuation)
    return text.translate(table)