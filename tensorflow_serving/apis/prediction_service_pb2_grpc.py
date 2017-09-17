# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from tensorflow_serving.apis import classification_pb2 as tensorflow__serving_dot_apis_dot_classification__pb2
from tensorflow_serving.apis import get_model_metadata_pb2 as tensorflow__serving_dot_apis_dot_get__model__metadata__pb2
from tensorflow_serving.apis import inference_pb2 as tensorflow__serving_dot_apis_dot_inference__pb2
from tensorflow_serving.apis import model_config_pb2 as tensorflow__serving_dot_apis_dot_model__config__pb2
from tensorflow_serving.apis import predict_pb2 as tensorflow__serving_dot_apis_dot_predict__pb2
from tensorflow_serving.apis import regression_pb2 as tensorflow__serving_dot_apis_dot_regression__pb2


class PredictionServiceStub(object):
  """open source marker; do not remove
  PredictionService provides access to machine-learned models loaded by
  model_servers.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Classify = channel.unary_unary(
        '/tensorflow.serving.PredictionService/Classify',
        request_serializer=tensorflow__serving_dot_apis_dot_classification__pb2.ClassificationRequest.SerializeToString,
        response_deserializer=tensorflow__serving_dot_apis_dot_classification__pb2.ClassificationResponse.FromString,
        )
    self.Regress = channel.unary_unary(
        '/tensorflow.serving.PredictionService/Regress',
        request_serializer=tensorflow__serving_dot_apis_dot_regression__pb2.RegressionRequest.SerializeToString,
        response_deserializer=tensorflow__serving_dot_apis_dot_regression__pb2.RegressionResponse.FromString,
        )
    self.Predict = channel.unary_unary(
        '/tensorflow.serving.PredictionService/Predict',
        request_serializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictRequest.SerializeToString,
        response_deserializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictResponse.FromString,
        )
    self.MultiInference = channel.unary_unary(
        '/tensorflow.serving.PredictionService/MultiInference',
        request_serializer=tensorflow__serving_dot_apis_dot_inference__pb2.MultiInferenceRequest.SerializeToString,
        response_deserializer=tensorflow__serving_dot_apis_dot_inference__pb2.MultiInferenceResponse.FromString,
        )
    self.GetModelMetadata = channel.unary_unary(
        '/tensorflow.serving.PredictionService/GetModelMetadata',
        request_serializer=tensorflow__serving_dot_apis_dot_get__model__metadata__pb2.GetModelMetadataRequest.SerializeToString,
        response_deserializer=tensorflow__serving_dot_apis_dot_get__model__metadata__pb2.GetModelMetadataResponse.FromString,
        )
    self.UpdateModelConfig = channel.unary_unary(
        '/tensorflow.serving.PredictionService/UpdateModelConfig',
        request_serializer=tensorflow__serving_dot_apis_dot_model__config__pb2.UpdateModelConfigRequest.SerializeToString,
        response_deserializer=tensorflow__serving_dot_apis_dot_model__config__pb2.UpdateModelConfigResponse.FromString,
        )


class PredictionServiceServicer(object):
  """open source marker; do not remove
  PredictionService provides access to machine-learned models loaded by
  model_servers.
  """

  def Classify(self, request, context):
    """Classify.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Regress(self, request, context):
    """Regress.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Predict(self, request, context):
    """Predict -- provides access to loaded TensorFlow model.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MultiInference(self, request, context):
    """MultiInference API for multi-headed models.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetModelMetadata(self, request, context):
    """GetModelMetadata - provides access to metadata for loaded models.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateModelConfig(self, request, context):
    """UpdateModelConfig - dynamically update the model config list
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PredictionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Classify': grpc.unary_unary_rpc_method_handler(
          servicer.Classify,
          request_deserializer=tensorflow__serving_dot_apis_dot_classification__pb2.ClassificationRequest.FromString,
          response_serializer=tensorflow__serving_dot_apis_dot_classification__pb2.ClassificationResponse.SerializeToString,
      ),
      'Regress': grpc.unary_unary_rpc_method_handler(
          servicer.Regress,
          request_deserializer=tensorflow__serving_dot_apis_dot_regression__pb2.RegressionRequest.FromString,
          response_serializer=tensorflow__serving_dot_apis_dot_regression__pb2.RegressionResponse.SerializeToString,
      ),
      'Predict': grpc.unary_unary_rpc_method_handler(
          servicer.Predict,
          request_deserializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictRequest.FromString,
          response_serializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictResponse.SerializeToString,
      ),
      'MultiInference': grpc.unary_unary_rpc_method_handler(
          servicer.MultiInference,
          request_deserializer=tensorflow__serving_dot_apis_dot_inference__pb2.MultiInferenceRequest.FromString,
          response_serializer=tensorflow__serving_dot_apis_dot_inference__pb2.MultiInferenceResponse.SerializeToString,
      ),
      'GetModelMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.GetModelMetadata,
          request_deserializer=tensorflow__serving_dot_apis_dot_get__model__metadata__pb2.GetModelMetadataRequest.FromString,
          response_serializer=tensorflow__serving_dot_apis_dot_get__model__metadata__pb2.GetModelMetadataResponse.SerializeToString,
      ),
      'UpdateModelConfig': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateModelConfig,
          request_deserializer=tensorflow__serving_dot_apis_dot_model__config__pb2.UpdateModelConfigRequest.FromString,
          response_serializer=tensorflow__serving_dot_apis_dot_model__config__pb2.UpdateModelConfigResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tensorflow.serving.PredictionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
