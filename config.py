"""FDA規制インサイト - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "FDA規制インサイト"
BLOG_DESCRIPTION = (
    "FDAの承認プロセス・規制要件・ガイダンス文書を日本語でわかりやすく解説。"
    "海外の最新FDA動向を翻訳・要約し、日本の製薬企業・CROの実務担当者に向けた情報を毎日発信。"
)
BLOG_URL = "https://pharmaworkerka.github.io/fda-insight"
BLOG_TAGLINE = "FDA規制の最新動向を日本語で発信"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "PharmaworkerKA/fda-insight"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "FDA承認プロセス",
    "FDAガイダンス文書",
    "Warning Letter分析",
    "PMDA vs FDA比較",
    "FDA最新ニュース",
    "eCTD・電子申請",
    "バイオ医薬品規制",
    "海外トレンド翻訳",
]

THEME = {
    "primary": "#dc2626",
    "accent": "#991b1b",
    "gradient_start": "#dc2626",
    "gradient_end": "#b91c1c",
    "dark_bg": "#1a0000",
    "dark_surface": "#2d0a0a",
    "light_bg": "#fef2f2",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 1
SCHEDULE_HOURS = [8]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Amazon FDA/規制書籍": {
        "url": "https://www.amazon.co.jp",
        "text": "AmazonでFDA・薬事規制の書籍を探す",
        "description": "FDA規制・薬事申請の参考書",
    },
    "Udemy 薬事講座": {
        "url": "https://www.udemy.com",
        "text": "Udemyで薬事・レギュラトリー講座を探す",
        "description": "動画で学ぶFDA規制・薬事申請",
    },
    "楽天 医薬品規制書籍": {
        "url": "https://www.rakuten.co.jp",
        "text": "楽天で医薬品規制の書籍を探す",
        "description": "医薬品規制・承認申請の参考書",
    },
    "SAS認定資格": {
        "url": "https://www.sas.com/ja_jp/certification.html",
        "text": "SAS認定資格を取得する",
        "description": "SASプログラミングの公式認定",
    },
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)

DASHBOARD_HOST = "127.0.0.1"
DASHBOARD_PORT = 8092

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-CSFVD34MKK"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
