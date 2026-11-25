import re
import sys
from pathlib import Path

ALLOWED_DOMAINS = {"github.com", "gitlab.com", "docs.python.org"}
SUSPICIOUS_KEYWORDS = [
    r"\.env\b",
    r"id_rsa",
    r"base64",
    r"eval\(",
    r"exec\(",
    r"curl\s+",
    r"wget\s+",
    r"requests\.post",
    r"urllib\.request",
    r"ignore previous instructions",
    r"system override",
]


def check_file(filepath: Path) -> list[str]:
    errors = []
    content = filepath.read_text(encoding="utf-8", errors="replace")
    lines = content.splitlines()

    if re.search(r"[\u200B-\u200F\u202A-\u202E\uFEFF\U000E0000-\U000E007F]", content):
        errors.append("Обнаружены невидимые Unicode-символы (стеганография)")

    if filepath.suffix == ".md" and re.search(r"<!--[\s\S]*?-->", content):
        errors.append("Обнаружен HTML-комментарий <!-- ... --> (возможна маскировка промпта)")

    for idx, line in enumerate(lines, 1):
        if len(line) > 300:
            errors.append(f"Строка {idx} длиннее 300 символов ({len(line)} симв.)")

    for pattern in SUSPICIOUS_KEYWORDS:
        if re.search(pattern, content, re.IGNORECASE):
            errors.append(f"Найден подозрительный паттерн: '{pattern}'")

    urls = re.findall(r"https?://([a-zA-Z0-9.-]+)", content)
    for domain in set(urls):
        if not any(domain == allowed or domain.endswith("." + allowed) for allowed in ALLOWED_DOMAINS):
            errors.append(f"Недоверенный внешний домен: {domain}")

    return errors


def main():
    skills_dirs = [Path(".cursor/skills"), Path(".agents/skills")]
    has_errors = False

    for skills_dir in skills_dirs:
        if not skills_dir.exists():
            continue
        for file in skills_dir.rglob("*"):
            if file.is_file():
                file_errors = check_file(file)
                if file_errors:
                    has_errors = True
                    print(f"\n[FAIL] {file}:")
                    for err in file_errors:
                        print(f"  - {err}")

    if has_errors:
        print("\nПроверка безопасности Skills провалена!")
        sys.exit(1)

    print("[OK] Все Skills прошли проверку безопасности.")


if __name__ == "__main__":
    main()
