## 头条DevOps运维平台，官网：[walle](http://www.walle-web.io/)

## 介绍
个人基于头条开源walle项目改造学习

---

## walle 部署方法
### 1. Nginx配置

nginx配置目录：/etc/nginx/conf.d, 新增配置文件，重启NGINX生效
```
upstream webservers {
    server debian:5000 weight=1; ## 域名
}

server {
    listen       81;
    server_name  debian; ## 域名
    access_log   /var/log/walle.log;
    index index.html index.htm;

    location / {
        try_files $uri $uri/ /index.html;
        add_header access-control-allow-origin *;
        root /home/sample/code/new-walle-web/fe; ## walle-web fe目录绝对路径
    }

    location ^~ /api/ {
        add_header access-control-allow-origin *;
        proxy_pass      http://webservers;
        proxy_set_header X-Forwarded-Host $host:$server_port;
        proxy_set_header  X-Real-IP  $remote_addr;
        proxy_set_header    Origin        $host:$server_port;
        proxy_set_header    Referer       $host:$server_port;
    }

    location ^~ /socket.io/ {
        add_header access-control-allow-origin *;
        proxy_pass      http://webservers;
        proxy_set_header X-Forwarded-Host $host:$server_port;
        proxy_set_header  X-Real-IP  $remote_addr;
        proxy_set_header    Origin        $host:$server_port;
        proxy_set_header    Referer       $host:$server_port;
        proxy_set_header Host $http_host;
        proxy_set_header X-NginX-Proxy true;

        # WebScoket Support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}

```
### 2. 数据库数据初始化
bash admin.sh migration

### 3. 项目启动
bash admin.sh start

### 4. 项目访问
地址：debian:81

用户名/密码：
- 超管：super@walle-web.io \ Walle123
- 所有者：owner@walle-web.io \ Walle123
- 负责人：master@walle-web.io \ Walle123
- 开发者：developer@walle-web.io \ Walle123
- 访客：reporter@walle-web.io \ Walle123


---