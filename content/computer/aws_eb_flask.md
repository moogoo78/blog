Title: Deploying Flask (Python) to AWS Elastic Beanstalk
Date: 2013-11-12 17:31
Category: computer
Tags: flask, aws
Slug: aws_elastic_beanstalk_flask

# quickstart
## 1. 安裝eb commend tools

下載: [AWS Elastic Beanstalk Command Line Tool : Sample Code & Libraries : Amazon Web Services](http://aws.amazon.com/code/6752709412171743)
    
   設定好路徑(以mac為例), 就可以開始了

    :::text
    AWS-ElasticBeanstalk-CLI-2.5.1/eb/macosx/python2.7/eb

## 2. 跑起來

    :::bash
    eb init
    ; 會有選單, 開始勾選
    ; 平台選這個
    64bit Amazon Linux 2013.09 running Python 2.7
    ; 勾完後, 就可以啟動餓了
    eb start 
    ; 等個幾分鐘
    eb status --verbose 
git aws.push

### 限制

* bundle size can be up to 512MB
* 沒有filesystem

### 參考

* [Deploying a Flask Application to AWS Elastic Beanstalk - AWS Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Python_flask.html) 
* [AWS Elastic Beanstalk FAQs](http://aws.amazon.com/elasticbeanstalk/faqs/)
* [Using AWS Elastic Beanstalk with Amazon RDS - AWS Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.RDS.html)




http://blog.uptill3.com/2012/08/25/python-on-elastic-beanstalk.html
http://stackoverflow.com/questions/14077095/aws-elastic-beanstalk-running-a-cronjob
https://github.com/keithters/elasticbeanstalk-mysql-rds-flask
https://github.com/adamcrosby/elastic-flask-baseline
