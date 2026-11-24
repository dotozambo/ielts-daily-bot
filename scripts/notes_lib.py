"""정리 노트 데이터 헬퍼. 노트 파일(notes_w*.py)에서 사용한다."""
import re
from urllib.parse import quote


def _yg_phrase(en: str) -> str:
    """YouGlish 검색어: '~', '...', '+ 명사' 같은 표시를 지우고 첫 번째 대안만 남긴다."""
    s = en.split(" / ")[0].split(" → ")[0]
    s = re.sub(r"\+.*$", "", s)
    s = s.replace("~", "").replace("...", "").replace("…", "")
    s = re.sub(r"[,.?!]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def youglish(phrase: str) -> str:
    return f"https://youglish.com/pronounce/{quote(phrase)}/english"


def cambridge(word: str) -> str:
    return f"https://dictionary.cambridge.org/dictionary/english/{quote(word.lower().replace(' ', '-'))}"


def I(en, ko, usage, examples, mistake, kw=None, ipa=None, yg=None):
    """핵심 표현 1개.
    examples: [("w" | "s", 문장)]  w = Writing 예문, s = Speaking 예문
    kw/ipa: 발음 키워드와 IPA (없으면 YouGlish 링크만)
    yg: YouGlish 검색어 (없으면 en에서 자동 생성)
    """
    phrase = yg or _yg_phrase(en)
    return {
        "en": en, "ko": ko, "usage": usage,
        "examples": [{"type": t, "text": x} for t, x in examples],
        "mistake": mistake,
        "pron": {
            "word": kw, "ipa": ipa,
            "youglish": youglish(phrase),
            "dict": cambridge(kw) if kw else None,
        },
    }


def Q(q, a):
    return {"q": q, "a": a}


def P(en, ko, example):
    """추가 구문 1개"""
    return {"en": en, "ko": ko, "example": example, "youglish": youglish(_yg_phrase(en))}


def Wd(word, ipa, ko, example):
    """추가 단어 1개"""
    return {"en": word, "ipa": ipa, "ko": ko, "example": example,
            "youglish": youglish(word), "dict": cambridge(word)}
