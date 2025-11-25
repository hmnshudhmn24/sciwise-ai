import difflib
def unified_diff(a,b):
    return '\n'.join(difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm=''))
