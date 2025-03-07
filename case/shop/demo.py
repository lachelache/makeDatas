
def add(a, b):
    """
    @api {post} /add /:a /:b 两数加法运算
    @apiGroup 业务线
    @apiName add
    @apiDescription 执行两数求和，返回计算结果
    @apiPermission zs
    @apiParam {Number} a 入参数字1
    @apiParam {Number} b 入参数字2
    @apiParamExample {json} 请求示例：
    {
        "a": 1,
        "b": 11
    }
    @apiSuccess (200) {String} data 返回结果
    @apiSuccess (200) {Integer} code服务器码
    @apiSuccessExample {json} 返回示例：
    {
        "code": 0,
        "msg":"请求成功",
        "data": 12
    }
    """
    sum = a + b
    return dict(code=0, data=sum, msg='ok')
