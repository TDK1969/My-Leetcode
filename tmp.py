from flask import Flask, make_response, request
from urllib.parse import unquote
import logging
from img_embedding_model import ImgEmbeddingModel
import time
import json
import traceback

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

app.logger.info('model begin initial.')
start_tm = int(time.time() * 1000)
m = ImgEmbeddingModel()
app.logger.info('model initial success. cost %dms' % (int(time.time() * 1000) - start_tm))
        
@app.route("/getImgEmbedding/v1", methods=["GET"])
def getImgEmbedding():
    start_tm = int(time.time() * 1000)
    try:
        # request.args.get获取GET方法中的参数
        # unquote进行urldecode解码
        img_url = unquote(request.args.get('img_url'))
        img_source = request.args.get('img_source')
        num = request.args.get('num', 3)

        # 运行模型
        if img_source == "product":
            result = m.run(img_url, True)
        else:
            result = m.run(img_url)

        # 构建响应
        if result:
            response = make_response(
                json.dumps(
                    {
                        "code": 200,
                        "msg": "ok",
                        "data": {
                            "result": result
                        }
                    },
                    ensure_ascii=False
                )
            )
            response.headers['Content-Type'] = 'application/json'
            app.logger.info('request get /getImgEmbedding/v1 success. cost %dms' % (int(time.time() * 1000) - start_tm))
            return response
        else:
            response = make_response(
                json.dumps(
                    {
                        "code": -100,
                        "msg": "no instance found",
                        "data": {
                            "result": {}
                        }
                    },
                    ensure_ascii=False
                )
            )
            response.headers['Content-Type'] = 'application/json'
            app.logger.info('request get /getImgEmbedding/v1 success. cost %dms' % (int(time.time() * 1000) - start_tm))
            return response
    # 异常处理
    except:
        err_msg = 'url: %s, body: %s err_msg: %s' % (request.url, request.data, (str(traceback.format_exc())))
        app.logger.error(err_msg)
        app.logger.info('request get /getImgEmbedding/v1 fail. cost %dms' % (int(time.time() * 1000) - start_tm))
        response = make_response(
            json.dumps({"code": -1, "msg": err_msg}, ensure_ascii=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    
@app.route("/getImgEmbedding/v2", methods=["GET"])
def getImgEmbedding_v2():
    start_tm = int(time.time() * 1000)
    try:
        img_url = unquote(request.args.get('img_url'))
        img_source = request.args.get('img_source', '')
        num = request.args.get('num', 3)
        result = m.run_v2(img_url)

        if result:
            # 构建响应体
            response = make_response(
                json.dumps(
                    {
                        "code": 200,
                        "msg": "ok",
                        "data": {
                            "result": result
                        }
                    },
                    ensure_ascii=False
                )
            )
            response.headers['Content-Type'] = 'application/json'
            app.logger.info('request get /getImgEmbedding/v2 success. cost %dms' % (int(time.time() * 1000) - start_tm))
            return response
        else:
            response = make_response(
                json.dumps(
                    {
                        "code": -100,
                        "msg": "no instance found",
                        "data": {
                            "result": {}
                        }
                    },
                    ensure_ascii=False
                )
            )
            response.headers['Content-Type'] = 'application/json'
            app.logger.info('request get /getImgEmbedding/v2 success. cost %dms' % (int(time.time() * 1000) - start_tm))
            return response

    except:
        err_msg = 'url: %s, body: %s err_msg: %s' % (request.url, request.data, (str(traceback.format_exc())))
        app.logger.error(err_msg)
        app.logger.info('request get /getImgEmbedding/v2 fail. cost %dms' % (int(time.time() * 1000) - start_tm))
        response = make_response(
            json.dumps({"code": -1, "msg": err_msg}, ensure_ascii=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response

@app.route("/getSegResult/v1", methods=["GET"])
def get_seg_result():
    start_tm = int(time.time() * 1000)
    try:
        img_url = unquote(request.args.get('img_url'))
        result = m.get_seg_results_no_score_filter_2(img_url)
        # 构建响应体
        response = make_response(
            json.dumps(
                {
                    "code": 200,
                    "msg": "ok",
                    "data": result
                },
                ensure_ascii=False
            )
        )
        response.headers['Content-Type'] = 'application/json'
        app.logger.info('request get /getSegResult/v1 success. cost %dms' % (int(time.time() * 1000) - start_tm))
        return response
    except:
        err_msg = 'url: %s, body: %s err_msg: %s' % (request.url, request.data, (str(traceback.format_exc())))
        app.logger.error(err_msg)
        app.logger.info('request get /getSegResult/v1 fail. cost %dms' % (int(time.time() * 1000) - start_tm))
        response = make_response(
            json.dumps({"code": -1, "msg": err_msg}, ensure_ascii=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    
@app.route("/getProductEmbedding/v1", methods=["GET"])
def get_product_embedding():
    start_tm = int(time.time() * 1000)
    try:
        img_url = unquote(request.args.get('img_url'))
        result = m.get_product_embedding(img_url)
        # 构建响应体
        response = make_response(
            json.dumps(
                {
                    "code": 200,
                    "msg": "ok",
                    "data": result
                },
                ensure_ascii=False
            )
        )
        response.headers['Content-Type'] = 'application/json'
        app.logger.info('request get /getProductEmbedding/v1 success. cost %dms' % (int(time.time() * 1000) - start_tm))
        return response
    except:
        err_msg = 'url: %s, body: %s err_msg: %s' % (request.url, request.data, (str(traceback.format_exc())))
        app.logger.error(err_msg)
        app.logger.info('request get /getProductEmbedding/v1 fail. cost %dms' % (int(time.time() * 1000) - start_tm))
        response = make_response(
            json.dumps({"code": -1, "msg": err_msg}, ensure_ascii=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response

@app.route("/test", methods=["GET"])
def sayHello():
    return "Hello World."

if __name__ == '__main__':
    app.run("0.0.0.0", debug=False, use_reloader=False, port=8001)
