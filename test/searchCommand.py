#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from jieba.analyse import ChineseAnalyzer
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in
from whoosh.index import open_dir
import os.path

#构建索引，用于检索
def create_index(document_dir):
    analyzer = ChineseAnalyzer()
    schema = Schema(titel=TEXT(stored=True, analyzer=analyzer), path=ID(stored=True),
                    content=TEXT(stored=True, analyzer=analyzer))
    if not os.path.exists("index"):
        os.mkdir("index")
    ix = create_in("index", schema)
    writer = ix.writer()
    for parents, dirnames, filenames in os.walk(document_dir):
        for filename in filenames:
            title = filename.replace(".txt", "").decode('utf8')
            print title
            content = open(document_dir + '/' + filename, 'r').read().decode('utf-8')
            path = u"/b"
            writer.add_document(titel=title, path=path, content=content)
    writer.commit()

#检索函数
def search(search_str):
    title_list = []
    ix = open_dir("index")
    searcher = ix.searcher()
    print "search string:", search_str, type(search_str)
    results = searcher.find("content", search_str)
    for hit in results:
        print hit['titel']
        print hit.score
        print hit.highlights("content", top=10)
        title_list.append(hit['titel'])
    return title_list

# create_index("./text/")
lst = search("我是中国的")
print "list:",lst