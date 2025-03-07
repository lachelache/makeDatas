
from faker import Factory
from common.fun_response import CaseResponse
from common.fun_exception import except_script_error
from datetime import datetime

@except_script_error
def add(a, b):
    """
    @api {post} /add 两数相加
    @apiGroup 商城
    @apiName add
    @apiDescription  请求参数只是demo，实际只接收a,b，执行两数求和，返回计算结果
    @apiPermission fang
    @apiParam {String=7777,9999} a=77777    数字类型
    @apiParam {String=6666,7777} b=9999   数字类型
    @apiParamExample {json} 请求示例:
    {
         "a": "111",
         "b": "9999"
      }
    @apiSuccess (200) {Number} code=200 服务器码
    @apiSuccess (200) {String} data="4" 造数成功返回相关的数据
    @apiSuccess (200) {String} msg="造数成功" 提示语
    @apiSuccessExample {json} 返回示例:
    {
        "code": 0,
        "msg": "请求成功",
        "data": 12
    }
    """
    sum = int(a) + int(b)
    return CaseResponse.success(data= sum)
