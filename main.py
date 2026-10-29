#!/usr/bin/env python3

import json
import sys
from typing import List, Dict, Any

import requests

API_BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_posts(user_id: int | None = None) -> List[Dict[str, Any]]:
    endpoint = f"{API_BASE_URL}/posts"
    params = {"userId": user_id} if user_id is not None else None

    try:
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        print(f"Ошибка при запросе к API: {exc}", file=sys.stderr)
        return []


def save_to_json(data: List[Dict[str, Any]], filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Сохранено {len(data)} записей в файл '{filename}'")


def main() -> None:
    user_id = int(sys.argv[1]) if len(sys.argv) > 1 else None
    posts = fetch_posts(user_id=user_id)

    if not posts:
        print("Нет данных для сохранения.")
        return

    filename = f"posts_user_{user_id}.json" if user_id else "posts_all.json"
    save_to_json(posts, filename)

    titles = [post["title"] for post in posts[:5]]
    print("Первые 5 заголовков:")
    for title in titles:
        print(f"  - {title}")


if __name__ == "__main__":
    main()
