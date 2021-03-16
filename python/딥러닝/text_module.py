def preprocessing(txt):
    import re
    txt = re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', txt)
    sw = set() # 집합자료형 선언
    with open('stopwords-ko.txt', encoding='utf-8') as f:
        for w in f:
            sw.add(w.replace('\n',''))
    doc = []
    from eunjeon import Mecab
    mecab = Mecab()
    for word in mecab.morphs(txt):
        if word not in sw and len(word) > 1:
            doc.append(word)
    return doc
