from sentiment_classification.predict import VDCNN_model as VDCNN

def classify(sentences_in):
    # predict is language is english
    vdcnn = VDCNN(
                        model_weights_dir='./sentiment_classification/train_dir/1490994156/checkpoints',
                        num_channel=1, device="gpu", device_id=0, variable_reuse=None,is_chinese=False)
    sentences = sentences_in # example in rt_data_all
    res = vdcnn.predict(sentences)
    return res
