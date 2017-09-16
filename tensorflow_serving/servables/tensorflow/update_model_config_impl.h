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

#ifndef TENSORFLOW_SERVING_SERVABLES_TENSORFLOW_UPDATE_MODEL_CONFIG_IMPL_H_
#define TENSORFLOW_SERVING_SERVABLES_TENSORFLOW_UPDATE_MODEL_CONFIG_IMPL_H_

#include <limits>
#include <map>
#include <memory>
#include <string>
#include <utility>

#include "google/protobuf/any.pb.h"
#include "tensorflow/core/lib/core/status.h"
#include "tensorflow/core/platform/macros.h"
#include "tensorflow/core/platform/mutex.h"
#include "tensorflow/core/platform/types.h"
#include "tensorflow_serving/apis/model.pb.h"
#include "tensorflow_serving/config/logging_config.pb.h"
#include "tensorflow_serving/config/model_server_config.pb.h"
#include "tensorflow_serving/config/platform_config.pb.h"
#include "tensorflow_serving/core/aspired_versions_manager.h"
#include "tensorflow_serving/core/dynamic_source_router.h"
#include "tensorflow_serving/core/servable_state_monitor.h"
#include "tensorflow_serving/core/server_request_logger.h"
#include "tensorflow_serving/core/source.h"
#include "tensorflow_serving/core/source_adapter.h"
#include "tensorflow_serving/core/storage_path.h"
#include "tensorflow_serving/sources/storage_path/file_system_storage_path_source.h"
#include "tensorflow_serving/util/event_bus.h"
#include "tensorflow_serving/util/optional.h"
#include "tensorflow_serving/util/unique_ptr_with_deps.h"

#include "tensorflow_serving/apis/model_config.pb.h"
#include "tensorflow_serving/model_servers/server_core.h"

namespace tensorflow {
namespace serving {

class UpdateModelConfigImpl {
 public:
  static Status UpdateModelConfig(ServerCore* core,
                                 const UpdateModelConfigRequest& request,
                                 UpdateModelConfigResponse* response);
};

}  // namespace serving
}  // namespace tensorflow

#endif  // TENSORFLOW_SERVING_SERVABLES_TENSORFLOW_GET_MODEL_METADATA_IMPL_H_
