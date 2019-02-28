# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()   # 城市
    positionName = scrapy.Field()  # 职位名称
    positionType = scrapy.Field()  # 职位类型
    workYear = scrapy.Field()  # 工作经验
    education = scrapy.Field() # 学历要求
    financingStage = scrapy.Field()  # 融资阶段
    companySize = scrapy.Field()     # 公司规模
    CompanyField = scrapy.Field()    # 公司领域
    postTime = scrapy.Field()        # 发布时间
    salaryMax = scrapy.Field()       # 最高工资
    salaryMin = scrapy.Field()       # 最低工资
    companyFullName = scrapy.Field()  # 公司名称
    companyShortName = scrapy.Field() # 公司短名称
    jobNature = scrapy.Field()       # 工作类型
    positionAdvantage = scrapy.Field()   # 职位诱惑
    skillLables = scrapy.Field()     # 技能标签
    hitags = scrapy.Field()          # 标签
    positionId = scrapy.Field()      # 公司id
    url = scrapy.Field()             # 拉勾网的链接(https://www.lagou.com/jobs/positionId.html)
    jobDescription = scrapy.Field()  # 职位描述
    workAddress = scrapy.Field()     # 工作地址