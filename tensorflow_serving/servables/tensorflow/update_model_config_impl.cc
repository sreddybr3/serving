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

namespace tensorflow {
namespace serving {


Status UpdateModelConfigImpl::UpdateModelConfig(
    ServerCore* core, const UpdateModelConfigRequest& request,
    UpdateModelConfigResponse* response) {

/*
  ProtoType proto;
  if (tensorflow::protobuf::TextFormat::ParseFromString(request->get_config_list(),
                                                        &proto)) {
      response->set_config_update_response('Error: cannot parse model config from the input string');
  } else {
    response->set_config_update_response('Invalid model config: cannot parse the model config');
  } */

  std::string prefix("HelloModel ");
  response->set_config_update_response(prefix);

  
  return tensorflow::Status::OK();


}

}  // namespace serving
}  // namespace tensorflow