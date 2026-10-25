#!/usr/bin/env python3
"""Build the study site from the repo.

Sources (all optional, picked up automatically):
  NN-topic/README.md            topic page (first heading = title, a "Project:" line = project)
  NN-topic/NN-sub/notes.md      one page per sub-chunk; progress comes from its "Status:" checkboxes
  docs/*.md                     extra pages (material.md, study-loop.md, ...)
  boards/NN-*.html              illustration boards; a board whose name starts with a topic's
                                number is linked from that topic

Usage:  python site/build.py            -> writes _site/
Needs:  pip install markdown
"""
import html
import re
import shutil
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"
THEME = Path(__file__).resolve().parent / "theme.css"
REPO_URL = "https://github.com/ahmdhsn8/embedded-foundations"
NUM = re.compile(r"^(\d\d)-(.+)$")

MD_EXT = ["tables", "fenced_code", "sane_lists"]


# ---------------------------------------------------------------- helpers
def md_to_html(text: str) -> str:
    out = markdown.markdown(text, extensions=MD_EXT, output_format="html")
    out = out.replace("[x]", '<span class="box on">&#10003;</span>').replace("[X]", '<span class="box on">&#10003;</span>')
    out = out.replace("[ ]", '<span class="box"></span>')
    return out


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def strip_first_heading(text: str) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return "\n".join(lines[:i] + lines[i + 1:])
    return text


def pretty(slug: str) -> str:
    return slug.replace("-", " ").capitalize()


def status_of(notes: str) -> str:
    """'done' when every Status checkbox is ticked, 'doing' when some are, else 'todo'."""
    for line in notes.splitlines():
        if line.lower().startswith("status:"):
            ticked = len(re.findall(r"\[[xX]\]", line))
            total = ticked + line.count("[ ]")
            if total and ticked == total:
                return "done"
            return "doing" if ticked else "todo"
    return "todo"


STATUS_LABEL = {"done": "done", "doing": "in progress", "todo": "not started"}


def page(title: str, body: str, prefix: str, crumbs: list) -> str:
    nav = " <span>/</span> ".join(
        f'<a href="{prefix}{href}">{html.escape(label)}</a>' if href else html.escape(label)
        for label, href in crumbs
    )
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title)} · Embedded Foundations</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat+Brush&family=Patrick+Hand&display=swap">
<link rel="stylesheet" href="{prefix}theme.css">
</head><body>
<div class="wrap">
<nav class="crumbs">{nav}</nav>
{body}
<footer class="small">Built from <a href="{REPO_URL}">the repo</a>. Edit the markdown, push, and this page rebuilds.</footer>
</div>
</body></html>
"""


def write(rel: str, content: str):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------- collect
def collect():
    boards = sorted((ROOT / "boards").glob("*.html")) if (ROOT / "boards").is_dir() else []
    topics = []
    for d in sorted(ROOT.iterdir()):
        m = NUM.match(d.name)
        if not (d.is_dir() and m):
            continue
        readme = (d / "README.md").read_text(encoding="utf-8") if (d / "README.md").exists() else ""
        project = ""
        for line in readme.splitlines():
            if line.lower().startswith("project:"):
                project = line.split(":", 1)[1].strip()
        subs = []
        for s in sorted(d.iterdir()):
            sm = NUM.match(s.name)
            if s.is_dir() and sm and (s / "notes.md").exists():
                notes = (s / "notes.md").read_text(encoding="utf-8")
                srcs = sorted(p.relative_to(ROOT).as_posix() for p in s.rglob("*") if p.is_file() and p.name != "notes.md")
                subs.append({
                    "num": sm.group(1), "slug": s.name, "title": first_heading(notes, pretty(sm.group(2))),
                    "notes": notes, "status": status_of(notes), "src": srcs,
                })
        topics.append({
            "num": m.group(1), "slug": d.name, "title": first_heading(readme, pretty(m.group(2))),
            "readme": readme, "project": project, "subs": subs,
            "boards": [b for b in boards if b.name.startswith(m.group(1) + "-")],
        })
    docs = sorted((ROOT / "docs").glob("*.md")) if (ROOT / "docs").is_dir() else []
    return topics, boards, docs


def topic_status(t):
    if not t["subs"]:
        return "todo"
    st = [s["status"] for s in t["subs"]]
    if all(x == "done" for x in st):
        return "done"
    return "doing" if any(x != "todo" for x in st) else "todo"


# ---------------------------------------------------------------- render
def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copy(THEME, OUT / "theme.css")
    topics, boards, docs = collect()
    doc_titles = {}

    # docs pages
    for p in docs:
        text = p.read_text(encoding="utf-8")
        title = first_heading(text, pretty(p.stem))
        doc_titles[p.stem] = title
        body = f'<header class="hero"><span class="tag">reference</span><h1>{html.escape(title)}</h1></header>' \
               f'<article class="paper md">{md_to_html(strip_first_heading(text))}</article>'
        write(f"{p.stem}.html", page(title, body, "", [("Home", "index.html"), (title, None)]))

    # boards: copy, add a page skeleton when the file has none, add a back link
    for b in boards:
        src = b.read_text(encoding="utf-8")
        back = '<a class="back-to-site" href="../index.html">&larr; Embedded Foundations</a>'
        style = ('<style>.back-to-site{position:fixed;right:max(12px,env(safe-area-inset-right,0px));bottom:12px;z-index:50;'
                 'font:16px "Patrick Hand","Comic Sans MS",cursive;background:#ffe45c;color:#2b3034;border:2px solid #2b3034;'
                 'border-radius:8px;padding:2px 10px;text-decoration:none}</style>')
        if "<!doctype" not in src[:200].lower():
            src = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
                   '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
                   '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>'
                   f'</head><body>{src}{style}{back}</body></html>')
        else:
            src = src.replace("</body>", f"{style}{back}</body>", 1)
        write(f"boards/{b.name}", src)

    # topic + sub-chunk pages
    for t in topics:
        base = f"t/{t['slug']}"
        rows = []
        for i, s in enumerate(t["subs"]):
            rows.append(
                f'<li class="{s["status"]}"><a href="{s["slug"]}.html"><b>{int(s["num"])}</b>{html.escape(s["title"])}'
                f'<span class="st">{STATUS_LABEL[s["status"]]}</span></a></li>')
            prev_l = f'<a href="{t["subs"][i-1]["slug"]}.html">&larr; {html.escape(t["subs"][i-1]["title"])}</a>' if i > 0 else "<span></span>"
            next_l = f'<a href="{t["subs"][i+1]["slug"]}.html">{html.escape(t["subs"][i+1]["title"])} &rarr;</a>' if i + 1 < len(t["subs"]) else "<span></span>"
            src_links = "".join(f'<li><a href="{REPO_URL}/blob/main/{p}"><code>{html.escape(p)}</code></a></li>' for p in s["src"])
            board_links = "".join(f'<a class="chip" href="../../boards/{b.name}">open the illustration board</a>' for b in t["boards"])
            body = (
                f'<header class="hero"><span class="tag">topic {int(t["num"])} · sub-chunk {int(s["num"])} of {len(t["subs"])}</span>'
                f'<h1>{html.escape(s["title"])}</h1><p><span class="stamp {s["status"]}">{STATUS_LABEL[s["status"]]}</span>{board_links}</p></header>'
                f'<article class="paper md">{md_to_html(strip_first_heading(s["notes"]))}</article>'
                + (f'<article class="paper"><h3>Code and files</h3><ul>{src_links}</ul></article>' if src_links else "")
                + f'<nav class="pager">{prev_l}{next_l}</nav>'
            )
            write(f"{base}/{s['slug']}.html", page(s["title"], body, "../../",
                  [("Home", "index.html"), (t["title"], f"{base}/index.html"), (s["title"], None)]))

        done = sum(s["status"] == "done" for s in t["subs"])
        readme_body = strip_first_heading(t["readme"])
        readme_body = re.sub(r"(?im)^project:.*$", "", readme_body)
        readme_body = re.sub(r"(?s)\n\|\s*#\s*\|.*?(?=\n\n|\Z)", "", readme_body)  # drop the README's progress table; the strip replaces it
        board_cards = "".join(f'<a class="chip" href="../../boards/{b.name}">illustration board: {html.escape(pretty(NUM.match(b.stem).group(2) if NUM.match(b.stem) else b.stem))}</a>' for b in t["boards"])
        body = (
            f'<header class="hero"><span class="tag">topic {int(t["num"])} of {len(topics)}</span><h1>{html.escape(t["title"])}</h1>'
            + (f'<p><b>Project:</b> {html.escape(t["project"])}</p>' if t["project"] else "")
            + (f'<p>{board_cards}</p>' if board_cards else "") + "</header>"
            + (f'<section class="chapter"><h2>{done} of {len(t["subs"])} sub-chunks done</h2><ol class="dots">{"".join(rows)}</ol></section>' if t["subs"]
               else '<section class="chapter"><p class="paper">Sub-chunks get added when we reach this topic.</p></section>')
            + (f'<article class="paper md">{md_to_html(readme_body)}</article>' if readme_body.strip() else "")
        )
        write(f"{base}/index.html", page(t["title"], body, "../../", [("Home", "index.html"), (t["title"], None)]))

    # home
    all_subs = [s for t in topics for s in t["subs"]]
    done_all = sum(s["status"] == "done" for s in all_subs)
    cards = []
    for t in topics:
        st = topic_status(t)
        d = sum(s["status"] == "done" for s in t["subs"])
        count = f"{d}/{len(t['subs'])} sub-chunks" if t["subs"] else "not planned yet"
        cards.append(
            f'<li class="{st}"><a href="t/{t["slug"]}/index.html"><b>{int(t["num"])}</b>'
            f'<span class="tt">{html.escape(t["title"].split(":", 1)[-1].strip())}</span>'
            f'<span class="pj">{html.escape(t["project"])}</span><span class="st">{STATUS_LABEL[st]} · {count}</span></a></li>')
    board_list = "".join(
        f'<li><a href="boards/{b.name}">{html.escape(pretty(NUM.match(b.stem).group(2)) if NUM.match(b.stem) else pretty(b.stem))}</a></li>' for b in boards)
    doc_list = "".join(f'<li><a href="{stem}.html">{html.escape(title)}</a></li>' for stem, title in doc_titles.items())
    body = f"""
<header class="hero">
  <span class="tag">NUCLEO-F446RE · STM32F446RE · Cortex-M4F</span>
  <h1>Embedded Foundations</h1>
  <p>Seven topics, one project each, in order. Read the manual, predict, build it yourself, check it in GDB, break it, explain it back.</p>
  <p class="big">{done_all} of {len(all_subs)} planned sub-chunks done</p>
</header>
<section class="chapter"><span class="tag">part 1 · basics</span><ol class="dots topics">{''.join(cards[:4])}</ol></section>
<section class="chapter"><span class="tag">part 2 · the core</span><ol class="dots topics">{''.join(cards[4:])}</ol></section>
<section class="chapter grid">
  <article class="paper"><h3>Illustration boards</h3><ul>{board_list or '<li>None yet.</li>'}</ul></article>
  <article class="paper"><h3>Reference</h3><ul>{doc_list}</ul></article>
</section>"""
    write("index.html", page("Home", body, "", [("Home", None)]))
    (OUT / ".nojekyll").write_text("")
    print(f"built {OUT} : {len(topics)} topics, {len(all_subs)} sub-chunks, {len(boards)} boards, {len(docs)} docs")


if __name__ == "__main__":
    sys.exit(build())
