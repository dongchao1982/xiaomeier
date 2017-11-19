#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from jieba.analyse import ChineseAnalyzer
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in
from whoosh.index import open_dir
import os.path

class command(object):
    def __init__(self):
        self.indexPath = "../temp/index"
        self.commandPath = "../data/command/"

    #构建索引，用于检索
    def create_index(self):
        analyzer = ChineseAnalyzer()
        schema = Schema(titel=TEXT(stored=True, analyzer=analyzer), path=ID(stored=True),
                        content=TEXT(stored=True, analyzer=analyzer))
        if not os.path.exists(self.indexPath):
            os.mkdir(self.indexPath)
        ix = create_in(self.indexPath, schema)
        writer = ix.writer()
        for parents, dirnames, filenames in os.walk(self.commandPath):
            for filename in filenames:
                title = filename.replace(".txt", "").decode('utf8')
                print title
                content = open(self.commandPath + '/' + filename, 'r').read().decode('utf-8')
                path = u"/b"
                writer.add_document(titel=title, path=path, content=content)
        writer.commit()

    #检索函数
    def search(self,searchWords):
        title_list = []
        ix = open_dir(self.indexPath)
        searcher = ix.searcher()
        results = searcher.find("content", searchWords)
        #按匹配率降序排序
        # ...
        .
        for hit in results:
            print hit['titel'],hit.score,hit.highlights("content", top=10)
            title_list.append(hit['titel'])
        return title_list

if __name__=="__main__":
    cmd = command()
    print "BEGIN create_index"
    cmd.create_index()
    print "END create_index"