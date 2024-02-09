

with open('./external/poem.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()

print(lines)

out = []
for i in range(len(lines) - 1):
    if lines[i] == '\n' or lines[i + 1] == '\n':
        continue
    out.append({
        'instruction': '请为这一句诗续写下一句：' + lines[i],
        'output': lines[i + 1]
    })

with open('./external/jhz.json', 'w', encoding = 'utf-8') as f:
    print(str(out), file = f)