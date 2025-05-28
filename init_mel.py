# init_meili.py
import os
import meilisearch
from dotenv import load_dotenv

load_dotenv()

# MeiliSearch 연결
client = meilisearch.Client(
    url=os.getenv('MEILI_SEARCH_URL'),
    api_key=os.getenv('MEILI_SEARCH_KEY')
)

# 예시 데이터 (또는 result_d 변수로 로딩된 데이터)
documents = [
    {"id": 1, "symbol": "AAPL", "name": "Apple Inc."},
    {"id": 2, "symbol": "MSFT", "name": "Microsoft Corporation"},
    {"id": 3, "symbol": "GOOGL", "name": "Alphabet Inc."}
]

# 인덱스에 문서 추가 (없으면 자동 생성)
client.index('nasdaq').add_documents(documents, primary_key='id')
print("✅ 'nasdaq' 인덱스 생성 및 문서 추가 완료")
