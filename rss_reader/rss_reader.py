
import feedparser
import argparse
import json

name , version = "rss_reader", "0.1"

log = None
def get_logger(enable_verbose):
    if enable_verbose:
        def log(msg):
            print(msg)
        return log
    else:
        def fake_loger(msg):
            pass
        return fake_loger



def print_content(contents, asjson):
    if asjson:
        log(json.dumps(contents, sort_keys=False, indent=4))

    else:
        for content in contents:
            for item_key, item_val in content.items():
                print(f"{item_key}: {item_val}")
            print()
    log(f"Iteration has been succesful number of feed: {len(contents)}")

def get_contents(content_link: str, limit: int):
    feed = feedparser.parse(content_link)
    list_of_news = []
    entries = iter(feed["entries"])
    while limit != 0:
        try:
            item = next(entries)
            list_of_news.append({
                    "Title:": item["title"],
                    "Published:": item["published"],
                    "Link:": item["link"],
                    "[image 2:": item['title_detail']['value'],
                    })
            limit -= 1
        except StopIteration as e:
            log(e)
            break
    return tuple(list_of_news)



def parse_args():
    parser = argparse.ArgumentParser(description='show this help message and exit')
    parser.add_argument('source', help='Enter a RSS URL to receive its title.')
    parser.add_argument('--limit', help='Limit news topics if this parameter provided', type=int, required=False)
    parser.add_argument('--version', help='Print version info', action='version', version=f"{name} {version}")
    parser.add_argument('--json', help='Print result as JSON in stdout', default=False, action='store_true', required=False)
    parser.add_argument('--verbose', help='Outputs verbose status messages', default=False, action='store_true', required=False)
    return vars(parser.parse_args())



def main():
    args = parse_args()
    log = get_logger(args["verbose"])
    log(f"Args received: {args}")
    contents = get_contents(args.get("source"), args.get("limit") or -1)  # limit -1 is no limit
    print_content(contents, args.get("json"))

if __name__ == "__main__":
    main()


