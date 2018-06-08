# -- coding: utf-8 --

from aip import AipNlp
import json

APP_ID = '11369403'
API_KEY = 'XnQZAWv2HZmgsYvKDfzaCOH7'
SECRET_KEY = 'w0axcSkajOvqz25QVRT9HDkkfu5g1GxI'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# # 词法分析
# text = '云养邦是一家伟大的科技公司'
# print json.dumps(client.lexer(text), sort_keys = True, indent = 4).encode('utf-8').decode('unicode_escape')


# # 词法分析-定制版
# text = '云养邦是一家伟大的科技公司'
# print json.dumps(client.lexerCustom(text), sort_keys = True, indent = 4).encode('utf-8').decode('unicode_escape')

# # 依存句法分析
# text = '云养邦是一家伟大的科技公司'
# options = {}
# options["mode"] = 0
# print json.dumps(client.depParser(text,options), sort_keys = True, indent = 4).encode('utf-8').decode('unicode_escape')

# # 词向量表示
# text = '张飞'
# print json.dumps(client.wordEmbedding(text), sort_keys = True, indent = 4).encode('utf-8').decode('unicode_escape')

# # DNN语言模型
# text = '百度是一家伟大的科技公司'
# print json.dumps(client.dnnlm(text), sort_keys = True, indent = 4).encode('utf-8').decode('unicode_escape')

# # 词义相似度
# text1 = '北京'
# text2 = '上海'
# print json.dumps(client.wordSimEmbedding(text1, text2), sort_keys = True, indent = 4).encode('utf-8').decode('unicode_escape')

# # 短文本相似度
# text1 = '养胃粉'
# text2 = '养胃'
# print json.dumps(client.simnet(text1, text2), sort_keys = True, indent = 4).encode('utf-8').decode('unicode_escape')

# # 评论观点抽取
# text1 = '益生菌治疗腹泻的效果非常好'
# options = {}
# options['type'] = 4
# print json.dumps(client.commentTag(text1,options), sort_keys = True, indent = 4).encode('utf-8').decode('unicode_escape')

# # 情感倾向分析
# text1 = '养胃粉治疗胃胀的效果非常好'
# print json.dumps(client.sentimentClassify(text1), sort_keys = True, indent = 4).encode('utf-8').decode('unicode_escape')

# # 文章标签
# text1 = 'NC养胃粉的效果报告'
# content = '根据NC搜狐的调查报告来看，中国大部分人会有胃胀的毛病。临床现象来看，NC养胃粉对胃胀有非常显著的治疗效果'
# print json.dumps(client.keyword(text1,content), sort_keys = True, indent = 4).encode('utf-8').decode('unicode_escape')

# 文章分类
text1 = 'NC养胃粉的效果报告'
content = '根据NC搜狐的调查报告来看，中国大部分人会有胃胀的毛病。临床现象来看，NC养胃粉对胃胀有非常显著的治疗效果'
print json.dumps(client.topic(text1,content), sort_keys = True, indent = 4).encode('utf-8').decode('unicode_escape')
