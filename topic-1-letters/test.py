import re

patterns = [
    [r"\d*\.\d+  | \d+\.\d* | \d+", "number"],
    [r"\+", "+"],
    [r"\.", "error"]
]


for pattern in patterns:
    pattern[0] = re.compile(pattern[0]);
    print(pattern[0])

def tokenize(char):
    index = 0;
    while index < len(char):
        for pattern,tag in patterns:
            match = pattern.match(char,index);
            if match:
                break;
        assert match;

        if tag == "error":
            raise Exception(f"Syntax error: illegal character :{[match.group(0)]}");
        token = {"tag":tag,"position":index};
        value = match.group(0);