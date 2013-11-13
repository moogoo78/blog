Title: Deploying Flask (Python) to AWS Elastic Beanstalk
Date: 2013-11-12 17:31
Category: computer
Tags: flask, aws
Slug: aws_elastic_beanstalk_flask

# quickstart
## 1. 安裝eb commend tools

下載: [AWS Elastic Beanstalk Command Line Tool : Sample Code & Libraries : Amazon Web Services](http://aws.amazon.com/code/6752709412171743)
    
   設定好路徑(以mac為例), 就可以開始了

    :::bash
    AWS-ElasticBeanstalk-CLI-2.5.1/eb/macosx/python2.7/eb

    # 環境變數, 可以在shell下export或是寫在~/.elasticbeanstalk/aws_credential_file裡 (忘記是我自己加的還是eb工具自動加的)
    AWSAccessKeyId=Write your AWS access ID
    AWSSecretKey=Write your AWS secret key

## 2. 準備部署

### WSGI

預設是application.py:application, 自己要改application.py名字失敗

    :::plain
    [aws:elasticbeanstalk:container:python]
    ...
    WSGIPath=my_fail_wsgi

### 連接原本的RDS
要去RDS的security group那裡新增一個(因為等於是開了一個新的EC2)，通常是awseb-xxx 開頭的

### Elastic Beanstalk沒有filesystem

* 所以原本的media檔要改存到S3
* 原本logger有自己存檔, 也要取消 (反正會出現在eb的log裡)

## 3. 跑起來

    :::bash
    # 在git目錄下操作, 如果沒有repo就會叫你git init
    eb init
    # 會有選單, 開始勾選
    # 平台選這個
    64bit Amazon Linux 2013.09 running Python 2.7
    # 勾完後, 就可以啟動餓了
    eb start
    # 問你要用那個version deploy, 預設最新的
    # 等個幾分鐘

    # 改程式後git commit
    # git aws.push -> 自動傳到eb環境

    # 其他指令
    eb status --verbose 




## 設定
產生 **.ebextensions**目錄, 新增 python.config:

    option_settings:
      "aws:elasticbeanstalk:container:python:staticfiles":
        "/static/": "myapp/static/"


### 參考

* [Deploying a Flask Application to AWS Elastic Beanstalk - AWS Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Python_flask.html) 
* [AWS Elastic Beanstalk FAQs](http://aws.amazon.com/elasticbeanstalk/faqs/)
* [Using AWS Elastic Beanstalk with Amazon RDS - AWS Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.RDS.html)




http://blog.uptill3.com/2012/08/25/python-on-elastic-beanstalk.html
http://stackoverflow.com/questions/14077095/aws-elastic-beanstalk-running-a-cronjob
https://github.com/keithters/elasticbeanstalk-mysql-rds-flask
https://github.com/adamcrosby/elastic-flask-baseline
