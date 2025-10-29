def string_tools(s):
    """"返回常用字符串处理结果"""
    return {
        "upper": s.upper(),
        "lower": s.lower(),
        "title": s.title(),
        "strip": s.strip(),
        "replace": s.replace("a","@"),
        "join": "-".join(["a","b"]),
        "startswith": s.startswith("h"),
        "isdigit": s.isdigit(),
        "split": s.split(),
        "legth": len(s)
    }
text = "   hello world   "
result = string_tools(text)
print(result)