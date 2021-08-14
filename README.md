#### 功能说明
1. 支持多用户打卡
2. 支持邮件通知(邮件发送方默认使用的163邮箱, 所以配置文件里的host是163的, 其他邮箱暂不了解需要什么配置)
3. 在无需邮件通知时部署文件里的与邮件相关项可不填

#### 部署说明
进入到health目录下

```shell
cd health
pip install -e .
ln -s chromedriver /usr/local/bin/chromedriver
然后使用crontab设置定时任务, 命令是	"python执行路径	当前路径下的send.py"
```

#### 配置文件相关参数
alive:是否为活跃状态, 为true时打卡, 为false时不打卡

send_mail:执行完是否发送邮件通知

uri:打卡网址

host:邮件发送者的host

port:邮件发送端口

sender:发邮件的邮箱号

mail_pwd:邮件的客户端授权密码

receiver:收件人邮箱

user:浙大校园卡号

pwd:浙大校园卡密码

clock_info:后面的数字的表示选择第几个选项，从1开始编号

    sfyxjzxgym:是否愿意接种
    sfbyjzrq:是否是不宜接种人群
    jzxgymqk:当前接种情况
    sffrqjwdg:今日是否因发热请假未到岗（教职工）或未返校（学生）？
    sfqtyyqjwdg:今日是否因发热外的其他原因请假未到岗（教职工）或未返校（学生）？
    tw:今日是否有发热症状（高于37.2 ℃）？
    sfcxtz:一般用不到, 可直接设为2
    sfjcbh:一般用不到, 可直接设为2
    sfjcqz:一般用不到, 可直接设为2
    sfyqjzgc:今日是否被当地管理部门要求在集中隔离点医学观察？
    sfcyglq:今日是否居家隔离观察（居家非隔离状态填否）?
    jrsfqzys:一般用不到, 可直接设为2
    jrsfqzfy:一般用不到, 可直接设为2
    sfhsjc:一般用不到, 可直接设为1
    sfcxzysx:是否有任何与疫情相关的，值得注意的情况？
    sfsqhzjkk:是否已经申领校区所在地健康码？
    zgfx14rfh:一般用不到, 可直接设为2
    sfzx:今日是否在校
    sfzgn:所在地点
    area:所在地点（请打开手机位置功能，并在手机权限设置中选择允许访问位置信息）
    sfymqjczrj:本人家庭成员(包括其他密切接触人员)是否有近14日入境或近14日拟入境的情况？
    sfqrxxss:本人承诺
    sqhzjkkys:今日申领校区所在地健康码的颜色？
    bztcyy:当前地点与上次不在同一城市，原因如下
