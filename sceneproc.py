
# with open('./external/store stuff.txt', 'r', encoding = 'utf-8') as f:
#     lines = f.readlines()
#
# out = []
# curCls = ''
# for line in lines:
#     if line == '\n':
#         continue
#     if line.endswith('类\n'):
#         curCls = line[:-1]
#         continue
#
#     name, price = line[:-1].split()[0], line[:-1].split()[-1]
#     out.append({
#         'title': '商品名称：' + name,
#         'content': '商品类别：' + curCls + ' 商品价格：' + price
#     })
#
# with open('./external/store stuff.json', 'w', encoding = 'utf-8') as f:
#     print(str(out), file = f)

with open('./external/lib.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()

out = []
for i in range(0, len(lines), 4):
    out.append({
        'title': lines[i],
        'content': lines[i + 1] + lines[i + 2] + lines[i + 3]
    })

with open('./external/lib.json', 'w', encoding = 'utf-8') as f:
    print(str(out), file = f)