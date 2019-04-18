import re
res = re.findall(r"<title>(.+?)</title>", html)
#res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
#print("\nPage paragraph is: ", res[0])
print("\nPage title is: ", res[0])