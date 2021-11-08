# 校园网认证守护

使用`systemd`守护校园网认证, 防止被挤下线.  

## 安装

运行`./install.sh`, 将在`/etc`目录下创建一个名为`rz`的目录  
在`/etc/rz`目录下创建一个`user.json`用于存放用户登录信息, 示例如下

```json
{
    "action": "login",
    "ac_id": "1",
    "nas_ip": "",
    "user_mac": "",
    "url": "",
    "username": "00000000",
    "password": "123456"
}
```

只需修改`username`和`password`字段

## 参数设定

修改`/etc/rz/rz.json`来调整认证参数, 包括认证地址, 认证头, 认证用户等内容

```json
{
    "header": "/etc/rz/header.json", 
    "user": "/etc/rz/user.json",
    "url": "http://192.168.2.231/srun_portal_pc.php?ac_id=1&",
    "pingURL": "baidu.com",
    "pingCount": 1
}
```

## 启动守护

执行`sudo systemctl enable rz.service`
