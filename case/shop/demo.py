
def add(a, b):
    """

    @api{Post}/add 两数加法运算
    @apiGroup 业务线
    @apiParam {Number} a 入参数字1

    @apiParam {Number} b 入参数字2
    @apiSuccess {Integer} data 返回结果
    @apiSucess(200){Integer} code服务器码

    """
    sum = a + b
    return dict(code=0, data=sum)
