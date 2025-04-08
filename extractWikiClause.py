#!/usr/bin/python3

# This script is to extract clause from wiki_zh_2019
# file structure: wiki_zh/AA/wiki_00
# each line of the file a in JSON format:
# {"id": "13", "url": "https://zh.wikipedia.org/wiki?curid=13",
# "title": "数学", "text": "数学\n\n数学是利用符号语言研究数量、结构、变化以及空间等概念的一门学科，...另一新的七个重要问题，称为千禧年大奖难题，发表于2000年。对其每一个问题的解答都有著一百万美元的奖金，而当中只有一个问题（黎曼猜想）和希尔伯特的问题重复。\n\n\n\n"}

import os
import json
import re

wikiRoot = '../wiki_zh'

def extractClause(s):
    # 分割字符串
    parts = re.split(r'\s+|[，。、；：？！“”‘’()（）【】《》,.?!;:\"\'\[\]\(\)\{\}]', s)
    # 过滤只包含中文字符的元素
    return [part for part in parts if re.match(r'^[\u4e00-\u9fa5]+$', part)]

def processFiles(directory):
    allClauses = {}

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    try:
                        data = json.loads(line)
                        if 'text' in data:
                            clauses = extractClause(data['text'])
                            #[print(s) for s in clauses]
                            for clause in clauses:
                                if (len(clause) < 20):
                                    if (clause in allClauses):
                                        allClauses[clause] += 1
                                    else:
                                        allClauses[clause] = 1
                    except json.JSONDecodeError:
                        continue

    return allClauses

allClauses = processFiles(wikiRoot)
for clause, count in allClauses.items():
    if (count > 2):
        print(clause)