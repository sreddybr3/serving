/* Copyright 2017 Google Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#include "tensorflow_serving/servables/tensorflow/update_model_config_impl.h"

#include <map>
#include <memory>
#include <string>
#include <utility>
#include <vector>

#include "tensorflow/cc/saved_model/loader.h"
#include "tensorflow/contrib/session_bundle/bundle_shim.h"
#include "tensorflow/contrib/session_bundle/session_bundle.h"
#include "tensorflow/core/lib/core/errors.h"
#include "tensorflow_serving/core/servable_handle.h"

#include "tensorflow_serving/model_servers/server_core.h"

#include "google/protobuf/any.pb.h"
#include "google/protobuf/wrappers.pb.h"
#include "tensorflow/core/lib/core/stringpiece.h"
#include "tensorflow/core/lib/io/path.h"
#include "tensorflow/core/platform/logging.h"
#include "tensorflow_serving/core/load_servables_fast.h"
#include "tensorflow_serving/model_servers/model_platform_types.h"
#include "tensorflow_serving/resources/resource_values.h"
#include "tensorflow_serving/servables/tensorflow/saved_model_bundle_source_adapter.h"
#include "tensorflow_serving/servables/tensorflow/session_bundle_source_adapter.h"
#include "tensorflow_serving/servables/tensorflow/session_bundle_source_adapter.pb.h"
#include "tensorflow_serving/sources/storage_path/file_system_storage_path_source.h"
#include "tensorflow_serving/sources/storage_path/file_system_storage_path_source.pb.h"
#include "tensorflow_serving/config/model_server_config.pb.h"

namespace tensorflow {
namespace serving {


Status UpdateModelConfigImpl::UpdateModelConfig(
    ServerCore* core, const UpdateModelConfigRequest& request,
    UpdateModelConfigResponse* response) {


  ModelServerConfig proto;
  if (tensorflow::protobuf::TextFormat::ParseFromString(request->get_config_list(),
                                                        &proto)) {
    response->set_config_update_response("Success: parse model config from the input string");
    //LOG(INFO) << "Success: parse model config from the input string ";
  } else {
    response->set_config_update_response("Invalid model config: cannot parse the model config");
    //LOG(INFO) << "Invalid model config: cannot parse the model config";
  } 
 
  std::string str;
  google::protobuf::TextFormat::PrintToString(proto, &str);
  LOG(INFO) << "GOT BACK CONFIG STRING" << str.c_str();
  
  return tensorflow::Status::OK();


}

}  // namespace serving
}  // namespace tensorflow
