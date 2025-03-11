from datetime import datetime


def D4createOrder(distributorCode: str, productList: list, account: str = 'sysadmin'):
    """
        @api {post} /D4createOrder 创建D4订单
        @apiGroup 商城
        @apiName D4createOrder
        @apiDescription  创建D4订单
        @apiPermission fang
        @apiParam {String} distributorCode 配送商编码
        @apiParam {String} account 用户账号
        @apiParam {Object[]} productList 产品数组
        @apiParam {String} productList.productNo 产品编码
        @apiParam {String} productList.car 箱数
        @apiParamExample {json} 请求示例:
        {
                "distributorCode": "888666",
                "account": "sysadmin",
                "productList": [
                    {
                        "productNo": "1314520",
                        "car": "1"
                    }
                ]
            }
        @apiSuccess (200) {Integer} responseCode 服务器码
        @apiSuccess (200) {String} responseMsg 提示语
        @apiSuccess (200) {Object} responseData 造数成功返回相关的数据
        @apiSuccessExample {json} 返回示例:
        {
            "responseCode": 0,
            "responseMsg": "请求成功",
            "responseData": {
            }
        }
        """
    res = productList
    now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    demo_log = f"""
[{now_time}]: 脚本开始 -> 进行一键创建订单数据
[{now_time}]: 脚本执行 -> 获取登录 token
[{now_time}]: 脚本执行 -> token为xxxxxx
[{now_time}]: 脚本执行 -> 获取商品列表
[{now_time}]: 脚本执行 -> 选中商品
[{now_time}]: 脚本执行 -> 点击立即提交
[{now_time}]: 脚本执行 -> 调转订单确认
[{now_time}]: 脚本执行 -> 调用订单提交接口
[{now_time}]: 脚本结束 -> 进行一键创建订单数据
"""
    return CaseResponse.success(data=res), demo_log