import io
import sys
from cgan_mnist.models import ret_final
from flask import Flask,request,jsonify,send_file
app = Flask(__name__)
@app.route('/cgan',methods=['GET'])
def cgan():
    res={'status':'err','msg':''}
    if request.method=='GET':
        labels=request.args.get('labels') #eg. 1235
        try:
            labels=list(map(lambda x:int(x),labels))
        except Exception:
            res['msg']='label err'
            return jsonify(res)
        imgByteArr=ret_final(labels)
        return send_file(
            io.BytesIO(imgByteArr),
            mimetype='image/png',
            as_attachment=True,
            attachment_filename='cgan_mnist/models/mnist.jpg')
    return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug='True')
