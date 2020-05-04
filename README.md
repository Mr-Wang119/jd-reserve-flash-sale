# 京东抢购预约抢购

支持京东多商品预约+抢购

> 基于https://github.com/tychxn/jd-assistant

## 主要功能 

- 登陆京东商城（[www.jd.com](http://www.jd.com/)）
  - 手机扫码登录
  - 保存/加载登录cookies (可验证cookies是否过期)
- 商品查询操作
  - 提供完整的[`地址⇔ID`](./area_id/)对应关系
  - 根据商品ID和地址ID查询库存
  - 根据商品ID查询价格
- 购物车操作
  - 清空/添加购物车 (无货商品也可以加入购物车，预约商品无法加入)
  - 获取购物车商品详情
- 订单操作
  - 获取订单结算页面信息 (商品详情, 应付总额, 收货地址, 收货人等)
  - 提交订单（使用默认地址）
    - 直接提交
    - 有货提交
    - 定时提交
  - 查询订单 (可选择只显示未付款订单)
- 其他
  - 商品预约
  - 用户信息查询

## 运行环境

- [Python 3](https://www.python.org/)

## 第三方库

- [Requests](http://docs.python-requests.org/en/master/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [PyCryptodome](https://github.com/Legrandin/pycryptodome)

安装：
```sh
pip install -r requirements.txt
```

## 使用教程

程序主入口为`main.py`

👉 使用教程请参看Wiki