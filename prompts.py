"""FDA規制インサイト - プロンプト定義

FDA規制特化ブログ用のプロンプトを一元管理する。
"""

PERSONA = """あなたはFDA規制・薬事申請のエキスパートブロガーです。
RA（Regulatory Affairs・薬事）経験者として、FDAのガイダンス文書・Warning Letterを
翻訳・要約し、日本の製薬企業・CROの実務担当者に向けてわかりやすく解説します。

【文体ルール】
- 「です・ます」調で親しみやすく
- 専門用語には必ず（）で簡単な説明を添える
- FDA固有の略語（NDA、BLA、510(k)等）は初出時に正式名称を併記
- 具体的な操作手順はステップ形式で記載
- 日本（PMDA）との違いを意識した解説を含める
- 比較記事では必ず表形式を使用
- 記事の最初に「この記事でわかること」を箇条書きで提示

【SEOルール】
- タイトルにメインキーワードを必ず含める
- H2/H3見出しにもキーワードを自然に含める
- 冒頭150文字以内にメインキーワードを入れる
- 「結論から言うと」のパターンで冒頭にまとめを置く
- 内部リンク用のアンカーテキストを自然に含める
"""

ARTICLE_FORMAT = """
## この記事でわかること
（3-5個の箇条書き）

## 結論から言うと
（忙しい人向けの3行まとめ）

## {topic}とは？
（初心者向けの基礎解説）

## FDAの要件・プロセス解説
（具体的な規制要件・手順）

## 海外の最新動向
（FDA・EMA等の最新情報）

## 日本（PMDA）との比較・違い
（比較表形式を推奨）

## 実務での対応ポイント
（現場で使える具体的アドバイス）

## よくある質問（FAQ）
（Q&A形式 -- FAQスキーマ対応）

## まとめ
"""

CATEGORY_PROMPTS = {
    "FDA承認プロセス": (
        "NDA・BLA・ANDA・510(k)等の申請プロセスを詳しく解説。"
        "審査タイムライン、Priority Review、Breakthrough Therapy等の制度も説明。"
        "「FDA 承認」「FDA 申請」「NDA とは」をキーワードに。"
    ),
    "FDAガイダンス文書": (
        "FDAが発行するDraft/Final Guidanceの内容を翻訳・要約。"
        "実務への影響と対応策を具体的に提示。"
        "「FDAガイダンス」「FDA guidance 日本語」をキーワードに。"
    ),
    "Warning Letter分析": (
        "FDAが発行したWarning Letterの内容を分析。GMP違反・データインテグリティ違反等を解説。"
        "違反パターンの傾向分析と予防策を提示。"
        "「FDA Warning Letter」「GMP違反」「データインテグリティ」をキーワードに。"
    ),
    "PMDA vs FDA比較": (
        "日本のPMDAとFDAの規制要件・審査プロセスの違いを比較表で解説。"
        "国際共同治験での実務ポイントも含める。"
        "「PMDA FDA 違い」「日米 承認申請 比較」をキーワードに。"
    ),
    "FDA最新ニュース": (
        "FDAの最新承認情報、人事異動、政策変更等の速報。"
        "日本企業への影響を分析。速報性重視。"
    ),
    "eCTD・電子申請": (
        "eCTD（electronic Common Technical Document）のModule構成、"
        "eCTD 4.0への移行、電子申請の実務ポイントを解説。"
        "「eCTD とは」「eCTD 4.0」「電子申請」をキーワードに。"
    ),
    "バイオ医薬品規制": (
        "バイオシミラー・再生医療・遺伝子治療等のFDA規制を解説。"
        "BLA申請、バイオシミラー351(k)申請の実務ポイント。"
        "「バイオシミラー FDA」「BLA 申請」をキーワードに。"
    ),
    "海外トレンド翻訳": (
        "RAPS、Pink Sheet、DIA等の海外メディアの記事を翻訳・要約。"
        "グローバルな規制動向を日本語で解説。"
        "「FDA 最新情報」「海外 薬事 トレンド」をキーワードに。"
    ),
}

KEYWORD_PROMPT_EXTRA = """
FDA規制に関連する日本語キーワードを提案してください。
特に以下のパターンを重視:
- 「FDA 承認」「FDA 申請」系（基礎知識）
- 「FDA ○○ とは」「NDA BLA 違い」系（解説検索）
- 「Warning Letter ○○」「GMP違反 ○○」系（事例分析）
- 「PMDA FDA 違い」「日米 比較」系（比較検索）
- 「eCTD」「電子申請」系（実務系）
- 「FDA 最新」「FDA ガイダンス」系（ニュース系）
月間検索ボリュームが高いと推測されるキーワードを優先してください。
"""

AFFILIATE_SECTION_TITLE = "## FDA規制をもっと深く学ぶためのリソース"
AFFILIATE_INSERT_BEFORE = "## まとめ"

# トピック自動収集用ソース
NEWS_SOURCES = {
    "FDA News": "https://www.fda.gov/news-events",
    "FDA Guidance": "https://www.fda.gov/regulatory-information/search-fda-guidance-documents",
    "FDA Warning Letters": "https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/compliance-actions-and-activities/warning-letters",
    "RAPS": "https://www.raps.org/news-and-articles",
    "Regulatory Focus": "https://www.raps.org/regulatory-focus",
    "Pink Sheet": "https://pink.citeline.com/",
    "PMDA": "https://www.pmda.go.jp/english/about-pmda/outline/0002.html",
    "EMA News": "https://www.ema.europa.eu/en/news",
}

# FAQ用のスキーマテンプレート（SEO対策）
FAQ_SCHEMA_ENABLED = True


def build_keyword_prompt(config):
    """キーワード選定プロンプトを構築する"""
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    return (
        "FDA規制インサイト用のキーワードを選定してください。\n\n"
        "以下のカテゴリから1つ選び、そのカテゴリで今注目されている"
        "FDA規制関連のトピック・キーワードを1つ提案してください。\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    """FDA規制特化の記事生成プロンプトを構築する"""
    category_hint = CATEGORY_PROMPTS.get(category, "")

    return f"""{PERSONA}

以下のキーワードに関する高品質なブログ記事を生成してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度（じっくり読める長さ）

【カテゴリ固有の指示】
{category_hint}

【記事フォーマット】
{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. FAQセクション（よくある質問）を必ず含めること

【条件】
- {config.MAX_ARTICLE_LENGTH}文字程度
- 専門用語には必ず簡単な補足説明を付ける
- 具体的な数字やデータを含める
- 比較表がある場合はMarkdownテーブルで記載
- 内部リンクのプレースホルダーを2〜3箇所に配置（{{{{internal_link:関連トピック}}}}の形式）
- FAQセクションはQ&A形式で3〜5個

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}}
  ]
}}
```

【注意事項】
- content内のMarkdownは適切にエスケープしてJSON文字列として有効にすること
- tagsは5個ちょうど生成すること
- slugは半角英数字とハイフンのみ使用すること
- faqは3〜5個生成すること
- 読者にとって実用的で具体的な内容を心がけること"""
