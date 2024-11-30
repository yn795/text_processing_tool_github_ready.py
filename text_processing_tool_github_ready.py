
import re

def remove_unwanted_text(text, removal_list):
    """Remove unwanted words or symbols from the text."""
    for word in removal_list:
        text = re.sub(re.escape(word), '', text)
    return text

def replace_keywords(text, find_replace_pairs):
    """Replace specific keywords in the text based on a dictionary."""
    for find, replace in find_replace_pairs.items():
        text = re.sub(re.escape(find), replace, text)
    return text

def add_furigana(text, furigana_dict):
    """Add furigana (reading annotations) to specific words."""
    for word, furigana in furigana_dict.items():
        text = re.sub(re.escape(word), f"{word}（{furigana}）", text)
    return text

def process_text(input_file, output_file):
    """Main function to process text with the given functionalities."""
    # Define the removal list
    removal_list = [
        "/", "／", "0R000", "激しい絵", "ＯＮ", "※", "ドンパチ", "@", "ＮＡ", "NA", "･･･",
        "〝", "〟", "＜", "バン！", "＞", "リポ", "。", "場所時間", "⭐︎", "♪"
    ]

    # Define the find and replace dictionary
    find_replace_pairs = {
        "呼びかけ": "呼び掛け",
        "あまり": "余り",
        "パーセント": "％",
        "きょう": "今日",
        "あす": "明日",
        "あさって": "明後日",
        "きのう": "昨日",
        "おととい": "一昨日"
    }

    # Define the furigana dictionary
    furigana_dict = {
        "蔓延": "まんえん",
        "混沌": "こんとん",
        "対峙": "たいじ",
        "執拗": "しつよう",
        "脆弱": "ぜいじゃく",
        "躊躇": "ちゅうちょ",
        "冤罪": "えんざい",
        "徘徊": "はいかい",
        "晩餐": "ばんさん",
        "牽制": "けんせい",
        "翻弄": "ほんろう"
    }

    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Apply the transformations
    text = remove_unwanted_text(text, removal_list)
    text = replace_keywords(text, find_replace_pairs)
    text = add_furigana(text, furigana_dict)

    # Write the output to a new file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f"Processing complete. Output saved to {output_file}")

# Example usage
if __name__ == "__main__":
    input_file = "input_text.txt"
    output_file = "processed_text.txt"
    process_text(input_file, output_file)
