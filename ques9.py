import re
class Tokenizer:
        def __init__(self):
            self.regex = {
                'punctuation': r'[!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]',
                'date': r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})\b',
                'url': r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
                'number': r'\b(?:\d{1,3}(?:,\\d{3})*|\\d+)(?:\\.\\d+)?\b',
                'social_media': r'@[A-Za-z0-9_]+',
                'unicode': r'[\u00C0-\u024F\u1E00-\u1EFF]+'
            }
            self.token_pattern = '|'.join(f'(?P<{key}>{value})' for key, value in self.regex.items())

        def tokenize(self, text):
            tokens = []
            for match in re.finditer(self.token_pattern, text):
                for name, value in match.groupdict().items():
                    if value:
                        tokens.append((name, value))
            return tokens

text = """We use both first and third-party cookies to personalise web content, analyse visits to our websites and tailor advertisements. Some of these cookies are necessary for the website to function, whilst others require your consent. More detail can be found in our cookie policy and you can tailor your choices in the preference centre."""

tokenizer = Tokenizer()
tokens = tokenizer.tokenize(text)

for token in tokens:
        print(f"Type: {token[0]}, Value: {token[1]}")
