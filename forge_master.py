#!/usr/bin/env python3

import json
import random
import time
import urllib.request

QUESTS_URL = "https://jsonplaceholder.typicode.com/posts"
ENDPOINTS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/users/1",
]


def forge_quest():
    with urllib.request.urlopen(QUESTS_URL, timeout=10) as r:
        posts = json.loads(r.read().decode("utf-8"))
    post = random.choice(posts)
    return {"quest": f"Найти исполнителя для: {post['title']}", "post_id": post["id"]}


def pulse():
    out = []
    for e in ENDPOINTS:
        start = time.time()
        with urllib.request.urlopen(e, timeout=10) as r:
            out.append({"endpoint": e, "status": r.status, "ms": round((time.time() - start) * 1000, 2)})
    return out


def smith():
    with urllib.request.urlopen(QUESTS_URL, timeout=10) as r:
        posts = json.loads(r.read().decode("utf-8"))
    return {"total": len(posts), "titles": [p.get("title", "") for p in posts[:5]]}


def main():
    print(json.dumps({
        "quest": forge_quest(),
        "pulse": pulse(),
        "smith": smith(),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
