
# def add(a, b):
#     """
#
#     @api{Post}/add 两数加法运算
#     @apiGroup 业务线
#     @apiParam {Number} a 入参数字1
#
#     @apiParam {Number} b 入参数字2
#     @apiSuccess {Integer} data 返回结果
#     @apiSucess(200){Integer} code服务器码
#
#     """
#     sum = a + b
#     return dict(code=0, data=sum)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    """
    @api {post} /add 两数相加
    @apiName AddNumbers
    @apiGroup Math

    @apiParam {Number} num1 第一个数字
    @apiParam {Number} num2 第二个数字

    @apiSuccess {Number} result 计算结果

    @apiSuccessExample {json} 成功响应示例:
        HTTP/1.1 200 OK
        {
          "result": 5
        }

    @apiError BadRequest 参数错误

    @apiErrorExample {json} 错误响应示例:
        HTTP/1.1 400 Bad Request
        {
          "error": "Invalid parameters"
        }
    """
    data = request.get_json()

    num1 = data.get('num1')
    num2 = data.get('num2')

    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return jsonify({"error": "Invalid parameters"}), 400

    result = num1 + num2
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True)
